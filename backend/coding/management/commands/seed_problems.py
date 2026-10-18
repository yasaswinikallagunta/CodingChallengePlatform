from django.core.management.base import BaseCommand
from coding.models import CodingProblem
from coding.services import ensure_achievements_exist
from generate_500_problems import generate_problems


class Command(BaseCommand):
    help = 'Seeds 500 unique coding problems across Easy, Medium, and Hard tiers, and achievements'

    def handle(self, *args, **options):
        self.stdout.write("Ensuring achievements catalog is populated...")
        ensure_achievements_exist()

        self.stdout.write("Generating and seeding 500 unique coding challenges...")
        problems = generate_problems()

        CodingProblem.objects.all().delete()
        CodingProblem.objects.bulk_create(problems, batch_size=100)

        total = CodingProblem.objects.count()
        easy = CodingProblem.objects.filter(difficulty="Easy").count()
        medium = CodingProblem.objects.filter(difficulty="Medium").count()
        hard = CodingProblem.objects.filter(difficulty="Hard").count()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully verified 500 problems in DB!\n"
                f"Total: {total}\n"
                f"Easy: {easy}, Medium: {medium}, Hard: {hard}"
            )
        )
