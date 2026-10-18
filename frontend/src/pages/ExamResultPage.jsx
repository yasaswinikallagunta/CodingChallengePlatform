import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import confetti from 'canvas-confetti';
import api from '../services/api';
import {
  Award,
  CheckCircle2,
  XCircle,
  Clock,
  ShieldCheck,
  ChevronDown,
  ChevronUp,
  ArrowRight,
  RotateCcw,
  BookOpen,
  Sparkles,
  ExternalLink,
  Code2,
  HelpCircle,
  FileCheck
} from 'lucide-react';

const ExamResultPage = () => {
  const { attemptId } = useParams();
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [expandedQuestion, setExpandedQuestion] = useState(null);

  useEffect(() => {
    fetchResult();
  }, [attemptId]);

  const fetchResult = async () => {
    setIsLoading(true);
    try {
      const res = await api.get(`/exams/attempts/${attemptId}/result/`);
      setResult(res.data);

      if (res.data.passed) {
        // Fire confetti celebration
        triggerCelebration();
      }
    } catch (err) {
      console.error('Failed to load exam result:', err);
      setError('Could not load examination results. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const triggerCelebration = () => {
    try {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#16A34A', '#22C55E', '#86EFAC', '#FDE047'],
      });
    } catch (e) {
      // ignore
    }
  };

  const formatSeconds = (sec) => {
    const mins = Math.floor(sec / 60);
    const remainingSecs = sec % 60;
    return `${mins}m ${remainingSecs}s`;
  };

  if (isLoading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <div className="w-10 h-10 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-600 font-medium">Calculating official evaluation score...</p>
      </div>
    );
  }

  if (error || !result) {
    return (
      <div className="max-w-xl mx-auto px-4 py-16 text-center">
        <div className="p-4 rounded-xl bg-red-50 border border-red-200 text-red-700 text-sm mb-6">
          {error || 'Result not found.'}
        </div>
        <Link
          to="/exams"
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-sm"
        >
          <span>Back to Certifications</span>
        </Link>
      </div>
    );
  }

  const isPassed = result.passed;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      {/* Top Banner Result Card */}
      <div
        className={`rounded-3xl border p-8 sm:p-10 mb-8 text-white relative overflow-hidden shadow-xl ${
          isPassed
            ? 'bg-gradient-to-br from-emerald-800 via-emerald-700 to-green-900 border-emerald-600 shadow-emerald-900/15'
            : 'bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 border-slate-700 shadow-slate-900/15'
        }`}
      >
        <div className="relative z-10 max-w-3xl">
          {/* Status Chip */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-4 bg-white/10 backdrop-blur-md border border-white/20">
            {isPassed ? (
              <>
                <Sparkles className="w-3.5 h-3.5 text-emerald-300" />
                <span className="text-emerald-200">Official Certification Passed</span>
              </>
            ) : (
              <>
                <XCircle className="w-3.5 h-3.5 text-rose-300" />
                <span className="text-rose-200">Assessment Incomplete</span>
              </>
            )}
          </div>

          <h1 className="text-2xl sm:text-4xl font-black tracking-tight leading-tight">
            {isPassed ? 'Congratulations! You Passed.' : 'Keep Practicing & Try Again'}
          </h1>

          <p className="mt-2 text-sm sm:text-base text-slate-200 leading-relaxed">
            {isPassed
              ? `You have demonstrated technical competency in ${result.exam_title}. Your official verified certificate has been issued and is ready for preview and PDF download.`
              : `You scored ${result.percentage}% on the ${result.exam_title}. A minimum passing score of ${result.passing_percentage}% is required to earn the verified credential.`}
          </p>

          {/* Score & Certificate Action */}
          <div className="mt-8 pt-6 border-t border-white/15 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
            <div className="flex items-center gap-6">
              <div>
                <span className="text-3xl sm:text-4xl font-black text-white">{result.score_obtained}</span>
                <span className="text-sm font-semibold text-slate-300"> / {result.total_marks} Marks</span>
                <div className="text-xs text-slate-300 font-medium">Final Score</div>
              </div>

              <div className="border-l border-white/20 pl-6">
                <span className={`text-3xl sm:text-4xl font-black ${isPassed ? 'text-emerald-300' : 'text-amber-300'}`}>
                  {result.percentage}%
                </span>
                <div className="text-xs text-slate-300 font-medium">
                  {isPassed ? 'Exceeds' : 'Below'} {result.passing_percentage}% Pass
                </div>
              </div>
            </div>

            {isPassed && result.certificate_id && (
              <Link
                to={`/certificates/${result.certificate_id}`}
                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-white text-emerald-900 hover:bg-emerald-50 font-black text-sm shadow-lg transition"
              >
                <Award className="w-4 h-4 text-emerald-700" />
                <span>View & Download Certificate</span>
                <ArrowRight className="w-4 h-4 text-emerald-700" />
              </Link>
            )}

            {!isPassed && (
              <Link
                to={`/exams/${result.exam_slug}`}
                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-lg transition"
              >
                <RotateCcw className="w-4 h-4" />
                <span>Retake Examination</span>
              </Link>
            )}
          </div>
        </div>
      </div>

      {/* Quick Summary Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm text-center">
          <Clock className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
          <div className="text-lg font-black text-slate-900">{formatSeconds(result.time_spent_seconds || 0)}</div>
          <div className="text-xs text-slate-500 font-medium">Time Taken</div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm text-center">
          <ShieldCheck className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
          <div className="text-lg font-black text-slate-900">{result.passing_percentage}%</div>
          <div className="text-xs text-slate-500 font-medium">Pass Criteria</div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm text-center">
          <CheckCircle2 className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
          <div className="text-lg font-black text-slate-900">
            {result.answers?.filter((a) => a.is_correct).length} / {result.answers?.length}
          </div>
          <div className="text-xs text-slate-500 font-medium">Correct Answers</div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm text-center">
          <Award className="w-5 h-5 text-emerald-600 mx-auto mb-1.5" />
          <div className="text-lg font-black text-emerald-700 font-mono">
            {result.certificate_id ? 'ISSUED' : 'NOT ELIGIBLE'}
          </div>
          <div className="text-xs text-slate-500 font-medium">Credential Status</div>
        </div>
      </div>

      {/* Question Review Breakdown */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h3 className="text-lg font-bold text-slate-900">Comprehensive Performance Breakdown</h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Review your answers, correct solutions, and official conceptual explanations.
            </p>
          </div>
        </div>

        <div className="space-y-4">
          {result.answers?.map((ans, idx) => {
            const q = ans.question;
            const isExpanded = expandedQuestion === q.id;
            const isCorrect = ans.is_correct;
            const pointsAwarded = ans.marks_awarded || 0;

            return (
              <div
                key={ans.id}
                className={`rounded-2xl border transition overflow-hidden ${
                  isCorrect
                    ? 'border-emerald-200 bg-emerald-50/20'
                    : 'border-slate-200 bg-white hover:border-slate-300'
                }`}
              >
                {/* Accordion Header */}
                <button
                  onClick={() => setExpandedQuestion(isExpanded ? null : q.id)}
                  className="w-full p-4 sm:p-5 flex items-center justify-between gap-4 text-left"
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <div
                      className={`w-7 h-7 rounded-xl flex items-center justify-center font-bold text-xs flex-shrink-0 ${
                        isCorrect
                          ? 'bg-emerald-600 text-white'
                          : 'bg-rose-100 text-rose-700'
                      }`}
                    >
                      {idx + 1}
                    </div>

                    <div className="min-w-0">
                      <h4 className="text-sm font-bold text-slate-900 truncate">{q.title}</h4>
                      <div className="flex items-center gap-2 mt-0.5 text-xs text-slate-500">
                        <span className="capitalize">{q.question_type.replace('_', ' ')}</span>
                        <span>•</span>
                        <span className="font-semibold text-slate-700">
                          {pointsAwarded} / {q.points} Points
                        </span>
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-3 flex-shrink-0">
                    <span
                      className={`px-2.5 py-1 rounded-full text-xs font-bold ${
                        isCorrect
                          ? 'bg-emerald-100 text-emerald-800'
                          : pointsAwarded > 0
                          ? 'bg-amber-100 text-amber-800'
                          : 'bg-rose-100 text-rose-800'
                      }`}
                    >
                      {isCorrect ? 'Correct' : pointsAwarded > 0 ? 'Partial' : 'Incorrect'}
                    </span>
                    {isExpanded ? (
                      <ChevronUp className="w-4 h-4 text-slate-400" />
                    ) : (
                      <ChevronDown className="w-4 h-4 text-slate-400" />
                    )}
                  </div>
                </button>

                {/* Expanded Accordion Body */}
                {isExpanded && (
                  <div className="p-5 border-t border-slate-100 bg-white space-y-4 text-xs">
                    <div>
                      <span className="font-bold text-slate-900 block mb-1">Problem Statement:</span>
                      <p className="text-slate-700 whitespace-pre-line">{q.problem_statement}</p>
                    </div>

                    {/* Coding question review */}
                    {q.question_type === 'coding' ? (
                      <div className="space-y-3">
                        <div>
                          <span className="font-bold text-slate-900 block mb-1">Your Submitted Code ({ans.language}):</span>
                          <pre className="p-3 rounded-xl bg-slate-900 text-emerald-400 font-mono text-[11px] overflow-x-auto max-h-56">
                            {ans.code || '// No code submitted'}
                          </pre>
                        </div>

                        {ans.evaluation_details?.sample_results && (
                          <div>
                            <span className="font-bold text-slate-900 block mb-1">Test Cases Evaluation:</span>
                            <div className="space-y-1.5">
                              {ans.evaluation_details.sample_results.map((tc, tci) => (
                                <div
                                  key={tci}
                                  className={`p-2 rounded-lg border flex items-center justify-between ${
                                    tc.passed
                                      ? 'bg-emerald-50 border-emerald-200 text-emerald-800'
                                      : 'bg-rose-50 border-rose-200 text-rose-800'
                                  }`}
                                >
                                  <span>Test Case {tc.case}</span>
                                  <span className="font-bold">{tc.passed ? 'PASSED' : 'FAILED'}</span>
                                </div>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    ) : (
                      /* Conceptual question review */
                      <div className="space-y-3">
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                          <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                            <span className="text-slate-400 font-semibold block mb-0.5">Your Response:</span>
                            <span className="font-bold text-slate-900">
                              {Array.isArray(ans.selected_option)
                                ? ans.selected_option.join(', ')
                                : ans.selected_option || 'None'}
                            </span>
                          </div>

                          <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200">
                            <span className="text-emerald-700 font-semibold block mb-0.5">Correct Answer:</span>
                            <span className="font-bold text-emerald-950">
                              {Array.isArray(q.correct_answer)
                                ? q.correct_answer.join(', ')
                                : q.correct_answer}
                            </span>
                          </div>
                        </div>

                        {q.explanation && (
                          <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-100">
                            <span className="font-bold text-slate-900 block mb-1">Explanation:</span>
                            <p className="text-slate-600 leading-relaxed">{q.explanation}</p>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Footer Navigation */}
      <div className="mt-8 flex items-center justify-between">
        <Link
          to="/exams"
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition"
        >
          <BookOpen className="w-4 h-4" />
          <span>Browse All Certifications</span>
        </Link>

        {isPassed && result.certificate_id && (
          <Link
            to={`/certificates/${result.certificate_id}`}
            className="inline-flex items-center gap-2 px-6 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-600/20 transition"
          >
            <Award className="w-4 h-4" />
            <span>Open Certificate</span>
          </Link>
        )}
      </div>
    </div>
  );
};

export default ExamResultPage;
