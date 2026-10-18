import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';
import StatCard from '../components/StatCard';
import ActivityHeatmap from '../components/ActivityHeatmap';
import WeeklyActivityChart from '../components/WeeklyActivityChart';
import { 
  Terminal, 
  Flame, 
  Award, 
  CheckCircle2, 
  Target, 
  Compass, 
  ArrowRight, 
  Sparkles, 
  Clock, 
  ChevronRight, 
  Zap,
  TrendingUp,
  Code,
  GraduationCap,
  BookOpen
} from 'lucide-react';

const DashboardPage = () => {
  const { user } = useAuth();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const res = await api.get('/dashboard/stats/');
        setData(res.data);
      } catch (err) {
        console.error("Dashboard fetch error:", err);
        setError("Unable to load dashboard statistics from backend.");
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="animate-pulse space-y-6">
          <div className="h-16 bg-white rounded-2xl w-1/2" />
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="h-28 bg-white rounded-2xl" />
            <div className="h-28 bg-white rounded-2xl" />
            <div className="h-28 bg-white rounded-2xl" />
            <div className="h-28 bg-white rounded-2xl" />
          </div>
          <div className="h-64 bg-white rounded-2xl" />
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-center">
        <div className="inline-flex p-4 rounded-full bg-red-50 text-red-600 mb-4">
          <Terminal className="w-8 h-8" />
        </div>
        <h2 className="text-xl font-bold text-slate-800">Connection Error</h2>
        <p className="text-slate-500 text-sm mt-1 mb-6">{error || 'Please make sure the Django backend is running.'}</p>
        <button
          onClick={() => window.location.reload()}
          className="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-sm transition"
        >
          Retry Connection
        </button>
      </div>
    );
  }

  const { overview } = data;
  const userName = user?.first_name || user?.username || 'Developer';

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header Greeting Banner */}
      <div className="rounded-3xl bg-gradient-to-r from-emerald-800 via-emerald-700 to-green-800 p-6 sm:p-8 text-white shadow-xl shadow-emerald-900/10 relative overflow-hidden">
        <div className="absolute right-0 top-0 w-80 h-80 bg-white/5 rounded-full blur-2xl pointer-events-none" />
        <div className="relative z-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <div>
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-600/60 border border-emerald-400/30 text-emerald-100 text-xs font-semibold mb-3">
              <Sparkles className="w-3.5 h-3.5 text-emerald-300" /> Coding Dashboard
            </div>
            <h1 className="text-2xl sm:text-3xl md:text-4xl font-black tracking-tight">
              Welcome back, <span className="text-emerald-200">{userName}</span>!
            </h1>
            <p className="mt-2 text-sm sm:text-base text-emerald-100/90 font-medium max-w-xl">
              Your next breakthrough starts with one more line of code.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <Link
              to="/course/modern-frontend-development"
              className="px-5 py-3 rounded-xl bg-white text-emerald-800 font-bold text-sm shadow-md hover:bg-emerald-50 transition flex items-center gap-2"
            >
              <BookOpen className="w-4 h-4 text-emerald-600" />
              <span>Frontend Course</span>
            </Link>
            <Link
              to="/problems"
              className="px-5 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm shadow-md transition flex items-center gap-2"
            >
              <Compass className="w-4 h-4 text-white" />
              <span>Explore Challenges</span>
            </Link>
            <Link
              to="/exams"
              className="px-5 py-3 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 text-white font-bold text-sm shadow-md transition flex items-center gap-2"
            >
              <GraduationCap className="w-4 h-4 text-emerald-300" />
              <span>Certifications</span>
            </Link>
          </div>
        </div>
      </div>

      {/* Top Overview Metric Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <StatCard
          title="Problems Solved"
          value={overview.problems_solved}
          subtitle={`Out of ${overview.total_problems} available`}
          icon={CheckCircle2}
          badge={`${overview.completion_percentage}%`}
          highlight={true}
        />
        <StatCard
          title="Current Streak"
          value={`${overview.current_streak} Days`}
          subtitle={`Best: ${overview.longest_streak} consecutive days`}
          icon={Flame}
        />
        <StatCard
          title="Points Earned"
          value={overview.points_earned}
          subtitle="Score from challenges & badges"
          icon={TrendingUp}
        />
        <StatCard
          title="Achievements"
          value={`${overview.achievements_unlocked} / ${overview.total_achievements}`}
          subtitle="Milestones conquered"
          icon={Award}
        />
      </div>

      {/* Difficulty Breakdown & Continue Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Difficulty-wise progress card */}
        <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex flex-col justify-between">
          <div>
            <h3 className="font-bold text-slate-900 text-base mb-1">Difficulty Breakdown</h3>
            <p className="text-xs text-slate-500 mb-5">Problems solved across challenge tiers</p>

            <div className="space-y-4">
              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-emerald-700">Easy</span>
                  <span className="text-slate-600">{overview.easy_solved} / {overview.easy_total}</span>
                </div>
                <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-emerald-500 rounded-full transition-all duration-500"
                    style={{ width: `${overview.easy_total > 0 ? (overview.easy_solved / overview.easy_total) * 100 : 0}%` }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-amber-600">Medium</span>
                  <span className="text-slate-600">{overview.medium_solved} / {overview.medium_total}</span>
                </div>
                <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-amber-500 rounded-full transition-all duration-500"
                    style={{ width: `${overview.medium_total > 0 ? (overview.medium_solved / overview.medium_total) * 100 : 0}%` }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-rose-600">Hard</span>
                  <span className="text-slate-600">{overview.hard_solved} / {overview.hard_total}</span>
                </div>
                <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-rose-500 rounded-full transition-all duration-500"
                    style={{ width: `${overview.hard_total > 0 ? (overview.hard_solved / overview.hard_total) * 100 : 0}%` }}
                  />
                </div>
              </div>
            </div>
          </div>

          <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
            <span>Overall Completion</span>
            <span className="font-bold text-slate-800">{overview.completion_percentage}%</span>
          </div>
        </div>

        {/* Weekly Chart */}
        <div className="lg:col-span-2">
          <WeeklyActivityChart data={data.weekly_activity} />
        </div>
      </div>

      {/* Activity Heatmap */}
      <ActivityHeatmap data={data.heatmap_data} />

      {/* Featured Course: Modern Frontend Development */}
      <div className="p-6 rounded-2xl bg-gradient-to-r from-emerald-900 via-emerald-800 to-green-900 text-white shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div className="space-y-2 max-w-2xl">
          <div className="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-emerald-700/60 border border-emerald-400/30 text-emerald-200 text-xs font-bold">
            <Sparkles className="w-3.5 h-3.5" /> Featured Learning Course
          </div>
          <h3 className="text-xl sm:text-2xl font-black text-white tracking-tight">
            Modern Frontend Development
          </h3>
          <p className="text-xs sm:text-sm text-emerald-100/90 leading-relaxed">
            Hands-on career curriculum with theory, production examples, and 40 practice tasks across 8 core topics: HTML5, CSS3, Advanced CSS, JavaScript, Advanced JS, React, MongoDB, and Deployment.
          </p>
        </div>

        <Link
          to="/course/modern-frontend-development"
          className="px-6 py-3 rounded-xl bg-white text-emerald-800 hover:bg-emerald-50 font-bold text-sm shadow-md transition flex items-center gap-2 shrink-0"
        >
          <span>Open Frontend Course</span>
          <ArrowRight className="w-4 h-4 text-emerald-600" />
        </Link>
      </div>

      {/* Category Performance & Recommended Challenges */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Category Performance */}
        <div className="lg:col-span-1 p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <h3 className="font-bold text-slate-900 text-base mb-1">Category Performance</h3>
          <p className="text-xs text-slate-500 mb-4">Topic-level competency</p>

          <div className="space-y-3.5 max-h-80 overflow-y-auto pr-1">
            {data.category_performance?.map((cat) => (
              <div key={cat.category} className="p-2.5 rounded-xl bg-slate-50 border border-slate-100">
                <div className="flex justify-between items-center text-xs font-semibold mb-1">
                  <span className="text-slate-800">{cat.category}</span>
                  <span className="text-emerald-700 font-bold">{cat.solved} / {cat.total}</span>
                </div>
                <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-emerald-600 rounded-full"
                    style={{ width: `${cat.percentage}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Recommended & Recently Attempted Challenges */}
        <div className="lg:col-span-2 space-y-6">
          {/* Continue Coding / Recently Attempted */}
          <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
            <div className="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
              <div className="flex items-center gap-2">
                <Target className="w-5 h-5 text-emerald-600" />
                <h3 className="font-bold text-slate-900 text-base">Recommended Challenges</h3>
              </div>
              <Link to="/problems" className="text-xs font-bold text-emerald-600 hover:text-emerald-700 flex items-center gap-1">
                View All <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            <div className="space-y-3">
              {data.recommended_challenges?.length > 0 ? (
                data.recommended_challenges.map((prob) => (
                  <div
                    key={prob.id}
                    className="p-4 rounded-xl border border-slate-200 hover:border-emerald-300 hover:bg-emerald-50/20 transition flex flex-col sm:flex-row sm:items-center justify-between gap-3"
                  >
                    <div>
                      <div className="flex items-center gap-2 mb-1">
                        <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                          prob.difficulty === 'Easy' ? 'bg-emerald-100 text-emerald-800' :
                          prob.difficulty === 'Medium' ? 'bg-amber-100 text-amber-800' :
                          'bg-rose-100 text-rose-800'
                        }`}>
                          {prob.difficulty}
                        </span>
                        <span className="text-xs font-medium text-slate-500">{prob.category}</span>
                        <span className="text-xs font-bold text-emerald-600">+{prob.points} pts</span>
                      </div>
                      <h4 className="font-bold text-slate-900 text-sm">{prob.title}</h4>
                    </div>

                    <Link
                      to={`/workspace/${prob.slug}`}
                      className="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs transition flex items-center justify-center gap-1 shrink-0"
                    >
                      <span>Solve Challenge</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </Link>
                  </div>
                ))
              ) : (
                <div className="p-6 text-center text-xs text-slate-500">
                  You have conquered all current challenges! More coming soon.
                </div>
              )}
            </div>
          </div>

          {/* Recent Submissions Snippet */}
          <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
            <div className="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
              <div className="flex items-center gap-2">
                <Clock className="w-5 h-5 text-emerald-600" />
                <h3 className="font-bold text-slate-900 text-base">Recent Submissions</h3>
              </div>
              <Link to="/submissions" className="text-xs font-bold text-emerald-600 hover:text-emerald-700 flex items-center gap-1">
                History <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            {data.recent_submissions?.length > 0 ? (
              <div className="divide-y divide-slate-100">
                {data.recent_submissions.map((sub) => (
                  <div key={sub.id} className="py-2.5 flex items-center justify-between text-xs">
                    <div>
                      <span className="font-bold text-slate-800 mr-2">{sub.problem_title}</span>
                      <span className="text-slate-400 capitalize">{sub.language}</span>
                    </div>
                    <div className="flex items-center gap-3">
                      <span className={`font-bold px-2 py-0.5 rounded-full text-[11px] ${
                        sub.status === 'Accepted'
                          ? 'bg-emerald-100 text-emerald-800'
                          : 'bg-red-100 text-red-700'
                      }`}>
                        {sub.status}
                      </span>
                      <span className="text-slate-400">
                        {new Date(sub.submitted_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-xs text-slate-500 py-3 text-center">
                No submissions yet. Pick a challenge and write your first code!
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
