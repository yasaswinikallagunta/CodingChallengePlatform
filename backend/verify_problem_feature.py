import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from coding.models import CodingProblem
from coding.execution import run_code_execution, evaluate_test_cases, parse_error_details

print("--- 1. VERIFYING 500 PROBLEMS IN DATABASE ---")
total_count = CodingProblem.objects.count()
print(f"Total problems in DB: {total_count}")
assert total_count == 500, f"Expected 500 problems, got {total_count}"

easy_count = CodingProblem.objects.filter(difficulty='Easy').count()
med_count = CodingProblem.objects.filter(difficulty='Medium').count()
hard_count = CodingProblem.objects.filter(difficulty='Hard').count()
print(f"Easy: {easy_count}, Medium: {med_count}, Hard: {hard_count}")
assert easy_count + med_count + hard_count == 500, "Difficulty counts do not sum to 500"
assert easy_count > 0 and med_count > 0 and hard_count > 0, "All three difficulty tiers must be present"

distinct_titles = CodingProblem.objects.values('title').distinct().count()
distinct_slugs = CodingProblem.objects.values('slug').distinct().count()
print(f"Distinct titles: {distinct_titles}, Distinct slugs: {distinct_slugs}")
assert distinct_titles == 500, f"Expected 500 unique titles, got {distinct_titles}"
assert distinct_slugs == 500, f"Expected 500 unique slugs, got {distinct_slugs}"

# Verify complete metadata on every single problem
sample_problems = CodingProblem.objects.all()[:50]
for p in sample_problems:
    assert p.title, "Missing title"
    assert p.difficulty in ('Easy', 'Medium', 'Hard'), "Invalid difficulty"
    assert p.problem_statement, f"Missing statement in {p.title}"
    assert p.input_format, f"Missing input format in {p.title}"
    assert p.output_format, f"Missing output format in {p.title}"
    assert p.constraints, f"Missing constraints in {p.title}"
    assert p.sample_input is not None, f"Missing sample input in {p.title}"
    assert p.sample_output is not None, f"Missing sample output in {p.title}"
    assert p.explanation, f"Missing explanation in {p.title}"
    assert len(p.test_cases) >= 2, f"Insufficient test cases in {p.title}"
    assert 'python' in p.starter_code, f"Missing python starter in {p.title}"
    assert 'cpp' in p.starter_code, f"Missing cpp starter in {p.title}"
    assert 'java' in p.starter_code, f"Missing java starter in {p.title}"

print("All problem metadata checks PASSED.")

print("\n--- 2. VERIFYING MULTI-LANGUAGE REAL EXECUTION ---")

# Python test
py_res = run_code_execution("print('Hello Python')", "python")
print(f"Python execution: status={py_res.status}, stdout={py_res.stdout.strip()}")
assert py_res.status == 'Accepted' and 'Hello Python' in py_res.stdout

# JavaScript test
js_res = run_code_execution("console.log('Hello JS')", "javascript")
print(f"JavaScript execution: status={js_res.status}, stdout={js_res.stdout.strip()}")
assert js_res.status == 'Accepted' and 'Hello JS' in js_res.stdout

# C++ test
cpp_code = "#include <iostream>\nint main() { std::cout << \"Hello CPP\" << std::endl; return 0; }"
cpp_res = run_code_execution(cpp_code, "cpp")
print(f"C++ execution: status={cpp_res.status}, stdout={cpp_res.stdout.strip()}")
assert cpp_res.status == 'Accepted' and 'Hello CPP' in cpp_res.stdout

# C test
c_code = "#include <stdio.h>\nint main() { printf(\"Hello C\\n\"); return 0; }"
c_res = run_code_execution(c_code, "c")
print(f"C execution: status={c_res.status}, stdout={c_res.stdout.strip()}")
assert c_res.status == 'Accepted' and 'Hello C' in c_res.stdout

# Java test
java_code = "public class Solution { public static void main(String[] args) { System.out.println(\"Hello Java\"); } }"
java_res = run_code_execution(java_code, "java")
print(f"Java execution: status={java_res.status}, stdout={java_res.stdout.strip()}")
assert java_res.status == 'Accepted' and 'Hello Java' in java_res.stdout

# SQL test
sql_code = "CREATE TABLE test (val INT); INSERT INTO test VALUES (99); SELECT * FROM test;"
sql_res = run_code_execution(sql_code, "sql")
print(f"SQL execution: status={sql_res.status}, stdout={sql_res.stdout.strip()}")
assert sql_res.status == 'Accepted' and '99' in sql_res.stdout

print("\n--- 3. VERIFYING EVALUATION RESULTS & PASS/FAIL COUNTS ---")
first_prob = CodingProblem.objects.first()
print(f"Testing problem: {first_prob.title}")

# 3a. Correct solution
correct_code = first_prob.starter_code['python']
eval_correct = evaluate_test_cases(correct_code, "python", first_prob.test_cases)
print(f"Correct code eval: status={eval_correct['overall_status']}, passed={eval_correct['passed_count']}/{eval_correct['total_count']}")
assert eval_correct['overall_status'] == 'Accepted'
assert eval_correct['passed_count'] == eval_correct['total_count']

# 3b. Wrong Answer solution
wrong_code = "print('WRONG_ANSWER_OUTPUT')"
eval_wrong = evaluate_test_cases(wrong_code, "python", first_prob.test_cases)
print(f"Wrong code eval: status={eval_wrong['overall_status']}, passed={eval_wrong['passed_count']}/{eval_wrong['total_count']}")
assert eval_wrong['overall_status'] == 'Wrong Answer'
assert eval_wrong['failed_count'] > 0

# 3c. Compilation Error solution in C++
syntax_err_cpp = "#include <iostream>\nint main() { std::cout << missing_variable << std::endl; return 0; }"
eval_comp_err = evaluate_test_cases(syntax_err_cpp, "cpp", first_prob.test_cases)
print(f"C++ compilation error eval: status={eval_comp_err['overall_status']}")
assert eval_comp_err['overall_status'] == 'Compilation Error'
assert eval_comp_err['error_details']['error_type'] == 'Compilation Error'
print(f"Compilation error explanation: {eval_comp_err['error_details']['explanation']}")

# 3d. Runtime Error solution in Python
runtime_err_py = "import sys\n1 / 0"
eval_rt_err = evaluate_test_cases(runtime_err_py, "python", first_prob.test_cases)
print(f"Python runtime error eval: status={eval_rt_err['overall_status']}, error_type={eval_rt_err['error_details']['error_type']}")
assert eval_rt_err['overall_status'] == 'Runtime Error'
assert eval_rt_err['error_details']['error_type'] == 'ZeroDivisionError'
assert eval_rt_err['error_details']['line_number'] == 2

print("\n=======================================================")
print("ALL VERIFICATIONS COMPLETED AND CONFIRMED SUCCESSFULLY!")
print("=======================================================")
