import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import api from '../services/api';
import {
  Clock,
  CheckCircle2,
  AlertCircle,
  HelpCircle,
  Play,
  Send,
  ChevronLeft,
  ChevronRight,
  Terminal,
  Code2,
  Check,
  AlertTriangle,
  RotateCcw,
  Sparkles,
  FileCode,
  CheckSquare,
  Square
} from 'lucide-react';

const SUPPORTED_LANGUAGES = [
  { id: 'python', label: 'Python 3', monacoLang: 'python' },
  { id: 'javascript', label: 'JavaScript (Node)', monacoLang: 'javascript' },
  { id: 'cpp', label: 'C++', monacoLang: 'cpp' },
  { id: 'c', label: 'C', monacoLang: 'c' },
  { id: 'java', label: 'Java', monacoLang: 'java' },
];

const DEFAULT_STARTERS = {
  python: `import sys\n\ndef main():\n    line = sys.stdin.read().strip()\n    # Write your solution here\n    \nif __name__ == '__main__':\n    main()\n`,
  javascript: `const fs = require('fs');\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf-8').trim();\n    // Write your solution here\n}\n\nmain();\n`,
  cpp: `#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // Write your C++ solution here\n    return 0;\n}\n`,
  c: `#include <stdio.h>\n#include <string.h>\n\nint main() {\n    // Write your C solution here\n    return 0;\n}\n`,
  java: `import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Write your Java solution here\n    }\n}\n`,
};

