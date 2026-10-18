import React from 'react';
import { Calendar } from 'lucide-react';

const ActivityHeatmap = ({ data = [] }) => {
  // data: array of { date: 'YYYY-MM-DD', count: N }
  const getColor = (count) => {
    if (count === 0) return 'bg-slate-100 border-slate-200/60';
    if (count <= 2) return 'bg-emerald-200 border-emerald-300';
    if (count <= 4) return 'bg-emerald-400 border-emerald-500';
    return 'bg-emerald-600 border-emerald-700';
  };

  const totalSubmissions = data.reduce((acc, curr) => acc + (curr.count || 0), 0);

  return (
    <div className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-4 border-b border-slate-100 gap-2">
        <div className="flex items-center gap-2">
          <Calendar className="w-5 h-5 text-emerald-600" />
          <h3 className="font-bold text-slate-900 text-base">Coding Activity Heatmap</h3>
        </div>
        <div className="text-xs font-semibold text-slate-500">
          <span className="font-bold text-emerald-600">{totalSubmissions}</span> submissions in past 60 days
        </div>
      </div>

      <div className="mt-5 overflow-x-auto pb-2">
        <div className="flex gap-1.5 min-w-[500px]">
          {data.map((item, idx) => (
            <div
              key={item.date || idx}
              title={`${item.date}: ${item.count} submission${item.count === 1 ? '' : 's'}`}
              className={`w-3.5 h-3.5 sm:w-4 sm:h-4 rounded-sm border transition-transform hover:scale-125 cursor-pointer ${getColor(
                item.count
              )}`}
            />
          ))}
        </div>
      </div>

      {/* Legend */}
      <div className="mt-4 flex items-center justify-between text-xs text-slate-600 pt-3 border-t border-slate-100">
        <span>Past 60 Days</span>
        <div className="flex items-center gap-2">
          <span>Less</span>
          <div className="w-3 h-3 rounded-sm bg-slate-100 border border-slate-200" />
          <div className="w-3 h-3 rounded-sm bg-emerald-200 border border-emerald-300" />
          <div className="w-3 h-3 rounded-sm bg-emerald-400 border border-emerald-500" />
          <div className="w-3 h-3 rounded-sm bg-emerald-600 border border-emerald-700" />
          <span>More</span>
        </div>
      </div>
    </div>
  );
};

export default ActivityHeatmap;
