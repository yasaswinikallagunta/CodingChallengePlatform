import os
import sys
import re
import time
import shutil
import base64
import requests
import subprocess
import tempfile
from django.conf import settings

# Judge0 language IDs (CE edition)
JUDGE0_LANGUAGE_IDS = {
    'python': 71,       # Python (3.8.1)
    'python3': 71,
    'javascript': 63,   # JavaScript (Node.js 12.14.0)
    'c': 50,            # C (GCC 9.2.0)
    'cpp': 54,          # C++ (GCC 9.2.0)
    'c++': 54,
    'java': 62,         # Java (OpenJDK 13.0.1)
    'sql': 82,          # SQL (SQLite 3.27.2)
}


def find_executable(name, custom_candidates=None):
    """Finds binary in system PATH or common installation directories on Windows."""
    found = shutil.which(name)
    if found:
        return found
    if custom_candidates:
        for candidate in custom_candidates:
            if os.path.exists(candidate):
                return candidate
    return None


GPP_CANDIDATES = [
    r'C:\Program Files (x86)\Dev-Cpp\MinGW64\bin\g++.exe',
    r'C:\Program Files\Dev-Cpp\MinGW64\bin\g++.exe',
    r'C:\Dev-Cpp\bin\g++.exe',
    r'C:\MinGW\bin\g++.exe',
    r'C:\msys64\mingw64\bin\g++.exe',
]

GCC_CANDIDATES = [
    r'C:\Program Files (x86)\Dev-Cpp\MinGW64\bin\gcc.exe',
    r'C:\Program Files\Dev-Cpp\MinGW64\bin\gcc.exe',
    r'C:\Dev-Cpp\bin\gcc.exe',
    r'C:\MinGW\bin\gcc.exe',
    r'C:\msys64\mingw64\bin\gcc.exe',
]


class CodeExecutionResult:
    def __init__(self, status, stdout='', stderr='', compile_output='', execution_time=0.0, memory=0.0, error_message=''):
        self.status = status  # 'Accepted', 'Wrong Answer', 'Time Limit Exceeded', 'Compilation Error', 'Runtime Error', 'Service Unavailable'
        self.stdout = stdout or ''
        self.stderr = stderr or ''
        self.compile_output = compile_output or ''
        self.execution_time = execution_time
        self.memory = memory
        self.error_message = error_message

    def to_dict(self):
        return {
            'status': self.status,
            'stdout': self.stdout,
            'stderr': self.stderr,
            'compile_output': self.compile_output,
            'execution_time': self.execution_time,
            'memory': self.memory,
            'error_message': self.error_message,
        }


def normalize_output(text):
    if text is None:
        return ''
    return '\n'.join([line.rstrip() for line in str(text).strip().splitlines()])


