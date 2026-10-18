# 🚀 Interactive Coding Challenge Platform (React + Django)

A full-stack, professional **Interactive Coding Challenge Platform** designed with a SaaS-grade white-and-green theme. The platform features an interactive coding workspace powered by Monaco Editor, sandboxed execution, real-time evaluation across test cases, streak tracking, activity heatmaps, performance analytics, and milestone achievement badges.

---

## 🎨 Visual Design & Palette

Built with a consistent SaaS aesthetic:
- **White**: `#FFFFFF`
- **Primary Green**: `#16A34A`
- **Dark Green**: `#166534`
- **Soft Green**: `#DCFCE7`
- **Light Green Background**: `#F7FCF8`
- **Main Text**: `#172B21`
- **Secondary Text**: `#64748B`
- **Borders**: `#E2E8F0`

---

## 🌟 Key Features

1. **5-Second Animated Intro**:
   - Full-screen welcome with floating programming symbols (`</>`, `{ }`, `01`), platform title reveal, tagline (*"Code. Practice. Improve. Achieve."*), and smooth animated progress bar.
   - Automatically saved to `sessionStorage` so it doesn't replay on internal navigations (includes a "Skip Intro" option).
2. **Split-Screen Authentication**:
   - Left side: Animated coding illustrations, decorative shapes, headline, motivational quote, and code snippets.
   - Right side: Smooth toggle between **Sign In** and **Sign Up**, password visibility toggle, real-time password strength indicator, matching password validation, and duplicate prevention.
   - Secured with Django password hashing and JWT token authentication.
3. **Interactive Coding Workspace**:
   - Split-view layout: Problem statement, constraints, I/O formats, sample inputs/outputs, and previous submissions on the left.
   - Monaco Editor on the right with multi-language syntax highlighting (Python, JavaScript, C++, C, Java, SQL).
   - Custom test input toggle, **Run Code** (test against sample cases) and **Submit Code** (evaluates against full hidden test suite).
   - Execution console with passed test counts, execution time, and confetti celebration on Accepted verdict.
4. **Sandboxed Code Execution**:
   - Isolated sub-process execution runner with timeout and output limits.
   - Plug-and-play Judge0 CE support (RapidAPI or self-hosted) configured via environment variables.
5. **Real-Time Analytics & Dashboard**:
   - Metric cards: Problems solved, completion percentage, points, current streak, achievements unlocked.
   - 7-day interactive weekly submissions & solved bar chart.
   - 60-day GitHub-style green activity contribution heatmap.
   - Difficulty-wise progress bars (Easy, Medium, Hard).
   - Category-wise competency (Python, C, C++, Java, JavaScript, Data Structures, Algorithms, SQL).
   - Recommended challenges and recent submissions history.
6. **Milestone Achievements System**:
   - 10 automatically awarded achievements (First Problem Solved, 10/50/100 Problems Solved, 5-Day/7-Day Streak, Easy/Medium/Hard Master, Multi-Language Programmer).
   - Real-time bonus points with duplicate award prevention.
7. **Exams & Certifications Module**:
   - **20 Specialized Domains**: Python Programming, C, C++, Java, JavaScript, React.js, Full-Stack, Frontend, Backend, SQL & Database, Data Structures, Algorithms, OOP, HTML & CSS, Node.js, Django, Operating Systems, DBMS, Software Engineering, Programming Fundamentals.
   - **Timed Sessions**: Interactive countdown timer with auto-submit, question navigator with instant state tracking, split-screen Monaco code editor for practical coding questions, and structured inputs for conceptual questions.
   - **Automated Grading & Scoring**: Comprehensive score evaluation, test case verification, and detailed post-exam review with explanations.
   - **Digital Verification & PDF Generation**: Automatic issuance upon scoring >= 70%. High-resolution A4 landscape vector PDF certificates generated via ReportLab with unique Certificate IDs, authenticated candidate names, "Platform Representative" signature label, and strictly no marks/percentages/pass-fail wording.
   - **My Certificates Hub**: Personal portal to preview, print, share, and download earned credentials.

