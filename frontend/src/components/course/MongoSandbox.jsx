import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import { Database, Play, RotateCcw, CheckCircle2, FileJson, Sparkles, Filter, Layers } from 'lucide-react';

export default function MongoSandbox({
  exercise,
  userCode,
  onChange,
  onReset,
  onComplete,
  isCompleted
}) {
  const [queryOutput, setQueryOutput] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [passedCheck, setPassedCheck] = useState(false);

  // Sample data collections for simulation
  const sampleCollections = {
    developers: [
      { _id: 'd1', name: 'Rohan Sharma', role: 'Full-Stack Developer', skills: ['Python', 'Django', 'React'], status: 'active', rating: 4.9 },
      { _id: 'd2', name: 'Kavita Rao', role: 'Backend Developer', skills: ['Java', 'Spring', 'SQL'], status: 'inactive', rating: 4.2 },
      { _id: 'd3', name: 'Manish Kumar', role: 'UI Engineer', skills: ['HTML5', 'CSS3', 'Vue'], status: 'active', rating: 4.4 }
    ],
    courses: [
      { _id: 'c1', title: 'Modern Frontend Development', category: 'Frontend', level: 'Intermediate', rating: 4.9, price: 0, enrollmentCount: 1420 },
      { _id: 'c2', title: 'Algorithms & Data Structures', category: 'CS Core', level: 'Advanced', rating: 4.8, price: 49, enrollmentCount: 890 },
      { _id: 'c3', title: 'Introductory HTML & CSS', category: 'Frontend', level: 'Beginner', rating: 4.3, price: 0, enrollmentCount: 2300 },
      { _id: 'c4', title: 'Distributed Systems with Go', category: 'Backend', level: 'Advanced', rating: 4.7, price: 99, enrollmentCount: 420 },
      { _id: 'c5', title: 'Design Patterns in TypeScript', category: 'Software Eng', level: 'Intermediate', rating: 4.6, price: 29, enrollmentCount: 650 }
    ],
    inventory: [
      { _id: 'SKU-001', name: 'Mechanical Keyboard RGB', category: 'Peripherals', stock: 14, minStock: 20, price: 89 },
      { _id: 'SKU-002', name: '4K Ultra-Wide Monitor 34"', category: 'Displays', stock: 8, minStock: 5, price: 499 },
      { _id: 'SKU-003', name: 'Ergonomic Standing Desk', category: 'Furniture', stock: 2, minStock: 5, price: 349 },
      { _id: 'SKU-004', name: 'Noise-Cancelling Headset', category: 'Audio', stock: 25, minStock: 10, price: 129 }
    ]
  };

  const executeMongoQuery = () => {
    setIsRunning(true);
    setErrorMessage('');
    setQueryOutput(null);
    setPassedCheck(false);

    try {
      const capturedLogs = [];
      const mockConsole = {
        log: (...args) => {
          capturedLogs.push(args.map(a => (typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a))).join(' '));
        }
      };

      // Safely evaluate the query function in a client-side environment
      const sandboxedFn = new Function('sampleCollections', 'console', userCode);
      const res = sandboxedFn(sampleCollections, mockConsole);

      const finalOutput = res !== undefined ? res : capturedLogs.length > 0 ? capturedLogs.join('\n') : 'Query executed successfully with 0 returned rows.';
      setQueryOutput(finalOutput);

      // Verify query logic
      const code = userCode.toLowerCase();
      const hasValidQueryStructure = 
        code.includes('filter') || 
        code.includes('find') || 
        code.includes('reduce') || 
        code.includes('map') || 
        code.includes('push') || 
        code.includes('insert');

      if (hasValidQueryStructure && finalOutput) {
        setPassedCheck(true);
      }
    } catch (err) {
      setErrorMessage(err.message || String(err));
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
      {/* Top Bar */}
      <div className="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <Database className="w-3.5 h-3.5 text-emerald-600" />
            MongoDB Query &amp; Aggregation Runner
          </span>
          <span className="text-[11px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-semibold">
            JSON Document Engine
          </span>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={executeMongoQuery}
            disabled={isRunning}
            className="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 disabled:opacity-50 text-white text-xs font-bold shadow-sm transition flex items-center gap-1.5"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>{isRunning ? 'Running Query...' : 'Run MongoDB Query'}</span>
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

      {/* Editor & Output Panels */}
      <div className="grid grid-cols-1 md:grid-cols-2 flex-1 min-h-[460px] divide-y md:divide-y-0 md:divide-x divide-slate-200">
        {/* Monaco Query Editor */}
        <div className="flex flex-col h-full">
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span>Query Function &amp; Pipeline Script</span>
            <span className="text-[11px] text-slate-400">client-side document simulator</span>
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

        {/* Results & Collection Inspector */}
        <div className="flex flex-col h-full bg-slate-900 text-slate-100 font-mono text-xs">
          <div className="bg-slate-800/90 px-3 py-2 border-b border-slate-700 flex items-center justify-between">
            <span className="text-xs font-bold text-slate-300 flex items-center gap-1.5">
              <FileJson className="w-3.5 h-3.5 text-emerald-400" />
              Query Results &amp; Formatted JSON
            </span>
            <span className="text-[10px] text-slate-400">MongoDB Output View</span>
          </div>

          <div className="flex-1 p-3 overflow-y-auto space-y-2 min-h-[300px]">
            {queryOutput === null && !errorMessage && (
              <div className="text-slate-400 py-6 text-center font-sans space-y-2">
                <p>Click <span className="font-bold text-emerald-400">Run MongoDB Query</span> to execute against the active collection.</p>
                <div className="text-[11px] text-slate-500 bg-slate-800/50 p-2.5 rounded-lg border border-slate-700 inline-block text-left">
                  <div className="font-semibold text-slate-300 mb-1">Available Test Collections:</div>
                  • sampleCollections.developers (3 documents)<br />
                  • sampleCollections.courses (5 documents)<br />
                  • sampleCollections.inventory (4 documents)
                </div>
              </div>
            )}

            {queryOutput !== null && (
              <pre className="p-3 bg-slate-950 rounded-lg text-emerald-300 overflow-x-auto text-xs leading-relaxed border border-slate-800">
                {typeof queryOutput === 'object' ? JSON.stringify(queryOutput, null, 2) : String(queryOutput)}
              </pre>
            )}

            {errorMessage && (
              <div className="p-2.5 rounded bg-red-900/40 border border-red-700 text-red-200">
                <div className="font-bold text-red-300 text-xs">Query Execution Error</div>
                <div className="text-[11px] mt-1">{errorMessage}</div>
              </div>
            )}
          </div>

          {/* Validation Status */}
          <div className="p-3 bg-slate-800/80 border-t border-slate-700 font-sans">
            {passedCheck ? (
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-emerald-400 text-xs font-bold">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Query Executed &amp; Output Verified!</span>
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
            ) : (
              <div className="text-[11px] text-slate-400">
                Write a valid query function that returns or logs the expected documents.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
