from datetime import timedelta
from django.utils import timezone
from django.db.models import Q, Count, Case, When, IntegerField
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import (
    CodingProblem,
    CodingSubmission,
    UserCodingProgress,
    CodingAchievement,
    UserAchievement,
    CodingActivity,
    CourseProgress
)
from .serializers import (
    UserRegistrationSerializer,
    UserSerializer,
    CodingProblemListSerializer,
    CodingProblemDetailSerializer,
    CodingSubmissionSerializer,
    UserCodingProgressSerializer,
    CodingAchievementSerializer,
    CodingActivitySerializer,
    CourseProgressSerializer
)
from .execution import run_code_execution, evaluate_test_cases, parse_error_details
from .services import (
    process_submission_and_update_stats,
    ensure_achievements_exist,
    calculate_user_streak
)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Registration successful! Welcome to the Coding Challenge Platform.',
                'user': UserSerializer(user).data,
                'tokens': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '')

        if not username or not password:
            return Response(
                {'detail': 'Please provide both username and password.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Allow logging in with either username or email
        user = authenticate(username=username, password=password)
        if not user:
            # Check if username passed is actually an email
            try:
                user_obj = User.objects.get(email__iexact=username)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if not user:
            return Response(
                {'detail': 'Invalid credentials. Please verify your username and password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Ensure progress record exists
        UserCodingProgress.objects.get_or_create(user=user)

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful.',
            'user': UserSerializer(user).data,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)


class CurrentUserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        progress, _ = UserCodingProgress.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        progress_data = UserCodingProgressSerializer(progress).data
        return Response({
            'user': user_data,
            'progress': progress_data
        })


class ProblemListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = CodingProblem.objects.all()

        # Search query
        search_query = request.query_params.get('search', '').strip()
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(problem_statement__icontains=search_query) |
                Q(category__icontains=search_query)
            )

        # Category filter
        category = request.query_params.get('category', '').strip()
        if category and category.lower() != 'all':
            queryset = queryset.filter(category__iexact=category)

        # Difficulty filter
        difficulty = request.query_params.get('difficulty', '').strip()
        if difficulty and difficulty.lower() != 'all':
            queryset = queryset.filter(difficulty__iexact=difficulty)

        # Solved / Unsolved filter for authenticated users
        status_filter = request.query_params.get('status', '').strip().lower()
        if request.user.is_authenticated and status_filter in ('solved', 'unsolved'):
            progress, _ = UserCodingProgress.objects.get_or_create(user=request.user)
            solved_ids = progress.solved_problems.values_list('id', flat=True)
            if status_filter == 'solved':
                queryset = queryset.filter(id__in=solved_ids)
            elif status_filter == 'unsolved':
                queryset = queryset.exclude(id__in=solved_ids)

        # Sorting
        sort_by = request.query_params.get('sort', 'id').strip()
        if sort_by == 'points_asc':
            queryset = queryset.order_by('points', 'id')
        elif sort_by == 'points_desc':
            queryset = queryset.order_by('-points', 'id')
        elif sort_by == 'title_asc':
            queryset = queryset.order_by('title')
        elif sort_by == 'difficulty':
            # Custom difficulty ordering
            queryset = queryset.order_by(
                Case(
                    When(difficulty='Easy', then=1),
                    When(difficulty='Medium', then=2),
                    When(difficulty='Hard', then=3),
                    default=4,
                    output_field=IntegerField(),
                )
            )
        else:
            queryset = queryset.order_by('id')

        # Pagination
        page_size = int(request.query_params.get('page_size', 10))
        page = int(request.query_params.get('page', 1))
        total_count = queryset.count()
        start = (page - 1) * page_size
        end = start + page_size

        serializer = CodingProblemListSerializer(
            queryset[start:end],
            many=True,
            context={'request': request}
        )

        return Response({
            'count': total_count,
            'page': page,
            'page_size': page_size,
            'total_pages': (total_count + page_size - 1) // page_size if page_size > 0 else 1,
            'results': serializer.data
        })


class ProblemDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, identifier):
        if identifier.isdigit():
            problem = get_object_or_404(CodingProblem, id=int(identifier))
        else:
            problem = get_object_or_404(CodingProblem, slug=identifier)

        serializer = CodingProblemDetailSerializer(problem, context={'request': request})
        return Response(serializer.data)


class RunCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, identifier):
        if identifier.isdigit():
            problem = get_object_or_404(CodingProblem, id=int(identifier))
        else:
            problem = get_object_or_404(CodingProblem, slug=identifier)

        code = request.data.get('code', '')
        language = request.data.get('language', 'python')
        custom_input = request.data.get('custom_input', None)

        if not code.strip():
            return Response({'detail': 'Code cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

        # If custom input is supplied, run against custom input
        if custom_input is not None:
            exec_res = run_code_execution(code, language, custom_input)
            err_details = parse_error_details(
                exec_res.status,
                exec_res.compile_output,
                exec_res.stderr or exec_res.error_message,
                exec_res.stdout
            )
            return Response({
                'mode': 'custom_input',
                'status': exec_res.status,
                'stdout': exec_res.stdout,
                'stderr': exec_res.stderr,
                'compile_output': exec_res.compile_output,
                'execution_time': exec_res.execution_time,
                'error_message': exec_res.error_message,
                'error_details': err_details,
                'output': exec_res.stdout or exec_res.stderr or exec_res.error_message or exec_res.compile_output,
            })

        # Otherwise evaluate against visible sample test cases
        visible_cases = [tc for tc in problem.test_cases if not tc.get('is_hidden', False)]
        if not visible_cases and problem.test_cases:
            visible_cases = [problem.test_cases[0]]

        eval_result = evaluate_test_cases(code, language, visible_cases)
        return Response({
            'mode': 'sample_test_cases',
            'status': eval_result['overall_status'],
            'passed_count': eval_result['passed_count'],
            'failed_count': eval_result['failed_count'],
            'total_count': eval_result['total_count'],
            'sample_results': eval_result['sample_results'],
            'avg_time': eval_result['avg_time'],
            'output': eval_result['console_output'],
            'error_details': eval_result.get('error_details'),
            'first_failed_info': eval_result.get('first_failed_info'),
        })


class SubmitCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, identifier):
        if identifier.isdigit():
            problem = get_object_or_404(CodingProblem, id=int(identifier))
        else:
            problem = get_object_or_404(CodingProblem, slug=identifier)

        code = request.data.get('code', '')
        language = request.data.get('language', 'python')

        if not code.strip():
            return Response({'detail': 'Code cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

        # Evaluate against ALL test cases (including hidden)
        all_test_cases = problem.test_cases or []
        eval_result = evaluate_test_cases(code, language, all_test_cases)

        # Process submission, update progress and awards
        result_data = process_submission_and_update_stats(
            user=request.user,
            problem=problem,
            language=language,
            code=code,
            eval_result=eval_result
        )

        return Response(result_data, status=status.HTTP_200_OK)


class SubmissionHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = CodingSubmission.objects.filter(user=request.user)

        # Filter by problem
        problem_id = request.query_params.get('problem_id')
        if problem_id:
            queryset = queryset.filter(problem_id=problem_id)

        # Filter by language
        language = request.query_params.get('language')
        if language and language.lower() != 'all':
            queryset = queryset.filter(language__iexact=language)

        # Filter by status
        sub_status = request.query_params.get('status')
        if sub_status and sub_status.lower() != 'all':
            queryset = queryset.filter(status__iexact=sub_status)

        # Pagination
        page_size = int(request.query_params.get('page_size', 10))
        page = int(request.query_params.get('page', 1))
        total_count = queryset.count()
        start = (page - 1) * page_size
        end = start + page_size

        serializer = CodingSubmissionSerializer(queryset[start:end], many=True)
        return Response({
            'count': total_count,
            'page': page,
            'page_size': page_size,
            'total_pages': (total_count + page_size - 1) // page_size if page_size > 0 else 1,
            'results': serializer.data
        })


class DashboardStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        progress, _ = UserCodingProgress.objects.get_or_create(user=user)
        ensure_achievements_exist()

        total_problems = CodingProblem.objects.count()
        easy_total = CodingProblem.objects.filter(difficulty='Easy').count()
        medium_total = CodingProblem.objects.filter(difficulty='Medium').count()
        hard_total = CodingProblem.objects.filter(difficulty='Hard').count()

        solved_count = progress.problems_solved_count
        completion_pct = round((solved_count / total_problems * 100), 1) if total_problems > 0 else 0

        # Weekly Activity (Past 7 days)
        today = timezone.localdate()
        past_week_dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
        activity_dict = {
            a.date: a for a in CodingActivity.objects.filter(user=user, date__in=past_week_dates)
        }
        weekly_activity = []
        for d in past_week_dates:
            act = activity_dict.get(d)
            weekly_activity.append({
                'day': d.strftime('%a'),
                'date': str(d),
                'submissions': act.submission_count if act else 0,
                'solved': act.solved_count if act else 0
            })

        # Activity Heatmap (Past 60 days)
        past_60_days = [today - timedelta(days=i) for i in range(59, -1, -1)]
        heatmap_dict = {
            a.date: a.submission_count for a in CodingActivity.objects.filter(user=user, date__in=past_60_days)
        }
        heatmap_data = [{'date': str(d), 'count': heatmap_dict.get(d, 0)} for d in past_60_days]

        # Category performance
        categories = ['Python', 'C', 'C++', 'Java', 'JavaScript', 'Data Structures', 'Algorithms', 'SQL']
        category_performance = []
        for cat in categories:
            cat_total = CodingProblem.objects.filter(category=cat).count()
            cat_solved = progress.solved_problems.filter(category=cat).count()
            category_performance.append({
                'category': cat,
                'total': cat_total,
                'solved': cat_solved,
                'percentage': round((cat_solved / cat_total * 100), 1) if cat_total > 0 else 0
            })

        # Recent Submissions (last 5)
        recent_subs = CodingSubmission.objects.filter(user=user).order_by('-submitted_at')[:5]
        recent_submissions_data = CodingSubmissionSerializer(recent_subs, many=True).data

        # Recently Attempted Problems
        recently_attempted = progress.attempted_problems.all().order_by('-updated_at')[:4]
        recent_problems_data = CodingProblemListSerializer(
            recently_attempted, many=True, context={'request': request}
        ).data

        # Recommended Challenges (Unsolved problems)
        recommended = CodingProblem.objects.exclude(
            id__in=progress.solved_problems.values_list('id', flat=True)
        ).order_by('id')[:3]
        recommended_data = CodingProblemListSerializer(
            recommended, many=True, context={'request': request}
        ).data

        # Recent Unlocked Achievements
        unlocked_achievements = UserAchievement.objects.filter(user=user).order_by('-unlocked_at')[:4]
        unlocked_data = [
            {
                'title': ua.achievement.title,
                'description': ua.achievement.description,
                'badge_icon': ua.achievement.badge_icon,
                'points': ua.achievement.points_reward,
                'unlocked_at': ua.unlocked_at
            }
            for ua in unlocked_achievements
        ]

        return Response({
            'overview': {
                'total_problems': total_problems,
                'problems_solved': solved_count,
                'problems_attempted': progress.problems_attempted_count,
                'easy_solved': progress.easy_solved_count,
                'easy_total': easy_total,
                'medium_solved': progress.medium_solved_count,
                'medium_total': medium_total,
                'hard_solved': progress.hard_solved_count,
                'hard_total': hard_total,
                'completion_percentage': completion_pct,
                'points_earned': progress.points,
                'current_streak': progress.current_streak,
                'longest_streak': progress.longest_streak,
                'achievements_unlocked': UserAchievement.objects.filter(user=user).count(),
                'total_achievements': CodingAchievement.objects.count(),
            },
            'weekly_activity': weekly_activity,
            'heatmap_data': heatmap_data,
            'category_performance': category_performance,
            'recent_submissions': recent_submissions_data,
            'recently_attempted': recent_problems_data,
            'recommended_challenges': recommended_data,
            'recent_achievements': unlocked_data,
        })


class PerformanceAnalysisView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        progress, _ = UserCodingProgress.objects.get_or_create(user=user)

        total_submissions = CodingSubmission.objects.filter(user=user).count()
        accepted_submissions = CodingSubmission.objects.filter(user=user, status='Accepted').count()
        acceptance_rate = round((accepted_submissions / total_submissions * 100), 1) if total_submissions > 0 else 0.0

        # Language-wise statistics
        language_stats = CodingSubmission.objects.filter(user=user).values('language').annotate(
            total=Count('id'),
            accepted=Count(Case(When(status='Accepted', then=1), output_field=IntegerField()))
        )

        # Average attempts before solving
        solved_problems = progress.solved_problems.all()
        attempts_list = []
        for p in solved_problems:
            att_count = CodingSubmission.objects.filter(user=user, problem=p).count()
            if att_count > 0:
                attempts_list.append(att_count)
        avg_attempts = round(sum(attempts_list) / len(attempts_list), 1) if attempts_list else 0.0

        # Category strengths
        categories = ['Python', 'C', 'C++', 'Java', 'JavaScript', 'Data Structures', 'Algorithms', 'SQL']
        category_stats = []
        for cat in categories:
            total_cat = CodingProblem.objects.filter(category=cat).count()
            solved_cat = progress.solved_problems.filter(category=cat).count()
            pct = round((solved_cat / total_cat * 100), 1) if total_cat > 0 else 0
            category_stats.append({
                'category': cat,
                'total': total_cat,
                'solved': solved_cat,
                'percentage': pct
            })

        sorted_by_pct = sorted(category_stats, key=lambda x: x['percentage'], reverse=True)
        strongest = [c for c in sorted_by_pct if c['solved'] > 0][:3]
        needs_improvement = [c for c in reversed(sorted_by_pct) if c['total'] > 0][:3]

        return Response({
            'total_submissions': total_submissions,
            'accepted_submissions': accepted_submissions,
            'acceptance_rate': acceptance_rate,
            'problems_solved': progress.problems_solved_count,
            'problems_attempted': progress.problems_attempted_count,
            'current_streak': progress.current_streak,
            'longest_streak': progress.longest_streak,
            'avg_attempts_to_solve': avg_attempts,
            'language_breakdown': list(language_stats),
            'category_breakdown': category_stats,
            'strongest_categories': strongest,
            'topics_needing_improvement': needs_improvement,
        })


class AchievementListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ensure_achievements_exist()
        achievements = CodingAchievement.objects.all()
        serializer = CodingAchievementSerializer(
            achievements, many=True, context={'user': request.user}
        )
        return Response(serializer.data)


# ============================================================================
# EXAMS & CERTIFICATIONS VIEWS
# ============================================================================

from django.http import HttpResponse
from .models import (
    ExamCategory,
    Exam,
    ExamQuestion,
    ExamAttempt,
    ExamAnswer,
    ExamResult,
    Certificate
)
from .serializers import (
    ExamCategorySerializer,
    ExamListSerializer,
    ExamDetailSerializer,
    ExamAttemptSessionSerializer,
    ExamResultDetailSerializer,
    CertificateSerializer
)
from .certificate_generator import generate_certificate_pdf


class ExamCategoryListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        categories = ExamCategory.objects.all().order_by('order', 'name')
        serializer = ExamCategorySerializer(categories, many=True)
        return Response(serializer.data)


class ExamListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = Exam.objects.filter(is_active=True).select_related('category')

        # Filter by category slug
        category_slug = request.query_params.get('category')
        if category_slug and category_slug.lower() != 'all':
            queryset = queryset.filter(category__slug=category_slug)

        # Filter by difficulty
        difficulty = request.query_params.get('difficulty')
        if difficulty and difficulty.lower() != 'all':
            queryset = queryset.filter(difficulty__iexact=difficulty)

        # Search by title or description
        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        # Filter by user status if authenticated
        status_filter = request.query_params.get('status')
        if status_filter and request.user.is_authenticated and status_filter.lower() != 'all':
            if status_filter == 'passed':
                passed_ids = ExamResult.objects.filter(user=request.user, passed=True).values_list('exam_id', flat=True)
                queryset = queryset.filter(id__in=passed_ids)
            elif status_filter == 'attempted':
                attempted_ids = ExamAttempt.objects.filter(user=request.user).values_list('exam_id', flat=True)
                queryset = queryset.filter(id__in=attempted_ids)

        serializer = ExamListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class ExamDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug):
        exam = get_object_or_404(Exam, slug=slug, is_active=True)
        serializer = ExamDetailSerializer(exam, context={'request': request})
        return Response(serializer.data)


class ExamStartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        exam = get_object_or_404(Exam, slug=slug, is_active=True)

        # Check if an active, unexpired attempt already exists for this user
        existing_attempt = ExamAttempt.objects.filter(
            user=request.user,
            exam=exam,
            status='in_progress'
        ).first()

        if existing_attempt:
            if not existing_attempt.is_expired:
                return Response({
                    'message': 'Resuming your active exam session.',
                    'attempt_id': existing_attempt.id,
                }, status=status.HTTP_200_OK)
            else:
                # Mark as timed out
                existing_attempt.status = 'timed_out'
                existing_attempt.save()

        # Create a new attempt
        expires_at = timezone.now() + timedelta(minutes=exam.duration_minutes)
        new_attempt = ExamAttempt.objects.create(
            user=request.user,
            exam=exam,
            status='in_progress',
            expires_at=expires_at
        )

        return Response({
            'message': 'Exam session started successfully.',
            'attempt_id': new_attempt.id,
        }, status=status.HTTP_201_CREATED)


class ExamSessionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, attempt_id):
        attempt = get_object_or_404(
            ExamAttempt.objects.select_related('exam').prefetch_related('answers'),
            id=attempt_id,
            user=request.user
        )

        # Check if expired while in progress
        if attempt.status == 'in_progress' and attempt.is_expired:
            attempt.status = 'timed_out'
            attempt.save()

        serializer = ExamAttemptSessionSerializer(attempt)
        return Response(serializer.data)


class ExamSaveAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, attempt_id):
        attempt = get_object_or_404(ExamAttempt, id=attempt_id, user=request.user)

        if attempt.status != 'in_progress':
            return Response(
                {'detail': f'Cannot save answer. Exam attempt is {attempt.status}.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if attempt.is_expired:
            attempt.status = 'timed_out'
            attempt.save()
            return Response(
                {'detail': 'Time has expired for this exam session.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        question_id = request.data.get('question_id')
        question = get_object_or_404(ExamQuestion, id=question_id, exam=attempt.exam)

        answer, _ = ExamAnswer.objects.get_or_create(attempt=attempt, question=question)

        if question.question_type == 'coding':
            answer.code = request.data.get('code', '')
            answer.language = request.data.get('language', 'python')
        else:
            answer.selected_option = request.data.get('selected_option')

        answer.save()
        return Response({'status': 'saved', 'question_id': question_id}, status=status.HTTP_200_OK)


class ExamRunCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, attempt_id):
        attempt = get_object_or_404(ExamAttempt, id=attempt_id, user=request.user)
        if attempt.status != 'in_progress':
            return Response({'detail': 'Exam is no longer active.'}, status=status.HTTP_400_BAD_REQUEST)

        question_id = request.data.get('question_id')
        code = request.data.get('code', '')
        language = request.data.get('language', 'python')
        custom_input = request.data.get('custom_input', None)

        question = get_object_or_404(ExamQuestion, id=question_id, exam=attempt.exam)

        if not code.strip():
            return Response({'detail': 'Code cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

        # Run against custom input if provided
        if custom_input is not None:
            exec_res = run_code_execution(code, language, custom_input)
            err_details = parse_error_details(
                exec_res.status,
                exec_res.compile_output,
                exec_res.stderr or exec_res.error_message,
                exec_res.stdout
            )
            return Response({
                'mode': 'custom_input',
                'status': exec_res.status,
                'stdout': exec_res.stdout,
                'stderr': exec_res.stderr,
                'compile_output': exec_res.compile_output,
                'execution_time': exec_res.execution_time,
                'error_message': exec_res.error_message,
                'error_details': err_details,
                'output': exec_res.stdout or exec_res.stderr or exec_res.error_message or exec_res.compile_output,
            })

        # Run only on visible sample test cases
        visible_cases = [tc for tc in question.test_cases if not tc.get('is_hidden', False)]
        if not visible_cases and question.test_cases:
            visible_cases = [question.test_cases[0]]

        eval_result = evaluate_test_cases(code, language, visible_cases)
        status_val = eval_result.get('overall_status') or eval_result.get('status')
        passed_val = eval_result.get('passed_count')
        if passed_val is None:
            passed_val = eval_result.get('passed_test_cases', 0)
        total_val = eval_result.get('total_count')
        if total_val is None:
            total_val = eval_result.get('total_test_cases', len(visible_cases))

        return Response({
            'mode': 'sample_test_cases',
            'status': status_val,
            'passed_test_cases': passed_val,
            'total_test_cases': total_val,
            'execution_time': eval_result.get('avg_time') or eval_result.get('execution_time'),
            'sample_results': eval_result.get('sample_results'),
            'compiler_output': eval_result.get('compiler_output') or eval_result.get('console_output'),
            'error_output': eval_result.get('error_output'),
        })


class ExamSubmitView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, attempt_id):
        attempt = get_object_or_404(ExamAttempt, id=attempt_id, user=request.user)

        # If already submitted and has result, return that
        if attempt.status == 'submitted' and hasattr(attempt, 'result'):
            return Response({
                'detail': 'Exam already submitted.',
                'attempt_id': attempt.id,
                'result_id': attempt.result.id,
                'passed': attempt.result.passed,
                'score_obtained': attempt.result.score_obtained,
                'total_marks': attempt.result.total_marks,
                'percentage': attempt.result.percentage,
            }, status=status.HTTP_200_OK)

        exam = attempt.exam
        total_exam_points = sum(q.points for q in exam.questions.all()) or 100
        score_obtained = 0.0

        for question in exam.questions.all():
            answer, _ = ExamAnswer.objects.get_or_create(attempt=attempt, question=question)

            if question.question_type == 'coding':
                code = (answer.code or '').strip()
                language = answer.language or 'python'
                test_cases = question.test_cases or []

                if not code or not test_cases:
                    answer.is_correct = False
                    answer.marks_awarded = 0.0
                    answer.evaluation_details = {'reason': 'No code submitted.'}
                else:
                    eval_result = evaluate_test_cases(code, language, test_cases)
                    passed_tc = eval_result.get('passed_count')
                    if passed_tc is None:
                        passed_tc = eval_result.get('passed_test_cases', 0)
                    total_tc = eval_result.get('total_count')
                    if total_tc is None:
                        total_tc = eval_result.get('total_test_cases', len(test_cases)) or 1
                    ratio = passed_tc / total_tc
                    awarded = round(ratio * question.points, 2)
                    answer.is_correct = (passed_tc == total_tc and total_tc > 0)
                    answer.marks_awarded = awarded
                    answer.evaluation_details = eval_result
                    score_obtained += awarded

            elif question.question_type in ['single_choice', 'code_completion', 'short_answer']:
                user_sel = answer.selected_option
                correct_ans = question.correct_answer

                is_correct = False
                if isinstance(user_sel, str) and isinstance(correct_ans, str):
                    is_correct = (user_sel.strip().upper() == correct_ans.strip().upper())
                else:
                    is_correct = (user_sel == correct_ans)

                answer.is_correct = is_correct
                awarded = float(question.points) if is_correct else 0.0
                answer.marks_awarded = awarded
                answer.evaluation_details = {'user_answer': user_sel, 'is_correct': is_correct}
                score_obtained += awarded

            elif question.question_type == 'multiple_choice':
                user_sel = answer.selected_option or []
                correct_ans = question.correct_answer or []
                if isinstance(user_sel, list) and isinstance(correct_ans, list):
                    is_correct = (sorted(user_sel) == sorted(correct_ans))
                else:
                    is_correct = (user_sel == correct_ans)

                answer.is_correct = is_correct
                awarded = float(question.points) if is_correct else 0.0
                answer.marks_awarded = awarded
                answer.evaluation_details = {'user_answer': user_sel, 'is_correct': is_correct}
                score_obtained += awarded

            answer.save()

        # Update attempt status
        attempt.status = 'submitted'
        attempt.completed_at = timezone.now()
        time_spent = int((attempt.completed_at - attempt.started_at).total_seconds())
        attempt.time_spent_seconds = min(time_spent, exam.duration_minutes * 60)
        attempt.save()

        # Score & pass computation
        percentage = round((score_obtained / total_exam_points) * 100, 2)
        passed = percentage >= exam.passing_percentage

        result, _ = ExamResult.objects.update_or_create(
            attempt=attempt,
            defaults={
                'user': request.user,
                'exam': exam,
                'total_marks': total_exam_points,
                'score_obtained': score_obtained,
                'percentage': percentage,
                'passed': passed,
                'certificate_eligible': passed,
            }
        )

        # Automatic Certificate Creation upon Passing
        cert = None
        if passed:
            user_full_name = f"{request.user.first_name} {request.user.last_name}".strip()
            candidate_name = user_full_name if user_full_name else request.user.username
            cert, created = Certificate.objects.get_or_create(
                attempt=attempt,
                defaults={
                    'user': request.user,
                    'exam': exam,
                    'candidate_name': candidate_name,
                    'issue_date': timezone.now().date(),
                    'signatory_title': 'Platform Representative'
                }
            )

        return Response({
            'detail': 'Exam submitted successfully.',
            'attempt_id': attempt.id,
            'result_id': result.id,
            'passed': passed,
            'score_obtained': score_obtained,
            'total_marks': total_exam_points,
            'percentage': percentage,
            'certificate_id': cert.certificate_id if cert else None
        }, status=status.HTTP_200_OK)


class ExamResultView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, attempt_id):
        attempt = get_object_or_404(ExamAttempt, id=attempt_id, user=request.user)
        result = get_object_or_404(ExamResult, attempt=attempt)
        serializer = ExamResultDetailSerializer(result)
        return Response(serializer.data)


class UserCertificatesListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        certificates = Certificate.objects.filter(user=request.user).order_by('-issue_date')
        serializer = CertificateSerializer(certificates, many=True)
        return Response(serializer.data)


class CertificateDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request, certificate_id):
        cert = get_object_or_404(Certificate, certificate_id=certificate_id)
        serializer = CertificateSerializer(cert)
        return Response(serializer.data)


class CertificateDownloadPDFView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request, certificate_id):
        cert = get_object_or_404(Certificate, certificate_id=certificate_id)
        pdf_buffer = generate_certificate_pdf(cert)

        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        filename = f"Certificate_{cert.certificate_id}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


class CourseProgressView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, course_slug='modern-frontend-development'):
        progress_qs = CourseProgress.objects.filter(user=request.user, course_slug=course_slug)
        serializer = CourseProgressSerializer(progress_qs, many=True)
        completed_exercises = list(progress_qs.filter(completed=True).values_list('exercise_id', flat=True))
        completed_count = len(completed_exercises)
        total_exercises = 40
        percentage = round((completed_count / total_exercises) * 100, 1) if total_exercises > 0 else 0
        
        # Calculate by topic
        topic_progress = {}
        for item in progress_qs:
            t = item.topic_slug
            if t not in topic_progress:
                topic_progress[t] = {'completed': [], 'total_completed': 0}
            if item.completed:
                topic_progress[t]['completed'].append(item.exercise_id)
                topic_progress[t]['total_completed'] += 1

        return Response({
            'course_slug': course_slug,
            'completed_count': completed_count,
            'completed_exercises_count': completed_count,
            'total_exercises_count': total_exercises,
            'percentage': percentage,
            'completed_exercises': completed_exercises,
            'topic_progress': topic_progress,
            'progress': serializer.data,
            'progress_items': serializer.data
        }, status=status.HTTP_200_OK)


