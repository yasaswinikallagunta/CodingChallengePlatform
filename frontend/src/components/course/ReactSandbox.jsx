import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import { 
  Play, 
  RotateCcw, 
  Layers, 
  Sparkles, 
  CheckCircle2, 
  Star, 
  Send, 
  Check, 
  X, 
  Plus, 
  Trash2, 
  ChevronDown, 
  ChevronUp, 
  ExternalLink 
} from 'lucide-react';

export default function ReactSandbox({
  exercise,
  userCode,
  onChange,
  onReset,
  onComplete,
  isCompleted
}) {
  const [activeTab, setActiveTab] = useState('split'); // 'split' | 'code' | 'preview'
  const [validationResults, setValidationResults] = useState([]);

  // Interactive Simulator States for the 5 React Exercises:
  // Exercise 1: Star Rating
  const [rating, setRating] = useState(4);
  const [hoverRating, setHoverRating] = useState(0);

  // Exercise 2: Feedback Form
  const [feedbackName, setFeedbackName] = useState('');
  const [feedbackCategory, setFeedbackCategory] = useState('React');
  const [feedbackText, setFeedbackText] = useState('This course provides comprehensive real-world exercises!');
  const [feedbackSubmitted, setFeedbackSubmitted] = useState(false);

  // Exercise 3: Task Tracker
  const [tasks, setTasks] = useState([
    { id: 1, title: 'Learn React Props & State', completed: true },
    { id: 2, title: 'Build Custom Hooks', completed: false },
    { id: 3, title: 'Master Context API & Redux', completed: false }
  ]);
  const [taskFilter, setTaskFilter] = useState('all');
  const [newTaskInput, setNewTaskInput] = useState('');

  // Exercise 4: Modal
  const [isModalOpen, setIsModalOpen] = useState(false);

  // Exercise 5: Accordion
  const [allowMultiple, setAllowMultiple] = useState(false);
  const [expandedSections, setExpandedSections] = useState([0]);

  const runValidation = () => {
    const code = userCode.toLowerCase();
    const results = (exercise.requirements || []).map((req) => {
      const lowerReq = req.toLowerCase();
      let passed = false;

      if (lowerReq.includes('usestate')) {
        passed = code.includes('usestate');
      } else if (lowerReq.includes('props') || lowerReq.includes('onratingchange') || lowerReq.includes('children')) {
        passed = code.includes('props') || code.includes('{') || code.includes('onratingchange') || code.includes('children');
      } else if (lowerReq.includes('button') || lowerReq.includes('star')) {
        passed = code.includes('<button') || code.includes('star');
      } else if (lowerReq.includes('form') || lowerReq.includes('onsubmit')) {
        passed = code.includes('<form') || code.includes('onsubmit') || code.includes('preventdefault');
      } else if (lowerReq.includes('filter') || lowerReq.includes('map')) {
        passed = code.includes('.map') || code.includes('.filter');
      } else if (lowerReq.includes('modal') || lowerReq.includes('dialog')) {
        passed = code.includes('modal') || code.includes('fixed') || code.includes('role="dialog"');
      } else if (lowerReq.includes('accordion') || lowerReq.includes('toggle')) {
        passed = code.includes('accordion') || code.includes('toggle') || code.includes('expanded');
      } else {
        passed = code.trim().length > 50;
      }

      return { text: req, passed };
    });

    setValidationResults(results);
  };

  const allPassed = validationResults.length > 0 && validationResults.every((r) => r.passed);

  // Helper for task filter
  const filteredTasks = tasks.filter((t) => {
    if (taskFilter === 'active') return !t.completed;
    if (taskFilter === 'completed') return t.completed;
    return true;
  });

  const toggleTask = (id) => {
    setTasks(tasks.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t)));
  };

  const addTask = (e) => {
    e.preventDefault();
    if (!newTaskInput.trim()) return;
    setTasks([...tasks, { id: Date.now(), title: newTaskInput.trim(), completed: false }]);
    setNewTaskInput('');
  };

  const toggleAccordion = (index) => {
    if (allowMultiple) {
      if (expandedSections.includes(index)) {
        setExpandedSections(expandedSections.filter((i) => i !== index));
      } else {
        setExpandedSections([...expandedSections, index]);
      }
    } else {
      setExpandedSections(expandedSections.includes(index) ? [] : [index]);
    }
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
      {/* Top Toolbar */}
      <div className="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <Layers className="w-3.5 h-3.5 text-emerald-600" />
            React Component Interactive Studio
          </span>
          <span className="text-[11px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-semibold">
            JSX & State Runtime
          </span>
        </div>

        <div className="flex items-center gap-2">
          {/* View Toggles */}
          <div className="flex items-center bg-white rounded-lg border border-slate-200 p-0.5 text-xs">
            <button
              onClick={() => setActiveTab('split')}
              className={`px-2.5 py-1 rounded-md font-medium transition ${
                activeTab === 'split' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Split View
            </button>
            <button
              onClick={() => setActiveTab('code')}
              className={`px-2.5 py-1 rounded-md font-medium transition ${
                activeTab === 'code' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Code
            </button>
            <button
              onClick={() => setActiveTab('preview')}
              className={`px-2.5 py-1 rounded-md font-medium transition ${
                activeTab === 'preview' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Live Component
            </button>
          </div>

          <button
            onClick={runValidation}
            className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-sm transition flex items-center gap-1.5"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>Validate React Code</span>
          </button>

          <button
            onClick={onReset}
            className="p-1.5 text-slate-500 hover:text-slate-800 hover:bg-slate-200/60 rounded-lg transition"
            title="Reset code"
          >
            <RotateCcw className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* Editor & Live Interactive Simulation Panel */}
      <div className="grid grid-cols-1 md:grid-cols-2 flex-1 min-h-[460px] divide-y md:divide-y-0 md:divide-x divide-slate-200">
        {/* Editor */}
        <div className={`flex flex-col h-full ${activeTab === 'preview' ? 'hidden' : activeTab === 'code' ? 'col-span-2' : ''}`}>
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span>React JSX Component Code</span>
            <span className="text-[11px] text-slate-400">ES6+ & Hooks</span>
          </div>
          <div className="flex-1 min-h-[420px]">
            <Editor
              height="100%"
              language="javascript"
              value={userCode}
              onChange={(val) => onChange(val || '')}
              theme="vs"
              options={{
                fontSize: 13,
                minimap: { enabled: false },
                wordWrap: 'on',
                automaticLayout: true,
                tabSize: 2,
                scrollBeyondLastLine: false,
                fontFamily: "'Fira Code', monospace"
              }}
            />
          </div>
        </div>

        {/* Live Interactive Simulator */}
        <div className={`flex flex-col h-full bg-slate-50 ${activeTab === 'code' ? 'hidden' : activeTab === 'preview' ? 'col-span-2' : ''}`}>
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span className="flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
              Live Interactive Component Runner
            </span>
            <span className="text-[11px] text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
              Interactive State & Props
            </span>
          </div>

          <div className="flex-1 p-4 bg-white flex flex-col justify-center items-center min-h-[300px]">
            {/* Simulation for Exercise 1: Star Rating */}
            {exercise.id.includes('react-ex-1') && (
              <div className="w-full max-w-sm p-6 rounded-xl border border-slate-200 bg-slate-50 text-center shadow-xs">
                <h4 className="text-sm font-bold text-slate-800 mb-2">Interactive Star Rating</h4>
                <div
                  className="flex items-center justify-center gap-1.5 mb-3"
                  onMouseLeave={() => setHoverRating(0)}
                >
                  {[1, 2, 3, 4, 5].map((starIndex) => {
                    const isFilled = (hoverRating || rating) >= starIndex;
                    return (
                      <button
                        key={starIndex}
                        type="button"
                        onClick={() => setRating(rating === starIndex ? 0 : starIndex)}
                        onMouseEnter={() => setHoverRating(starIndex)}
                        className="p-1 text-2xl transition-transform hover:scale-110 focus:outline-hidden"
                      >
                        <Star
                          className={`w-7 h-7 ${
                            isFilled ? 'text-amber-400 fill-amber-400' : 'text-slate-300'
                          }`}
                        />
                      </button>
                    );
                  })}
                </div>
                <p className="text-xs font-semibold text-slate-600">
                  You rated this <span className="text-emerald-700 font-bold">{rating}</span> out of 5 stars
                </p>
                <div className="mt-3 text-[11px] text-slate-400">
                  Click to rate, hover to preview, click active star to clear.
                </div>
              </div>
            )}

            {/* Simulation for Exercise 2: Feedback Form */}
            {exercise.id.includes('react-ex-2') && (
              <div className="w-full max-w-md p-5 rounded-xl border border-slate-200 bg-slate-50 shadow-xs">
                <h4 className="text-sm font-bold text-slate-800 mb-3">Course Feedback Form</h4>
                <form
                  onSubmit={(e) => {
                    e.preventDefault();
                    setFeedbackSubmitted(true);
                  }}
                  className="space-y-3"
                >
                  <div>
                    <label className="block text-xs font-semibold text-slate-700 mb-1">Your Name</label>
                    <input
                      type="text"
                      required
                      value={feedbackName}
                      onChange={(e) => setFeedbackName(e.target.value)}
                      placeholder="e.g. Alex Chen"
                      className="w-full px-3 py-1.5 text-xs rounded-lg border border-slate-300 focus:outline-emerald-500"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-700 mb-1">Topic</label>
                    <select
                      value={feedbackCategory}
                      onChange={(e) => setFeedbackCategory(e.target.value)}
                      className="w-full px-3 py-1.5 text-xs rounded-lg border border-slate-300 focus:outline-emerald-500"
                    >
                      <option value="React">React & Components</option>
                      <option value="JavaScript">Advanced JavaScript</option>
                      <option value="CSS">Advanced CSS & Styling</option>
                    </select>
                  </div>
                  <div>
                    <div className="flex justify-between items-center mb-1">
                      <label className="text-xs font-semibold text-slate-700">Comments</label>
                      <span className={`text-[10px] ${feedbackText.length > 280 ? 'text-red-500' : 'text-slate-400'}`}>
                        {feedbackText.length} / 300
                      </span>
                    </div>
                    <textarea
                      rows={3}
                      maxLength={300}
                      value={feedbackText}
                      onChange={(e) => setFeedbackText(e.target.value)}
                      className="w-full px-3 py-1.5 text-xs rounded-lg border border-slate-300 focus:outline-emerald-500"
                    />
                  </div>
                  <button
                    type="submit"
                    className="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-lg shadow-xs transition"
                  >
                    Submit Verified Feedback
                  </button>
                  {feedbackSubmitted && (
                    <div className="p-2 bg-emerald-50 border border-emerald-200 rounded text-emerald-800 text-xs font-semibold flex items-center gap-1.5">
                      <Check className="w-3.5 h-3.5" /> Feedback recorded successfully!
                    </div>
                  )}
                </form>
              </div>
            )}

            {/* Simulation for Exercise 3: Filterable Task Tracker */}
            {exercise.id.includes('react-ex-3') && (
              <div className="w-full max-w-md p-5 rounded-xl border border-slate-200 bg-slate-50 shadow-xs">
                <h4 className="text-sm font-bold text-slate-800 mb-2">Filterable Task Tracker</h4>
                <div className="flex gap-1.5 mb-3">
                  {['all', 'active', 'completed'].map((f) => (
                    <button
                      key={f}
                      onClick={() => setTaskFilter(f)}
                      className={`px-2.5 py-1 text-xs rounded-md capitalize font-semibold transition ${
                        taskFilter === f ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-700 hover:bg-slate-300'
                      }`}
                    >
                      {f}
                    </button>
                  ))}
                </div>
                <form onSubmit={addTask} className="flex gap-2 mb-3">
                  <input
                    type="text"
                    value={newTaskInput}
                    onChange={(e) => setNewTaskInput(e.target.value)}
                    placeholder="New engineering task..."
                    className="flex-1 px-3 py-1.5 text-xs rounded-lg border border-slate-300 focus:outline-emerald-500"
                  />
                  <button
                    type="submit"
                    className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1"
                  >
                    <Plus className="w-3.5 h-3.5" /> Add
                  </button>
                </form>
                <div className="space-y-1.5 max-h-40 overflow-y-auto">
                  {filteredTasks.map((t) => (
                    <div
                      key={t.id}
                      onClick={() => toggleTask(t.id)}
                      className="p-2 bg-white rounded-lg border border-slate-200 flex items-center justify-between text-xs cursor-pointer hover:bg-slate-100 transition"
                    >
                      <span className={t.completed ? 'line-through text-slate-400' : 'text-slate-800 font-medium'}>
                        {t.title}
                      </span>
                      <span className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${
                        t.completed ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                      }`}>
                        {t.completed ? 'Done' : 'Pending'}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Simulation for Exercise 4: Modal */}
            {exercise.id.includes('react-ex-4') && (
              <div className="text-center">
                <button
                  onClick={() => setIsModalOpen(true)}
                  className="px-4 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-lg shadow-sm transition flex items-center gap-2 mx-auto"
                >
                  <ExternalLink className="w-3.5 h-3.5" />
                  <span>Open Accessible Modal</span>
                </button>
                <p className="text-xs text-slate-500 mt-2">
                  Click to test backdrop blur, keyboard dismiss, and children slots.
                </p>

                {isModalOpen && (
                  <div
                    className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4 animate-in fade-in"
                    onClick={() => setIsModalOpen(false)}
                  >
                    <div
                      className="bg-white rounded-xl shadow-xl max-w-sm w-full p-5 text-left border border-slate-200"
                      onClick={(e) => e.stopPropagation()}
                    >
                      <div className="flex items-center justify-between border-b border-slate-200 pb-2 mb-3">
                        <h5 className="font-bold text-slate-900 text-sm">Enrollment Confirmation</h5>
                        <button
                          onClick={() => setIsModalOpen(false)}
                          className="p-1 text-slate-400 hover:text-slate-700 rounded"
                        >
                          <X className="w-4 h-4" />
                        </button>
                      </div>
                      <p className="text-xs text-slate-600 mb-4 leading-relaxed">
                        You are enrolled in the Modern Frontend Development curriculum. Real-time progress is synchronized automatically.
                      </p>
                      <button
                        onClick={() => setIsModalOpen(false)}
                        className="w-full py-2 bg-emerald-600 text-white text-xs font-bold rounded-lg hover:bg-emerald-700 transition"
                      >
                        Understood &amp; Close
                      </button>
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Simulation for Exercise 5: Accordion */}
            {exercise.id.includes('react-ex-5') && (
              <div className="w-full max-w-md p-5 rounded-xl border border-slate-200 bg-slate-50 shadow-xs">
                <div className="flex items-center justify-between mb-3">
                  <h4 className="text-sm font-bold text-slate-800">Engineering FAQ Accordion</h4>
                  <label className="flex items-center gap-1.5 text-xs font-semibold text-slate-600 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={allowMultiple}
                      onChange={(e) => setAllowMultiple(e.target.checked)}
                      className="rounded text-emerald-600 focus:ring-emerald-500"
                    />
                    <span>Multi-expand</span>
                  </label>
                </div>
                <div className="space-y-2">
                  {[
                    { q: 'What is the Virtual DOM in React?', a: 'A lightweight in-memory representation of the real DOM that enables fast batch updates through reconciliation.' },
                    { q: 'Why do hooks require calls at top level?', a: 'React relies on execution call order to maintain state between component renders.' },
                    { q: 'How does useEffect clean up side-effects?', a: 'Return a cleanup function from the effect to unsubscribe or cancel pending network requests.' }
                  ].map((item, idx) => {
                    const isExpanded = expandedSections.includes(idx);
                    return (
                      <div key={idx} className="border border-slate-200 rounded-lg overflow-hidden bg-white">
                        <button
                          onClick={() => toggleAccordion(idx)}
                          className="w-full px-3 py-2.5 text-left text-xs font-bold text-slate-800 flex items-center justify-between hover:bg-slate-50 transition"
                        >
                          <span>{item.q}</span>
                          {isExpanded ? <ChevronUp className="w-3.5 h-3.5 text-emerald-600" /> : <ChevronDown className="w-3.5 h-3.5 text-slate-400" />}
                        </button>
                        {isExpanded && (
                          <div className="px-3 pb-3 pt-1 text-xs text-slate-600 border-t border-slate-100 bg-slate-50/50">
                            {item.a}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}
          </div>

          {/* Validation Checklist */}
          {validationResults.length > 0 && (
            <div className="p-3 bg-white border-t border-slate-200">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                  Component Criteria Checklist
                </span>
                <span
                  className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${
                    allPassed ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                  }`}
                >
                  {validationResults.filter((r) => r.passed).length} / {validationResults.length} Passed
                </span>
              </div>
              <ul className="space-y-1.5 text-xs">
                {validationResults.map((result, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    {result.passed ? (
                      <Check className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                    ) : (
                      <div className="w-4 h-4 rounded-full border border-slate-300 shrink-0 mt-0.5" />
                    )}
                    <span className={result.passed ? 'text-slate-800 font-medium' : 'text-slate-500'}>
                      {result.text}
                    </span>
                  </li>
                ))}
              </ul>

              {allPassed && (
                <div className="mt-3 p-2.5 rounded-lg bg-emerald-50 border border-emerald-200 flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Sparkles className="w-4 h-4 text-emerald-600" />
                    <span className="text-xs font-bold text-emerald-800">
                      Component design criteria satisfied!
                    </span>
                  </div>
                  {!isCompleted && (
                    <button
                      onClick={onComplete}
                      className="px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-md text-xs font-bold shadow-xs transition"
                    >
                      Mark Completed
                    </button>
                  )}
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
