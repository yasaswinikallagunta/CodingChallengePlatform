import os
import sys
import django

sys.path.append('backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from coding.models import CodingProblem
from coding.execution import evaluate_test_cases, run_code_execution

def test_problem_1():
    print("=" * 60)
    print("TESTING PROBLEM 1: Two Sum Variant across C, Python, Java, C++, JS")
    print("=" * 60)
    p1 = CodingProblem.objects.get(id=514)
    assert p1.title == "Two Sum Variant"
    all_tc = p1.test_cases
    print(f"Problem 1 test cases count: {len(all_tc)}")
    print(f"Sample input:\n{p1.sample_input}")
    print(f"Sample output: {p1.sample_output}")

    # 1. Python Correct
    py_code_correct = (
        "import sys\n"
        "tokens = sys.stdin.read().split()\n"
        "target = int(tokens[0])\n"
        "n = int(tokens[1])\n"
        "nums = [int(x) for x in tokens[2:2+n]]\n"
        "seen = {}\n"
        "for i, num in enumerate(nums):\n"
        "    diff = target - num\n"
        "    if diff in seen:\n"
        "        print(f'{seen[diff]} {i}')\n"
        "        break\n"
        "    seen[num] = i\n"
    )
    res = evaluate_test_cases(py_code_correct, 'python', all_tc)
    print(f"Python Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # Python Wrong
    py_code_wrong = "print('99 99')"
    res = evaluate_test_cases(py_code_wrong, 'python', all_tc)
    print(f"Python Wrong: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Wrong Answer'

    # 2. C Correct
    c_code_correct = (
        "#include <stdio.h>\n"
        "#include <stdlib.h>\n"
        "int main() {\n"
        "    int target, n;\n"
        "    if (scanf(\"%d %d\", &target, &n) != 2) return 0;\n"
        "    int *arr = (int*)malloc(n * sizeof(int));\n"
        "    for (int i = 0; i < n; i++) scanf(\"%d\", &arr[i]);\n"
        "    for (int i = 0; i < n; i++) {\n"
        "        for (int j = i + 1; j < n; j++) {\n"
        "            if (arr[i] + arr[j] == target) {\n"
        "                printf(\"%d %d\\n\", i, j);\n"
        "                free(arr);\n"
        "                return 0;\n"
        "            }\n"
        "        }\n"
        "    }\n"
        "    free(arr);\n"
        "    return 0;\n"
        "}\n"
    )
    for i, tc in enumerate(all_tc):
        tc_res = run_code_execution(c_code_correct, 'c', tc['input'])
        print(f"  TC {i}: exp={repr(tc['expected_output'])}, got={repr(tc_res.stdout.strip())}, status={tc_res.status}")
    res = evaluate_test_cases(c_code_correct, 'c', all_tc)
    print(f"C Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # C Wrong
    c_code_wrong = (
        "#include <stdio.h>\n"
        "int main() { printf(\"0 0\\n\"); return 0; }\n"
    )
    res = evaluate_test_cases(c_code_wrong, 'c', all_tc)
    print(f"C Wrong: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Wrong Answer'

    # 3. C++ Correct
    cpp_code_correct = (
        "#include <iostream>\n"
        "#include <vector>\n"
        "#include <unordered_map>\n"
        "using namespace std;\n"
        "int main() {\n"
        "    int target, n;\n"
        "    if (!(cin >> target >> n)) return 0;\n"
        "    unordered_map<int, int> seen;\n"
        "    for (int i = 0; i < n; i++) {\n"
        "        int val;\n"
        "        cin >> val;\n"
        "        int diff = target - val;\n"
        "        if (seen.count(diff)) {\n"
        "            cout << seen[diff] << \" \" << i << endl;\n"
        "            return 0;\n"
        "        }\n"
        "        seen[val] = i;\n"
        "    }\n"
        "    return 0;\n"
        "}\n"
    )
    res = evaluate_test_cases(cpp_code_correct, 'cpp', all_tc)
    print(f"C++ Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}, sample_res={res.get('sample_results')}")
    assert res['overall_status'] == 'Accepted'

    # C++ Wrong
    cpp_code_wrong = (
        "#include <iostream>\n"
        "using namespace std;\n"
        "int main() { cout << \"-1 -1\" << endl; return 0; }\n"
    )
    res = evaluate_test_cases(cpp_code_wrong, 'cpp', all_tc)
    print(f"C++ Wrong: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Wrong Answer'

    # 4. JavaScript Correct
    js_code_correct = (
        "const fs = require('fs');\n"
        "const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n"
        "const target = parseInt(tokens[0], 10);\n"
        "const n = parseInt(tokens[1], 10);\n"
        "const nums = tokens.slice(2, 2 + n).map(Number);\n"
        "const seen = new Map();\n"
        "for (let i = 0; i < nums.length; i++) {\n"
        "    const diff = target - nums[i];\n"
        "    if (seen.has(diff)) {\n"
        "        console.log(`${seen.get(diff)} ${i}`);\n"
        "        break;\n"
        "    }\n"
        "    seen.set(nums[i], i);\n"
        "}\n"
    )
    res = evaluate_test_cases(js_code_correct, 'javascript', all_tc)
    print(f"JavaScript Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # JavaScript Wrong
    js_code_wrong = "console.log('10 20');"
    res = evaluate_test_cases(js_code_wrong, 'javascript', all_tc)
    print(f"JavaScript Wrong: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Wrong Answer'

    # 5. Java Correct
    java_code_correct = (
        "import java.util.*;\n"
        "public class Solution {\n"
        "    public static void main(String[] args) {\n"
        "        Scanner sc = new Scanner(System.in);\n"
        "        if (!sc.hasNextInt()) return;\n"
        "        int target = sc.nextInt();\n"
        "        int n = sc.nextInt();\n"
        "        Map<Integer, Integer> seen = new HashMap<>();\n"
        "        for (int i = 0; i < n; i++) {\n"
        "            int val = sc.nextInt();\n"
        "            int diff = target - val;\n"
        "            if (seen.containsKey(diff)) {\n"
        "                System.out.println(seen.get(diff) + \" \" + i);\n"
        "                return;\n"
        "            }\n"
        "            seen.put(val, i);\n"
        "        }\n"
        "    }\n"
        "}\n"
    )
    res = evaluate_test_cases(java_code_correct, 'java', all_tc)
    print(f"Java Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # Java Wrong
    java_code_wrong = (
        "public class Solution {\n"
        "    public static void main(String[] args) {\n"
        "        System.out.println(\"0 0\");\n"
        "    }\n"
        "}\n"
    )
    res = evaluate_test_cases(java_code_wrong, 'java', all_tc)
    print(f"Java Wrong: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Wrong Answer'

    print("ALL 5 LANGUAGES VERIFIED FOR PROBLEM 1 (BOTH CORRECT & WRONG LOGIC)!\n")

def test_problem_2():
    print("=" * 60)
    print("TESTING PROBLEM 2: Prefix Sum Queries across C, Python, Java, C++, JS")
    print("=" * 60)
    p2 = CodingProblem.objects.get(id=515)
    assert p2.title == "Prefix Sum Queries"
    all_tc = p2.test_cases
    print(f"Problem 2 test cases count: {len(all_tc)}")
    print(f"Sample input:\n{p2.sample_input}")
    print(f"Sample output: {p2.sample_output}")

    # Python Correct
    py_code = (
        "import sys\n"
        "tokens = sys.stdin.read().split()\n"
        "n = int(tokens[0])\n"
        "arr = [int(x) for x in tokens[1:1+n]]\n"
        "l = int(tokens[1+n])\n"
        "r = int(tokens[2+n])\n"
        "print(sum(arr[l:r+1]))\n"
    )
    res = evaluate_test_cases(py_code, 'python', all_tc)
    print(f"Python Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # Python Wrong
    py_wrong = "print(0)"
    res = evaluate_test_cases(py_wrong, 'python', all_tc)
    print(f"Python Wrong: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Wrong Answer'

    # C Correct
    c_code = (
        "#include <stdio.h>\n"
        "#include <stdlib.h>\n"
        "int main() {\n"
        "    int n;\n"
        "    if (scanf(\"%d\", &n) != 1) return 0;\n"
        "    int *arr = (int*)malloc(n * sizeof(int));\n"
        "    for (int i = 0; i < n; i++) scanf(\"%d\", &arr[i]);\n"
        "    int l, r;\n"
        "    scanf(\"%d %d\", &l, &r);\n"
        "    long long sum = 0;\n"
        "    for (int i = l; i <= r; i++) sum += arr[i];\n"
        "    printf(\"%lld\\n\", sum);\n"
        "    free(arr);\n"
        "    return 0;\n"
        "}\n"
    )
    res = evaluate_test_cases(c_code, 'c', all_tc)
    print(f"C Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # C++ Correct
    cpp_code = (
        "#include <iostream>\n"
        "#include <vector>\n"
        "using namespace std;\n"
        "int main() {\n"
        "    int n;\n"
        "    if (!(cin >> n)) return 0;\n"
        "    vector<int> arr(n);\n"
        "    for (int i = 0; i < n; i++) cin >> arr[i];\n"
        "    int l, r;\n"
        "    cin >> l >> r;\n"
        "    long long sum = 0;\n"
        "    for (int i = l; i <= r; i++) sum += arr[i];\n"
        "    cout << sum << endl;\n"
        "    return 0;\n"
        "}\n"
    )
    res = evaluate_test_cases(cpp_code, 'cpp', all_tc)
    print(f"C++ Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # JS Correct
    js_code = (
        "const fs = require('fs');\n"
        "const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n"
        "const n = parseInt(tokens[0], 10);\n"
        "const arr = tokens.slice(1, 1 + n).map(Number);\n"
        "const l = parseInt(tokens[1 + n], 10);\n"
        "const r = parseInt(tokens[2 + n], 10);\n"
        "let sum = 0;\n"
        "for (let i = l; i <= r; i++) sum += arr[i];\n"
        "console.log(sum);\n"
    )
    res = evaluate_test_cases(js_code, 'javascript', all_tc)
    print(f"JavaScript Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    # Java Correct
    java_code = (
        "import java.util.*;\n"
        "public class Solution {\n"
        "    public static void main(String[] args) {\n"
        "        Scanner sc = new Scanner(System.in);\n"
        "        if (!sc.hasNextInt()) return;\n"
        "        int n = sc.nextInt();\n"
        "        int[] arr = new int[n];\n"
        "        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n"
        "        int l = sc.nextInt();\n"
        "        int r = sc.nextInt();\n"
        "        long sum = 0;\n"
        "        for (int i = l; i <= r; i++) sum += arr[i];\n"
        "        System.out.println(sum);\n"
        "    }\n"
        "}\n"
    )
    res = evaluate_test_cases(java_code, 'java', all_tc)
    print(f"Java Correct: status={res['overall_status']}, passed={res['passed_count']}/{res['total_count']}")
    assert res['overall_status'] == 'Accepted'

    print("ALL 5 LANGUAGES VERIFIED FOR PROBLEM 2!\n")

if __name__ == '__main__':
    test_problem_1()
    test_problem_2()
    print("ALL MULTI-LANGUAGE EXECUTION AND VALIDATION TESTS PASSED 100%!")
