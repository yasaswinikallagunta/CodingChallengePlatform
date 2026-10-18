from django.contrib import admin
from .models import (
    CodingProblem,
    CodingSubmission,
    UserCodingProgress,
    CodingAchievement,
    UserAchievement,
    CodingActivity
)


@admin.register(CodingProblem)
class CodingProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'difficulty', 'points', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('title', 'problem_statement')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CodingSubmission)
class CodingSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'language', 'status', 'passed_test_cases', 'total_test_cases', 'submitted_at')
    list_filter = ('status', 'language', 'submitted_at')
    search_fields = ('user__username', 'problem__title')


@admin.register(UserCodingProgress)
class UserCodingProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'problems_solved_count', 'problems_attempted_count', 'current_streak', 'longest_streak')
    search_fields = ('user__username',)


@admin.register(CodingAchievement)
class CodingAchievementAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'points_reward', 'badge_icon')
    search_fields = ('code', 'title')


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'unlocked_at')
    list_filter = ('achievement',)
    search_fields = ('user__username', 'achievement__title')


@admin.register(CodingActivity)
class CodingActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'submission_count', 'solved_count')
    list_filter = ('date',)
    search_fields = ('user__username',)
