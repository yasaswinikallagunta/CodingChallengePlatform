"""
Aggregator and Database Syncer for all 500 Coding Problems.
Builds 260 base problems + 240 advanced variant tier problems (500 total).
Computes exact test case outputs using domain reference solvers.
Generates multi-language starter code for C, Python, Java, C++, JavaScript.
"""

import re
from coding.problem_catalog.starters import generate_starters
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

DOMAIN_METADATA = [
    (D1, "Algorithms", "Array & Math"),
    (D2, "Python", "String & Parsing"),
    (D3, "Data Structures", "Stack & Queue"),
    (D4, "C++", "Pointers & Linked Lists"),
    (D5, "Data Structures", "Binary Trees & BST"),
    (D6, "Algorithms", "Binary Search & Divide Conquer"),
    (D7, "Algorithms", "Graph & BFS/DFS"),
    (D8, "Algorithms", "Dynamic Programming"),
    (D9, "JavaScript", "Hash Table & Maps"),
    (D10, "C", "Bitwise & Memory"),
    (D11, "Java", "Priority Queue & Greedy"),
    (D12, "SQL", "Relational & Aggregates"),
    (D13, "Algorithms", "Backtracking & Recursion"),
]

def build_all_500_problems():
    """
    Constructs exactly 500 problem dictionaries with full metadata,
    deterministic test cases, and multi-language starter code.
    """
    base_items = []
    for domain_probs, category, subdomain in DOMAIN_METADATA:
        for p in domain_probs:
            base_items.append({
                **p,
                "category": category,
                "subdomain": subdomain,
            })

    assert len(base_items) == 260, f"Expected 260 base items, got {len(base_items)}"

    all_500 = []
    seen_slugs = set()

    for idx in range(500):
        if idx < 200:
            difficulty = "Easy"
            points = 10
        elif idx < 400:
            difficulty = "Medium"
            points = 20
        else:
            difficulty = "Hard"
            points = 35

        if idx < 260:
            # Base Problem
            item = base_items[idx]
            title = item["title_base"]
            desc = item["description"]
            sample_in = item["sample_input"]
            sample_out = item["sample_output"]
            explanation = item["explanation"]
            constraints = item["constraints"]

            test_cases = [
                {
                    "input": sample_in,
                    "expected_output": sample_out,
                    "is_hidden": False
                },
                {
                    "input": item["test_inputs"][0],
                    "expected_output": item["solver"](item["test_inputs"][0]),
                    "is_hidden": False
                },
                {
                    "input": item["test_inputs"][1],
                    "expected_output": item["solver"](item["test_inputs"][1]),
                    "is_hidden": True
                },
                {
                    "input": item["variant_inputs"][0],
                    "expected_output": item["solver"](item["variant_inputs"][0]),
                    "is_hidden": True
                }
            ]
            category = item["category"]
            archetype = item.get("starter_archetype", "general")
        else:
            # Advanced Variant Problem (indices 260 to 499 cover base items 0 to 239)
            base_idx = idx - 260
            item = base_items[base_idx]
            title = f"{item['title_base']} II (Advanced Constraints)"
            desc = f"Advanced variant with extended constraints.\n\n{item['description']}"
            sample_in = item["variant_inputs"][0]
            sample_out = item["solver"](sample_in)
            explanation = f"Under advanced constraints, executing the variant input yields '{sample_out}'."
            constraints = f"Extended Constraints:\n{item['constraints']}\nMemory limit: 256 MB\nTime limit: 2.0s"

            test_cases = [
                {
                    "input": sample_in,
                    "expected_output": sample_out,
                    "is_hidden": False
                },
                {
                    "input": item["variant_inputs"][1],
                    "expected_output": item["solver"](item["variant_inputs"][1]),
                    "is_hidden": False
                },
                {
                    "input": item["sample_input"],
                    "expected_output": item["sample_output"],
                    "is_hidden": True
                },
                {
                    "input": item["test_inputs"][0],
                    "expected_output": item["solver"](item["test_inputs"][0]),
                    "is_hidden": True
                }
            ]
            category = item["category"]
            archetype = item.get("starter_archetype", "general")

        slug = re.sub(r'[^a-zA-Z0-9]+', '-', title).strip('-').lower()
        if slug in seen_slugs:
            slug = f"{slug}-{idx + 1}"
        seen_slugs.add(slug)

        starters = generate_starters(archetype, desc)

        all_500.append({
            "index": idx + 1,
            "title": title,
            "slug": slug,
            "category": category,
            "difficulty": difficulty,
            "points": points,
            "problem_statement": desc,
            "input_format": item["input_format"],
            "output_format": item["output_format"],
            "constraints": constraints,
            "sample_input": sample_in,
            "sample_output": sample_out,
            "explanation": explanation,
            "starter_code": starters,
            "test_cases": test_cases,
            "solver": item["solver"]
        })

    return all_500

def sync_database_problems():
    """
    Synchronizes the database with all 500 validated coding challenges,
    updating existing records in place to preserve IDs, primary keys,
    and foreign keys.
    """
    from coding.models import CodingProblem
    from coding.services import ensure_achievements_exist

    ensure_achievements_exist()
    problems = build_all_500_problems()

    existing_rows = list(CodingProblem.objects.order_by('id'))
    total_existing = len(existing_rows)

    if total_existing == 500:
        print(f"Updating {total_existing} existing CodingProblem records in place...")
        for i, existing in enumerate(existing_rows):
            prob_data = problems[i]
            existing.title = prob_data["title"]
            existing.slug = prob_data["slug"]
            existing.category = prob_data["category"]
            existing.difficulty = prob_data["difficulty"]
            existing.points = prob_data["points"]
            existing.problem_statement = prob_data["problem_statement"]
            existing.input_format = prob_data["input_format"]
            existing.output_format = prob_data["output_format"]
            existing.constraints = prob_data["constraints"]
            existing.sample_input = prob_data["sample_input"]
            existing.sample_output = prob_data["sample_output"]
            existing.explanation = prob_data["explanation"]
            existing.starter_code = prob_data["starter_code"]
            existing.test_cases = prob_data["test_cases"]
            existing.save()
        print("All 500 existing records updated in place successfully!")
    else:
        print(f"Found {total_existing} problems in DB (expected 500). Re-seeding...")
        CodingProblem.objects.all().delete()
        model_objs = [
            CodingProblem(
                title=p["title"],
                slug=p["slug"],
                category=p["category"],
                difficulty=p["difficulty"],
                points=p["points"],
                problem_statement=p["problem_statement"],
                input_format=p["input_format"],
                output_format=p["output_format"],
                constraints=p["constraints"],
                sample_input=p["sample_input"],
                sample_output=p["sample_output"],
                explanation=p["explanation"],
                starter_code=p["starter_code"],
                test_cases=p["test_cases"]
            )
            for p in problems
        ]
        CodingProblem.objects.bulk_create(model_objs, batch_size=100)
        print(f"Seeded {len(model_objs)} new CodingProblem records.")

    return problems