class CourseSaveProgressView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_slug='modern-frontend-development'):
        topic_slug = request.data.get('topic_slug')
        exercise_id = request.data.get('exercise_id')
        completed = request.data.get('completed', True)
        user_code = request.data.get('user_code', '')

        if not topic_slug or not exercise_id:
            return Response({'error': 'topic_slug and exercise_id are required'}, status=status.HTTP_400_BAD_REQUEST)

        defaults = {
            'completed': completed,
            'user_code': user_code,
        }
        if completed:
            defaults['completed_at'] = timezone.now()

        obj, created = CourseProgress.objects.update_or_create(
            user=request.user,
            course_slug=course_slug,
            topic_slug=topic_slug,
            exercise_id=exercise_id,
            defaults=defaults
        )

        progress_qs = CourseProgress.objects.filter(user=request.user, course_slug=course_slug)
        completed_exercises = list(progress_qs.filter(completed=True).values_list('exercise_id', flat=True))
        completed_count = len(completed_exercises)
        total_exercises = 40
        percentage = round((completed_count / total_exercises) * 100, 1) if total_exercises > 0 else 0

        return Response({
            'message': 'Progress saved successfully',
            'exercise_id': exercise_id,
            'completed': obj.completed,
            'completed_count': completed_count,
            'completed_exercises_count': completed_count,
            'total_exercises_count': total_exercises,
            'percentage': percentage,
            'completed_exercises': completed_exercises,
            'item': CourseProgressSerializer(obj).data
        }, status=status.HTTP_200_OK)


