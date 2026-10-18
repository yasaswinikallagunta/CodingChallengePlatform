import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import { Play, RotateCcw, Terminal, CheckCircle2, XCircle, Clock, Sparkles, AlertTriangle } from 'lucide-react';

export default function JsSandbox({
  exercise,
  userCode,
  onChange,
  onReset,
  onComplete,
  isCompleted
}) {
  const [logs, setLogs] = useState([]);
  const [executionTime, setExecutionTime] = useState(null);
  const [hasError, setHasError] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [passedCheck, setPassedCheck] = useState(false);

  const runCode = () => {
    setIsRunning(true);
    setLogs([]);
    setHasError(false);
    setErrorMessage('');
    setPassedCheck(false);

    const startTime = performance.now();
    const capturedLogs = [];

    // Create a mock console object to safely capture logs
    const mockConsole = {
      log: (...args) => {
        capturedLogs.push({
          type: 'log',
          text: args.map(arg => formatLogArgument(arg)).join(' ')
        });
      },
      error: (...args) => {
        capturedLogs.push({
          type: 'error',
          text: args.map(arg => formatLogArgument(arg)).join(' ')
        });
      },
      warn: (...args) => {
        capturedLogs.push({
          type: 'warn',
          text: args.map(arg => formatLogArgument(arg)).join(' ')
        });
      },
      info: (...args) => {
        capturedLogs.push({
          type: 'info',
          text: args.map(arg => formatLogArgument(arg)).join(' ')
        });
      }
    };

    try {
      // Execute user code in a function sandbox
      // Note: Never executed on the Django server, strictly client-side sandbox
      const sandboxedFn = new Function('console', userCode);
      const returnValue = sandboxedFn(mockConsole);

      if (returnValue !== undefined) {
        capturedLogs.push({
          type: 'return',
          text: `↪ Return Value: ${formatLogArgument(returnValue)}`
        });
      }

      const elapsed = (performance.now() - startTime).toFixed(2);
      setExecutionTime(elapsed);
      setLogs(capturedLogs);

      // Check if output meets expected behavior or requirements
      const fullLogText = capturedLogs.map(l => l.text).join(' ');
      const passed = evaluateRequirements(exercise, userCode, fullLogText);
      setPassedCheck(passed);
    } catch (err) {
      const elapsed = (performance.now() - startTime).toFixed(2);
      setExecutionTime(elapsed);
      setHasError(true);
      setErrorMessage(err.message || String(err));
      capturedLogs.push({
        type: 'error',
        text: `Runtime Error: ${err.message}`
      });
      setLogs(capturedLogs);
    } finally {
      setIsRunning(false);
    }
  };

  const formatLogArgument = (arg) => {
    if (arg === null) return 'null';
    if (arg === undefined) return 'undefined';
    if (typeof arg === 'object') {
      try {
        return JSON.stringify(arg, null, 2);
      } catch (e) {
        return String(arg);
      }
    }
    return String(arg);
  };

  const evaluateRequirements = (ex, code, logText) => {
    const lowerCode = code.toLowerCase();
    const lowerLog = logText.toLowerCase();

    // Check basic length and execution without error
    if (code.trim().length < 30) return false;

    // Exercise specific checks
    if (ex.id.includes('js-ex-1')) {
      // Temperature converter
      return lowerCode.includes('convert') && (lowerLog.includes('celsius') || lowerLog.includes('°c') || lowerLog.includes('68') || lowerLog.includes('37'));
    }
    if (ex.id.includes('js-ex-2')) {
      // Cart calculator
      return lowerCode.includes('calculate') && (lowerLog.includes('subtotal') || lowerLog.includes('total') || lowerLog.includes('discount'));
    }
    if (ex.id.includes('js-ex-3')) {
      // DOM / Todo list
      return lowerCode.includes('todo') || lowerCode.includes('createelement') || lowerCode.includes('push');
    }
    if (ex.id.includes('js-ex-4')) {
      // Password validator
      return lowerCode.includes('password') && (lowerLog.includes('score') || lowerLog.includes('strength') || lowerLog.includes('strong'));
    }
    if (ex.id.includes('js-ex-5')) {
      // Catalog filter
      return lowerCode.includes('filter') && (lowerLog.includes('laptop') || lowerLog.includes('electronics') || lowerLog.includes('headphones'));
    }
    if (ex.id.includes('adv-js-ex-1')) {
      // Immutable state
      return (lowerCode.includes('spread') || lowerCode.includes('...')) && (lowerLog.includes('dark') || lowerLog.includes('settings') || lowerLog.includes('alex'));
    }
    if (ex.id.includes('adv-js-ex-2')) {
      // Rate limiter
      return lowerCode.includes('createratelimiter') && (lowerLog.includes('true') || lowerLog.includes('false') || lowerLog.includes('blocked'));
    }
    if (ex.id.includes('adv-js-ex-3')) {
      // Async fetch with retry
      return (lowerCode.includes('async') || lowerCode.includes('promise')) && (lowerLog.includes('attempt') || lowerLog.includes('success'));
    }
    if (ex.id.includes('adv-js-ex-4')) {
      // Promise.allSettled
      return lowerCode.includes('allsettled') || lowerCode.includes('promise');
    }
    if (ex.id.includes('adv-js-ex-5')) {
      // Event emitter
      return lowerCode.includes('eventemitter') || (lowerCode.includes('on') && lowerCode.includes('emit'));
    }

    // Default pass if logs were produced with no error
    return capturedLogsHaveContent(logText);
  };

  const capturedLogsHaveContent = (logText) => {
    return logText.trim().length > 0;
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
      {/* Top Bar */}
      <div className="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <Terminal className="w-3.5 h-3.5 text-emerald-600" />
            JavaScript Interactive Console
          </span>
          <span className="text-[11px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-semibold">
            ES6+ Engine
          </span>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={runCode}
            disabled={isRunning}
            className="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 disabled:opacity-50 text-white text-xs font-bold shadow-sm transition flex items-center gap-1.5"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>{isRunning ? 'Executing...' : 'Run Code'}</span>
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

      {/* Editor & Console Output */}
      <div className="grid grid-cols-1 md:grid-cols-2 flex-1 min-h-[460px] divide-y md:divide-y-0 md:divide-x divide-slate-200">
        {/* Monaco Editor */}
        <div className="flex flex-col h-full">
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span>JavaScript Script Editor</span>
            <span className="text-[11px] text-slate-400">client-side sandboxed</span>
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

        {/* Terminal Output */}
        <div className="flex flex-col h-full bg-slate-900 text-slate-100 font-mono text-xs">
          <div className="bg-slate-800/90 px-3 py-2 border-b border-slate-700 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="w-2.5 h-2.5 rounded-full bg-red-500" />
              <div className="w-2.5 h-2.5 rounded-full bg-amber-500" />
              <div className="w-2.5 h-2.5 rounded-full bg-emerald-500" />
              <span className="ml-1 text-[11px] font-semibold text-slate-300">Console Terminal</span>
            </div>

            {executionTime && (
              <span className="flex items-center gap-1 text-[10px] text-emerald-400 font-medium">
                <Clock className="w-3 h-3" />
                {executionTime} ms
              </span>
            )}
          </div>

          <div className="flex-1 p-3 overflow-y-auto space-y-1.5 min-h-[300px]">
            {logs.length === 0 && !hasError && (
              <div className="text-slate-500 italic py-6 text-center font-sans">
                Click <span className="font-bold text-emerald-400">Run Code</span> to execute your JavaScript in real-time.
              </div>
            )}

            {logs.map((log, index) => (
              <div
                key={index}
                className={`p-1.5 rounded whitespace-pre-wrap break-all ${
                  log.type === 'error'
                    ? 'bg-red-950/40 text-red-300 border-l-2 border-red-500'
                    : log.type === 'warn'
                    ? 'bg-amber-950/40 text-amber-300 border-l-2 border-amber-500'
                    : log.type === 'return'
                    ? 'bg-emerald-950/40 text-emerald-300 border-l-2 border-emerald-500 font-semibold'
                    : 'text-slate-200'
                }`}
              >
                {log.text}
              </div>
            ))}

            {hasError && (
              <div className="p-2 rounded bg-red-900/40 border border-red-700 text-red-200 flex items-start gap-2">
                <AlertTriangle className="w-4 h-4 text-red-400 shrink-0 mt-0.5" />
                <div>
                  <div className="font-bold text-red-300">Execution Error</div>
                  <div className="text-[11px]">{errorMessage}</div>
                </div>
              </div>
            )}
          </div>

          {/* Validation Status footer */}
          <div className="p-3 bg-slate-800/80 border-t border-slate-700 font-sans">
            {passedCheck ? (
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-emerald-400 text-xs font-bold">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Test Output Verified Successfully!</span>
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
                Ensure all requirements and test cases in the problem statement are covered.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
