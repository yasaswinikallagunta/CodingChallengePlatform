import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from coding.models import CodingProblem
from coding.services import ensure_achievements_exist
from coding.problem_catalog.builder import build_all_500_problems, sync_database_problems

def generate_problems():
    """Generates exactly 500 unique coding challenges as model objects."""
    problems_data = build_all_500_problems()
    problem_objs = []
    for p in problems_data:
        problem_objs.append(CodingProblem(
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
            test_cases=p["test_cases"],
        ))
    return problem_objs

def main():
    print("Synchronizing 500 problems in database...")
    sync_database_problems()
    total = CodingProblem.objects.count()
    easy = CodingProblem.objects.filter(difficulty="Easy").count()
    medium = CodingProblem.objects.filter(difficulty="Medium").count()
    hard = CodingProblem.objects.filter(difficulty="Hard").count()

    print(f"Total problems in DB: {total}")
    print(f"Easy: {easy}, Medium: {medium}, Hard: {hard}")

if __name__ == '__main__':
    main()
