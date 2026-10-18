import React, { useState, useEffect, useRef } from 'react';
import Editor from '@monaco-editor/react';
import { Play, RotateCcw, CheckCircle2, XCircle, Eye, Code2, Sparkles, Check, AlertCircle } from 'lucide-react';

export default function HtmlCssSandbox({
  exercise,
  userCode,
  onChange,
  onReset,
  onComplete,
  isCompleted
}) {
  const [activeTab, setActiveTab] = useState('split'); // 'split' | 'code' | 'preview'
  const [previewContent, setPreviewContent] = useState('');
  const [validationResults, setValidationResults] = useState([]);
  const [hasRun, setHasRun] = useState(false);
  const iframeRef = useRef(null);

  // Initialize preview on mount or code change
  useEffect(() => {
    runPreview(userCode || exercise.starterCode);
  }, [exercise.id]);

  const runPreview = (codeToRun) => {
    const code = codeToRun !== undefined ? codeToRun : userCode;
    setPreviewContent(code);
    setHasRun(true);

    // Validate requirements against the HTML/CSS
    if (exercise.requirements && exercise.requirements.length > 0) {
      const results = exercise.requirements.map((req) => {
        const passed = checkRequirement(req, code);
        return { text: req, passed };
      });
      setValidationResults(results);
    }
  };

  const checkRequirement = (reqText, code) => {
    const lower = code.toLowerCase();
    const req = reqText.toLowerCase();

    if (req.includes('<article') || req.includes('article element')) {
      return lower.includes('<article') && lower.includes('</article>');
    }
    if (req.includes('<header') || req.includes('header')) {
      return lower.includes('<header') && lower.includes('</header>');
    }
    if (req.includes('<footer') || req.includes('footer')) {
      return lower.includes('<footer') && lower.includes('</footer');
    }
    if (req.includes('<section') || req.includes('section')) {
      return lower.includes('<section');
    }
    if (req.includes('<img') || req.includes('image') || req.includes('avatar')) {
      return lower.includes('<img') && lower.includes('alt=');
    }
    if (req.includes('<ul>') || req.includes('list') || req.includes('competencies')) {
      return lower.includes('<ul') && lower.includes('<li');
    }
    if (req.includes('<form') || req.includes('form')) {
      return lower.includes('<form');
    }
    if (req.includes('required') || req.includes('validation')) {
      return lower.includes('required');
    }
    if (req.includes('<table') || req.includes('table')) {
      return lower.includes('<table') && (lower.includes('<thead') || lower.includes('<tbody'));
    }
    if (req.includes('<video') || req.includes('<audio') || req.includes('multimedia')) {
      return lower.includes('<video') || lower.includes('<audio');
    }
    if (req.includes('<meta') || req.includes('og:') || req.includes('opengraph')) {
      return lower.includes('<meta');
    }
    if (req.includes('flex') || req.includes('display: flex')) {
      return lower.includes('display: flex') || lower.includes('display:flex');
    }
    if (req.includes('grid') || req.includes('display: grid')) {
      return lower.includes('display: grid') || lower.includes('display:grid');
    }
    if (req.includes('keyframes') || req.includes('animation')) {
      return lower.includes('@keyframes') || lower.includes('animation');
    }
    if (req.includes('var(') || req.includes('custom properties') || req.includes('--')) {
      return lower.includes('--') || lower.includes('var(');
    }
    if (req.includes('box-shadow') || req.includes('backdrop-filter') || req.includes('glass')) {
      return lower.includes('backdrop-filter') || lower.includes('box-shadow') || lower.includes('border');
    }

    // Default heuristic: non-empty check
    return code.trim().length > 30;
  };

  const allPassed = validationResults.length > 0 && validationResults.every((r) => r.passed);

  return (
    <div className="flex flex-col h-full bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
      {/* Top Toolbar */}
      <div className="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <Code2 className="w-3.5 h-3.5 text-emerald-600" />
            HTML & CSS Live Workspace
          </span>
          <span className="text-[11px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-semibold">
            Realtime Sandbox
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
              Code Only
            </button>
            <button
              onClick={() => setActiveTab('preview')}
              className={`px-2.5 py-1 rounded-md font-medium transition ${
                activeTab === 'preview' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Live Preview
            </button>
          </div>

          <button
            onClick={() => runPreview()}
            className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-sm transition flex items-center gap-1.5"
            title="Render code in preview sandbox"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>Render Preview</span>
          </button>

          <button
            onClick={onReset}
            className="p-1.5 text-slate-500 hover:text-slate-800 hover:bg-slate-200/60 rounded-lg transition"
            title="Reset to starter code"
          >
            <RotateCcw className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* Editor & Preview Panels */}
      <div className="grid grid-cols-1 md:grid-cols-2 flex-1 min-h-[460px] divide-y md:divide-y-0 md:divide-x divide-slate-200">
        {/* Code Editor Panel */}
        <div
          className={`flex flex-col h-full ${
            activeTab === 'preview' ? 'hidden' : activeTab === 'code' ? 'col-span-2' : ''
          }`}
        >
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span>Markup & Stylesheet Editor</span>
            <span className="text-[11px] text-slate-400">Ctrl+Enter to render</span>
          </div>
          <div className="flex-1 min-h-[420px]">
            <Editor
              height="100%"
              language="html"
              value={userCode}
              onChange={(val) => {
                onChange(val || '');
              }}
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

        {/* Live Preview Panel */}
        <div
          className={`flex flex-col h-full bg-slate-50 ${
            activeTab === 'code' ? 'hidden' : activeTab === 'preview' ? 'col-span-2' : ''
          }`}
        >
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span className="flex items-center gap-1.5">
              <Eye className="w-3.5 h-3.5 text-emerald-600" />
              Live Webpage Sandbox
            </span>
            <span className="text-[11px] text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
              Isolated DOM Preview
            </span>
          </div>

          <div className="flex-1 bg-white p-3 min-h-[300px]">
            <iframe
              ref={iframeRef}
              title="Practice Sandbox Preview"
              srcDoc={`<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      body {
        margin: 0;
        padding: 14px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #1e293b;
        background-color: #ffffff;
      }
      * { box-sizing: border-box; }
    </style>
  </head>
  <body>
    ${previewContent}
  </body>
</html>`}
              sandbox="allow-scripts"
              className="w-full h-full min-h-[300px] border border-slate-200 rounded-lg bg-white shadow-inner"
            />
          </div>

          {/* Requirements & Validation Checklist */}
          {validationResults.length > 0 && (
            <div className="p-3 bg-white border-t border-slate-200">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                  Requirements Checklist
                </span>
                <span
                  className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${
                    allPassed ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                  }`}
                >
                  {validationResults.filter((r) => r.passed).length} / {validationResults.length} Met
                </span>
              </div>
              <ul className="space-y-1.5 text-xs">
                {validationResults.map((result, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    {result.passed ? (
                      <Check className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                    ) : (
                      <AlertCircle className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
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
                      Outstanding! All structural requirements satisfied.
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
