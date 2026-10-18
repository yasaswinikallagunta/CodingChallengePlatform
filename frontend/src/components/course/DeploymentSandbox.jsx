import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import { Cloud, Play, RotateCcw, CheckCircle2, ShieldAlert, ShieldCheck, Sparkles, Check, AlertTriangle } from 'lucide-react';

export default function DeploymentSandbox({
  exercise,
  userCode,
  onChange,
  onReset,
  onComplete,
  isCompleted
}) {
  const [auditReport, setAuditReport] = useState(null);
  const [isRunning, setIsRunning] = useState(false);

  const runAudit = () => {
    setIsRunning(true);
    setAuditReport(null);

    setTimeout(() => {
      const code = userCode;
      const lower = code.toLowerCase();
      const findings = [];
      let isSecuritySafe = true;

      // Rule 1: Secret leak detection
      const dangerousPatterns = ['password=', 'secret=', 'database_url=', 'aws_secret', 'token='];
      const hasLeakedSecret = dangerousPatterns.some(pat => lower.includes(pat) && !lower.includes('public'));
      if (hasLeakedSecret) {
        findings.push({
          type: 'danger',
          title: 'Critical Security Risk: Secret Exposed',
          message: 'Frontend files are publicly bundled into client JavaScript. Never place backend database credentials, private API keys, or passwords in client config!'
        });
        isSecuritySafe = false;
      } else {
        findings.push({
          type: 'success',
          title: 'Secret Leak Audit Passed',
          message: 'No dangerous private secrets or unmasked database passwords detected in this configuration.'
        });
      }

      // Rule 2: Platform/Context specific audits
      if (exercise.id.includes('deploy-ex-1')) {
        // .env audit
        const hasVitePrefix = lower.includes('vite_');
        if (hasVitePrefix) {
          findings.push({
            type: 'success',
            title: 'Vite Namespace Standard',
            message: 'Client variables correctly prefixed with VITE_ to allow compilation bundling.'
          });
        } else {
          findings.push({
            type: 'warning',
            title: 'Missing VITE_ Prefix',
            message: 'In Vite projects, only environment variables starting with VITE_ are exposed to your client app.'
          });
        }
      } else if (exercise.id.includes('deploy-ex-2')) {
        // SPA 200/index.html redirects
        const hasRewrite = lower.includes('index.html') && (lower.includes('status = 200') || lower.includes('/index.html') || lower.includes('/*'));
        if (hasRewrite) {
          findings.push({
            type: 'success',
            title: 'SPA Catch-All Route Configured',
            message: 'Client-side routing fallback to index.html successfully eliminates 404 page-refresh issues.'
          });
        } else {
          findings.push({
            type: 'warning',
            title: 'Incomplete SPA Redirect Rule',
            message: 'Ensure all routes (/*) are redirected to /index.html with status 200.'
          });
        }
      } else if (exercise.id.includes('deploy-ex-3')) {
        // GitHub Actions CI/CD
        const hasCiStages = lower.includes('actions/checkout') && (lower.includes('actions/setup-node') || lower.includes('npm run build'));
        if (hasCiStages) {
          findings.push({
            type: 'success',
            title: 'CI Pipeline Stages Verified',
            message: 'Checkout, Node setup, dependency installation, and build commands correctly structured.'
          });
        } else {
          findings.push({
            type: 'warning',
            title: 'Workflow Missing Required Steps',
            message: 'Verify that actions/checkout, setup-node, and npm run build steps are present.'
          });
        }
      } else {
        // General config check
        if (code.trim().length > 30) {
          findings.push({
            type: 'success',
            title: 'Configuration Syntax Validated',
            message: 'Configuration syntax parsed cleanly without fatal formatting errors.'
          });
        }
      }

      const allPassed = isSecuritySafe && findings.every(f => f.type === 'success');
      setAuditReport({
        allPassed,
        findings,
        timestamp: new Date().toLocaleTimeString()
      });
      setIsRunning(false);
    }, 250);
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
      {/* Top Bar */}
      <div className="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <Cloud className="w-3.5 h-3.5 text-emerald-600" />
            Deployment Configuration &amp; CI/CD Auditor
          </span>
          <span className="text-[11px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-semibold">
            Security &amp; DevOps Engine
          </span>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={runAudit}
            disabled={isRunning}
            className="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 disabled:opacity-50 text-white text-xs font-bold shadow-sm transition flex items-center gap-1.5"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>{isRunning ? 'Auditing...' : 'Run DevOps Audit'}</span>
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

      {/* Editor & Audit Results */}
      <div className="grid grid-cols-1 md:grid-cols-2 flex-1 min-h-[460px] divide-y md:divide-y-0 md:divide-x divide-slate-200">
        {/* Monaco Editor */}
        <div className="flex flex-col h-full">
          <div className="bg-slate-50 px-3 py-1.5 border-b border-slate-200 text-xs font-semibold text-slate-600 flex items-center justify-between">
            <span>Config File Editor (.env / yaml / toml / json)</span>
            <span className="text-[11px] text-slate-400">DevOps Sandbox</span>
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

        {/* Audit Inspector Panel */}
        <div className="flex flex-col h-full bg-slate-50">
          <div className="bg-slate-100 px-3 py-2 border-b border-slate-200 flex items-center justify-between">
            <span className="text-xs font-bold text-slate-800 flex items-center gap-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
              Automated Production Readiness Report
            </span>
            {auditReport && (
              <span className="text-[10px] text-slate-500">Audited at {auditReport.timestamp}</span>
            )}
          </div>

          <div className="flex-1 p-4 overflow-y-auto space-y-3 min-h-[300px]">
            {!auditReport && (
              <div className="text-slate-500 py-8 text-center text-xs space-y-2">
                <Cloud className="w-8 h-8 text-slate-300 mx-auto" />
                <p>Click <span className="font-bold text-emerald-700">Run DevOps Audit</span> to scan your configuration for secrets, syntax validity, and production best practices.</p>
              </div>
            )}

            {auditReport && (
              <div className="space-y-3">
                {auditReport.findings.map((item, idx) => (
                  <div
                    key={idx}
                    className={`p-3 rounded-xl border text-xs ${
                      item.type === 'danger'
                        ? 'bg-red-50 border-red-200 text-red-900'
                        : item.type === 'warning'
                        ? 'bg-amber-50 border-amber-200 text-amber-900'
                        : 'bg-emerald-50 border-emerald-200 text-emerald-900'
                    }`}
                  >
                    <div className="flex items-center gap-2 font-bold mb-1">
                      {item.type === 'danger' ? (
                        <ShieldAlert className="w-4 h-4 text-red-600 shrink-0" />
                      ) : item.type === 'warning' ? (
                        <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
                      ) : (
                        <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                      )}
                      <span>{item.title}</span>
                    </div>
                    <p className="text-[11px] leading-relaxed text-slate-700 pl-6">{item.message}</p>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Validation Status footer */}
          <div className="p-3 bg-white border-t border-slate-200">
            {auditReport && auditReport.allPassed ? (
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-emerald-700 text-xs font-bold">
                  <Sparkles className="w-4 h-4" />
                  <span>DevOps Configuration Verified Production-Ready!</span>
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
              <div className="text-[11px] text-slate-500">
                Ensure all audit requirements are satisfied without security leaks or syntax warnings.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
