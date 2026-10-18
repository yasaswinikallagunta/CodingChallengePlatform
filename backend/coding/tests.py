from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from coding.models import (
    CodingProblem,
    CodingSubmission,
    UserCodingProgress,
    CodingAchievement,
    UserAchievement,
    CodingActivity
)
from coding.services import ensure_achievements_exist


class CodingPlatformAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        ensure_achievements_exist()

        # Seed sample problem
        self.problem = CodingProblem.objects.create(
            title="Two Sum Test",
            slug="two-sum-test",
            category="Algorithms",
            difficulty="Easy",
            points=10,
            problem_statement="Find two indices that sum up to target.",
            starter_code={"python": "import sys\nprint('0 1')\n"},
            test_cases=[
                {"input": "9\n2 7 11 15", "expected_output": "0 1", "is_hidden": False},
                {"input": "6\n3 2 4", "expected_output": "1 2", "is_hidden": True},
            ]
        )

        self.reg_data = {
            "full_name": "Test Developer",
            "email": "testdev@example.com",
            "username": "testdev",
            "password": "Password123!",
            "confirm_password": "Password123!"
        }

    def test_01_registration_valid(self):
        response = self.client.post('/api/auth/register/', self.reg_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('tokens', response.data)
        self.assertIn('access', response.data['tokens'])
        self.assertTrue(User.objects.filter(username="testdev").exists())
        self.assertTrue(UserCodingProgress.objects.filter(user__username="testdev").exists())

    def test_02_registration_duplicate_prevention(self):
        self.client.post('/api/auth/register/', self.reg_data)
        # Try duplicate username
        dup_user = self.reg_data.copy()
        dup_user['email'] = 'unique@example.com'
        res1 = self.client.post('/api/auth/register/', dup_user)
        self.assertEqual(res1.status_code, status.HTTP_400_BAD_REQUEST)

        # Try duplicate email
        dup_email = self.reg_data.copy()
        dup_email['username'] = 'unique_username'
        res2 = self.client.post('/api/auth/register/', dup_email)
        self.assertEqual(res2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_03_registration_password_mismatch(self):
        bad_data = self.reg_data.copy()
        bad_data['confirm_password'] = 'DifferentPass!'
        res = self.client.post('/api/auth/register/', bad_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_04_login_success_and_failure(self):
        self.client.post('/api/auth/register/', self.reg_data)

        # Failure with wrong password
        fail_res = self.client.post('/api/auth/login/', {
            'username': 'testdev',
            'password': 'WrongPassword!'
        })
        self.assertEqual(fail_res.status_code, status.HTTP_401_UNAUTHORIZED)

        # Success with username
        succ_res = self.client.post('/api/auth/login/', {
            'username': 'testdev',
            'password': 'Password123!'
        })
        self.assertEqual(succ_res.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', succ_res.data)

        # Success with email
        email_res = self.client.post('/api/auth/login/', {
            'username': 'testdev@example.com',
            'password': 'Password123!'
        })
        self.assertEqual(email_res.status_code, status.HTTP_200_OK)

    def test_05_authenticated_profile(self):
        reg = self.client.post('/api/auth/register/', self.reg_data)
        token = reg.data['tokens']['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        res = self.client.get('/api/auth/me/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['user']['username'], 'testdev')

    def test_06_problem_listing_and_filtering(self):
        res = self.client.get('/api/problems/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(res.data['count'], 1)

        # Filter by category
        res_cat = self.client.get('/api/problems/', {'category': 'Algorithms'})
        self.assertEqual(res_cat.status_code, status.HTTP_200_OK)
        self.assertTrue(all(p['category'] == 'Algorithms' for p in res_cat.data['results']))

        # Filter by difficulty
        res_diff = self.client.get('/api/problems/', {'difficulty': 'Easy'})
        self.assertEqual(res_diff.status_code, status.HTTP_200_OK)
        self.assertTrue(all(p['difficulty'] == 'Easy' for p in res_diff.data['results']))

        # Problem detail
        res_det = self.client.get(f'/api/problems/{self.problem.slug}/')
        self.assertEqual(res_det.status_code, status.HTTP_200_OK)
        self.assertEqual(res_det.data['title'], 'Two Sum Test')

    def test_07_code_run_and_submission(self):
        reg = self.client.post('/api/auth/register/', self.reg_data)
        token = reg.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # 1. Run code against sample case
        python_code = "print('0 1')"
        run_res = self.client.post(f'/api/problems/{self.problem.slug}/run/', {
            'code': python_code,
            'language': 'python'
        })
        self.assertEqual(run_res.status_code, status.HTTP_200_OK)
        self.assertEqual(run_res.data['status'], 'Accepted')

        # 2. Submit code (which will pass sample 1 but fail sample 2 since output is hardcoded '0 1')
        sub_res = self.client.post(f'/api/problems/{self.problem.slug}/submit/', {
            'code': python_code,
            'language': 'python'
        })
        self.assertEqual(sub_res.status_code, status.HTTP_200_OK)
        self.assertEqual(sub_res.data['status'], 'Wrong Answer')
        self.assertEqual(sub_res.data['passed_count'], 1)
        self.assertEqual(sub_res.data['total_count'], 2)

        # 3. Submit full working solution
        working_code = (
            "import sys\n"
            "lines = sys.stdin.read().splitlines()\n"
            "target = int(lines[0].strip())\n"
            "nums = list(map(int, lines[1].strip().split()))\n"
            "seen = {}\n"
            "for i, n in enumerate(nums):\n"
            "    diff = target - n\n"
            "    if diff in seen:\n"
            "        print(f'{seen[diff]} {i}')\n"
            "        break\n"
            "    seen[n] = i\n"
        )
        full_sub = self.client.post(f'/api/problems/{self.problem.slug}/submit/', {
            'code': working_code,
            'language': 'python'
        })
        self.assertEqual(full_sub.status_code, status.HTTP_200_OK)
        self.assertEqual(full_sub.data['status'], 'Accepted')
        self.assertEqual(full_sub.data['passed_count'], 2)
        self.assertTrue(full_sub.data['is_newly_solved'])
        self.assertEqual(full_sub.data['points_awarded'], 10)

        # Check First Problem Solved achievement was awarded
        ach_unlocked = full_sub.data['new_achievements']
        self.assertTrue(any(a['code'] == 'FIRST_SOLVED' for a in ach_unlocked))

        # Check re-submission does NOT duplicate points
        repeat_sub = self.client.post(f'/api/problems/{self.problem.slug}/submit/', {
            'code': working_code,
            'language': 'python'
        })
        self.assertFalse(repeat_sub.data['is_newly_solved'])
        self.assertEqual(repeat_sub.data['points_awarded'], 0)

    def test_08_dashboard_and_analytics_endpoints(self):
        reg = self.client.post('/api/auth/register/', self.reg_data)
        token = reg.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Check dashboard stats
        dash_res = self.client.get('/api/dashboard/stats/')
        self.assertEqual(dash_res.status_code, status.HTTP_200_OK)
        self.assertIn('overview', dash_res.data)
        self.assertIn('weekly_activity', dash_res.data)
        self.assertIn('heatmap_data', dash_res.data)

        # Check analytics
        perf_res = self.client.get('/api/progress/analysis/')
        self.assertEqual(perf_res.status_code, status.HTTP_200_OK)
        self.assertIn('acceptance_rate', perf_res.data)
        self.assertIn('category_breakdown', perf_res.data)

        # Check achievements list
        ach_res = self.client.get('/api/achievements/')
        self.assertEqual(ach_res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(ach_res.data), 5)
