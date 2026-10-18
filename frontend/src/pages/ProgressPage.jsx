import React, { useState, useEffect } from 'react';
import api from '../services/api';
import StatCard from '../components/StatCard';
import { 
  LineChart, 
  CheckCircle2, 
  Target, 
  Flame, 
  Percent, 
  Cpu, 
  Award, 
  Zap, 
  TrendingUp, 
  AlertCircle 
} from 'lucide-react';

const ProgressPage = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const res = await api.get('/progress/analysis/');
        setData(res.data);
      } catch (err) {
        console.error("Failed to load analytics:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchAnalytics();
  }, []);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 animate-pulse space-y-6">
        <div className="h-10 bg-white rounded-2xl w-1/3" />
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="h-28 bg-white rounded-2xl" />
          <div className="h-28 bg-white rounded-2xl" />
          <div className="h-28 bg-white rounded-2xl" />
          <div className="h-28 bg-white rounded-2xl" />
        </div>
        <div className="h-64 bg-white rounded-2xl" />
      </div>
    );
  }

  if (!data) return null;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="pb-4 border-b border-slate-200">
        <h1 className="text-3xl font-black text-slate-900 tracking-tight flex items-center gap-3">
          <LineChart className="w-8 h-8 text-emerald-600" />
          <span>Performance & Analytics</span>
        </h1>
        <p className="text-sm text-slate-500 mt-1">
          Detailed metrics based directly on your code executions, submissions, and algorithmic growth.
        </p>
      </div>

      {/* Top Metrics Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <StatCard
          title="Acceptance Rate"
          value={`${data.acceptance_rate}%`}
          subtitle={`${data.accepted_submissions} accepted / ${data.total_submissions} total submissions`}
          icon={Percent}
          highlight={true}
        />
        <StatCard
          title="Problems Solved"
          value={data.problems_solved}
          subtitle={`Attempted: ${data.problems_attempted}`}
          icon={CheckCircle2}
        />
        <StatCard
          title="Coding Streak"
          value={`${data.current_streak} Days`}
          subtitle={`Longest: ${data.longest_streak} days`}
          icon={Flame}
        />
        <StatCard
          title="Avg Attempts to Solve"
          value={data.avg_attempts_to_solve || '1.0'}
          subtitle="Submissions per solved problem"
          icon={Zap}
        />
      </div>

      {/* Strongest Categories vs Topics Needing Improvement */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Strongest */}
        <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <div className="flex items-center gap-2 pb-3 border-b border-slate-100 mb-4">
            <TrendingUp className="w-5 h-5 text-emerald-600" />
            <h3 className="font-bold text-slate-900 text-base">Strongest Domains</h3>
          </div>
          {data.strongest_categories?.length > 0 ? (
            <div className="space-y-3">
              {data.strongest_categories.map((c) => (
                <div key={c.category} className="p-3 rounded-xl bg-emerald-50/50 border border-emerald-100 flex items-center justify-between">
                  <span className="font-bold text-slate-800 text-sm">{c.category}</span>
                  <span className="text-xs font-bold text-emerald-700 bg-white px-2.5 py-1 rounded-lg border border-emerald-200">
                    {c.percentage}% ({c.solved}/{c.total})
                  </span>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-500 py-4 text-center">Solve challenges to identify your strongest areas.</p>
          )}
        </div>

        {/* Needs Improvement */}
        <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <div className="flex items-center gap-2 pb-3 border-b border-slate-100 mb-4">
            <AlertCircle className="w-5 h-5 text-amber-500" />
            <h3 className="font-bold text-slate-900 text-base">Topics Needing Practice</h3>
          </div>
          {data.topics_needing_improvement?.length > 0 ? (
            <div className="space-y-3">
              {data.topics_needing_improvement.map((c) => (
                <div key={c.category} className="p-3 rounded-xl bg-amber-50/50 border border-amber-100 flex items-center justify-between">
                  <span className="font-bold text-slate-800 text-sm">{c.category}</span>
                  <span className="text-xs font-bold text-amber-700 bg-white px-2.5 py-1 rounded-lg border border-amber-200">
                    {c.percentage}% ({c.solved}/{c.total})
                  </span>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-500 py-4 text-center">All topics are currently at high mastery!</p>
          )}
        </div>
      </div>

      {/* Language Breakdown & Comprehensive Category Table */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Language usage */}
        <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <div className="flex items-center gap-2 pb-3 border-b border-slate-100 mb-4">
            <Cpu className="w-5 h-5 text-emerald-600" />
            <h3 className="font-bold text-slate-900 text-base">Language Usage</h3>
          </div>
          {data.language_breakdown?.length > 0 ? (
            <div className="space-y-3">
              {data.language_breakdown.map((l) => (
                <div key={l.language} className="p-3 rounded-xl bg-slate-50 border border-slate-100">
                  <div className="flex justify-between items-center text-xs font-semibold mb-1">
                    <span className="capitalize font-mono text-slate-800">{l.language}</span>
                    <span className="text-emerald-700 font-bold">{l.accepted} / {l.total} accepted</span>
                  </div>
                  <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-emerald-600 rounded-full"
                      style={{ width: `${l.total > 0 ? (l.accepted / l.total) * 100 : 0}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-500 py-4 text-center">No language data recorded yet.</p>
          )}
        </div>

        {/* Category Breakdown Table */}
        <div className="lg:col-span-2 p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <h3 className="font-bold text-slate-900 text-base mb-1">Category Breakdown</h3>
          <p className="text-xs text-slate-500 mb-4">All tracked technical domains</p>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                <tr>
                  <th className="py-2.5 px-3">Category</th>
                  <th className="py-2.5 px-3">Available</th>
                  <th className="py-2.5 px-3">Solved</th>
                  <th className="py-2.5 px-3">Progress</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 font-medium">
                {data.category_breakdown?.map((cat) => (
                  <tr key={cat.category}>
                    <td className="py-3 px-3 font-bold text-slate-800">{cat.category}</td>
                    <td className="py-3 px-3 text-slate-500">{cat.total}</td>
                    <td className="py-3 px-3 text-emerald-700 font-bold">{cat.solved}</td>
                    <td className="py-3 px-3 w-40">
                      <div className="flex items-center gap-2">
                        <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                          <div
                            className="h-full bg-emerald-600 rounded-full"
                            style={{ width: `${cat.percentage}%` }}
                          />
                        </div>
                        <span className="text-[11px] font-bold text-slate-600 w-9 text-right">{cat.percentage}%</span>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProgressPage;