class CourseResetProgressView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_slug='modern-frontend-development'):
        topic_slug = request.data.get('topic_slug')
        exercise_id = request.data.get('exercise_id')

        if topic_slug and exercise_id:
            CourseProgress.objects.filter(
                user=request.user,
                course_slug=course_slug,
                topic_slug=topic_slug,
                exercise_id=exercise_id
            ).delete()
        elif topic_slug:
            CourseProgress.objects.filter(
                user=request.user,
                course_slug=course_slug,
                topic_slug=topic_slug
            ).delete()
        else:
            # Reset all course progress
            CourseProgress.objects.filter(
                user=request.user,
                course_slug=course_slug
            ).delete()

        progress_qs = CourseProgress.objects.filter(user=request.user, course_slug=course_slug)
        completed_exercises = list(progress_qs.filter(completed=True).values_list('exercise_id', flat=True))
        completed_count = len(completed_exercises)
        total_exercises = 40
        percentage = round((completed_count / total_exercises) * 100, 1) if total_exercises > 0 else 0

        return Response({
            'message': 'Progress reset successfully',
            'completed_count': completed_count,
            'completed_exercises_count': completed_count,
            'total_exercises_count': total_exercises,
            'percentage': percentage,
            'completed_exercises': completed_exercises
        }, status=status.HTTP_200_OK)