def parse_error_details(status, compile_output='', stderr='', stdout=''):
    """
    Extracts structured, genuine error details from compiler or runtime output.
    Does not invent error details or line numbers.
    """
    raw_error = compile_output or stderr or ''
    error_type = status
    line_number = None
    explanation = ''

    if status == 'Compilation Error':
        error_type = 'Compilation Error'
        # Parse GCC / G++ line numbers: filename.cpp:12:5: error: ...
        line_match = re.search(r':(\d+):\d*:\s*(?:fatal\s+)?error:', raw_error, re.IGNORECASE)
        if line_match:
            try:
                line_number = int(line_match.group(1))
            except ValueError:
                pass
        
        # Parse javac line numbers: Solution.java:12: error: ...
        if not line_number:
            java_line_match = re.search(r'\.java:(\d+):\s*error:', raw_error, re.IGNORECASE)
            if java_line_match:
                try:
                    line_number = int(java_line_match.group(1))
                except ValueError:
                    pass

        explanation = "The program failed to compile. Check for syntax mistakes, missing headers, or mismatched types."

    elif status == 'Runtime Error':
        # Look for Python exceptions: SyntaxError, TypeError, IndexError, ZeroDivisionError, etc.
        py_exc_match = re.search(r'([A-Za-z]+Error|[A-Za-z]+Exception):\s*(.*)', raw_error)
        if py_exc_match:
            error_type = py_exc_match.group(1)
            msg = py_exc_match.group(2)
            explanation = f"Python raised {error_type}: {msg}"
        
        # Look for Python line number: File "...", line 12, in ...
        py_line_match = re.findall(r'line\s+(\d+)', raw_error, re.IGNORECASE)
        if py_line_match:
            try:
                line_number = int(py_line_match[-1])
            except ValueError:
                pass

        # Look for Java exceptions: java.lang.NullPointerException, etc.
        java_exc_match = re.search(r'Exception in thread ".*?"\s+([\w\.]+):\s*(.*)', raw_error)
        if java_exc_match:
            error_type = java_exc_match.group(1).split('.')[-1]
            explanation = f"Java thrown {error_type}: {java_exc_match.group(2)}"
        
        # Look for Node.js exceptions
        js_exc_match = re.search(r'([A-Za-z]+Error):\s*(.*)', raw_error)
        if js_exc_match and not py_exc_match:
            error_type = js_exc_match.group(1)
            explanation = f"JavaScript runtime error: {js_exc_match.group(2)}"

        if not explanation:
            explanation = "The program crashed during execution. Check for invalid array indices, division by zero, or memory limits."

    elif status == 'Time Limit Exceeded':
        error_type = 'Time Limit Exceeded'
        explanation = "The execution exceeded the allocated time limit (4.0s). Check for infinite loops or inefficient algorithms."

    return {
        'error_type': error_type,
        'line_number': line_number,
        'compiler_error': compile_output,
        'runtime_error': stderr,
        'error_output': raw_error.strip(),
        'explanation': explanation,
    }


def execute_via_judge0(code, language, stdin=''):
    """
    Submits code to Judge0 API (RapidAPI or self-hosted CE).
    """
    lang_key = language.lower().strip()
    language_id = JUDGE0_LANGUAGE_IDS.get(lang_key)
    if not language_id:
        return CodeExecutionResult(
            status='Runtime Error',
            error_message=f"Unsupported language '{language}'. Supported: Python, JavaScript, C, C++, Java, SQL."
        )

    api_url = getattr(settings, 'JUDGE0_API_URL', 'https://judge0-ce.p.rapidapi.com').rstrip('/')
    api_key = getattr(settings, 'JUDGE0_API_KEY', '').strip()
    api_host = getattr(settings, 'JUDGE0_API_HOST', 'judge0-ce.p.rapidapi.com').strip()

    headers = {'content-type': 'application/json'}
    if api_key:
        headers['X-RapidAPI-Key'] = api_key
        headers['X-RapidAPI-Host'] = api_host

    payload = {
        'language_id': language_id,
        'source_code': code,
        'stdin': stdin or '',
        'cpu_time_limit': 4.0,
        'memory_limit': 128000,
    }

    try:
        endpoint = f"{api_url}/submissions?base64_encoded=false&wait=true"
        response = requests.post(endpoint, json=payload, headers=headers, timeout=12)
        
        if response.status_code not in (200, 201):
            return CodeExecutionResult(
                status='Service Unavailable',
                error_message=f"Judge0 API returned status {response.status_code}: {response.text[:300]}"
            )

        data = response.json()
        status_id = data.get('status', {}).get('id')
        status_desc = data.get('status', {}).get('description', 'Unknown')
        stdout = data.get('stdout') or ''
        stderr = data.get('stderr') or ''
        compile_output = data.get('compile_output') or ''
        exec_time = float(data.get('time') or 0.0)
        memory = float(data.get('memory') or 0.0)

        if status_id == 3:
            status = 'Accepted'
        elif status_id == 4:
            status = 'Wrong Answer'
        elif status_id == 5:
            status = 'Time Limit Exceeded'
        elif status_id == 6:
            status = 'Compilation Error'
        elif status_id in (7, 8, 9, 10, 11, 12):
            status = 'Runtime Error'
        else:
            status = status_desc

        return CodeExecutionResult(
            status=status,
            stdout=stdout,
            stderr=stderr,
            compile_output=compile_output,
            execution_time=exec_time,
            memory=memory
        )
    except requests.exceptions.RequestException as e:
        return CodeExecutionResult(
            status='Service Unavailable',
            error_message=f"Could not reach Judge0 service: {str(e)}"
        )


