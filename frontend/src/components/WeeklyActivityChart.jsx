import React from 'react';
import { BarChart3 } from 'lucide-react';

const WeeklyActivityChart = ({ data = [] }) => {
  // data: array of { day: 'Mon', date: '...', submissions: N, solved: N }
  const maxVal = Math.max(...data.map(d => d.submissions), 4);

  return (
    <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex flex-col justify-between">
      <div className="flex items-center justify-between pb-4 border-b border-slate-100">
        <div className="flex items-center gap-2">
          <BarChart3 className="w-5 h-5 text-emerald-600" />
          <h3 className="font-bold text-slate-900 text-base">Weekly Activity</h3>
        </div>
        <div className="flex items-center gap-4 text-xs font-medium text-slate-500">
          <span className="flex items-center gap-1.5">
            <span className="w-3 h-3 rounded bg-emerald-600" /> Submissions
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-3 h-3 rounded bg-emerald-300" /> Solved
          </span>
        </div>
      </div>

      <div className="mt-6 flex items-end justify-between gap-2 h-44 px-2">
        {data.map((item, idx) => {
          const subHeight = Math.max((item.submissions / maxVal) * 100, item.submissions > 0 ? 8 : 4);
          const solHeight = Math.max((item.solved / maxVal) * 100, item.solved > 0 ? 8 : 4);

          return (
            <div key={item.date || idx} className="flex-1 flex flex-col items-center gap-2 group">
              <div className="w-full flex items-end justify-center gap-1 h-36 relative">
                {/* Tooltip */}
                <div className="absolute -top-10 opacity-0 group-hover:opacity-100 transition-opacity bg-slate-900 text-white text-[10px] py-1 px-2 rounded pointer-events-none whitespace-nowrap z-20">
                  {item.day}: {item.submissions} sub, {item.solved} solved
                </div>

                {/* Submissions Bar */}
                <div
                  style={{ height: `${subHeight}%` }}
                  className={`w-3.5 sm:w-4 rounded-t-md transition-all duration-300 group-hover:brightness-110 ${
                    item.submissions > 0 ? 'bg-emerald-600' : 'bg-slate-100'
                  }`}
                />

                {/* Solved Bar */}
                <div
                  style={{ height: `${solHeight}%` }}
                  className={`w-3.5 sm:w-4 rounded-t-md transition-all duration-300 group-hover:brightness-110 ${
                    item.solved > 0 ? 'bg-emerald-300' : 'bg-slate-100'
                  }`}
                />
              </div>

              <span className="text-xs font-semibold text-slate-500 group-hover:text-emerald-700">
                {item.day}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default WeeklyActivityChart;
