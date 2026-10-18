import React, { useState, useEffect } from 'react';
import { Code, Terminal, Cpu, Sparkles, ChevronRight } from 'lucide-react';

const AnimatedIntro = ({ onComplete }) => {
  const [stage, setStage] = useState(1);
  const [fadeExit, setFadeExit] = useState(false);

  useEffect(() => {
    // Stage 1: Initial lighting and symbols
    // Stage 2: Title reveal (1.2s)
    const t1 = setTimeout(() => setStage(2), 1100);
    // Stage 3: Tagline & Progress bar start (2.3s)
    const t2 = setTimeout(() => setStage(3), 2200);
    // Stage 4: Fade out start (4.6s)
    const t3 = setTimeout(() => setFadeExit(true), 4600);
    // Complete intro at 5.0s
    const t4 = setTimeout(() => {
      sessionStorage.setItem('ccp_has_seen_intro', 'true');
      onComplete();
    }, 5100);

    return () => {
      clearTimeout(t1);
      clearTimeout(t2);
      clearTimeout(t3);
      clearTimeout(t4);
    };
  }, [onComplete]);

  const handleSkip = () => {
    sessionStorage.setItem('ccp_has_seen_intro', 'true');
    setFadeExit(true);
    setTimeout(() => onComplete(), 300);
  };

  return (
    <div
      className={`fixed inset-0 z-50 flex flex-col items-center justify-center bg-white transition-opacity duration-700 select-none overflow-hidden ${
        fadeExit ? 'opacity-0 pointer-events-none' : 'opacity-100'
      }`}
    >
      {/* Background radial lighting */}
      <div className="absolute w-[600px] h-[600px] rounded-full bg-emerald-100/40 blur-[120px] pointer-events-none animate-pulse-subtle" />
      <div className="absolute -top-24 -left-24 w-80 h-80 rounded-full bg-green-50 blur-[90px] pointer-events-none" />
      <div className="absolute -bottom-24 -right-24 w-80 h-80 rounded-full bg-green-50 blur-[90px] pointer-events-none" />

      {/* Skip button */}
      <button
        onClick={handleSkip}
        className="absolute top-6 right-8 text-xs font-semibold text-slate-400 hover:text-emerald-600 transition flex items-center gap-1 px-3 py-1.5 rounded-full border border-slate-200 hover:border-emerald-300 bg-white/80"
      >
        Skip Intro <ChevronRight className="w-3.5 h-3.5" />
      </button>

      {/* Floating programming symbols */}
      <div className="relative flex flex-col items-center max-w-xl mx-auto px-6 text-center z-10">
        <div className="flex items-center justify-center gap-4 mb-8">
          <div className="w-12 h-12 rounded-2xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 shadow-sm animate-float-soft">
            <span className="font-mono font-bold text-lg">&lt;/&gt;</span>
          </div>
          <div className="w-14 h-14 rounded-2xl bg-emerald-600 text-white flex items-center justify-center shadow-lg shadow-emerald-600/25 scale-105">
            <Terminal className="w-7 h-7" />
          </div>
          <div className="w-12 h-12 rounded-2xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 shadow-sm animate-float-soft" style={{ animationDelay: '1s' }}>
            <span className="font-mono font-bold text-lg">&#123; &#125;</span>
          </div>
        </div>

        {/* Ambient floating bits */}
        <div className="absolute -top-12 -left-16 text-emerald-500/30 font-mono text-sm tracking-widest font-bold select-none">
          010101
        </div>
        <div className="absolute -bottom-8 -right-12 text-emerald-500/30 font-mono text-sm tracking-widest font-bold select-none">
          101010
        </div>

        {/* Platform Title */}
        <div
          className={`transition-all duration-700 transform ${
            stage >= 2
              ? 'translate-y-0 opacity-100 scale-100'
              : 'translate-y-4 opacity-0 scale-95'
          }`}
        >
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 border border-emerald-200/60 text-emerald-700 text-xs font-semibold tracking-wide uppercase mb-3">
            <Sparkles className="w-3 h-3 text-emerald-600" /> Professional SaaS Platform
          </div>
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight text-slate-900 leading-tight">
            CODING CHALLENGE <span className="text-emerald-600">PLATFORM</span>
          </h1>
        </div>

        {/* Tagline */}
        <div
          className={`mt-4 transition-all duration-700 delay-100 transform ${
            stage >= 3
              ? 'translate-y-0 opacity-100'
              : 'translate-y-4 opacity-0'
          }`}
        >
          <p className="text-base sm:text-lg font-medium text-slate-600">
            Code. Practice. Improve. Achieve.
          </p>
        </div>

        {/* Animated Green Progress Line */}
        <div className="w-64 h-1.5 bg-slate-100 rounded-full mt-8 overflow-hidden relative">
          <div className="h-full bg-gradient-to-r from-emerald-500 to-green-600 rounded-full animate-progress-sweep" />
        </div>
      </div>
    </div>
  );
};

export default AnimatedIntro;
