import React, { useState } from 'react';
import { Code2, Eye, Copy, Check, Info, Sparkles, Terminal } from 'lucide-react';

export default function ExampleViewer({ example }) {
  const [copied, setCopied] = useState(false);
  const [activeTab, setActiveTab] = useState('both'); // 'both' | 'code' | 'preview'

  const handleCopy = () => {
    navigator.clipboard.writeText(example.code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-6">
      {/* Header Overview Card */}
      <div className="p-6 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div className="flex flex-wrap items-center justify-between gap-3 mb-2">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">
            <Sparkles className="w-3.5 h-3.5" /> Working Production Example
          </div>
          <span className="text-xs text-slate-500 font-mono">
            Format: {example.language?.toUpperCase() || 'CODE'}
          </span>
        </div>
        <h2 className="text-xl font-black text-slate-900 tracking-tight">{example.title}</h2>
        <p className="mt-2 text-sm text-slate-600 leading-relaxed">{example.description}</p>
      </div>

      {/* Code & Live Preview Split */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        {/* Toolbar */}
        <div className="bg-slate-100/90 px-4 py-2.5 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <button
              onClick={() => setActiveTab('both')}
              className={`px-3 py-1 rounded-md text-xs font-semibold transition ${
                activeTab === 'both' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Side-by-Side
            </button>
            <button
              onClick={() => setActiveTab('code')}
              className={`px-3 py-1 rounded-md text-xs font-semibold transition ${
                activeTab === 'code' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Code Only
            </button>
            <button
              onClick={() => setActiveTab('preview')}
              className={`px-3 py-1 rounded-md text-xs font-semibold transition ${
                activeTab === 'preview' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Output Preview Only
            </button>
          </div>

          <button
            onClick={handleCopy}
            className="flex items-center gap-1.5 px-3 py-1 bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 rounded-lg text-xs font-bold shadow-xs transition"
          >
            {copied ? (
              <>
                <Check className="w-3.5 h-3.5 text-emerald-600" />
                <span className="text-emerald-700">Copied to Clipboard</span>
              </>
            ) : (
              <>
                <Copy className="w-3.5 h-3.5 text-slate-500" />
                <span>Copy Example Code</span>
              </>
            )}
          </button>
        </div>

        {/* Display Panels */}
        <div className="grid grid-cols-1 lg:grid-cols-2 divide-y lg:divide-y-0 lg:divide-x divide-slate-200 min-h-[440px]">
          {/* Example Code */}
          <div className={`flex flex-col ${activeTab === 'preview' ? 'hidden' : activeTab === 'code' ? 'col-span-2' : ''}`}>
            <div className="bg-slate-900 text-slate-400 px-4 py-2 text-xs font-mono border-b border-slate-800 flex items-center justify-between">
              <span className="flex items-center gap-1.5 text-slate-200">
                <Code2 className="w-3.5 h-3.5 text-emerald-400" />
                Source Implementation
              </span>
              <span>{example.language || 'html'}</span>
            </div>
            <pre className="flex-1 p-4 bg-slate-950 text-slate-100 font-mono text-xs leading-relaxed overflow-x-auto m-0">
              <code className="text-emerald-300">{example.code}</code>
            </pre>
          </div>

          {/* Visual Output / Live Preview */}
          <div className={`flex flex-col bg-slate-50 ${activeTab === 'code' ? 'hidden' : activeTab === 'preview' ? 'col-span-2' : ''}`}>
            <div className="bg-slate-100 px-4 py-2 text-xs font-semibold text-slate-700 border-b border-slate-200 flex items-center justify-between">
              <span className="flex items-center gap-1.5">
                <Eye className="w-3.5 h-3.5 text-emerald-600" />
                Rendered Webpage Output
              </span>
              <span className="text-[11px] text-emerald-700 bg-emerald-100/60 px-2 py-0.5 rounded font-bold">
                Live Output
              </span>
            </div>

            <div className="flex-1 p-4 flex items-center justify-center bg-white min-h-[360px]">
              {example.previewHtml ? (
                <div
                  className="w-full h-full min-h-[340px] flex items-center justify-center"
                  dangerouslySetInnerHTML={{ __html: example.previewHtml }}
                />
              ) : (
                <div className="text-slate-400 text-xs italic text-center p-6">
                  Interactive preview container
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Line-by-Line Explanation Card */}
      {example.explanation && (
        <div className="p-6 bg-white rounded-2xl border border-slate-200 shadow-xs">
          <div className="flex items-center gap-2 mb-3">
            <Info className="w-5 h-5 text-emerald-600" />
            <h3 className="text-base font-bold text-slate-900">
              Deep Dive: Line-by-Line Explanation of Critical Sections
            </h3>
          </div>
          <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs text-slate-700 font-mono whitespace-pre-wrap leading-relaxed">
            {example.explanation}
          </div>
        </div>
      )}
    </div>
  );
}
