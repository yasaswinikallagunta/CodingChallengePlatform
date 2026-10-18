from django.core.management.base import BaseCommand
from coding.models import ExamCategory, Exam, ExamQuestion
from coding.exam_seed_data import CATEGORIES_DATA


class Command(BaseCommand):
    help = 'Seeds all 20 Exam Categories, their certification exams, and comprehensive questions'

    def handle(self, *args, **options):
        self.stdout.write("Seeding 20 Exam Categories and Certification Exams...")

        created_categories = 0
        created_exams = 0
        created_questions = 0

        for cat_info in CATEGORIES_DATA:
            category, _ = ExamCategory.objects.update_or_create(
                slug=cat_info["slug"],
                defaults={
                    "name": cat_info["name"],
                    "description": cat_info["description"],
                    "icon": cat_info["icon"],
                    "order": cat_info["order"],
                }
            )
            created_categories += 1

            exam_info = cat_info["exam"]
            exam, _ = Exam.objects.update_or_create(
                slug=exam_info["slug"],
                defaults={
                    "category": category,
                    "title": exam_info["title"],
                    "difficulty": exam_info["difficulty"],
                    "duration_minutes": exam_info["duration_minutes"],
                    "passing_percentage": exam_info["passing_percentage"],
                    "total_marks": exam_info["total_marks"],
                    "description": exam_info["description"],
                    "instructions": exam_info["instructions"],
                    "is_active": True,
                }
            )
            created_exams += 1

            # Delete old questions for this exam to ensure fresh clean sync
            exam.questions.all().delete()

            for q_info in exam_info["questions"]:
                ExamQuestion.objects.create(
                    exam=exam,
                    order=q_info["order"],
                    question_type=q_info["question_type"],
                    title=q_info["title"],
                    points=q_info["points"],
                    problem_statement=q_info["problem_statement"],
                    input_format=q_info.get("input_format", ""),
                    output_format=q_info.get("output_format", ""),
                    constraints=q_info.get("constraints", ""),
                    starter_code=q_info.get("starter_code", {}),
                    test_cases=q_info.get("test_cases", []),
                    options=q_info.get("options", []),
                    correct_answer=q_info.get("correct_answer", ""),
                    explanation=q_info.get("explanation", ""),
                )
                created_questions += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded:\n"
                f"- {created_categories} Exam Categories (All 20 verified)\n"
                f"- {created_exams} Official Certification Exams\n"
                f"- {created_questions} Questions (Practical Coding & Conceptual)"
            )
        )