def execute_via_isolated_subprocess(code, language, stdin=''):
    """
    Executes source code in an isolated sub-process with timeouts and output bounds.
    Never executes within the Django main process.
    Supports Python, JavaScript, C++, C, Java, and SQL.
    """
    lang_key = language.lower().strip()

    # 1. PYTHON
    if lang_key in ('python', 'python3'):
        with tempfile.NamedTemporaryFile(suffix='.py', delete=False, mode='w', encoding='utf-8') as f:
            f.write(code)
            temp_path = f.name

        try:
            start_time = time.time()
            proc = subprocess.run(
                [sys.executable, '-I', temp_path],
                input=stdin,
                text=True,
                capture_output=True,
                timeout=4.0
            )
            elapsed = round(time.time() - start_time, 3)

            if proc.returncode != 0:
                return CodeExecutionResult(
                    status='Runtime Error',
                    stdout=proc.stdout[:8000],
                    stderr=proc.stderr[:8000],
                    execution_time=elapsed
                )

            return CodeExecutionResult(
                status='Accepted',
                stdout=proc.stdout[:8000],
                stderr=proc.stderr[:8000],
                execution_time=elapsed
            )
        except subprocess.TimeoutExpired:
            return CodeExecutionResult(
                status='Time Limit Exceeded',
                error_message='Execution timed out after 4 seconds.',
                execution_time=4.0
            )
        except Exception as e:
            return CodeExecutionResult(status='Runtime Error', error_message=str(e))
        finally:
            if os.path.exists(temp_path):
                try: os.remove(temp_path)
                except OSError: pass

    # 2. JAVASCRIPT (NODE.JS)
    elif lang_key in ('javascript', 'node', 'js'):
        node_bin = shutil.which('node')
        if not node_bin:
            return CodeExecutionResult(
                status='Service Unavailable',
                error_message='Node.js runtime is not available locally for JavaScript execution.'
            )

        with tempfile.NamedTemporaryFile(suffix='.js', delete=False, mode='w', encoding='utf-8') as f:
            f.write(code)
            temp_path = f.name

        try:
            start_time = time.time()
            proc = subprocess.run(
                [node_bin, temp_path],
                input=stdin,
                text=True,
                capture_output=True,
                timeout=4.0
            )
            elapsed = round(time.time() - start_time, 3)

            if proc.returncode != 0:
                return CodeExecutionResult(
                    status='Runtime Error',
                    stdout=proc.stdout[:8000],
                    stderr=proc.stderr[:8000],
                    execution_time=elapsed
                )

            return CodeExecutionResult(
                status='Accepted',
                stdout=proc.stdout[:8000],
                stderr=proc.stderr[:8000],
                execution_time=elapsed
            )
        except subprocess.TimeoutExpired:
            return CodeExecutionResult(
                status='Time Limit Exceeded',
                error_message='Execution timed out after 4 seconds.',
                execution_time=4.0
            )
        except Exception as e:
            return CodeExecutionResult(status='Runtime Error', error_message=str(e))
        finally:
            if os.path.exists(temp_path):
                try: os.remove(temp_path)
                except OSError: pass

    # 3. C++ (G++)
    elif lang_key in ('cpp', 'c++'):
        gpp_bin = find_executable('g++', GPP_CANDIDATES)
        if not gpp_bin:
            return CodeExecutionResult(
                status='Service Unavailable',
                error_message='G++ compiler is not configured or found on the host machine. Configure JUDGE0_API_KEY in backend/.env for cloud execution.'
            )

        with tempfile.NamedTemporaryFile(suffix='.cpp', delete=False, mode='w', encoding='utf-8') as f:
            f.write(code)
            src_path = f.name
        exe_path = src_path.replace('.cpp', '.exe')

        try:
            # Compile step
            comp = subprocess.run(
                [gpp_bin, '-O2', '-std=c++11', '-o', exe_path, src_path],
                capture_output=True,
                text=True,
                timeout=6.0
            )
            if comp.returncode != 0:
                return CodeExecutionResult(
                    status='Compilation Error',
                    compile_output=comp.stderr[:8000],
                    stderr=comp.stderr[:8000]
                )

            # Run step
            start_time = time.time()
            proc = subprocess.run(
                [exe_path],
                input=stdin,
                text=True,
                capture_output=True,
                timeout=4.0
            )
            elapsed = round(time.time() - start_time, 3)

            if proc.returncode != 0:
                return CodeExecutionResult(
                    status='Runtime Error',
                    stdout=proc.stdout[:8000],
                    stderr=proc.stderr[:8000],
                    execution_time=elapsed
                )

            return CodeExecutionResult(
                status='Accepted',
                stdout=proc.stdout[:8000],
                stderr=proc.stderr[:8000],
                execution_time=elapsed
            )
        except subprocess.TimeoutExpired:
            return CodeExecutionResult(
                status='Time Limit Exceeded',
                error_message='Execution timed out after 4 seconds.',
                execution_time=4.0
            )
        except Exception as e:
            return CodeExecutionResult(status='Runtime Error', error_message=str(e))
        finally:
            if os.path.exists(src_path):
                try: os.remove(src_path)
                except OSError: pass
            if os.path.exists(exe_path):
                try: os.remove(exe_path)
                except OSError: pass

    # 4. C (GCC)
    elif lang_key == 'c':
        gcc_bin = find_executable('gcc', GCC_CANDIDATES)
        if not gcc_bin:
            return CodeExecutionResult(
                status='Service Unavailable',
                error_message='GCC compiler is not configured or found on the host machine. Configure JUDGE0_API_KEY in backend/.env for cloud execution.'
            )

        with tempfile.NamedTemporaryFile(suffix='.c', delete=False, mode='w', encoding='utf-8') as f:
            f.write(code)
            src_path = f.name
        exe_path = src_path.replace('.c', '.exe')

        try:
            # Compile step
            comp = subprocess.run(
                [gcc_bin, '-O2', '-std=c11', '-o', exe_path, src_path],
                capture_output=True,
                text=True,
                timeout=6.0
            )
            if comp.returncode != 0:
                return CodeExecutionResult(
                    status='Compilation Error',
                    compile_output=comp.stderr[:8000],
                    stderr=comp.stderr[:8000]
                )

            # Run step
            start_time = time.time()
            proc = subprocess.run(
                [exe_path],
                input=stdin,
                text=True,
                capture_output=True,
                timeout=4.0
            )
            elapsed = round(time.time() - start_time, 3)

            if proc.returncode != 0:
                return CodeExecutionResult(
                    status='Runtime Error',
                    stdout=proc.stdout[:8000],
                    stderr=proc.stderr[:8000],
                    execution_time=elapsed
                )

            return CodeExecutionResult(
                status='Accepted',
                stdout=proc.stdout[:8000],
                stderr=proc.stderr[:8000],
                execution_time=elapsed
            )
        except subprocess.TimeoutExpired:
            return CodeExecutionResult(
                status='Time Limit Exceeded',
                error_message='Execution timed out after 4 seconds.',
                execution_time=4.0
            )
        except Exception as e:
            return CodeExecutionResult(status='Runtime Error', error_message=str(e))
        finally:
            if os.path.exists(src_path):
                try: os.remove(src_path)
                except OSError: pass
            if os.path.exists(exe_path):
                try: os.remove(exe_path)
                except OSError: pass

    # 5. JAVA (JAVAC / JAVA)
    elif lang_key == 'java':
        javac_bin = shutil.which('javac')
        java_bin = shutil.which('java')
        if not javac_bin or not java_bin:
            return CodeExecutionResult(
                status='Service Unavailable',
                error_message='Java JDK (javac/java) is not found in PATH. Configure JUDGE0_API_KEY in backend/.env for cloud execution.'
            )

        # Detect public class name from code, default to Solution
        class_match = re.search(r'public\s+class\s+([A-Za-z0-9_]+)', code)
        class_name = class_match.group(1) if class_match else 'Solution'

        temp_dir = tempfile.mkdtemp()
        src_path = os.path.join(temp_dir, f"{class_name}.java")
        with open(src_path, 'w', encoding='utf-8') as f:
            f.write(code)

        try:
            # Compile step
            comp = subprocess.run(
                [javac_bin, src_path],
                capture_output=True,
                text=True,
                timeout=8.0
            )
            if comp.returncode != 0:
                return CodeExecutionResult(
                    status='Compilation Error',
                    compile_output=comp.stderr[:8000],
                    stderr=comp.stderr[:8000]
                )

            # Run step
            start_time = time.time()
            proc = subprocess.run(
                [java_bin, '-cp', temp_dir, class_name],
                input=stdin,
                text=True,
                capture_output=True,
                timeout=4.0
            )
            elapsed = round(time.time() - start_time, 3)

            if proc.returncode != 0:
                return CodeExecutionResult(
                    status='Runtime Error',
                    stdout=proc.stdout[:8000],
                    stderr=proc.stderr[:8000],
                    execution_time=elapsed
                )

            return CodeExecutionResult(
                status='Accepted',
                stdout=proc.stdout[:8000],
                stderr=proc.stderr[:8000],
                execution_time=elapsed
            )
        except subprocess.TimeoutExpired:
            return CodeExecutionResult(
                status='Time Limit Exceeded',
                error_message='Execution timed out after 4 seconds.',
                execution_time=4.0
            )
        except Exception as e:
            return CodeExecutionResult(status='Runtime Error', error_message=str(e))
        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)

    # 6. SQL (SQLite in-memory runner)
    elif lang_key == 'sql':
        # Safely execute SQL script against in-memory SQLite in isolated python subprocess
        py_runner = (
            "import sys, sqlite3\n"
            "try:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    cur = conn.cursor()\n"
            "    script = sys.stdin.read()\n"
            "    statements = [s.strip() for s in script.split(';') if s.strip()]\n"
            "    last_res = None\n"
            "    for s in statements:\n"
            "        cur.execute(s)\n"
            "        if cur.description:\n"
            "            rows = cur.fetchall()\n"
            "            for row in rows:\n"
            "                print(' '.join(str(val) if val is not None else 'null' for val in row))\n"
            "except Exception as e:\n"
            "    sys.stderr.write(str(e))\n"
            "    sys.exit(1)\n"
        )
        try:
            start_time = time.time()
            proc = subprocess.run(
                [sys.executable, '-I', '-c', py_runner],
                input=code,
                text=True,
                capture_output=True,
                timeout=4.0
            )
            elapsed = round(time.time() - start_time, 3)

            if proc.returncode != 0:
                return CodeExecutionResult(
                    status='Runtime Error',
                    stdout=proc.stdout[:8000],
                    stderr=proc.stderr[:8000],
                    execution_time=elapsed
                )

            return CodeExecutionResult(
                status='Accepted',
                stdout=proc.stdout[:8000],
                stderr=proc.stderr[:8000],
                execution_time=elapsed
            )
        except subprocess.TimeoutExpired:
            return CodeExecutionResult(status='Time Limit Exceeded', error_message='Execution timed out.')
        except Exception as e:
            return CodeExecutionResult(status='Runtime Error', error_message=str(e))

    else:
        return CodeExecutionResult(
            status='Service Unavailable',
            error_message=(
                f"Unsupported language '{language}'. "
                "Supported languages: Python, JavaScript, C, C++, Java, SQL."
            )
        )


