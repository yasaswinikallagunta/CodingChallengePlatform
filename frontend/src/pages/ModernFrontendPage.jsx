import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import { COURSE_METADATA, COURSE_TOPICS, getTopicBySlug } from '../data/modernFrontendCourseData';
import TheoryViewer from '../components/course/TheoryViewer';
import ExampleViewer from '../components/course/ExampleViewer';
import ExerciseWorkspace from '../components/course/ExerciseWorkspace';
import { 
  BookOpen, 
  Code2, 
  Sparkles, 
  CheckCircle2, 
  CheckCircle, 
  FileCode, 
  Layers, 
  Database, 
  Cloud, 
  Terminal, 
  Palette, 
  Flame, 
  Award, 
  ChevronRight, 
  RotateCcw,
  Clock,
  Compass,
  ArrowRight
} from 'lucide-react';

const TOPIC_ICON_MAP = {
  FileCode: FileCode,
  Palette: Palette,
  Sparkles: Sparkles,
  Terminal: Terminal,
  Flame: Flame,
  Layers: Layers,
  Database: Database,
  Cloud: Cloud
};

export default function ModernFrontendPage() {
  const { topicSlug } = useParams();
  const navigate = useNavigate();

  // Active topic state
  const activeTopic = getTopicBySlug(topicSlug);
  const [activeTab, setActiveTab] = useState('practice'); // 'theory' | 'example' | 'practice'

  // Backend Progress State
  const [loadingProgress, setLoadingProgress] = useState(true);
  const [completedMap, setCompletedMap] = useState({}); // { `${topic_slug}-${exercise_id}`: true }
  const [userCodesMap, setUserCodesMap] = useState({}); // { `${topic_slug}-${exercise_id}`: 'code' }
  const [stats, setStats] = useState({
    completed_exercises_count: 0,
    total_exercises_count: 40,
    percentage: 0
  });

  // Fetch student progress from backend API
  const fetchProgress = async () => {
    try {
      const res = await api.get('/courses/modern-frontend-development/progress/');
      if (res.data) {
        const cMap = {};
        const uMap = {};
        (res.data.progress_items || []).forEach((item) => {
          const key = `${item.topic_slug}-${item.exercise_id}`;
          if (item.completed) {
            cMap[key] = true;
          }
          if (item.user_code) {
            uMap[key] = item.user_code;
          }
        });
        setCompletedMap(cMap);
        setUserCodesMap(uMap);
        setStats({
          completed_exercises_count: res.data.completed_exercises_count || 0,
          total_exercises_count: res.data.total_exercises_count || 40,
          percentage: res.data.percentage || 0
        });
      }
    } catch (err) {
      console.warn('Unable to load course progress from backend, using local session state:', err);
    } finally {
      setLoadingProgress(false);
    }
  };

  useEffect(() => {
    fetchProgress();
  }, []);

  const handleSaveProgress = async (topicId, exerciseId, completed, code) => {
    const key = `${topicId}-${exerciseId}`;

    // Optimistically update local state
    setCompletedMap((prev) => {
      const next = { ...prev };
      if (completed) {
        next[key] = true;
      } else {
        delete next[key];
      }
      return next;
    });

    if (code) {
      setUserCodesMap((prev) => ({
        ...prev,
        [key]: code
      }));
    }

    try {
      const res = await api.post('/courses/modern-frontend-development/save-progress/', {
        topic_slug: topicId,
        exercise_id: exerciseId,
        completed: completed,
        user_code: code || ''
      });

      if (res.data) {
        setStats({
          completed_exercises_count: res.data.completed_exercises_count || 0,
          total_exercises_count: res.data.total_exercises_count || 40,
          percentage: res.data.percentage || 0
        });
      }
    } catch (err) {
      console.error('Failed to sync course progress to backend:', err);
    }
  };

  const handleResetCourseProgress = async () => {
    if (!window.confirm('Are you sure you want to reset all practice progress for Modern Frontend Development?')) {
      return;
    }

    try {
      await api.post('/courses/modern-frontend-development/reset-progress/');
      setCompletedMap({});
      setUserCodesMap({});
      setStats({
        completed_exercises_count: 0,
        total_exercises_count: 40,
        percentage: 0
      });
    } catch (err) {
      console.error('Error resetting progress:', err);
    }
  };

  const handleSelectTopic = (slug) => {
    navigate(`/course/modern-frontend-development/${slug}`);
  };

  const handleNextTopic = () => {
    const currentIndex = COURSE_TOPICS.findIndex((t) => t.id === activeTopic.id);
    if (currentIndex < COURSE_TOPICS.length - 1) {
      const nextSlug = COURSE_TOPICS[currentIndex + 1].id;
      navigate(`/course/modern-frontend-development/${nextSlug}`);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  // Helper to count completed exercises for a specific topic
  const getTopicCompletedCount = (topicId) => {
    const topic = COURSE_TOPICS.find((t) => t.id === topicId);
    if (!topic || !topic.exercises) return 0;
    return topic.exercises.filter((ex) => completedMap[`${topicId}-${ex.id}`]).length;
  };

  const ActiveIcon = TOPIC_ICON_MAP[activeTopic.icon] || FileCode;

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 pb-16">
      {/* Course Hero Banner */}
      <section className="bg-gradient-to-br from-emerald-800 via-emerald-700 to-green-900 text-white border-b border-emerald-950/40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-10">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
            <div className="space-y-3 max-w-3xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-600/70 border border-emerald-400/30 text-emerald-100 text-xs font-bold tracking-wide">
                <Sparkles className="w-3.5 h-3.5 text-emerald-300" />
                <span>{COURSE_METADATA.badge}</span>
                <span className="text-emerald-300">•</span>
                <span>{COURSE_METADATA.level}</span>
              </div>

              <h1 className="text-3xl sm:text-4xl font-black tracking-tight text-white">
                {COURSE_METADATA.title}
              </h1>

              <p className="text-sm sm:text-base text-emerald-100/90 leading-relaxed max-w-2xl">
                {COURSE_METADATA.description}
              </p>

              <div className="flex flex-wrap items-center gap-4 text-xs text-emerald-200 pt-1">
                <span className="flex items-center gap-1.5">
                  <BookOpen className="w-4 h-4 text-emerald-300" />
                  <strong>8 Syllabus Topics</strong>
                </span>
                <span>•</span>
                <span className="flex items-center gap-1.5">
                  <Code2 className="w-4 h-4 text-emerald-300" />
                  <strong>40 Practice Tasks</strong> (5 per topic)
                </span>
                <span>•</span>
                <span className="flex items-center gap-1.5">
                  <Clock className="w-4 h-4 text-emerald-300" />
                  <strong>~{COURSE_METADATA.estimatedHours} Hours of Hands-on Lab</strong>
                </span>
              </div>
            </div>

            {/* Overall Course Progress Widget */}
            <div className="w-full lg:w-80 bg-white/10 backdrop-blur-md p-5 rounded-2xl border border-white/20 shadow-lg">
              <div className="flex items-center justify-between text-xs font-bold text-emerald-100 mb-2">
                <span>Curriculum Mastery</span>
                <span className="text-base text-white">{stats.percentage}%</span>
              </div>

              {/* Progress Bar */}
              <div className="w-full h-3 bg-black/20 rounded-full overflow-hidden p-0.5 border border-white/10">
                <div
                  className="h-full bg-gradient-to-r from-emerald-400 to-green-300 rounded-full transition-all duration-500 shadow-sm"
                  style={{ width: `${stats.percentage}%` }}
                />
              </div>

              <div className="flex items-center justify-between text-xs text-emerald-200 mt-2 font-medium">
                <span>{stats.completed_exercises_count} of {stats.total_exercises_count} Tasks Completed</span>
                <button
                  onClick={handleResetCourseProgress}
                  className="text-emerald-300 hover:text-white transition flex items-center gap-1 text-[11px] underline"
                >
                  <RotateCcw className="w-3 h-3" /> Reset
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Main Course Content Container */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Topic Navigation Sidebar (8 Topics cleanly organized directly under Modern Frontend Development) */}
          <aside className="lg:col-span-4 space-y-4">
            <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between px-2 pb-3 mb-2 border-b border-slate-100">
                <span className="text-xs font-extrabold uppercase tracking-wider text-slate-500">
                  Course Syllabus Topics
                </span>
                <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                  8 Topics
                </span>
              </div>

              <nav className="space-y-1.5" aria-label="Course Topics">
                {COURSE_TOPICS.map((topic, index) => {
                  const isSelected = topic.id === activeTopic.id;
                  const completedCount = getTopicCompletedCount(topic.id);
                  const isAllDone = completedCount === (topic.exercises?.length || 5);
                  const TopicIcon = TOPIC_ICON_MAP[topic.icon] || FileCode;

                  return (
                    <button
                      key={topic.id}
                      onClick={() => handleSelectTopic(topic.id)}
                      className={`w-full p-3 rounded-xl text-left transition flex items-center justify-between gap-3 group ${
                        isSelected
                          ? 'bg-emerald-600 text-white shadow-md shadow-emerald-600/20 font-bold'
                          : 'bg-white text-slate-700 hover:bg-slate-50 hover:text-slate-900 border border-slate-100'
                      }`}
                    >
                      <div className="flex items-center gap-3 min-w-0">
                        <div
                          className={`w-8 h-8 rounded-lg flex items-center justify-center shrink-0 transition ${
                            isSelected
                              ? 'bg-white/20 text-white'
                              : 'bg-emerald-50 text-emerald-700 group-hover:bg-emerald-100'
                          }`}
                        >
                          <TopicIcon className="w-4 h-4" />
                        </div>
                        <div className="truncate">
                          <div className="text-xs sm:text-sm font-bold truncate">
                            {topic.title}
                          </div>
                          <div
                            className={`text-[11px] truncate ${
                              isSelected ? 'text-emerald-100' : 'text-slate-400'
                            }`}
                          >
                            5 Practice Tasks
                          </div>
                        </div>
                      </div>

                      <div className="shrink-0 flex items-center gap-1.5">
                        <span
                          className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${
                            isSelected
                              ? 'bg-white/20 text-white'
                              : isAllDone
                              ? 'bg-emerald-100 text-emerald-800'
                              : 'bg-slate-100 text-slate-600'
                          }`}
                        >
                          {completedCount}/5
                        </span>
                        {isAllDone && (
                          <CheckCircle className={`w-4 h-4 ${isSelected ? 'text-white' : 'text-emerald-600'}`} />
                        )}
                      </div>
                    </button>
                  );
                })}
              </nav>
            </div>

            {/* Quick Skills Summary Card */}
            <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hidden lg:block">
              <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider mb-3 flex items-center gap-2">
                <Award className="w-4 h-4 text-emerald-600" />
                Industry Competencies
              </h3>
              <ul className="space-y-2 text-xs text-slate-600">
                {COURSE_METADATA.skillsCovered.map((skill, sIdx) => (
                  <li key={sIdx} className="flex items-start gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-1.5 shrink-0" />
                    <span>{skill}</span>
                  </li>
                ))}
              </ul>
            </div>
          </aside>

          {/* Active Topic Main Workspace */}
          <main className="lg:col-span-8 space-y-6">
            {/* Active Topic Header Card */}
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
              <div className="flex flex-wrap items-center justify-between gap-3 mb-3">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center">
                    <ActiveIcon className="w-5 h-5" />
                  </div>
                  <div>
                    <h2 className="text-2xl font-black text-slate-900 tracking-tight">
                      {activeTopic.title}
                    </h2>
                    <span className="text-xs font-semibold text-emerald-700">
                      Topic {COURSE_TOPICS.findIndex(t => t.id === activeTopic.id) + 1} of 8
                    </span>
                  </div>
                </div>

                <div className="flex items-center gap-2 text-xs font-bold">
                  <span className="px-3 py-1 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
                    {getTopicCompletedCount(activeTopic.id)} / 5 Tasks Done
                  </span>
                </div>
              </div>

              <p className="text-sm text-slate-600 leading-relaxed mb-6">
                {activeTopic.description}
              </p>

              {/* 3 Core Learning Mode Tabs */}
              <div className="grid grid-cols-3 gap-2 bg-slate-100/90 p-1.5 rounded-xl border border-slate-200">
                <button
                  onClick={() => setActiveTab('theory')}
                  className={`py-2 px-3 rounded-lg text-xs font-bold transition flex items-center justify-center gap-2 ${
                    activeTab === 'theory'
                      ? 'bg-white text-emerald-800 shadow-sm'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  <BookOpen className="w-4 h-4 text-emerald-600" />
                  <span className="hidden sm:inline">1. Theory &amp; Concepts</span>
                  <span className="sm:hidden">Theory</span>
                </button>

                <button
                  onClick={() => setActiveTab('example')}
                  className={`py-2 px-3 rounded-lg text-xs font-bold transition flex items-center justify-center gap-2 ${
                    activeTab === 'example'
                      ? 'bg-white text-emerald-800 shadow-sm'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  <Code2 className="w-4 h-4 text-emerald-600" />
                  <span className="hidden sm:inline">2. Code &amp; Live Preview</span>
                  <span className="sm:hidden">Example</span>
                </button>

                <button
                  onClick={() => setActiveTab('practice')}
                  className={`py-2 px-3 rounded-lg text-xs font-bold transition flex items-center justify-center gap-2 ${
                    activeTab === 'practice'
                      ? 'bg-white text-emerald-800 shadow-sm'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  <Sparkles className="w-4 h-4 text-emerald-600" />
                  <span className="hidden sm:inline">3. Practice Lab (5 Tasks)</span>
                  <span className="sm:hidden">Practice</span>
                </button>
              </div>
            </div>

            {/* Tab 1: Theory */}
            {activeTab === 'theory' && (
              <TheoryViewer topic={activeTopic} />
            )}

            {/* Tab 2: Example Code & Live Preview */}
            {activeTab === 'example' && activeTopic.example && (
              <ExampleViewer example={activeTopic.example} />
            )}

            {/* Tab 3: Practice Exercises (5 distinct exercises) */}
            {activeTab === 'practice' && (
              <ExerciseWorkspace
                topic={activeTopic}
                completedMap={completedMap}
                userCodesMap={userCodesMap}
                onSaveProgress={handleSaveProgress}
                onNextTopic={handleNextTopic}
              />
            )}
          </main>
        </div>
      </div>
    </div>
  );
}