---

## 📁 Project Structure

```
CodingChallengePlatform/
├── backend/
│   ├── .venv/                         # Python Virtual Environment
│   ├── config/                        # Django Project Settings & Root URLs
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── coding/                        # Core Coding App
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_problems.py   # Idempotent problem & achievement seeder
│   │   ├── migrations/                # Database migrations
│   │   ├── admin.py                   # Django Admin registration
│   │   ├── execution.py               # Sandboxed execution & Judge0 engine
│   │   ├── models.py                  # Problem, Submission, Progress, Achievement models
│   │   ├── serializers.py             # DRF serializers
│   │   ├── services.py                # Streaks, points, achievement unlock service
│   │   ├── tests.py                   # Automated API integration tests
│   │   ├── urls.py                    # REST API routes (/api/...)
│   │   └── views.py                   # API views
│   ├── db.sqlite3                     # Local SQLite database (pre-seeded)
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .env
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ActivityHeatmap.jsx    # GitHub-style green activity heatmap
│   │   │   ├── AnimatedIntro.jsx      # 5-second animated entrance
│   │   │   ├── Footer.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── ProtectedRoute.jsx
│   │   │   ├── StatCard.jsx
│   │   │   └── WeeklyActivityChart.jsx# 7-day SVG bar chart
│   │   ├── context/
│   │   │   └── AuthContext.jsx        # JWT session & user state management
│   │   ├── pages/
│   │   │   ├── AchievementsPage.jsx   # Milestone badges grid
│   │   │   ├── AuthPage.jsx           # Split-screen Sign In / Sign Up
│   │   │   ├── DashboardPage.jsx      # Overview metrics, charts, recommendations
│   │   │   ├── ProblemsListPage.jsx   # Search, filters, sort, pagination
│   │   │   ├── ProgressPage.jsx       # Analytics & domain mastery
│   │   │   ├── SubmissionsPage.jsx    # Submissions log & code viewer modal
│   │   │   └── WorkspacePage.jsx      # Monaco Editor coding workspace
│   │   ├── services/
│   │   │   └── api.js                 # Axios instance with Bearer interceptor
│   │   ├── App.jsx
│   │   ├── index.css                  # Tailwind styles & theme variables
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   ├── .env.example
│   └── .env
├── .gitignore
└── README.md
```

---

## 💻 Prerequisites

Ensure you have the following installed on your machine:
- **Node.js** (v18 or higher) & **npm** (v9 or higher)
- **Python** (3.10 to 3.13) with `py` launcher or `python` command

---

## ⚡ Quick Start Guide (Run in VS Code)

Open the `CodingChallengePlatform` root folder in VS Code.

> [!IMPORTANT]
> The backend and frontend run in **two separate terminals** simultaneously.

---

### Terminal 1 — Django Backend

1. Open a new terminal in VS Code:
```powershell
cd backend
```

2. If the virtual environment is not already active:
```powershell
# Windows:
.venv\Scripts\activate

# macOS / Linux:
source .venv/bin/activate
```
*(If you need to create a fresh venv on Windows: `py -m venv .venv` or `python -m venv .venv`)*

3. Verify dependencies are installed:
```powershell
pip install -r requirements.txt
```

4. Apply database migrations:
```powershell
py manage.py migrate
# Or on macOS/Linux: python manage.py migrate
```

5. Seed sample coding challenges and achievements:
```powershell
py manage.py seed_problems
# Or: python manage.py seed_problems
```

6. Start the Django API server:
```powershell
py manage.py runserver
# Or: python manage.py runserver
```
The backend API is now running at: **`http://127.0.0.1:8000/api/`**

---

### Terminal 2 — React Frontend (Vite)

1. Open a second terminal in VS Code:
```powershell
cd frontend
```

