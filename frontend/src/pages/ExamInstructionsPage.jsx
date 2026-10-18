import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import {
  Clock,
  HelpCircle,
  ShieldCheck,
  CheckCircle2,
  AlertTriangle,
  ArrowLeft,
  Play,
  Award,
  Sparkles,
  BookOpen,
  Code2,
  CheckCircle,
  FileText
} from 'lucide-react';

const ExamInstructionsPage = () => {
  const { slug } = useParams();
  const navigate = useNavigate();
  const [exam, setExam] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isStarting, setIsStarting] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchExamDetail();
  }, [slug]);

  const fetchExamDetail = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const res = await api.get(`/exams/${slug}/`);
      setExam(res.data);
    } catch (err) {
      console.error('Failed to load exam details:', err);
      setError('Could not load examination details. Please check the URL.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleStartExam = async () => {
    setIsStarting(true);
    setError(null);
    try {
      const res = await api.post(`/exams/${slug}/start/`);
      const attemptId = res.data.attempt_id;
      navigate(`/exams/${slug}/session/${attemptId}`);
    } catch (err) {
      console.error('Failed to start exam:', err);
      setError(err.response?.data?.detail || 'Failed to start examination session. Please try again.');
      setIsStarting(false);
    }
  };

  if (isLoading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <div className="w-10 h-10 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-600 font-medium">Preparing examination brief...</p>
      </div>
    );
  }

  if (error && !exam) {
    return (
      <div className="max-w-xl mx-auto px-4 py-16 text-center">
        <div className="p-4 rounded-xl bg-red-50 border border-red-200 text-red-700 text-sm mb-6">
          {error}
        </div>
        <Link
          to="/exams"
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-sm"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Catalog</span>
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      {/* Back button */}
      <Link
        to="/exams"
        className="inline-flex items-center gap-2 text-sm font-semibold text-slate-500 hover:text-emerald-600 mb-6 transition"
      >
        <ArrowLeft className="w-4 h-4" />
        <span>Back to Certification Catalog</span>
      </Link>

      {/* Main Brief Card */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden mb-8">
        {/* Header Ribbon */}
        <div className="bg-emerald-700 text-white p-6 sm:p-8">
          <div className="flex flex-wrap items-center justify-between gap-3 mb-3">
            <span className="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-white/20 backdrop-blur-md text-emerald-100">
              {exam.category_name} Domain
            </span>
            <span className="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-white/10 text-white border border-white/20">
              Difficulty: {exam.difficulty}
            </span>
          </div>

          <h1 className="text-2xl sm:text-3xl font-black tracking-tight leading-snug">
            {exam.title}
          </h1>

          <p className="mt-3 text-emerald-100 text-sm sm:text-base leading-relaxed max-w-2xl">
            {exam.description}
          </p>
        </div>

        {/* 4 Key Pillars */}
        <div className="grid grid-cols-2 sm:grid-cols-4 border-b border-slate-200 bg-slate-50 divide-x divide-y sm:divide-y-0 divide-slate-200">
          <div className="p-4 sm:p-5 text-center">
            <Clock className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
            <div className="text-xl font-black text-slate-900">{exam.duration_minutes} Mins</div>
            <div className="text-xs text-slate-500 font-medium">Time Limit</div>
          </div>

          <div className="p-4 sm:p-5 text-center">
            <HelpCircle className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
            <div className="text-xl font-black text-slate-900">{exam.questions_count}</div>
            <div className="text-xs text-slate-500 font-medium">Total Questions</div>
          </div>

          <div className="p-4 sm:p-5 text-center">
            <ShieldCheck className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
            <div className="text-xl font-black text-slate-900">{exam.total_marks}</div>
            <div className="text-xs text-slate-500 font-medium">Max Marks</div>
          </div>

          <div className="p-4 sm:p-5 text-center">
            <CheckCircle2 className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
            <div className="text-xl font-black text-slate-900">{exam.passing_percentage}%</div>
            <div className="text-xs text-slate-500 font-medium">Pass Threshold</div>
          </div>
        </div>

        {/* Instructions Body */}
        <div className="p-6 sm:p-8 space-y-6">
          {/* Previous Achievement banner if passed */}
          {exam.user_passed && exam.latest_certificate_id && (
            <div className="p-5 rounded-2xl bg-emerald-50 border border-emerald-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center flex-shrink-0">
                  <Award className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-emerald-950">You have earned this Certification!</h4>
                  <p className="text-xs text-emerald-700">Your credential is verified and available for download.</p>
                </div>
              </div>
              <Link
                to={`/certificates/${exam.latest_certificate_id}`}
                className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-sm transition"
              >
                View Certificate
              </Link>
            </div>
          )}

          {/* Guidelines */}
          <div>
            <h3 className="text-base font-bold text-slate-900 flex items-center gap-2 mb-3">
              <FileText className="w-4 h-4 text-emerald-600" />
              <span>Assessment Instructions & Code of Conduct</span>
            </h3>

            <div className="prose prose-sm text-slate-600 leading-relaxed space-y-2">
              <p>{exam.instructions}</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-4">
              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 flex items-start gap-3">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <div className="text-xs text-slate-700">
                  <span className="font-bold">Live Execution Engine:</span> Practical coding questions can be compiled and verified against test cases directly in the workspace.
                </div>
              </div>

              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 flex items-start gap-3">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <div className="text-xs text-slate-700">
                  <span className="font-bold">Auto-Save State:</span> Answers and code edits are automatically saved on the server. You can refresh or switch questions safely.
                </div>
              </div>

              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 flex items-start gap-3">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <div className="text-xs text-slate-700">
                  <span className="font-bold">Automatic Timer Submission:</span> When the countdown reaches 00:00, all answers are submitted automatically for final scoring.
                </div>
              </div>

              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 flex items-start gap-3">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <div className="text-xs text-slate-700">
                  <span className="font-bold">Instant Credential:</span> Scoring {exam.passing_percentage}% or higher immediately generates your official verified certificate with a unique ID.
                </div>
              </div>
            </div>
          </div>

          {/* Start Actions */}
          <div className="pt-6 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-xs text-slate-500">
              <AlertTriangle className="w-4 h-4 text-amber-500 flex-shrink-0" />
              <span>The timer starts immediately once you click Launch.</span>
            </div>

            <button
              onClick={handleStartExam}
              disabled={isStarting}
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-3.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-lg shadow-emerald-600/25 transition disabled:opacity-50"
            >
              {isStarting ? (
                <>
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                  <span>Launching Session...</span>
                </>
              ) : (
                <>
                  <Play className="w-4 h-4 fill-current" />
                  <span>Launch Certification Exam</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExamInstructionsPage;
