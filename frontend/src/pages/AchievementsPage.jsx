import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { 
  Award, 
  Sparkles, 
  Target, 
  Flame, 
  Zap, 
  CheckCircle, 
  Shield, 
  Trophy, 
  Code, 
  Crown, 
  Lock, 
  CheckCircle2 
} from 'lucide-react';

const ICON_MAP = {
  Sparkles,
  Target,
  Award,
  Crown,
  Flame,
  Zap,
  CheckCircle,
  Shield,
  Trophy,
  Code,
};

const AchievementsPage = () => {
  const [achievements, setAchievements] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAchievements = async () => {
      try {
        const res = await api.get('/achievements/');
        setAchievements(res.data || []);
      } catch (err) {
        console.error("Failed to fetch achievements:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchAchievements();
  }, []);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 animate-pulse space-y-6">
        <div className="h-10 bg-white rounded-2xl w-1/3" />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="h-44 bg-white rounded-3xl" />
          ))}
        </div>
      </div>
    );
  }

  const unlockedCount = achievements.filter((a) => a.is_unlocked).length;
  const totalCount = achievements.length;
  const progressPct = totalCount > 0 ? Math.round((unlockedCount / totalCount) * 100) : 0;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header & Overall Achievement Progress */}
      <div className="rounded-3xl bg-gradient-to-r from-emerald-800 via-emerald-700 to-green-800 p-8 text-white shadow-xl shadow-emerald-900/10 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-600/60 border border-emerald-400/30 text-emerald-100 text-xs font-semibold mb-3">
            <Award className="w-3.5 h-3.5 text-emerald-300" /> Milestone Rewards
          </div>
          <h1 className="text-3xl sm:text-4xl font-black tracking-tight">Achievements & Badges</h1>
          <p className="mt-2 text-sm text-emerald-100/90 max-w-xl">
            Conquer challenges, build streaks, and master multiple languages to unlock exclusive badges and boost your points.
          </p>
        </div>

        <div className="bg-white/10 backdrop-blur-md p-5 rounded-2xl border border-white/20 min-w-[240px]">
          <div className="flex justify-between items-center text-xs font-bold mb-2">
            <span>Unlocked</span>
            <span className="text-emerald-200">{unlockedCount} of {totalCount} ({progressPct}%)</span>
          </div>
          <div className="w-full h-2 bg-black/20 rounded-full overflow-hidden">
            <div
              className="h-full bg-emerald-300 rounded-full transition-all duration-500"
              style={{ width: `${progressPct}%` }}
            />
          </div>
        </div>
      </div>

      {/* Achievements Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {achievements.map((item) => {
          const IconComponent = ICON_MAP[item.badge_icon] || Award;
          const isUnlocked = item.is_unlocked;

          return (
            <div
              key={item.id}
              className={`p-6 rounded-3xl border transition-all duration-200 flex flex-col justify-between ${
                isUnlocked
                  ? 'bg-white border-emerald-300 ring-2 ring-emerald-50 shadow-md shadow-emerald-900/5'
                  : 'bg-slate-50/70 border-slate-200 opacity-75'
              }`}
            >
              <div>
                <div className="flex items-start justify-between mb-4">
                  <div className={`w-12 h-12 rounded-2xl flex items-center justify-center ${
                    isUnlocked
                      ? 'bg-emerald-600 text-white shadow-md shadow-emerald-600/25'
                      : 'bg-slate-200 text-slate-400'
                  }`}>
                    {isUnlocked ? <IconComponent className="w-6 h-6" /> : <Lock className="w-5 h-5" />}
                  </div>

                  <span className={`text-xs font-bold px-2.5 py-1 rounded-full ${
                    isUnlocked
                      ? 'bg-emerald-100 text-emerald-800'
                      : 'bg-slate-200 text-slate-500'
                  }`}>
                    +{item.points_reward} pts
                  </span>
                </div>

                <h3 className="font-extrabold text-slate-900 text-base">{item.title}</h3>
                <p className="text-xs text-slate-600 mt-1.5 leading-relaxed">
                  {item.description}
                </p>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs">
                {isUnlocked ? (
                  <span className="flex items-center gap-1.5 text-emerald-700 font-bold">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                    Unlocked {new Date(item.unlocked_at).toLocaleDateString()}
                  </span>
                ) : (
                  <span className="text-slate-400 font-medium flex items-center gap-1">
                    <Lock className="w-3.5 h-3.5" /> Locked
                  </span>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default AchievementsPage;
