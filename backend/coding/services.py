from datetime import date, timedelta
from django.utils import timezone
from django.db.models import Count
from .models import (
    CodingProblem,
    CodingSubmission,
    UserCodingProgress,
    CodingAchievement,
    UserAchievement,
    CodingActivity
)

# Standard Achievement Definitions
ACHIEVEMENTS_CATALOG = [
    {
        'code': 'FIRST_SOLVED',
        'title': 'First Problem Solved',
        'description': 'Solved your first coding challenge on the platform.',
        'badge_icon': 'Sparkles',
        'points_reward': 50,
    },
    {
        'code': 'SOLVED_10',
        'title': '10 Problems Solved',
        'description': 'Reached the milestone of solving 10 unique problems.',
        'badge_icon': 'Target',
        'points_reward': 100,
    },
    {
        'code': 'SOLVED_50',
        'title': '50 Problems Solved',
        'description': 'Demonstrated real dedication by solving 50 problems.',
        'badge_icon': 'Award',
        'points_reward': 300,
    },
    {
        'code': 'SOLVED_100',
        'title': '100 Problems Solved',
        'description': 'Century club! Solved 100 coding challenges.',
        'badge_icon': 'Crown',
        'points_reward': 500,
    },
    {
        'code': 'STREAK_5',
        'title': '5-Day Streak',
        'description': 'Maintained a coding streak for 5 consecutive days.',
        'badge_icon': 'Flame',
        'points_reward': 100,
    },
    {
        'code': 'STREAK_7',
        'title': '7-Day Streak',
        'description': 'Committed code every single day for an entire week.',
        'badge_icon': 'Zap',
        'points_reward': 200,
    },
    {
        'code': 'EASY_MASTER',
        'title': 'Easy Master',
        'description': 'Solved at least 5 Easy level coding problems.',
        'badge_icon': 'CheckCircle',
        'points_reward': 75,
    },
    {
        'code': 'MEDIUM_MASTER',
        'title': 'Medium Master',
        'description': 'Conquered at least 5 Medium level coding challenges.',
        'badge_icon': 'Shield',
        'points_reward': 150,
    },
    {
        'code': 'HARD_MASTER',
        'title': 'Hard Master',
        'description': 'Proved advanced skills by solving at least 2 Hard challenges.',
        'badge_icon': 'Trophy',
        'points_reward': 250,
    },
    {
        'code': 'MULTI_LANG',
        'title': 'Multi-Language Programmer',
        'description': 'Solved challenges using at least 2 different programming languages.',
        'badge_icon': 'Code',
        'points_reward': 100,
    },
]


def ensure_achievements_exist():
    """Seeds default achievements in database if missing."""
    for item in ACHIEVEMENTS_CATALOG:
        CodingAchievement.objects.get_or_create(
            code=item['code'],
            defaults={
                'title': item['title'],
                'description': item['description'],
                'badge_icon': item['badge_icon'],
                'points_reward': item['points_reward'],
            }
        )


def calculate_user_streak(user):
    """
    Computes current and longest streak from user's daily CodingActivity records.
    """
    activities = CodingActivity.objects.filter(user=user, submission_count__gt=0).order_by('-date')
    dates = [a.date for a in activities]
    if not dates:
        return 0, 0

    today = timezone.localdate()
    yesterday = today - timedelta(days=1)

    # Current streak calculation
    current_streak = 0
    if dates[0] in (today, yesterday):
        current_streak = 1
        expected = dates[0] - timedelta(days=1)
        for d in dates[1:]:
            if d == expected:
                current_streak += 1
                expected -= timedelta(days=1)
            elif d > expected:
                continue
            else:
                break
    else:
        current_streak = 0

    # Longest streak calculation
    longest_streak = 0
    temp_streak = 1 if dates else 0
    sorted_asc = sorted(list(set(dates)))
    for i in range(1, len(sorted_asc)):
        if sorted_asc[i] == sorted_asc[i - 1] + timedelta(days=1):
            temp_streak += 1
        else:
            temp_streak = 1
        if temp_streak > longest_streak:
            longest_streak = temp_streak
    if not longest_streak and dates:
        longest_streak = 1

    return current_streak, max(current_streak, longest_streak)