def run_code_execution(code, language, stdin=''):
    """
    Routes execution to Judge0 when configured with an API key,
    or falls back to isolated local sub-process execution.
    """
    has_judge0 = bool(getattr(settings, 'JUDGE0_API_KEY', '').strip())
    enable_fallback = getattr(settings, 'ENABLE_LOCAL_FALLBACK_EXECUTION', True)

    if has_judge0:
        return execute_via_judge0(code, language, stdin)
    elif enable_fallback:
        return execute_via_isolated_subprocess(code, language, stdin)
    else:
        return CodeExecutionResult(
            status='Service Unavailable',
            error_message=(
                "Code execution service is not configured. "
                "Configure JUDGE0_API_KEY in backend/.env or set ENABLE_LOCAL_FALLBACK_EXECUTION=True."
            )
        )


def evaluate_test_cases(code, language, test_cases):
    """
    Evaluates source code against test cases with detailed error and verdict tracking.
    Never exposes hidden test case inputs or expected outputs.
    """
    total_count = len(test_cases)
    passed_count = 0
    sample_results = []
    total_time = 0.0
    final_status = 'Accepted'
    first_error_output = ''
    first_failed_info = None

    if not test_cases:
        res = run_code_execution(code, language, '')
        err_details = parse_error_details(res.status, res.compile_output, res.stderr, res.stdout)
        return {
            'overall_status': res.status,
            'passed_count': 1 if res.status == 'Accepted' else 0,
            'failed_count': 0 if res.status == 'Accepted' else 1,
            'total_count': 1,
            'sample_results': [{'case': 1, 'passed': res.status == 'Accepted', 'output': res.stdout, 'error': res.stderr or res.error_message}],
            'avg_time': res.execution_time,
            'memory': res.memory,
            'console_output': res.stdout or res.stderr or res.error_message or res.compile_output,
            'error_details': err_details,
            'first_failed_info': None,
        }

    for idx, tc in enumerate(test_cases, 1):
        inp = tc.get('input', '')
        expected = tc.get('expected_output', '')
        is_hidden = tc.get('is_hidden', False)

        result = run_code_execution(code, language, inp)
        total_time += result.execution_time

        if result.status == 'Service Unavailable':
            err_details = parse_error_details('Service Unavailable', error_message=result.error_message)
            return {
                'overall_status': 'Service Unavailable',
                'passed_count': 0,
                'failed_count': total_count,
                'total_count': total_count,
                'sample_results': [],
                'avg_time': 0,
                'memory': 0,
                'console_output': result.error_message,
                'error_details': err_details,
                'first_failed_info': None,
            }

        if result.status in ('Compilation Error', 'Time Limit Exceeded'):
            final_status = result.status
            first_error_output = result.compile_output or result.stderr or result.error_message
            if not is_hidden:
                sample_results.append({
                    'case': idx,
                    'passed': False,
                    'input': inp,
                    'expected': expected,
                    'actual': result.stdout,
                    'error': first_error_output,
                })
            first_failed_info = {
                'case_number': idx,
                'is_hidden': is_hidden,
                'reason': f"{result.status} on test case {idx}",
            }
            break

        if result.status == 'Runtime Error':
            final_status = 'Runtime Error'
            first_error_output = result.stderr or result.error_message
            if not is_hidden:
                sample_results.append({
                    'case': idx,
                    'passed': False,
                    'input': inp,
                    'expected': expected,
                    'actual': result.stdout,
                    'error': first_error_output,
                })
            first_failed_info = {
                'case_number': idx,
                'is_hidden': is_hidden,
                'reason': f"Runtime Error on test case {idx}",
            }
            break

        actual_clean = normalize_output(result.stdout)
        expected_clean = normalize_output(expected)
        case_passed = (actual_clean == expected_clean)

        if case_passed:
            passed_count += 1
        else:
            if final_status == 'Accepted':
                final_status = 'Wrong Answer'
                first_failed_info = {
                    'case_number': idx,
                    'is_hidden': is_hidden,
                    'reason': f"Output mismatch on test case {idx}" if is_hidden else f"Expected '{expected_clean}', got '{actual_clean}'",
                }

        if not is_hidden:
            sample_results.append({
                'case': idx,
                'passed': case_passed,
                'input': inp,
                'expected': expected,
                'actual': actual_clean,
                'error': result.stderr,
            })

    failed_count = total_count - passed_count
    avg_time = round(total_time / total_count, 3) if total_count > 0 else 0.0
    err_details = parse_error_details(final_status, first_error_output, first_error_output, '')

    return {
        'overall_status': final_status,
        'passed_count': passed_count,
        'failed_count': failed_count,
        'total_count': total_count,
        'sample_results': sample_results,
        'avg_time': avg_time,
        'memory': 0.0,
        'console_output': first_error_output or (sample_results[0]['actual'] if sample_results else ''),
        'error_details': err_details,
        'first_failed_info': first_failed_info,
    }