2. Verify dependencies:
```powershell
npm install
```

3. Start the Vite development server:
```powershell
npm run dev
```

4. Open your browser and navigate to:
**`http://localhost:5173`**

---

## 🔑 How to Create an Account & Use the Platform

1. When you first open `http://localhost:5173`, the **5-second animated intro** will greet you (you can also click **Skip Intro** in the top right).
2. On the authentication page, switch to **Create Account**.
3. Fill in:
   - **Full Name**: e.g., `Alex Turing`
   - **Email**: e.g., `alex@example.com`
   - **Username**: e.g., `alexturing`
   - **Password**: e.g., `CodeMaster2026!`
   - **Confirm Password**: e.g., `CodeMaster2026!`
4. Click **Create Account**. You will be securely authenticated and redirected straight to your **Dashboard**.
5. From the Dashboard:
   - Click **Explore Challenges** to browse problems.
   - Filter by category (e.g. *Algorithms*, *Python*, *SQL*) or difficulty (*Easy*, *Medium*, *Hard*).
   - Select **Solve Challenge** on any problem (e.g., *Two Sum*).
   - Choose your programming language, click **Run Code** to test against sample cases, and click **Submit Code** to evaluate against the entire suite!
   - Watch your points increase, your streak increment, and milestone achievements unlock!

---

## ⚙️ Configuration & Environment Variables

### Backend (`backend/.env`)

```ini
SECRET_KEY=django-insecure-development-key-change-in-production-codingplatform2026
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

# Optional: Judge0 Sandboxed Execution API
# (Leave blank to use the built-in isolated sub-process runner for Python/JavaScript)
JUDGE0_API_KEY=
JUDGE0_API_HOST=judge0-ce.p.rapidapi.com
JUDGE0_API_URL=https://judge0-ce.p.rapidapi.com

# Enable local isolated fallback execution for local development
ENABLE_LOCAL_FALLBACK_EXECUTION=True
```

### Frontend (`frontend/.env`)

```ini
VITE_API_URL=http://127.0.0.1:8000/api
```

---

## 🛡️ Optional: Judge0 Code Execution Setup

By default, the platform includes a built-in isolated sub-process execution runner for local testing (Python and Node.js) with strict timeouts and memory boundaries.

If you wish to route compilation for all languages (C, C++, Java, SQL) to a cloud sandbox:
1. Obtain a free Judge0 API key from [RapidAPI Judge0 CE](https://rapidapi.com/judge0-official/api/judge0-ce).
2. Open `backend/.env` and paste your key into `JUDGE0_API_KEY`:
   ```ini
   JUDGE0_API_KEY=your_rapidapi_key_here
   ```
3. Restart the Django server. All code executions will automatically route through the Judge0 sandbox.

---

## 🧪 Automated Testing

To run the complete automated test suite covering authentication, duplicate prevention, password hashing, code execution, test-case scoring, submission persistence, streaks, and analytics:

```powershell
cd backend
.venv\Scripts\activate
py manage.py test coding
```

Expected output:
```
Ran 8 tests in 9.021s

OK
```

To test the frontend build:
```powershell
cd frontend
npm run build
```

Expected output:
```
✓ built in ~2s
```

---

## 🔧 Troubleshooting Common Issues

1. **"Python was not found" on Windows**:
   - Use the `py` launcher: `py manage.py runserver`
   - Or point directly to the virtual environment Python: `.venv\Scripts\python.exe manage.py runserver`

2. **CORS errors or Network Error when logging in**:
   - Verify the Django backend is running on `http://127.0.0.1:8000`.
   - Check `frontend/.env` has `VITE_API_URL=http://127.0.0.1:8000/api`.

3. **Port 5173 or 8000 already in use**:
   - Backend on a different port: `py manage.py runserver 8001` (update `VITE_API_URL` accordingly in `frontend/.env`).
   - Frontend: Vite will automatically suggest port 5174 if 5173 is busy.