def check_and_unlock_achievements(user, progress):
    """
    Evaluates achievement unlock criteria and persists unlocks without duplicates.
    Returns list of newly unlocked achievements.
    """
    ensure_achievements_exist()
    newly_unlocked = []

    # Get distinct languages with Accepted submissions
    distinct_languages = CodingSubmission.objects.filter(
        user=user, status='Accepted'
    ).values('language').distinct().count()

    checks = {
        'FIRST_SOLVED': progress.problems_solved_count >= 1,
        'SOLVED_10': progress.problems_solved_count >= 10,
        'SOLVED_50': progress.problems_solved_count >= 50,
        'SOLVED_100': progress.problems_solved_count >= 100,
        'STREAK_5': progress.current_streak >= 5,
        'STREAK_7': progress.current_streak >= 7,
        'EASY_MASTER': progress.easy_solved_count >= 5,
        'MEDIUM_MASTER': progress.medium_solved_count >= 5,
        'HARD_MASTER': progress.hard_solved_count >= 2,
        'MULTI_LANG': distinct_languages >= 2,
    }

    for code, condition_met in checks.items():
        if condition_met:
            achievement = CodingAchievement.objects.filter(code=code).first()
            if achievement:
                user_ach, created = UserAchievement.objects.get_or_create(
                    user=user,
                    achievement=achievement
                )
                if created:
                    progress.points += achievement.points_reward
                    newly_unlocked.append({
                        'code': achievement.code,
                        'title': achievement.title,
                        'description': achievement.description,
                        'badge_icon': achievement.badge_icon,
                        'points_reward': achievement.points_reward,
                    })

    if newly_unlocked:
        progress.save(update_fields=['points'])

    return newly_unlocked


def process_submission_and_update_stats(user, problem, language, code, eval_result):
    """
    Saves submission, updates user progress, daily activity, streaks, and achievements.
    Guarantees no duplicate points for already-solved problems.
    """
    progress, _ = UserCodingProgress.objects.get_or_create(user=user)
    today = timezone.localdate()

    status = eval_result['overall_status']
    passed_cases = eval_result['passed_count']
    total_cases = eval_result['total_count']
    avg_time = eval_result['avg_time']
    memory = eval_result['memory']
    console_out = eval_result['console_output']

    # 1. Create Submission record
    submission = CodingSubmission.objects.create(
        user=user,
        problem=problem,
        language=language,
        code=code,
        status=status,
        passed_test_cases=passed_cases,
        total_test_cases=total_cases,
        execution_time=avg_time,
        memory_usage=memory,
        output=console_out
    )

    # 2. Update attempted problems
    is_first_attempt = not progress.attempted_problems.filter(id=problem.id).exists()
    if is_first_attempt:
        progress.attempted_problems.add(problem)
        progress.problems_attempted_count = progress.attempted_problems.count()

    is_newly_solved = False
    points_awarded = 0

    # 3. If accepted and not previously solved, award points & increment solved metrics
    if status == 'Accepted':
        already_solved = progress.solved_problems.filter(id=problem.id).exists()
        if not already_solved:
            is_newly_solved = True
            progress.solved_problems.add(problem)
            points_awarded = problem.points
            progress.points += points_awarded
            progress.problems_solved_count = progress.solved_problems.count()

            if problem.difficulty == 'Easy':
                progress.easy_solved_count += 1
            elif problem.difficulty == 'Medium':
                progress.medium_solved_count += 1
            elif problem.difficulty == 'Hard':
                progress.hard_solved_count += 1

    # 4. Update Daily Activity
    activity, _ = CodingActivity.objects.get_or_create(user=user, date=today)
    activity.submission_count += 1
    if is_newly_solved:
        activity.solved_count += 1
    activity.save()

    # 5. Update Streaks
    current_streak, longest_streak = calculate_user_streak(user)
    progress.current_streak = current_streak
    progress.longest_streak = max(progress.longest_streak, longest_streak)
    progress.last_active_date = today
    progress.save()

    # 6. Check and award achievements
    new_achievements = check_and_unlock_achievements(user, progress)

    return {
        'submission_id': submission.id,
        'status': status,
        'passed_count': passed_cases,
        'failed_count': eval_result.get('failed_count', total_cases - passed_cases),
        'total_count': total_cases,
        'is_newly_solved': is_newly_solved,
        'points_awarded': points_awarded,
        'new_achievements': new_achievements,
        'execution_time': avg_time,
        'output': console_out,
        'sample_results': eval_result.get('sample_results', []),
        'error_details': eval_result.get('error_details'),
        'first_failed_info': eval_result.get('first_failed_info'),
    }
