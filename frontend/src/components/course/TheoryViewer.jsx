import React, { useState } from 'react';
import { BookOpen, Copy, Check, Info, Lightbulb, Sparkles, CheckCircle2 } from 'lucide-react';

export default function TheoryViewer({ topic }) {
  const [copiedIndex, setCopiedIndex] = useState(null);

  const handleCopy = (code, index) => {
    navigator.clipboard.writeText(code);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="space-y-8">
      {/* Topic Subtopics Pill Header */}
      <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div className="flex items-center gap-2 mb-3">
          <BookOpen className="w-5 h-5 text-emerald-600" />
          <h3 className="text-sm font-bold text-slate-900 uppercase tracking-wider">
            Syllabus Subtopics Covered
          </h3>
        </div>
        <div className="flex flex-wrap gap-2">
          {topic.subtopics.map((subtopic, index) => (
            <span
              key={index}
              className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-emerald-50 text-emerald-800 border border-emerald-200/60"
            >
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
              {subtopic}
            </span>
          ))}
        </div>
      </div>

      {/* Main Theory Articles */}
      <div className="space-y-6">
        {topic.theory.map((section, idx) => (
          <div
            key={idx}
            className="p-6 bg-white rounded-2xl border border-slate-200 shadow-xs hover:border-slate-300 transition-colors"
          >
            <h2 className="text-xl font-black text-slate-900 mb-4 pb-2 border-b border-slate-100 flex items-center justify-between">
              <span>{section.title}</span>
              <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-600">
                Part {idx + 1}
              </span>
            </h2>

            <div className="prose prose-slate max-w-none text-sm text-slate-700 leading-relaxed space-y-4">
              {renderFormattedContent(section.content, idx, handleCopy, copiedIndex)}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// Helper to render markdown-like content cleanly with code blocks and alerts
function renderFormattedContent(content, sectionIdx, handleCopy, copiedIndex) {
  // Split on code fences ```...```
  const parts = content.split(/(```[\s\S]*?```)/g);

  return parts.map((part, pIdx) => {
    if (part.startsWith('```')) {
      const match = part.match(/^```(\w+)?\n([\s\S]*?)```$/);
      const lang = match ? match[1] || 'code' : 'code';
      const code = match ? match[2] : part.slice(3, -3);
      const copyKey = `${sectionIdx}-${pIdx}`;

      return (
        <div key={pIdx} className="my-4 rounded-xl overflow-hidden border border-slate-700 bg-slate-900 text-slate-100">
          <div className="bg-slate-800 px-4 py-1.5 flex items-center justify-between border-b border-slate-700 text-xs font-mono text-slate-400">
            <span>{lang.toUpperCase()}</span>
            <button
              onClick={() => handleCopy(code, copyKey)}
              className="flex items-center gap-1 text-slate-300 hover:text-white transition px-2 py-0.5 rounded hover:bg-slate-700"
            >
              {copiedIndex === copyKey ? (
                <>
                  <Check className="w-3.5 h-3.5 text-emerald-400" />
                  <span className="text-emerald-400">Copied</span>
                </>
              ) : (
                <>
                  <Copy className="w-3.5 h-3.5" />
                  <span>Copy</span>
                </>
              )}
            </button>
          </div>
          <pre className="p-4 text-xs font-mono leading-relaxed overflow-x-auto text-emerald-300">
            <code>{code}</code>
          </pre>
        </div>
      );
    }

    // Process headings, lists, bold text
    const paragraphs = part.split('\n\n').filter((p) => p.trim().length > 0);
    return (
      <React.Fragment key={pIdx}>
        {paragraphs.map((para, paraIdx) => {
          if (para.startsWith('### ')) {
            return (
              <h4 key={paraIdx} className="text-base font-bold text-slate-900 mt-4 mb-2">
                {para.replace('### ', '')}
              </h4>
            );
          }
          if (para.startsWith('## ')) {
            return (
              <h3 key={paraIdx} className="text-lg font-bold text-slate-900 mt-5 mb-2">
                {para.replace('## ', '')}
              </h3>
            );
          }
          if (para.startsWith('- ') || para.startsWith('* ')) {
            const items = para.split('\n').filter((l) => l.trim().startsWith('- ') || l.trim().startsWith('* '));
            return (
              <ul key={paraIdx} className="space-y-1.5 my-2 pl-2">
                {items.map((item, itemIdx) => (
                  <li key={itemIdx} className="flex items-start gap-2 text-slate-700">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-600 mt-2 shrink-0" />
                    <span>{renderInlineFormatting(item.replace(/^[-*]\s+/, ''))}</span>
                  </li>
                ))}
              </ul>
            );
          }
          if (para.startsWith('> ')) {
            return (
              <blockquote
                key={paraIdx}
                className="p-3 my-3 bg-emerald-50/60 border-l-4 border-emerald-500 rounded-r-lg text-emerald-900 text-xs italic"
              >
                {para.replace(/^>\s+/, '')}
              </blockquote>
            );
          }
          return (
            <p key={paraIdx} className="leading-relaxed">
              {renderInlineFormatting(para)}
            </p>
          );
        })}
      </React.Fragment>
    );
  });
}

function renderInlineFormatting(text) {
  const parts = text.split(/(`[^`]+`|\*\*[^*]+\*\*)/g);
  return parts.map((seg, idx) => {
    if (seg.startsWith('`') && seg.endsWith('`')) {
      return (
        <code key={idx} className="px-1.5 py-0.5 rounded bg-slate-100 text-emerald-700 font-mono text-[13px] font-semibold border border-slate-200">
          {seg.slice(1, -1)}
        </code>
      );
    }
    if (seg.startsWith('**') && seg.endsWith('**')) {
      return (
        <strong key={idx} className="font-bold text-slate-900">
          {seg.slice(2, -2)}
        </strong>
      );
    }
    return seg;
  });
}
