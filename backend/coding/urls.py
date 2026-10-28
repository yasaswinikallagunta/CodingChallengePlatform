from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    CurrentUserProfileView,
    ProblemListView,
    ProblemDetailView,
    RunCodeView,
    SubmitCodeView,
    SubmissionHistoryView,
    DashboardStatsView,
    PerformanceAnalysisView,
    AchievementListView,
    ExamCategoryListView,
    ExamListView,
    ExamDetailView,
    ExamStartView,
    ExamSessionView,
    ExamSaveAnswerView,
    ExamRunCodeView,
    ExamSubmitView,
    ExamResultView,
    UserCertificatesListView,
    CertificateDetailView,
    CertificateDownloadPDFView,
    CourseProgressView,
    CourseSaveProgressView,
    CourseResetProgressView,
)

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/register', RegisterView.as_view(), name='auth-register-noslash'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/login', LoginView.as_view(), name='auth-login-noslash'),
    path('auth/me/', CurrentUserProfileView.as_view(), name='auth-me'),
    path('auth/me', CurrentUserProfileView.as_view(), name='auth-me-noslash'),

    # Problems
    path('problems/', ProblemListView.as_view(), name='problem-list'),
    path('problems/<str:identifier>/', ProblemDetailView.as_view(), name='problem-detail'),
    path('problems/<str:identifier>/run/', RunCodeView.as_view(), name='problem-run'),
    path('problems/<str:identifier>/submit/', SubmitCodeView.as_view(), name='problem-submit'),

    # Submissions
    path('submissions/', SubmissionHistoryView.as_view(), name='submission-history'),

    # Dashboard & Analytics
    path('dashboard/stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('progress/analysis/', PerformanceAnalysisView.as_view(), name='performance-analysis'),

    # Achievements
    path('achievements/', AchievementListView.as_view(), name='achievements-list'),

    # Exams & Certifications
    path('exams/categories/', ExamCategoryListView.as_view(), name='exam-categories'),
    path('exams/attempts/<int:attempt_id>/save-answer/', ExamSaveAnswerView.as_view(), name='exam-save-answer'),
    path('exams/attempts/<int:attempt_id>/run-code/', ExamRunCodeView.as_view(), name='exam-run-code'),
    path('exams/attempts/<int:attempt_id>/submit/', ExamSubmitView.as_view(), name='exam-submit'),
    path('exams/attempts/<int:attempt_id>/result/', ExamResultView.as_view(), name='exam-result'),
    path('exams/attempts/<int:attempt_id>/', ExamSessionView.as_view(), name='exam-session'),
    path('exams/<slug:slug>/start/', ExamStartView.as_view(), name='exam-start'),
    path('exams/<slug:slug>/', ExamDetailView.as_view(), name='exam-detail'),
    path('exams/', ExamListView.as_view(), name='exam-list'),

    # Certificates
    path('certificates/', UserCertificatesListView.as_view(), name='user-certificates'),
    path('certificates/<str:certificate_id>/', CertificateDetailView.as_view(), name='certificate-detail'),
    path('certificates/<str:certificate_id>/download/', CertificateDownloadPDFView.as_view(), name='certificate-download'),

    # Course Learning & Progress Tracking
    path('courses/<str:course_slug>/progress/', CourseProgressView.as_view(), name='course-progress'),
    path('courses/<str:course_slug>/save-progress/', CourseSaveProgressView.as_view(), name='course-save-progress'),
    path('courses/<str:course_slug>/reset-progress/', CourseResetProgressView.as_view(), name='course-reset-progress'),
]

