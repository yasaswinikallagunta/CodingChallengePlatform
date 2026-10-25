import sys
sys.path.append('backend')
from coding.problem_catalog.builder import build_all_500_problems

problems = build_all_500_problems()
print(f"Total problems generated: {len(problems)}")
assert len(problems) == 500

easy = sum(1 for p in problems if p['difficulty'] == 'Easy')
medium = sum(1 for p in problems if p['difficulty'] == 'Medium')
hard = sum(1 for p in problems if p['difficulty'] == 'Hard')
print(f"Difficulties: Easy={easy}, Medium={medium}, Hard={hard} (Total: {easy+medium+hard})")
assert easy + medium + hard == 500

# Verify every single problem
for i, p in enumerate(problems):
    title = p['title']
    assert len(p['test_cases']) >= 4, f"Problem {title} has fewer than 4 test cases"
    assert p['sample_input'] != "", f"Problem {title} has empty sample input"
    assert p['sample_output'] != "", f"Problem {title} has empty sample output"
    assert p['problem_statement'] != "", f"Problem {title} has empty statement"
    assert p['input_format'] != "", f"Problem {title} has empty input format"
    assert p['output_format'] != "", f"Problem {title} has empty output format"
    assert p['constraints'] != "", f"Problem {title} has empty constraints"
    assert p['explanation'] != "", f"Problem {title} has empty explanation"

    # Check starter code for all 5 languages
    for lang in ['python', 'c', 'cpp', 'java', 'javascript']:
        assert lang in p['starter_code'], f"Missing starter for {lang} in {title}"
        assert len(p['starter_code'][lang]) > 20, f"Starter code too short for {lang} in {title}"

    # Verify each test case
    for tc_idx, tc in enumerate(p['test_cases']):
        assert tc['expected_output'] != "", f"Empty expected_output for {title} tc {tc_idx}"
        # verify solver produces exactly expected_output
        res = p['solver'](tc['input'])
        assert res == tc['expected_output'], f"Solver mismatch for {title} on tc {tc_idx}: got '{res}', expected '{tc['expected_output']}'"

print("100% OF ALL 500 PROBLEMS VERIFIED WITH SOLVER ACCURACY AND COMPREHENSIVE TEST CASES!")