const ExamSessionPage = () => {
  const { slug, attemptId } = useParams();
  const navigate = useNavigate();

  const [session, setSession] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({}); // questionId -> { selected_option, code, language }
  const [timeRemaining, setTimeRemaining] = useState(0);
  const [isLoading, setIsLoading] = useState(true);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showSubmitModal, setShowSubmitModal] = useState(false);
  const [autoSubmitTriggered, setAutoSubmitTriggered] = useState(false);

  // Coding workspace states
  const [selectedLanguage, setSelectedLanguage] = useState('python');
  const [isRunningCode, setIsRunningCode] = useState(false);
  const [executionOutput, setExecutionOutput] = useState(null);
  const [useCustomInput, setUseCustomInput] = useState(false);
  const [customInput, setCustomInput] = useState('');

  const saveTimeoutRef = useRef(null);

  // Load session
  useEffect(() => {
    fetchSession();
  }, [attemptId]);

  const fetchSession = async () => {
    setIsLoading(true);
    try {
      const res = await api.get(`/exams/attempts/${attemptId}/`);
      const data = res.data;

      if (data.status === 'submitted' || data.status === 'timed_out') {
        navigate(`/exams/attempts/${attemptId}/result`, { replace: true });
        return;
      }

      setSession(data);
      setQuestions(data.questions || []);
      setTimeRemaining(data.time_remaining_seconds || 0);

      // Preload saved answers
      const preloaded = {};
      (data.questions || []).forEach((q) => {
        const saved = data.saved_answers?.[q.id];
        if (saved) {
          preloaded[q.id] = saved;
        } else if (q.question_type === 'coding') {
          const starter = q.starter_code?.python || q.starter_code?.javascript || DEFAULT_STARTERS.python;
          preloaded[q.id] = { code: starter, language: 'python', selected_option: null };
        } else {
          preloaded[q.id] = { code: '', language: '', selected_option: null };
        }
      });
      setAnswers(preloaded);
    } catch (err) {
      console.error('Failed to load exam session:', err);
      alert('Failed to load examination session. Redirecting...');
      navigate('/exams');
    } finally {
      setIsLoading(false);
    }
  };

  // Sync editor language when navigating between questions
  useEffect(() => {
    if (questions[currentIndex]?.question_type === 'coding') {
      const qId = questions[currentIndex].id;
      const savedLang = answers[qId]?.language || 'python';
      setSelectedLanguage(savedLang);
    }
    setExecutionOutput(null);
  }, [currentIndex, questions]);

  // Timer countdown
  useEffect(() => {
    if (isLoading || timeRemaining <= 0) return;

    const interval = setInterval(() => {
      setTimeRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          if (!autoSubmitTriggered) {
            setAutoSubmitTriggered(true);
            handleAutoSubmitOnTimeout();
          }
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [timeRemaining, isLoading, autoSubmitTriggered]);

  const handleAutoSubmitOnTimeout = async () => {
    alert('Time has expired! Submitting your examination now...');
    await performSubmit();
  };

  const formatTimer = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const currentQuestion = questions[currentIndex] || null;
  const currentAnswer = currentQuestion ? answers[currentQuestion.id] || {} : {};

  // Debounced auto-save to server
  const saveAnswerToServer = (qId, answerData) => {
    if (saveTimeoutRef.current) clearTimeout(saveTimeoutRef.current);

    saveTimeoutRef.current = setTimeout(async () => {
      try {
        await api.post(`/exams/attempts/${attemptId}/save-answer/`, {
          question_id: qId,
          ...answerData,
        });
      } catch (err) {
        console.warn('Silent save failed:', err);
      }
    }, 600);
  };

  // Option select handler for MCQs
  const handleOptionSelect = (optionId) => {
    if (!currentQuestion) return;
    const qId = currentQuestion.id;

    if (currentQuestion.question_type === 'multiple_choice') {
      const currentList = Array.isArray(currentAnswer.selected_option) ? currentAnswer.selected_option : [];
      let nextList;
      if (currentList.includes(optionId)) {
        nextList = currentList.filter((id) => id !== optionId);
      } else {
        nextList = [...currentList, optionId];
      }

      const updated = { ...currentAnswer, selected_option: nextList };
      setAnswers((prev) => ({ ...prev, [qId]: updated }));
      saveAnswerToServer(qId, updated);
    } else {
      const updated = { ...currentAnswer, selected_option: optionId };
      setAnswers((prev) => ({ ...prev, [qId]: updated }));
      saveAnswerToServer(qId, updated);
    }
  };

  // Code editor change handler
  const handleCodeChange = (newCode) => {
    if (!currentQuestion) return;
    const qId = currentQuestion.id;
    const updated = {
      ...currentAnswer,
      code: newCode,
      language: selectedLanguage,
    };
    setAnswers((prev) => ({ ...prev, [qId]: updated }));
    saveAnswerToServer(qId, updated);
  };

  // Language switch handler
  const handleLanguageChange = (newLang) => {
    setSelectedLanguage(newLang);
    if (!currentQuestion) return;
    const qId = currentQuestion.id;

    let nextCode = currentAnswer.code;
    const isStarterOrEmpty =
      !nextCode ||
      Object.values(DEFAULT_STARTERS).includes(nextCode) ||
      Object.values(currentQuestion.starter_code || {}).includes(nextCode);

    if (isStarterOrEmpty) {
      nextCode = currentQuestion.starter_code?.[newLang] || DEFAULT_STARTERS[newLang] || '';
    }

    const updated = {
      ...currentAnswer,
      code: nextCode,
      language: newLang,
    };
    setAnswers((prev) => ({ ...prev, [qId]: updated }));
    saveAnswerToServer(qId, updated);
  };

  // Run code against sample cases or custom input
  const handleRunCode = async () => {
    if (!currentQuestion || currentQuestion.question_type !== 'coding') return;
    setIsRunningCode(true);
    setExecutionOutput(null);

    try {
      const payload = {
        question_id: currentQuestion.id,
        code: currentAnswer.code || '',
        language: selectedLanguage,
      };
      if (useCustomInput && customInput.trim()) {
        payload.custom_input = customInput;
      }

      const res = await api.post(`/exams/attempts/${attemptId}/run-code/`, payload);
      setExecutionOutput(res.data);
    } catch (err) {
      console.error('Run code failed:', err);
      setExecutionOutput({
        status: 'Error',
        output: err.response?.data?.detail || 'Execution request failed.',
      });
    } finally {
      setIsRunningCode(false);
    }
  };

  // Submit whole exam
  const performSubmit = async () => {
    setIsSubmitting(true);
    try {
      const res = await api.post(`/exams/attempts/${attemptId}/submit/`);
      navigate(`/exams/attempts/${attemptId}/result`, { replace: true });
    } catch (err) {
      console.error('Failed to submit exam:', err);
      alert(err.response?.data?.detail || 'Failed to submit examination.');
      setIsSubmitting(false);
    }
  };

  // Calculate answered count
  const answeredCount = questions.filter((q) => {
    const ans = answers[q.id];
    if (!ans) return false;
    if (q.question_type === 'coding') {
      return (ans.code || '').trim().length > 0;
    }
    if (q.question_type === 'multiple_choice') {
      return Array.isArray(ans.selected_option) && ans.selected_option.length > 0;
    }
    return Boolean(ans.selected_option);
  }).length;

  if (isLoading) {
    return (
      <div className="min-h-screen bg-slate-900 text-white flex items-center justify-center p-4">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-emerald-400 font-semibold tracking-wide">Initializing secure assessment environment...</p>
        </div>
      </div>
    );
  }

  const isTimerLow = timeRemaining < 300; // < 5 mins

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      {/* Top Session Bar */}
      <header className="sticky top-0 z-30 bg-white border-b border-slate-200 px-4 sm:px-6 py-3 shadow-sm">
        <div className="max-w-7xl mx-auto flex items-center justify-between gap-4">
          {/* Exam Title & Progress */}
          <div>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
              <h2 className="text-sm font-bold text-slate-900 tracking-tight line-clamp-1">
                {session?.exam_title}
              </h2>
            </div>
            <div className="text-[11px] font-semibold text-slate-500">
              Answered <span className="text-emerald-600 font-bold">{answeredCount}</span> of {questions.length} questions
            </div>
          </div>

          {/* Center Timer */}
          <div
            className={`flex items-center gap-2 px-4 py-1.5 rounded-full font-mono text-sm font-black border transition ${
              isTimerLow
                ? 'bg-rose-50 text-rose-700 border-rose-300 animate-pulse'
                : 'bg-emerald-50 text-emerald-800 border-emerald-200'
            }`}
          >
            <Clock className={`w-4 h-4 ${isTimerLow ? 'text-rose-600' : 'text-emerald-600'}`} />
            <span>{formatTimer(timeRemaining)}</span>
          </div>

          {/* Submit Button */}
          <button
            onClick={() => setShowSubmitModal(true)}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-md shadow-emerald-600/20 transition"
          >
            <Send className="w-3.5 h-3.5" />
            <span>Submit Exam</span>
          </button>
        </div>
      </header>

      {/* Main Workspace Area */}
      <div className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Question Navigator & Content */}
        <div className="lg:col-span-6 flex flex-col space-y-4">
          {/* Question Navigator Pills */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="text-xs font-bold text-slate-700 mb-2.5 flex items-center justify-between">
              <span>Question Navigator</span>
              <span className="text-[11px] text-slate-400 font-medium">Click to jump</span>
            </div>
            <div className="flex flex-wrap gap-2">
              {questions.map((q, idx) => {
                const ans = answers[q.id];
                const isAnswered =
                  q.question_type === 'coding'
                    ? Boolean(ans?.code?.trim())
                    : Boolean(ans?.selected_option);
                const isActive = idx === currentIndex;

                return (
                  <button
                    key={q.id}
                    onClick={() => setCurrentIndex(idx)}
                    className={`w-9 h-9 rounded-xl text-xs font-bold transition flex items-center justify-center relative ${
                      isActive
                        ? 'bg-emerald-600 text-white shadow-md shadow-emerald-600/30 ring-2 ring-emerald-600 ring-offset-2'
                        : isAnswered
                        ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                        : 'bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200'
                    }`}
                  >
                    {idx + 1}
                    {isAnswered && !isActive && (
                      <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-600 rounded-full border-2 border-white" />
                    )}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Question Details Card */}
          {currentQuestion && (
            <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex-1 flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="px-2.5 py-1 rounded-md text-[11px] font-bold uppercase tracking-wider bg-slate-100 text-slate-700">
                    Question {currentIndex + 1} of {questions.length}
                  </span>
                  <span className="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-800 border border-emerald-200">
                    {currentQuestion.points} Points
                  </span>
                </div>

                <h3 className="text-lg font-bold text-slate-900 mb-4 leading-snug">
                  {currentQuestion.title}
                </h3>

                <div className="prose prose-sm text-slate-700 leading-relaxed whitespace-pre-line mb-6">
                  {currentQuestion.problem_statement}
                </div>

                {/* Additional coding specifications */}
                {currentQuestion.question_type === 'coding' && (
                  <div className="space-y-3 mb-6 text-xs">
                    {currentQuestion.input_format && (
                      <div className="p-3 rounded-xl bg-slate-50 border border-slate-100">
                        <span className="font-bold text-slate-900 block mb-1">Input Format:</span>
                        <span className="text-slate-600">{currentQuestion.input_format}</span>
                      </div>
                    )}
                    {currentQuestion.output_format && (
                      <div className="p-3 rounded-xl bg-slate-50 border border-slate-100">
                        <span className="font-bold text-slate-900 block mb-1">Output Format:</span>
                        <span className="text-slate-600">{currentQuestion.output_format}</span>
                      </div>
                    )}
                    {currentQuestion.constraints && (
                      <div className="p-3 rounded-xl bg-slate-50 border border-slate-100">
                        <span className="font-bold text-slate-900 block mb-1">Constraints:</span>
                        <span className="text-slate-600 font-mono">{currentQuestion.constraints}</span>
                      </div>
                    )}
                  </div>
                )}
              </div>

              {/* Prev / Next Controls */}
              <div className="flex items-center justify-between pt-4 border-t border-slate-100 mt-6">
                <button
                  onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
                  disabled={currentIndex === 0}
                  className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-600 hover:bg-slate-100 disabled:opacity-40 transition"
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>Previous</span>
                </button>

                <button
                  onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
                  disabled={currentIndex === questions.length - 1}
                  className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-slate-100 hover:bg-slate-200 text-slate-800 disabled:opacity-40 transition"
                >
                  <span>Next</span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Right Column: Interactive Response Area */}
        <div className="lg:col-span-6 flex flex-col space-y-4">
          {currentQuestion?.question_type === 'coding' ? (
            /* CODING CHALLENGE WORKSPACE */
            <div className="bg-white rounded-2xl border border-slate-200 shadow-sm flex flex-col flex-1 overflow-hidden">
              {/* Toolbar */}
              <div className="flex items-center justify-between px-4 py-3 bg-slate-50 border-b border-slate-200">
                <div className="flex items-center gap-2">
                  <Code2 className="w-4 h-4 text-emerald-600" />
                  <select
                    value={selectedLanguage}
                    onChange={(e) => handleLanguageChange(e.target.value)}
                    className="px-2.5 py-1.5 rounded-lg bg-white border border-slate-200 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  >
                    {SUPPORTED_LANGUAGES.map((l) => (
                      <option key={l.id} value={l.id}>
                        {l.label}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={handleRunCode}
                    disabled={isRunningCode}
                    className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-sm transition disabled:opacity-50"
                  >
                    {isRunningCode ? (
                      <>
                        <div className="w-3 h-3 border-2 border-white border-t-transparent rounded-full animate-spin" />
                        <span>Running...</span>
                      </>
                    ) : (
                      <>
                        <Play className="w-3.5 h-3.5 fill-current" />
                        <span>Run Code</span>
                      </>
                    )}
                  </button>
                </div>
              </div>

              {/* Monaco Editor */}
              <div className="flex-1 min-h-[320px]">
                <Editor
                  height="340px"
                  language={
                    SUPPORTED_LANGUAGES.find((l) => l.id === selectedLanguage)?.monacoLang || 'python'
                  }
                  theme="light"
                  value={currentAnswer.code || ''}
                  onChange={(val) => handleCodeChange(val || '')}
                  options={{
                    minimap: { enabled: false },
                    fontSize: 13,
                    lineNumbers: 'on',
                    scrollBeyondLastLine: false,
                    automaticLayout: true,
                    tabSize: 4,
                  }}
                />
              </div>

              {/* Test Output / Console Drawer */}
              <div className="border-t border-slate-200 bg-slate-900 text-slate-100 p-4 font-mono text-xs">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2 text-slate-400 font-bold">
                    <Terminal className="w-3.5 h-3.5" />
                    <span>Execution Output</span>
                  </div>
                  {executionOutput?.status && (
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${
                        executionOutput.status === 'Accepted'
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                          : 'bg-rose-950 text-rose-400 border border-rose-800'
                      }`}
                    >
                      {executionOutput.status}
                    </span>
                  )}
                </div>

                {executionOutput ? (
                  <div className="space-y-2 max-h-40 overflow-y-auto">
                    {executionOutput.error_output && (
                      <pre className="text-rose-400 whitespace-pre-wrap">
                        {executionOutput.error_output}
                      </pre>
                    )}
                    {executionOutput.compiler_output && (
                      <pre className="text-amber-400 whitespace-pre-wrap">
                        {executionOutput.compiler_output}
                      </pre>
                    )}
                    {executionOutput.sample_results?.map((res, i) => (
                      <div
                        key={i}
                        className={`p-2 rounded border text-[11px] ${
                          res.passed
                            ? 'bg-emerald-900/30 border-emerald-800 text-emerald-300'
                            : 'bg-rose-900/30 border-rose-800 text-rose-300'
                        }`}
                      >
                        <div className="font-bold mb-1">
                          Sample Test Case {res.case}: {res.passed ? 'PASSED' : 'FAILED'}
                        </div>
                        <div>Input: <span className="text-white">{res.input}</span></div>
                        <div>Expected: <span className="text-white">{res.expected}</span></div>
                        <div>Actual: <span className="text-white">{res.actual}</span></div>
                      </div>
                    ))}
                    {executionOutput.output && !executionOutput.sample_results && (
                      <pre className="whitespace-pre-wrap text-emerald-300">
                        {executionOutput.output}
                      </pre>
                    )}
                  </div>
                ) : (
                  <p className="text-slate-500 italic">
                    Click 'Run Code' to execute against sample cases.
                  </p>
                )}
              </div>
            </div>
          ) : (
            /* CONCEPTUAL / MULTIPLE CHOICE OPTIONS */
            <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex-1 flex flex-col justify-between">
              <div>
                <h4 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                  <span>
                    {currentQuestion?.question_type === 'multiple_choice'
                      ? 'Select all applicable options:'
                      : 'Select the correct option:'}
                  </span>
                </h4>

                <div className="space-y-3">
                  {currentQuestion?.options?.map((opt) => {
                    const isSelected =
                      currentQuestion.question_type === 'multiple_choice'
                        ? Array.isArray(currentAnswer.selected_option) &&
                          currentAnswer.selected_option.includes(opt.id)
                        : currentAnswer.selected_option === opt.id;

                    return (
                      <button
                        key={opt.id}
                        onClick={() => handleOptionSelect(opt.id)}
                        className={`w-full text-left p-4 rounded-xl border text-sm transition flex items-start gap-3 ${
                          isSelected
                            ? 'bg-emerald-50 border-emerald-500 text-emerald-950 font-medium ring-1 ring-emerald-500 shadow-sm'
                            : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300'
                        }`}
                      >
                        <div
                          className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5 ${
                            isSelected
                              ? 'bg-emerald-600 text-white'
                              : 'bg-slate-100 text-slate-600 border border-slate-300'
                          }`}
                        >
                          {opt.id}
                        </div>
                        <span className="leading-relaxed">{opt.text}</span>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Status info */}
              <div className="pt-6 border-t border-slate-100 mt-6 flex items-center justify-between text-xs text-slate-500">
                <span>Responses are automatically saved in real-time.</span>
                <span className="text-emerald-600 font-semibold flex items-center gap-1">
                  <Check className="w-3.5 h-3.5" />
                  Saved
                </span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Submit Confirmation Modal */}
      {showSubmitModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 animate-in fade-in zoom-in-95">
            <div className="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center mx-auto mb-4">
              <Send className="w-6 h-6" />
            </div>

            <h3 className="text-lg font-bold text-slate-900 text-center">
              Submit Certification Exam?
            </h3>

            <p className="text-xs text-slate-600 text-center mt-2 leading-relaxed">
              You have answered <span className="font-bold text-emerald-600">{answeredCount}</span> of {questions.length} questions.
              {answeredCount < questions.length && (
                <span className="block mt-1 text-amber-600 font-semibold">
                  Warning: You have {questions.length - answeredCount} unanswered questions!
                </span>
              )}
            </p>

            <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 my-4 text-xs text-slate-600 space-y-1">
              <div className="flex justify-between">
                <span>Time Remaining:</span>
                <span className="font-bold">{formatTimer(timeRemaining)}</span>
              </div>
              <div className="flex justify-between">
                <span>Pass Threshold:</span>
                <span className="font-bold">70% Required</span>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-3 mt-6">
              <button
                onClick={() => setShowSubmitModal(false)}
                className="px-4 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition"
              >
                Keep Reviewing
              </button>

              <button
                onClick={performSubmit}
                disabled={isSubmitting}
                className="inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-600/20 transition disabled:opacity-50"
              >
                {isSubmitting ? (
                  <>
                    <div className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                    <span>Evaluating...</span>
                  </>
                ) : (
                  <span>Confirm & Submit</span>
                )}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExamSessionPage;
