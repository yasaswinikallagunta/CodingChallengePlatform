from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    CodingProblem,
    CodingSubmission,
    UserCodingProgress,
    CodingAchievement,
    UserAchievement,
    CodingActivity,
    CourseProgress
)


class UserRegistrationSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
        default='',
        trim_whitespace=True
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
        default=''
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=6,
        error_messages={
            'min_length': 'Password must be at least 6 characters long.',
            'required': 'Password is required.',
            'blank': 'Password cannot be blank.'
        }
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'password', 'confirm_password')

    def to_internal_value(self, data):
        # Support camelCase and alternate field aliases from frontend
        normalized = data.copy() if hasattr(data, 'copy') else dict(data)
        if 'fullName' in normalized and 'full_name' not in normalized:
            normalized['full_name'] = normalized['fullName']
        elif 'name' in normalized and 'full_name' not in normalized:
            normalized['full_name'] = normalized['name']

        if 'confirmPassword' in normalized and 'confirm_password' not in normalized:
            normalized['confirm_password'] = normalized['confirmPassword']

        # If confirm_password wasn't provided, mirror password to satisfy validation
        if 'password' in normalized and ('confirm_password' not in normalized or not normalized['confirm_password']):
            normalized['confirm_password'] = normalized['password']

        return super().to_internal_value(normalized)

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        value = value.strip().lower()
        if '@' not in value or '.' not in value:
            raise serializers.ValidationError("Please provide a valid email address.")
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("An account with this email already exists.")
        return value

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username is required.")
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if confirm_password and password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        full_name = validated_data.pop('full_name', '').strip()
        validated_data.pop('confirm_password', None)
        
        first_name = full_name
        last_name = ''
        if ' ' in full_name:
            parts = full_name.split(' ', 1)
            first_name = parts[0]
            last_name = parts[1]

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name
        )
        # Create initial user progress safely
        UserCodingProgress.objects.get_or_create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'date_joined')

    def get_full_name(self, obj):
        name = f"{obj.first_name} {obj.last_name}".strip()
        return name if name else obj.username


