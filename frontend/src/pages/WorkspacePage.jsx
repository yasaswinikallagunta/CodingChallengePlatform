import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import confetti from 'canvas-confetti';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { 
  Play, 
  Send, 
  RotateCcw, 
  CheckCircle2, 
  XCircle, 
  AlertTriangle, 
  Clock, 
  Award, 
  Terminal, 
  Code2, 
  Layers, 
  ChevronLeft,
  FileCode,
  History,
  Sparkles,
  Info,
  X,
  Bug,
  HelpCircle
} from 'lucide-react';

const SUPPORTED_LANGUAGES = [
  { id: 'python', label: 'Python 3', monacoLang: 'python' },
  { id: 'javascript', label: 'JavaScript (Node)', monacoLang: 'javascript' },
  { id: 'cpp', label: 'C++', monacoLang: 'cpp' },
  { id: 'c', label: 'C', monacoLang: 'c' },
  { id: 'java', label: 'Java', monacoLang: 'java' },
  { id: 'sql', label: 'SQL (SQLite)', monacoLang: 'sql' },
];

const WorkspacePage = () => {
  const { slug } = useParams();
  const { refreshProfile } = useAuth();

  const [problem, setProblem] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeLeftTab, setActiveLeftTab] = useState('description'); // 'description' | 'submissions'
  const [problemSubmissions, setProblemSubmissions] = useState([]);

  // Language & Code states
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('');
  // Map of language_id -> user code, preventing silent overwrites when switching languages
  const [codePerLanguage, setCodePerLanguage] = useState({});

  // Custom Input
  const [useCustomInput, setUseCustomInput] = useState(false);
  const [customInput, setCustomInput] = useState('');

  // Execution states
  const [isRunning, setIsRunning] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [executionMode, setExecutionMode] = useState(null); // 'custom_input' | 'sample_test_cases' | 'submit'
  const [runResult, setRunResult] = useState(null);
  const [submissionResult, setSubmissionResult] = useState(null);
  const [activeCaseTab, setActiveCaseTab] = useState(0);

  // Clickable Error Details Modal/Drawer
  const [showErrorModal, setShowErrorModal] = useState(false);
  const [activeErrorData, setActiveErrorData] = useState(null);

  // Fetch problem details
  const fetchProblem = async () => {
    setLoading(true);
    try {
      const res = await api.get(`/problems/${slug}/`);
      setProblem(res.data);

      const starters = res.data.starter_code || {};
      const initialLang = starters.python ? 'python' : Object.keys(starters)[0] || 'python';
      
      // Initialize codePerLanguage with problem starters
      const initialCodeMap = {};
      SUPPORTED_LANGUAGES.forEach(l => {
        initialCodeMap[l.id] = starters[l.id] || `// Write your ${l.label} solution here\n`;
      });

      setCodePerLanguage(initialCodeMap);
      setLanguage(initialLang);
      setCode(initialCodeMap[initialLang]);

      if (res.data.sample_test_cases && res.data.sample_test_cases.length > 0) {
        setCustomInput(res.data.sample_test_cases[0].input || '');
      }
    } catch (err) {
      console.error("Failed to load problem:", err);
    } finally {
      setLoading(false);
    }
  };

  // Fetch submissions for this problem
  const fetchSubmissions = async () => {
    if (!problem?.id) return;
    try {
      const res = await api.get('/submissions/', { params: { problem_id: problem.id } });
      setProblemSubmissions(res.data.results || []);
    } catch (err) {
      console.error("Failed to fetch submissions:", err);
    }
  };

  useEffect(() => {
    fetchProblem();
  }, [slug]);

  useEffect(() => {
    if (activeLeftTab === 'submissions') {
      fetchSubmissions();
    }
  }, [activeLeftTab, problem?.id]);

  // Handle language switch without overwriting code written by user
  const handleLanguageChange = (newLang) => {
    // 1. Save current code for current language
    setCodePerLanguage(prev => ({
      ...prev,
      [language]: code,
    }));

    // 2. Switch language
    setLanguage(newLang);

    // 3. Load user's previously edited code or fallback to starter code
    const existingCode = codePerLanguage[newLang];
    if (existingCode !== undefined) {
      setCode(existingCode);
    } else {
      const starters = problem?.starter_code || {};
      const starter = starters[newLang] || `// Write your ${newLang} solution here\n`;
      setCode(starter);
      setCodePerLanguage(prev => ({ ...prev, [newLang]: starter }));
    }
  };

  const handleEditorChange = (value) => {
    const val = value || '';
    setCode(val);
    setCodePerLanguage(prev => ({
      ...prev,
      [language]: val,
    }));
  };

  const handleResetCode = () => {
    if (confirm(`Reset editor to default starter template for ${language.toUpperCase()}? Your unsaved edits for this language will be reverted.`)) {
      const starters = problem?.starter_code || {};
      const defaultCode = starters[language] || `// Write your ${language} solution here\n`;
      setCode(defaultCode);
      setCodePerLanguage(prev => ({
        ...prev,
        [language]: defaultCode,
      }));
    }
  };

  // Run Code (runs against custom input or sample test cases)
  const handleRunCode = async () => {
    setIsRunning(true);
    setSubmissionResult(null);
    setRunResult(null);
    setShowErrorModal(false);

    const mode = useCustomInput ? 'custom_input' : 'sample_test_cases';
    setExecutionMode(mode);

    try {
      const payload = {
        code,
        language,
        custom_input: useCustomInput ? customInput : null,
      };
      const res = await api.post(`/problems/${slug}/run/`, payload);
      setRunResult(res.data);
      setActiveCaseTab(0);
      if (res.data.error_details) {
        setActiveErrorData(res.data.error_details);
      }
    } catch (err) {
      console.error("Run error:", err);
      const fallbackError = {
        error_type: 'Execution Failed',
        error_output: err.response?.data?.detail || err.message || 'Execution failed.',
        explanation: 'The execution service encountered a communication failure.',
      };
      setRunResult({
        status: 'Runtime Error',
        output: fallbackError.error_output,
        error_details: fallbackError,
      });
      setActiveErrorData(fallbackError);
    } finally {
      setIsRunning(false);
    }
  };

  // Submit Code (evaluates against full test suite, persists to DB, triggers points & achievements)
  const handleSubmitCode = async () => {
    setIsSubmitting(true);
    setRunResult(null);
    setSubmissionResult(null);
    setShowErrorModal(false);
    setExecutionMode('submit');

    try {
      const payload = { code, language };
      const res = await api.post(`/problems/${slug}/submit/`, payload);
      setSubmissionResult(res.data);
      setActiveCaseTab(0);

      if (res.data.error_details) {
        setActiveErrorData(res.data.error_details);
      } else if (res.data.status === 'Wrong Answer' && res.data.first_failed_info) {
        setActiveErrorData({
          error_type: 'Wrong Answer',
          error_output: res.data.first_failed_info.reason,
          explanation: `Test case ${res.data.first_failed_info.case_number} produced an incorrect result. Review your boundary conditions and edge cases.`,
        });
      }

      if (res.data.status === 'Accepted') {
        confetti({
          particleCount: 110,
          spread: 75,
          origin: { y: 0.6 },
          colors: ['#16A34A', '#22C55E', '#86EFAC', '#FACC15'],
        });
        refreshProfile();
      }

      fetchSubmissions();
    } catch (err) {
      console.error("Submit error:", err);
      const fallbackError = {
        error_type: 'Submission Failed',
        error_output: err.response?.data?.detail || err.message || 'Submission failed.',
        explanation: 'Unable to communicate with the submission evaluation service.',
      };
      setSubmissionResult({
        status: 'Runtime Error',
        output: fallbackError.error_output,
        error_details: fallbackError,
      });
      setActiveErrorData(fallbackError);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center bg-slate-50">
        <div className="flex flex-col items-center gap-3">
          <div className="w-8 h-8 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin" />
          <p className="text-sm font-semibold text-slate-500">Loading coding workspace...</p>
        </div>
      </div>
    );
  }

  if (!problem) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-16 text-center">
        <h2 className="text-xl font-bold text-slate-800">Challenge Not Found</h2>
        <p className="text-sm text-slate-500 mt-2 mb-6">The requested coding challenge does not exist or was moved.</p>
        <Link to="/problems" className="px-4 py-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">
          Return to Challenges
        </Link>
      </div>
    );
  }

  const selectedLangObj = SUPPORTED_LANGUAGES.find((l) => l.id === language) || SUPPORTED_LANGUAGES[0];
  const activeResult = submissionResult || runResult;
  const isAccepted = activeResult?.status === 'Accepted';
  const isWrongAnswer = activeResult?.status === 'Wrong Answer';
  const isFailed = activeResult && !isAccepted && !isWrongAnswer;

  return (
    <div className="min-h-[calc(100vh-4rem)] flex flex-col bg-slate-50 relative">
      {/* Top Header Bar */}
      <div className="bg-white border-b border-slate-200 px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between gap-3 shrink-0">
        <div className="flex items-center gap-3">
          <Link
            to="/problems"
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition"
            title="Back to Challenges"
          >
            <ChevronLeft className="w-5 h-5" />
          </Link>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-base sm:text-lg font-black text-slate-900">{problem.title}</h1>
              {problem.is_solved && (
                <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-full">
                  <CheckCircle2 className="w-3 h-3 text-emerald-600" /> Solved
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Badges */}
        <div className="flex items-center gap-2 text-xs">
          <span className={`font-bold px-2.5 py-0.5 rounded-full ${
            problem.difficulty === 'Easy' ? 'bg-emerald-100 text-emerald-800' :
            problem.difficulty === 'Medium' ? 'bg-amber-100 text-amber-800' :
            'bg-rose-100 text-rose-800'
          }`}>
            {problem.difficulty}
          </span>
          <span className="font-semibold text-slate-600 px-2 py-0.5 rounded-md bg-slate-100">
            {problem.category}
          </span>
          <span className="font-bold text-emerald-700 px-2 py-0.5 rounded-md bg-emerald-50">
            +{problem.points} pts
          </span>
        </div>
      </div>

      {/* Main Workspace Split View */}
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 min-h-0 overflow-hidden">
        {/* Left Column: Problem Details / Submissions */}
        <div className="lg:col-span-5 bg-white border-r border-slate-200 flex flex-col h-[550px] lg:h-[calc(100vh-8.5rem)] overflow-hidden">
          {/* Tabs */}
          <div className="flex border-b border-slate-200 px-4 pt-2 bg-slate-50/50">
            <button
              onClick={() => setActiveLeftTab('description')}
              className={`flex items-center gap-2 px-4 py-2 text-xs font-bold border-b-2 transition ${
                activeLeftTab === 'description'
                  ? 'border-emerald-600 text-emerald-700'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <FileCode className="w-3.5 h-3.5" /> Description
            </button>
            <button
              onClick={() => setActiveLeftTab('submissions')}
              className={`flex items-center gap-2 px-4 py-2 text-xs font-bold border-b-2 transition ${
                activeLeftTab === 'submissions'
                  ? 'border-emerald-600 text-emerald-700'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <History className="w-3.5 h-3.5" /> Submissions ({problemSubmissions.length})
            </button>
          </div>

          {/* Tab Content */}
          <div className="flex-1 p-6 overflow-y-auto space-y-6 text-sm text-slate-700">
            {activeLeftTab === 'description' ? (
              <>
                {/* Problem Statement */}
                <div>
                  <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Problem Statement</h3>
                  <div className="whitespace-pre-line text-slate-800 leading-relaxed font-normal">
                    {problem.problem_statement}
                  </div>
                </div>

                {/* Input / Output Formats */}
                {problem.input_format && (
                  <div className="space-y-2 pt-2 border-t border-slate-100">
                    <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Input Format</h4>
                    <p className="text-xs text-slate-600 whitespace-pre-line bg-slate-50 p-3 rounded-xl border border-slate-200 font-mono">
                      {problem.input_format}
                    </p>
                  </div>
                )}

                {problem.output_format && (
                  <div className="space-y-2">
                    <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Output Format</h4>
                    <p className="text-xs text-slate-600 whitespace-pre-line bg-slate-50 p-3 rounded-xl border border-slate-200 font-mono">
                      {problem.output_format}
                    </p>
                  </div>
                )}

                {/* Constraints */}
                {problem.constraints && (
                  <div className="space-y-2 pt-2 border-t border-slate-100">
                    <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Constraints</h4>
                    <pre className="text-xs text-slate-600 whitespace-pre-line bg-slate-50 p-3 rounded-xl border border-slate-200 font-mono">
                      {problem.constraints}
                    </pre>
                  </div>
                )}

                {/* Sample Cases */}
                {problem.sample_input && (
                  <div className="space-y-3 pt-2 border-t border-slate-100">
                    <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Example</h4>
                    <div className="space-y-2">
                      <div>
                        <span className="text-[11px] font-semibold text-slate-500 block mb-1">Input:</span>
                        <pre className="bg-slate-100 p-2.5 rounded-lg text-xs font-mono text-slate-800 overflow-x-auto">
                          {problem.sample_input}
                        </pre>
                      </div>
                      <div>
                        <span className="text-[11px] font-semibold text-slate-500 block mb-1">Output:</span>
                        <pre className="bg-slate-100 p-2.5 rounded-lg text-xs font-mono text-slate-800 overflow-x-auto">
                          {problem.sample_output}
                        </pre>
                      </div>
                      {problem.explanation && (
                        <p className="text-xs text-slate-600 mt-2 bg-emerald-50/50 p-2.5 rounded-lg border border-emerald-100">
                          <span className="font-bold text-emerald-800">Explanation:</span> {problem.explanation}
                        </p>
                      )}
                    </div>
                  </div>
                )}
              </>
            ) : (
              /* Submissions History */
              <div className="space-y-3">
                <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Your Past Attempts</h3>
                {problemSubmissions.length === 0 ? (
                  <p className="text-xs text-slate-500 text-center py-8">
                    No submissions for this challenge yet. Click Submit Code when ready!
                  </p>
                ) : (
                  problemSubmissions.map((sub) => (
                    <div
                      key={sub.id}
                      className="p-3.5 rounded-xl border border-slate-200 bg-white hover:bg-slate-50 transition flex items-center justify-between text-xs"
                    >
                      <div>
                        <div className="flex items-center gap-2 mb-1">
                          <span className={`font-bold px-2 py-0.5 rounded-full text-[10px] ${
                            sub.status === 'Accepted'
                              ? 'bg-emerald-100 text-emerald-800'
                              : 'bg-red-100 text-red-700'
                          }`}>
                            {sub.status}
                          </span>
                          <span className="text-slate-500 font-semibold capitalize">{sub.language}</span>
                        </div>
                        <span className="text-[11px] text-slate-400">
                          {new Date(sub.submitted_at).toLocaleString()}
                        </span>
                      </div>
                      <div className="text-right">
                        <span className="text-slate-600 font-bold block">
                          {sub.passed_test_cases} / {sub.total_test_cases} passed
                        </span>
                        {sub.execution_time != null && (
                          <span className="text-[11px] text-slate-400">{sub.execution_time}s</span>
                        )}
                      </div>
                    </div>
                  ))
                )}
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Code Editor & Execution Results */}
        <div className="lg:col-span-7 flex flex-col h-[750px] lg:h-[calc(100vh-8.5rem)] overflow-hidden bg-white">
          {/* Editor Toolbar with Language Dropdown */}
          <div className="bg-slate-50 border-b border-slate-200 px-4 py-2.5 flex flex-wrap items-center justify-between gap-3 shrink-0">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-500">Language:</span>
              <select
                value={language}
                onChange={(e) => handleLanguageChange(e.target.value)}
                className="py-1 px-3 rounded-lg border border-slate-200 text-xs font-bold text-slate-800 bg-white focus:ring-2 focus:ring-emerald-500 shadow-sm"
              >
                {SUPPORTED_LANGUAGES.map((l) => (
                  <option key={l.id} value={l.id}>{l.label}</option>
                ))}
              </select>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={handleResetCode}
                className="px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-200/60 transition flex items-center gap-1"
                title="Reset code for current language"
              >
                <RotateCcw className="w-3.5 h-3.5" /> Reset Starter
              </button>
            </div>
          </div>

          {/* Monaco Editor Canvas */}
          <div className="flex-1 min-h-[300px] border-b border-slate-200 relative">
            <Editor
              height="100%"
              language={selectedLangObj.monacoLang}
              value={code}
              onChange={handleEditorChange}
              theme="vs"
              options={{
                fontSize: 13,
                minimap: { enabled: false },
                scrollBeyondLastLine: false,
                wordWrap: 'on',
                automaticLayout: true,
                tabSize: 4,
                fontFamily: "'Fira Code', monospace",
              }}
            />
          </div>

          {/* Custom Input Drawer Toggle & Action Buttons */}
          <div className="bg-slate-50 px-4 py-2.5 border-b border-slate-200 flex flex-wrap items-center justify-between gap-3">
            <label className="flex items-center gap-2 text-xs font-semibold text-slate-700 cursor-pointer select-none">
              <input
                type="checkbox"
                checked={useCustomInput}
                onChange={(e) => setUseCustomInput(e.target.checked)}
                className="rounded text-emerald-600 focus:ring-emerald-500 h-3.5 w-3.5"
              />
              <span>Test with Custom Input</span>
            </label>

            <div className="flex items-center gap-2">
              <button
                onClick={handleRunCode}
                disabled={isRunning || isSubmitting}
                className="px-3.5 py-1.5 rounded-lg bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold text-xs transition flex items-center gap-1.5 disabled:opacity-50"
              >
                <Play className="w-3.5 h-3.5 text-emerald-700" />
                <span>{isRunning ? 'Executing...' : 'Run Code'}</span>
              </button>

              <button
                onClick={handleSubmitCode}
                disabled={isRunning || isSubmitting}
                className="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-sm transition flex items-center gap-1.5 disabled:opacity-50"
              >
                <Send className="w-3.5 h-3.5" />
                <span>{isSubmitting ? 'Evaluating...' : 'Submit Code'}</span>
              </button>
            </div>
          </div>

          {useCustomInput && (
            <div className="p-3 bg-slate-100 border-b border-slate-200">
              <span className="block text-[11px] font-bold text-slate-500 mb-1">Standard Input (stdin):</span>
              <textarea
                rows={2}
                value={customInput}
                onChange={(e) => setCustomInput(e.target.value)}
                placeholder="Enter custom input lines here..."
                className="w-full p-2 rounded-lg border border-slate-300 font-mono text-xs text-slate-800 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              />
            </div>
          )}

          {/* Execution Result Console Drawer */}
          <div className="h-64 bg-slate-900 text-slate-100 p-4 overflow-y-auto font-mono text-xs flex flex-col justify-between">
            <div>
              {/* Header with Mode & Status */}
              <div className="flex items-center justify-between pb-2.5 border-b border-slate-800 mb-2.5">
                <div className="flex items-center gap-2">
                  <Terminal className="w-4 h-4 text-emerald-400" />
                  <span className="font-bold text-slate-300 uppercase text-[11px] tracking-wider">
                    {executionMode === 'custom_input' ? 'Custom Input Execution' :
                     executionMode === 'submit' ? 'Evaluation Test Suite' :
                     'Sample Test Cases Run'}
                  </span>
                </div>

                {/* Status Badge & Runtime */}
                {activeResult && (
                  <div className="flex items-center gap-2.5">
                    <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold ${
                      isAccepted
                        ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40'
                        : isWrongAnswer
                        ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                        : 'bg-red-500/20 text-red-400 border border-red-500/40'
                    }`}>
                      {activeResult.status}
                    </span>

                    {(activeResult.execution_time != null || activeResult.avg_time != null) && (
                      <span className="text-slate-400 text-[11px] flex items-center gap-1">
                        <Clock className="w-3 h-3 text-slate-500" />
                        {activeResult.execution_time || activeResult.avg_time || 0}s
                      </span>
                    )}
                  </div>
                )}
              </div>

              {/* Banner for Status: Execution Successful / Wrong Answer / Execution Failed */}
              {activeResult && (
                <div className="mb-3">
                  {isAccepted ? (
                    <div className="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 flex items-center justify-between">
                      <div className="flex items-center gap-2 text-emerald-300">
                        <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                        <div>
                          <span className="font-bold">Execution Successful</span>
                          <span className="text-xs text-emerald-400/80 block">
                            All {activeResult.passed_count || activeResult.total_count} required test cases passed.
                          </span>
                        </div>
                      </div>
                      {submissionResult?.points_awarded > 0 && (
                        <span className="text-xs font-bold text-yellow-300 bg-yellow-950/40 px-2.5 py-1 rounded-lg border border-yellow-500/30">
                          +{submissionResult.points_awarded} pts
                        </span>
                      )}
                    </div>
                  ) : isWrongAnswer ? (
                    <div className="p-3 rounded-xl bg-amber-950/60 border border-amber-500/40 flex items-center justify-between">
                      <div className="flex items-center gap-2 text-amber-300">
                        <XCircle className="w-4 h-4 text-amber-400 shrink-0" />
                        <div>
                          <span className="font-bold">Wrong Answer</span>
                          <span className="text-xs text-amber-300/80 block">
                            {activeResult.passed_count} passed, {activeResult.failed_count || (activeResult.total_count - activeResult.passed_count)} failed out of {activeResult.total_count} total.
                          </span>
                        </div>
                      </div>

                      <button
                        onClick={() => setShowErrorModal(true)}
                        className="px-3 py-1 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-200 border border-amber-500/40 text-[11px] font-bold transition flex items-center gap-1"
                      >
                        <Bug className="w-3 h-3" /> View Error Details
                      </button>
                    </div>
                  ) : isFailed ? (
                    <div className="p-3 rounded-xl bg-red-950/60 border border-red-500/40 flex items-center justify-between">
                      <div className="flex items-center gap-2 text-red-300">
                        <AlertTriangle className="w-4 h-4 text-red-400 shrink-0" />
                        <div>
                          <span className="font-bold">Execution Failed</span>
                          <span className="text-xs text-red-300/80 block">
                            {activeResult.error_details?.error_type || activeResult.status} encountered during execution.
                          </span>
                        </div>
                      </div>

                      <button
                        onClick={() => setShowErrorModal(true)}
                        className="px-3 py-1 rounded-lg bg-red-500/20 hover:bg-red-500/30 text-red-200 border border-red-500/40 text-[11px] font-bold transition flex items-center gap-1"
                      >
                        <Bug className="w-3 h-3" /> View Error Details
                      </button>
                    </div>
                  ) : null}
                </div>
              )}

              {/* Achievements Unlocked Alert */}
              {submissionResult?.new_achievements?.length > 0 && (
                <div className="mb-3 p-2.5 rounded-lg bg-emerald-950 border border-emerald-500/50 text-emerald-300 text-xs flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-emerald-400 shrink-0" />
                  <div>
                    <span className="font-bold">Achievement Unlocked: </span>
                    {submissionResult.new_achievements.map((a) => a.title).join(', ')} (+{submissionResult.new_achievements.reduce((acc, a) => acc + a.points_reward, 0)} pts)
                  </div>
                </div>
              )}

              {/* Results & Console display */}
              {isRunning || isSubmitting ? (
                <div className="py-6 text-center">
                  <div className="inline-block w-6 h-6 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-2" />
                  <p className="text-slate-400 animate-pulse text-xs">
                    {isSubmitting ? 'Evaluating solution against full test suite...' : 'Executing code in isolated environment...'}
                  </p>
                </div>
              ) : activeResult ? (
                <div>
                  {/* Sample test cases tab view */}
                  {activeResult.sample_results && activeResult.sample_results.length > 0 ? (
                    <div>
                      <div className="flex gap-2 mb-2">
                        {activeResult.sample_results.map((c, i) => (
                          <button
                            key={i}
                            onClick={() => setActiveCaseTab(i)}
                            className={`px-2.5 py-1 rounded text-[11px] font-bold transition ${
                              activeCaseTab === i
                                ? 'bg-slate-700 text-white'
                                : 'bg-slate-800 text-slate-400 hover:text-white'
                            } ${c.passed ? 'border-b-2 border-emerald-500' : 'border-b-2 border-red-500'}`}
                          >
                            Case {c.case} {c.passed ? '✓' : '✗'}
                          </button>
                        ))}
                      </div>

                      {activeResult.sample_results[activeCaseTab] && (
                        <div className="space-y-1.5 text-slate-300 bg-slate-950/70 p-3 rounded-lg border border-slate-800">
                          <div>
                            <span className="text-slate-500 font-bold">Input:</span>{' '}
                            <span className="text-slate-200">{activeResult.sample_results[activeCaseTab].input}</span>
                          </div>
                          <div>
                            <span className="text-slate-500 font-bold">Expected Output:</span>{' '}
                            <span className="text-emerald-400">{activeResult.sample_results[activeCaseTab].expected}</span>
                          </div>
                          <div>
                            <span className="text-slate-500 font-bold">Actual Output:</span>{' '}
                            <span className={activeResult.sample_results[activeCaseTab].passed ? 'text-emerald-400' : 'text-red-400'}>
                              {activeResult.sample_results[activeCaseTab].actual || '(Empty Output)'}
                            </span>
                          </div>
                          {activeResult.sample_results[activeCaseTab].error && (
                            <div className="text-red-400 pt-1 border-t border-slate-800">
                              <span className="text-red-500 font-bold">Error:</span> {activeResult.sample_results[activeCaseTab].error}
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  ) : (
                    /* Raw console output */
                    <div className="space-y-1">
                      <span className="text-slate-500 text-[10px] block font-bold uppercase">Standard Output:</span>
                      <pre className="p-3 rounded-lg bg-slate-950/70 border border-slate-800 text-slate-200 whitespace-pre-wrap max-h-32 overflow-y-auto font-mono text-xs">
                        {activeResult.stdout || activeResult.output || activeResult.error_message || '(No output produced)'}
                      </pre>
                    </div>
                  )}
                </div>
              ) : (
                <p className="text-slate-500 py-4">Click "Run Code" to test sample cases, or "Submit Code" to test all cases.</p>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Clickable Error Details Modal / Drawer */}
      {showErrorModal && activeErrorData && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
          <div className="bg-white rounded-3xl max-w-2xl w-full max-h-[85vh] overflow-hidden flex flex-col shadow-2xl border border-slate-200 animate-in fade-in duration-200">
            <div className="p-5 border-b border-slate-200 flex items-center justify-between bg-red-50/50">
              <div className="flex items-center gap-2 text-red-700">
                <AlertTriangle className="w-5 h-5 text-red-600" />
                <h3 className="font-extrabold text-slate-900 text-base">Error Details & Diagnostics</h3>
              </div>
              <button
                onClick={() => setShowErrorModal(false)}
                className="p-1.5 rounded-xl text-slate-400 hover:text-slate-700 hover:bg-slate-200 transition"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-6 overflow-y-auto space-y-4 text-xs">
              {/* Error Type */}
              <div className="grid grid-cols-2 gap-3">
                <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <span className="text-slate-400 font-bold uppercase text-[10px] block mb-1">Error Type</span>
                  <span className="font-extrabold text-red-600 text-sm">{activeErrorData.error_type}</span>
                </div>

                <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <span className="text-slate-400 font-bold uppercase text-[10px] block mb-1">Line Number</span>
                  <span className="font-extrabold text-slate-800 text-sm">
                    {activeErrorData.line_number ? `Line ${activeErrorData.line_number}` : 'Not provided by compiler'}
                  </span>
                </div>
              </div>

              {/* Explanation */}
              {activeErrorData.explanation && (
                <div className="p-3.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-900">
                  <div className="flex items-center gap-1.5 font-bold mb-1">
                    <HelpCircle className="w-4 h-4 text-amber-600" />
                    <span>Diagnostics:</span>
                  </div>
                  <p className="leading-relaxed">{activeErrorData.explanation}</p>
                </div>
              )}

              {/* Raw Error Output from Execution Service */}
              {activeErrorData.error_output && (
                <div>
                  <span className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-1.5">
                    Service Error Output:
                  </span>
                  <pre className="p-4 rounded-xl bg-slate-900 text-red-300 font-mono text-xs overflow-x-auto whitespace-pre-wrap max-h-60 leading-relaxed">
                    {activeErrorData.error_output}
                  </pre>
                </div>
              )}
            </div>

            <div className="p-4 bg-slate-50 border-t border-slate-200 flex justify-end">
              <button
                onClick={() => setShowErrorModal(false)}
                className="px-5 py-2 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs transition"
              >
                Close & Return to Editor
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default WorkspacePage;
