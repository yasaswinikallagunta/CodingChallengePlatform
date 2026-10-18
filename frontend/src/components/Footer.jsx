import React from 'react';
import { Code2, Heart, ShieldCheck, Terminal } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-white border-t border-slate-200 mt-auto py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2 text-slate-800">
            <div className="w-7 h-7 rounded-lg bg-emerald-600 text-white flex items-center justify-center">
              <Code2 className="w-4 h-4" />
            </div>
            <span className="font-bold text-sm tracking-tight">
              Coding Challenge Platform
            </span>
            <span className="text-xs text-slate-600">
              — Master Algorithms, Data Structures & Systems
            </span>
          </div>

          <div className="flex items-center gap-6 text-xs text-slate-600">
            <span className="flex items-center gap-1">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" /> Sandboxed Execution
            </span>
            <span className="flex items-center gap-1">
              <Terminal className="w-3.5 h-3.5 text-emerald-600" /> Multiple Language Compilers
            </span>
            <span>&copy; {new Date().getFullYear()} All rights reserved.</span>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