class CodingProblemListSerializer(serializers.ModelSerializer):
    is_solved = serializers.SerializerMethodField()
    is_attempted = serializers.SerializerMethodField()

    class Meta:
        model = CodingProblem
        fields = (
            'id', 'title', 'slug', 'category', 'difficulty',
            'points', 'is_solved', 'is_attempted', 'created_at'
        )

    def get_is_solved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            progress = getattr(request.user, 'coding_progress', None)
            if progress:
                return progress.solved_problems.filter(id=obj.id).exists()
        return False

    def get_is_attempted(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            progress = getattr(request.user, 'coding_progress', None)
            if progress:
                return progress.attempted_problems.filter(id=obj.id).exists()
        return False


class CodingProblemDetailSerializer(serializers.ModelSerializer):
    is_solved = serializers.SerializerMethodField()
    is_attempted = serializers.SerializerMethodField()
    sample_test_cases = serializers.SerializerMethodField()

    class Meta:
        model = CodingProblem
        fields = (
            'id', 'title', 'slug', 'category', 'difficulty', 'points',
            'problem_statement', 'input_format', 'output_format',
            'constraints', 'sample_input', 'sample_output', 'explanation',
            'starter_code', 'sample_test_cases', 'is_solved', 'is_attempted',
            'created_at', 'updated_at'
        )

    def get_is_solved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            progress = getattr(request.user, 'coding_progress', None)
            if progress:
                return progress.solved_problems.filter(id=obj.id).exists()
        return False

    def get_is_attempted(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            progress = getattr(request.user, 'coding_progress', None)
            if progress:
                return progress.attempted_problems.filter(id=obj.id).exists()
        return False

    def get_sample_test_cases(self, obj):
        # Expose only non-hidden test cases to client
        test_cases = obj.test_cases or []
        visible = [tc for tc in test_cases if not tc.get('is_hidden', False)]
        if not visible and test_cases:
            # Fallback to first test case if none marked public
            visible = [test_cases[0]]
        return visible


class CodingSubmissionSerializer(serializers.ModelSerializer):
    problem_title = serializers.CharField(source='problem.title', read_only=True)
    problem_slug = serializers.CharField(source='problem.slug', read_only=True)
    problem_difficulty = serializers.CharField(source='problem.difficulty', read_only=True)
    problem_category = serializers.CharField(source='problem.category', read_only=True)

    class Meta:
        model = CodingSubmission
        fields = (
            'id', 'problem', 'problem_title', 'problem_slug', 'problem_difficulty',
            'problem_category', 'language', 'code', 'status', 'passed_test_cases',
            'total_test_cases', 'execution_time', 'memory_usage', 'output', 'submitted_at'
        )
        read_only_fields = (
            'id', 'status', 'passed_test_cases', 'total_test_cases',
            'execution_time', 'memory_usage', 'output', 'submitted_at'
        )


class UserCodingProgressSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = UserCodingProgress
        fields = (
            'id', 'username', 'full_name', 'points', 'problems_solved_count',
            'problems_attempted_count', 'easy_solved_count', 'medium_solved_count',
            'hard_solved_count', 'current_streak', 'longest_streak', 'last_active_date'
        )

    def get_full_name(self, obj):
        name = f"{obj.user.first_name} {obj.user.last_name}".strip()
        return name if name else obj.user.username


class CodingAchievementSerializer(serializers.ModelSerializer):
    is_unlocked = serializers.SerializerMethodField()
    unlocked_at = serializers.SerializerMethodField()

    class Meta:
        model = CodingAchievement
        fields = (
            'id', 'code', 'title', 'description', 'badge_icon',
            'points_reward', 'is_unlocked', 'unlocked_at'
        )

    def get_is_unlocked(self, obj):
        user = self.context.get('user')
        if user and user.is_authenticated:
            return UserAchievement.objects.filter(user=user, achievement=obj).exists()
        return False

    def get_unlocked_at(self, obj):
        user = self.context.get('user')
        if user and user.is_authenticated:
            ua = UserAchievement.objects.filter(user=user, achievement=obj).first()
            if ua:
                return ua.unlocked_at
        return None


class CodingActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingActivity
        fields = ('date', 'submission_count', 'solved_count')


# ============================================================================
# EXAMS & CERTIFICATIONS SERIALIZERS
# ============================================================================

from .models import (
    ExamCategory,
    Exam,
    ExamQuestion,
    ExamAttempt,
    ExamAnswer,
    ExamResult,
    Certificate
)


class ExamCategorySerializer(serializers.ModelSerializer):
    exams_count = serializers.SerializerMethodField()

    class Meta:
        model = ExamCategory
        fields = ('id', 'name', 'slug', 'description', 'icon', 'order', 'exams_count')

    def get_exams_count(self, obj):
        return obj.exams.filter(is_active=True).count()


class ExamListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    questions_count = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()
    user_certificate_id = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = (
            'id', 'title', 'slug', 'category_name', 'category_slug',
            'difficulty', 'duration_minutes', 'passing_percentage',
            'total_marks', 'description', 'questions_count',
            'user_status', 'user_certificate_id'
        )

    def get_questions_count(self, obj):
        return obj.questions.count()

    def get_user_status(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return 'not_started'
        # Check if user has passed
        has_passed = ExamResult.objects.filter(user=request.user, exam=obj, passed=True).exists()
        if has_passed:
            return 'passed'
        # Check if in progress
        in_progress = ExamAttempt.objects.filter(user=request.user, exam=obj, status='in_progress').first()
        if in_progress and not in_progress.is_expired:
            return 'in_progress'
        # Check if attempted
        attempted = ExamAttempt.objects.filter(user=request.user, exam=obj).exists()
        return 'attempted' if attempted else 'not_started'

    def get_user_certificate_id(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return None
        cert = Certificate.objects.filter(user=request.user, exam=obj).order_by('-issue_date').first()
        return cert.certificate_id if cert else None


class ExamDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    questions_count = serializers.SerializerMethodField()
    user_attempts_count = serializers.SerializerMethodField()
    user_passed = serializers.SerializerMethodField()
    latest_certificate_id = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = (
            'id', 'title', 'slug', 'category_name', 'category_slug',
            'difficulty', 'duration_minutes', 'passing_percentage',
            'total_marks', 'description', 'instructions',
            'questions_count', 'user_attempts_count', 'user_passed',
            'latest_certificate_id'
        )

    def get_questions_count(self, obj):
        return obj.questions.count()

    def get_user_attempts_count(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return ExamAttempt.objects.filter(user=request.user, exam=obj).count()
        return 0

    def get_user_passed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return ExamResult.objects.filter(user=request.user, exam=obj, passed=True).exists()
        return False

    def get_latest_certificate_id(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            cert = Certificate.objects.filter(user=request.user, exam=obj).order_by('-issue_date').first()
            return cert.certificate_id if cert else None
        return None


class ExamQuestionSessionSerializer(serializers.ModelSerializer):
    """Secure question serializer for an active exam session (hides answers and hidden test cases)."""
    sample_test_cases = serializers.SerializerMethodField()

    class Meta:
        model = ExamQuestion
        fields = (
            'id', 'order', 'question_type', 'title', 'problem_statement',
            'points', 'options', 'input_format', 'output_format',
            'constraints', 'starter_code', 'sample_test_cases'
        )

    def get_sample_test_cases(self, obj):
        if obj.question_type == 'coding':
            cases = obj.test_cases or []
            return [c for c in cases if not c.get('is_hidden', False)]
        return []


class ExamAnswerSessionSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='question.id', read_only=True)

    class Meta:
        model = ExamAnswer
        fields = ('id', 'question_id', 'selected_option', 'code', 'language', 'updated_at')


class ExamAttemptSessionSerializer(serializers.ModelSerializer):
    exam_title = serializers.CharField(source='exam.title', read_only=True)
    exam_slug = serializers.CharField(source='exam.slug', read_only=True)
    duration_minutes = serializers.IntegerField(source='exam.duration_minutes', read_only=True)
    time_remaining_seconds = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    saved_answers = serializers.SerializerMethodField()

    class Meta:
        model = ExamAttempt
        fields = (
            'id', 'exam_title', 'exam_slug', 'duration_minutes',
            'started_at', 'expires_at', 'status', 'time_spent_seconds',
            'time_remaining_seconds', 'questions', 'saved_answers'
        )

    def get_time_remaining_seconds(self, obj):
        from django.utils import timezone
        now = timezone.now()
        if now >= obj.expires_at:
            return 0
        return int((obj.expires_at - now).total_seconds())

    def get_questions(self, obj):
        questions = obj.exam.questions.all().order_by('order')
        return ExamQuestionSessionSerializer(questions, many=True).data

    def get_saved_answers(self, obj):
        answers = obj.answers.all()
        result = {}
        for ans in answers:
            result[ans.question_id] = {
                'selected_option': ans.selected_option,
                'code': ans.code,
                'language': ans.language,
            }
        return result


class ExamQuestionResultSerializer(serializers.ModelSerializer):
    """Detailed question serializer with correct answer & explanation for post-exam review."""
    class Meta:
        model = ExamQuestion
        fields = (
            'id', 'order', 'question_type', 'title', 'problem_statement',
            'points', 'options', 'correct_answer', 'explanation',
            'input_format', 'output_format', 'constraints', 'test_cases'
        )


class ExamAnswerReviewSerializer(serializers.ModelSerializer):
    question = ExamQuestionResultSerializer(read_only=True)

    class Meta:
        model = ExamAnswer
        fields = (
            'id', 'question', 'selected_option', 'code', 'language',
            'is_correct', 'marks_awarded', 'evaluation_details'
        )


class ExamResultDetailSerializer(serializers.ModelSerializer):
    exam_title = serializers.CharField(source='exam.title', read_only=True)
    exam_slug = serializers.CharField(source='exam.slug', read_only=True)
    category_name = serializers.CharField(source='exam.category.name', read_only=True)
    passing_percentage = serializers.IntegerField(source='exam.passing_percentage', read_only=True)
    certificate_id = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()
    time_spent_seconds = serializers.IntegerField(source='attempt.time_spent_seconds', read_only=True)

    class Meta:
        model = ExamResult
        fields = (
            'id', 'exam_title', 'exam_slug', 'category_name',
            'total_marks', 'score_obtained', 'percentage', 'passed',
            'passing_percentage', 'certificate_eligible', 'certificate_id',
            'time_spent_seconds', 'created_at', 'answers'
        )

    def get_certificate_id(self, obj):
        cert = getattr(obj.attempt, 'certificate', None)
        return cert.certificate_id if cert else None

    def get_answers(self, obj):
        answers = obj.attempt.answers.all().order_by('question__order')
        return ExamAnswerReviewSerializer(answers, many=True).data


class CertificateSerializer(serializers.ModelSerializer):
    exam_title = serializers.CharField(source='exam.title', read_only=True)
    exam_slug = serializers.CharField(source='exam.slug', read_only=True)
    category_name = serializers.CharField(source='exam.category.name', read_only=True)

    class Meta:
        model = Certificate
        fields = (
            'certificate_id', 'candidate_name', 'exam_title', 'exam_slug',
            'category_name', 'issue_date', 'signatory_title', 'created_at'
        )


class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = (
            'id', 'course_slug', 'topic_slug', 'exercise_id',
            'completed', 'user_code', 'completed_at', 'updated_at'
        )

