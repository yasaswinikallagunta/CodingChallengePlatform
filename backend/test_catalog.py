import sys
sys.path.append('backend')
from coding.problem_catalog.domain_01_arrays import PROBLEMS as D1
from coding.problem_catalog.domain_02_strings import PROBLEMS as D2
from coding.problem_catalog.domain_03_stacks import PROBLEMS as D3
from coding.problem_catalog.domain_04_linked_lists import PROBLEMS as D4
from coding.problem_catalog.domain_05_trees import PROBLEMS as D5
from coding.problem_catalog.domain_06_binary_search import PROBLEMS as D6
from coding.problem_catalog.domain_07_graphs import PROBLEMS as D7
from coding.problem_catalog.domain_08_dp import PROBLEMS as D8
from coding.problem_catalog.domain_09_hash_tables import PROBLEMS as D9
from coding.problem_catalog.domain_10_bitwise import PROBLEMS as D10
from coding.problem_catalog.domain_11_greedy_pq import PROBLEMS as D11
from coding.problem_catalog.domain_12_relational import PROBLEMS as D12
from coding.problem_catalog.domain_13_backtracking import PROBLEMS as D13

for name, probs in [
    ("Domain 1 Arrays", D1),
    ("Domain 2 Strings", D2),
    ("Domain 3 Stacks", D3),
    ("Domain 4 Lists", D4),
    ("Domain 5 Trees", D5),
    ("Domain 6 Binary Search", D6),
    ("Domain 7 Graphs", D7),
    ("Domain 8 Dynamic Programming", D8),
    ("Domain 9 Hash Tables", D9),
    ("Domain 10 Bitwise", D10),
    ("Domain 11 Greedy & PQ", D11),
    ("Domain 12 Relational", D12),
    ("Domain 13 Backtracking", D13),
]:
    print(f"Testing {name}:", len(probs))
    for p in probs:
        out = p['solver'](p['sample_input'])
        assert out == p['sample_output'], f"Mismatch in {p['title_base']}: got '{out}', expected '{p['sample_output']}'"
        for inp in p['test_inputs']:
            res = p['solver'](inp)
            assert res != '', f"Empty result for {p['title_base']} on {inp}"
        for inp in p['variant_inputs']:
            res = p['solver'](inp)
            assert res != '', f"Empty variant result for {p['title_base']} on {inp}"
    print(f"All {len(probs)} {name} problems verified with 100% solver accuracy!")

