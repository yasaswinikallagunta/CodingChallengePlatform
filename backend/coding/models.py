from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CodingProblem(models.Model):
    CATEGORY_CHOICES = [
        ('Python', 'Python'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('Data Structures', 'Data Structures'),
        ('Algorithms', 'Algorithms'),
        ('SQL', 'SQL'),
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, db_index=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, db_index=True)
    points = models.IntegerField(default=10)
    
    problem_statement = models.TextField()
    input_format = models.TextField(blank=True, default='')
    output_format = models.TextField(blank=True, default='')
    constraints = models.TextField(blank=True, default='')
    sample_input = models.TextField(blank=True, default='')
    sample_output = models.TextField(blank=True, default='')
    explanation = models.TextField(blank=True, default='')

    # starter_code maps language string -> starter code text
    starter_code = models.JSONField(default=dict, blank=True)
    # test_cases: list of {"input": "...", "expected_output": "...", "is_hidden": bool}
    test_cases = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.title} ({self.difficulty} - {self.category})"


class CodingSubmission(models.Model):
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Wrong Answer', 'Wrong Answer'),
        ('Time Limit Exceeded', 'Time Limit Exceeded'),
        ('Compilation Error', 'Compilation Error'),
        ('Runtime Error', 'Runtime Error'),
        ('Service Unavailable', 'Service Unavailable'),
        ('Pending', 'Pending'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(CodingProblem, on_delete=models.CASCADE, related_name='submissions')
    language = models.CharField(max_length=50)
    code = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    passed_test_cases = models.IntegerField(default=0)
    total_test_cases = models.IntegerField(default=0)
    execution_time = models.FloatField(null=True, blank=True)  # in seconds
    memory_usage = models.FloatField(null=True, blank=True)    # in KB
    output = models.TextField(blank=True, default='')
    submitted_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} ({self.status})"


class UserCodingProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coding_progress')
    points = models.IntegerField(default=0)
    problems_solved_count = models.IntegerField(default=0)
    problems_attempted_count = models.IntegerField(default=0)
    easy_solved_count = models.IntegerField(default=0)
    medium_solved_count = models.IntegerField(default=0)
    hard_solved_count = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_active_date = models.DateField(null=True, blank=True)

    solved_problems = models.ManyToManyField(CodingProblem, blank=True, related_name='solved_by_users')
    attempted_problems = models.ManyToManyField(CodingProblem, blank=True, related_name='attempted_by_users')

    def __str__(self):
        return f"Progress: {self.user.username} ({self.points} pts, {self.problems_solved_count} solved)"


class CodingAchievement(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    badge_icon = models.CharField(max_length=50, default='Award')
    points_reward = models.IntegerField(default=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_achievements')
    achievement = models.ForeignKey(CodingAchievement, on_delete=models.CASCADE, related_name='user_achievements')
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')
        ordering = ['-unlocked_at']

    def __str__(self):
        return f"{self.user.username} unlocked {self.achievement.title}"


class CodingActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    date = models.DateField(db_index=True)
    submission_count = models.IntegerField(default=0)
    solved_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} on {self.date}: {self.submission_count} submissions"


# ============================================================================
# EXAMS & CERTIFICATIONS MODELS
# ============================================================================

def generate_certificate_id():
    import uuid
    u = uuid.uuid4().hex.upper()
    return f"CCP-{u[:4]}-{u[4:8]}-{u[8:12]}"


class ExamCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, default='')
    icon = models.CharField(max_length=50, default='BookOpen')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Exam Categories'

    def __str__(self):
        return self.name


class Exam(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE, related_name='exams')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Medium')
    duration_minutes = models.IntegerField(default=45)
    passing_percentage = models.IntegerField(default=70)  # e.g., 70%
    total_marks = models.IntegerField(default=100)
    instructions = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category__order', 'id']

    def __str__(self):
        return f"{self.title} ({self.category.name})"


class ExamQuestion(models.Model):
    QUESTION_TYPES = [
        ('coding', 'Coding Challenge'),
        ('single_choice', 'Single Choice MCQ'),
        ('multiple_choice', 'Multiple Choice MCQ'),
        ('code_completion', 'Code Completion'),
        ('short_answer', 'Short Answer'),
    ]

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    order = models.IntegerField(default=1)
    question_type = models.CharField(max_length=30, choices=QUESTION_TYPES, default='single_choice')
    title = models.CharField(max_length=255)
    problem_statement = models.TextField()
    points = models.IntegerField(default=10)

    # Conceptual fields
    # options: [{"id": "A", "text": "..."}, {"id": "B", "text": "..."}]
    options = models.JSONField(default=list, blank=True)
    # correct_answer: "A" or ["A", "C"] or text string
    correct_answer = models.JSONField(default=dict, blank=True)
    explanation = models.TextField(blank=True, default='')

    # Coding question fields
    input_format = models.TextField(blank=True, default='')
    output_format = models.TextField(blank=True, default='')
    constraints = models.TextField(blank=True, default='')
    starter_code = models.JSONField(default=dict, blank=True)
    # test_cases: [{"input": "...", "expected_output": "...", "is_hidden": bool}]
    test_cases = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"[{self.exam.title}] Q{self.order}: {self.title} ({self.question_type})"


class ExamAttempt(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('timed_out', 'Timed Out'),
        ('abandoned', 'Abandoned'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='attempts')
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    time_spent_seconds = models.IntegerField(default=0)

    class Meta:
        ordering = ['-started_at']

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.user.username} - {self.exam.title} ({self.status})"


class ExamAnswer(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE, related_name='user_answers')
    selected_option = models.JSONField(null=True, blank=True)  # "A" or ["A", "B"] or text answer
    code = models.TextField(blank=True, default='')
    language = models.CharField(max_length=50, blank=True, default='')
    is_correct = models.BooleanField(null=True, blank=True)
    marks_awarded = models.FloatField(default=0.0)
    evaluation_details = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('attempt', 'question')

    def __str__(self):
        return f"Attempt {self.attempt_id} - Q{self.question.order} (Marks: {self.marks_awarded})"


class ExamResult(models.Model):
    attempt = models.OneToOneField(ExamAttempt, on_delete=models.CASCADE, related_name='result')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    total_marks = models.FloatField(default=0.0)
    score_obtained = models.FloatField(default=0.0)
    percentage = models.FloatField(default=0.0)
    passed = models.BooleanField(default=False)
    certificate_eligible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        status_str = "PASSED" if self.passed else "FAILED"
        return f"{self.user.username} - {self.exam.title}: {self.score_obtained}/{self.total_marks} ({self.percentage:.1f}%) - {status_str}"


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=64, unique=True, db_index=True, default=generate_certificate_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='certificates')
    attempt = models.OneToOneField(ExamAttempt, on_delete=models.CASCADE, related_name='certificate')
    candidate_name = models.CharField(max_length=255)
    issue_date = models.DateField(default=timezone.now)
    signatory_title = models.CharField(max_length=100, default='Platform Representative')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-issue_date', '-created_at']

    def __str__(self):
        return f"Certificate {self.certificate_id} for {self.candidate_name} ({self.exam.title})"


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_progress')
    course_slug = models.CharField(max_length=100, default='modern-frontend-development', db_index=True)
    topic_slug = models.CharField(max_length=100, db_index=True)
    exercise_id = models.CharField(max_length=100, db_index=True)
    completed = models.BooleanField(default=False)
    user_code = models.TextField(blank=True, default='')
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course_slug', 'topic_slug', 'exercise_id')
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.user.username} - {self.course_slug}/{self.topic_slug}/{self.exercise_id}: {'Completed' if self.completed else 'In Progress'}"
