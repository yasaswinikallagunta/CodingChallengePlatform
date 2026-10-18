import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { 
  Search, 
  Filter, 
  CheckCircle2, 
  ChevronRight, 
  ChevronLeft, 
  TerminalSquare, 
  Code2, 
  Layers, 
  SlidersHorizontal,
  Flame,
  ArrowUpDown,
  BookOpen
} from 'lucide-react';

const CATEGORIES = [
  'All',
  'Python',
  'C',
  'C++',
  'Java',
  'JavaScript',
  'Data Structures',
  'Algorithms',
  'SQL',
];

const DIFFICULTIES = ['All', 'Easy', 'Medium', 'Hard'];

const STATUSES = [
  { label: 'All Statuses', value: 'all' },
  { label: 'Solved Only', value: 'solved' },
  { label: 'Unsolved Only', value: 'unsolved' },
];

const SORT_OPTIONS = [
  { label: 'Default (ID)', value: 'id' },
  { label: 'Points: Low to High', value: 'points_asc' },
  { label: 'Points: High to Low', value: 'points_desc' },
  { label: 'Title (A-Z)', value: 'title_asc' },
  { label: 'Difficulty (Easy → Hard)', value: 'difficulty' },
];

const PAGE_SIZE_OPTIONS = [10, 20, 50, 100];

const ProblemsListPage = () => {
  const [problems, setProblems] = useState([]);
  const [totalCount, setTotalCount] = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(20);
  const [loading, setLoading] = useState(true);

  // Filters
  const [search, setSearch] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [selectedStatus, setSelectedStatus] = useState('all');
  const [selectedSort, setSelectedSort] = useState('id');

  const fetchProblems = async (page = 1) => {
    setLoading(true);
    try {
      const params = {
        page,
        page_size: pageSize,
        search: search.trim(),
        category: selectedCategory === 'All' ? '' : selectedCategory,
        difficulty: selectedDifficulty === 'All' ? '' : selectedDifficulty,
        status: selectedStatus === 'all' ? '' : selectedStatus,
        sort: selectedSort,
      };

      const res = await api.get('/problems/', { params });
      setProblems(res.data.results || []);
      setTotalCount(res.data.count || 0);
      setTotalPages(res.data.total_pages || 1);
      setCurrentPage(res.data.page || 1);
    } catch (err) {
      console.error("Error fetching problems:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const timer = setTimeout(() => {
      fetchProblems(1);
    }, 250);
    return () => clearTimeout(timer);
  }, [search, selectedCategory, selectedDifficulty, selectedStatus, selectedSort, pageSize]);

  const handlePageChange = (newPage) => {
    if (newPage >= 1 && newPage <= totalPages) {
      fetchProblems(newPage);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      {/* Page Title & Stats */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-200">
        <div>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center shadow-md shadow-emerald-600/20">
              <TerminalSquare className="w-6 h-6" />
            </div>
            <div>
              <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
                Coding Challenges
              </h1>
              <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
                Displaying {totalCount} verified algorithmic problems across Easy, Medium, and Hard tiers.
              </p>
            </div>
          </div>
        </div>

        {/* Search input */}
        <div className="relative w-full md:w-80">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
          <input
            type="text"
            placeholder="Search 500 problems, algorithms..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent bg-white shadow-sm transition"
          />
        </div>
      </div>

      {/* Filter Toolbar */}
      <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-4">
        {/* Category Pills */}
        <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider shrink-0 mr-1 flex items-center gap-1">
            <Layers className="w-3.5 h-3.5" /> Category:
          </span>
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold shrink-0 transition ${
                selectedCategory === cat
                  ? 'bg-emerald-600 text-white shadow-sm shadow-emerald-600/20'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Dropdowns Row: Difficulty, Status, Sorting, Page Size */}
        <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 pt-3 border-t border-slate-100">
          {/* Difficulty */}
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-500 shrink-0">Difficulty:</span>
            <select
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value)}
              className="w-full py-1.5 px-3 rounded-lg border border-slate-200 text-xs font-bold text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              {DIFFICULTIES.map((d) => (
                <option key={d} value={d}>{d}</option>
              ))}
            </select>
          </div>

          {/* Solved Status */}
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-500 shrink-0">Status:</span>
            <select
              value={selectedStatus}
              onChange={(e) => setSelectedStatus(e.target.value)}
              className="w-full py-1.5 px-3 rounded-lg border border-slate-200 text-xs font-bold text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              {STATUSES.map((s) => (
                <option key={s.value} value={s.value}>{s.label}</option>
              ))}
            </select>
          </div>

          {/* Sort */}
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-500 shrink-0 flex items-center gap-1">
              <ArrowUpDown className="w-3 h-3" /> Sort:
            </span>
            <select
              value={selectedSort}
              onChange={(e) => setSelectedSort(e.target.value)}
              className="w-full py-1.5 px-3 rounded-lg border border-slate-200 text-xs font-bold text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              {SORT_OPTIONS.map((o) => (
                <option key={o.value} value={o.value}>{o.label}</option>
              ))}
            </select>
          </div>

          {/* Page Size */}
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-500 shrink-0">Per Page:</span>
            <select
              value={pageSize}
              onChange={(e) => setPageSize(Number(e.target.value))}
              className="w-full py-1.5 px-3 rounded-lg border border-slate-200 text-xs font-bold text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              {PAGE_SIZE_OPTIONS.map((sz) => (
                <option key={sz} value={sz}>{sz} problems</option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Problems Table / List */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        {loading ? (
          <div className="p-12 text-center">
            <div className="inline-block w-8 h-8 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mb-3" />
            <p className="text-sm font-semibold text-slate-500">Loading challenges...</p>
          </div>
        ) : problems.length === 0 ? (
          <div className="p-16 text-center">
            <div className="w-12 h-12 rounded-full bg-slate-100 text-slate-400 flex items-center justify-center mx-auto mb-3">
              <Search className="w-6 h-6" />
            </div>
            <h3 className="font-bold text-slate-800 text-base">No challenges found</h3>
            <p className="text-xs text-slate-500 mt-1 max-w-sm mx-auto">
              No problems match your current search and filter combination.
            </p>
            <button
              onClick={() => {
                setSearch('');
                setSelectedCategory('All');
                setSelectedDifficulty('All');
                setSelectedStatus('all');
                setSelectedSort('id');
              }}
              className="mt-4 px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-xs font-bold text-slate-700 transition"
            >
              Reset Filters
            </button>
          </div>
        ) : (
          <div className="divide-y divide-slate-100">
            {problems.map((prob) => {
              const isEasy = prob.difficulty === 'Easy';
              const isMed = prob.difficulty === 'Medium';

              return (
                <div
                  key={prob.id}
                  className="p-4 sm:p-5 hover:bg-slate-50/80 transition flex flex-col sm:flex-row sm:items-center justify-between gap-4 group"
                >
                  <div className="flex items-start sm:items-center gap-3.5">
                    {/* Status checkmark / ID */}
                    <div className="mt-0.5 sm:mt-0 shrink-0">
                      {prob.is_solved ? (
                        <div className="w-7 h-7 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center" title="Solved">
                          <CheckCircle2 className="w-4 h-4" />
                        </div>
                      ) : prob.is_attempted ? (
                        <div className="w-7 h-7 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center text-xs font-bold" title="Attempted">
                          •
                        </div>
                      ) : (
                        <div className="w-7 h-7 rounded-full border border-slate-200 text-slate-400 flex items-center justify-center text-[11px] font-semibold" title="Unattempted">
                          #{prob.id}
                        </div>
                      )}
                    </div>

                    <div>
                      <div className="flex flex-wrap items-center gap-2 mb-1">
                        <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                          isEasy ? 'bg-emerald-100 text-emerald-800' :
                          isMed ? 'bg-amber-100 text-amber-800' :
                          'bg-rose-100 text-rose-800'
                        }`}>
                          {prob.difficulty}
                        </span>
                        <span className="text-xs font-semibold text-slate-500">
                          {prob.category}
                        </span>
                        <span className="text-xs font-bold text-emerald-600">
                          +{prob.points} pts
                        </span>
                      </div>
                      <Link
                        to={`/workspace/${prob.slug}`}
                        className="font-bold text-slate-900 group-hover:text-emerald-700 transition text-base block"
                      >
                        {prob.title}
                      </Link>
                    </div>
                  </div>

                  {/* Action button */}
                  <div className="flex items-center gap-3 shrink-0">
                    <Link
                      to={`/workspace/${prob.slug}`}
                      className={`px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                        prob.is_solved
                          ? 'bg-slate-100 hover:bg-slate-200 text-slate-700'
                          : 'bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm shadow-emerald-600/20'
                      }`}
                    >
                      <span>{prob.is_solved ? 'Practice Again' : 'Solve Challenge'}</span>
                      <ChevronRight className="w-3.5 h-3.5" />
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* Pagination Bar */}
        {totalPages > 1 && (
          <div className="p-4 bg-slate-50 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs font-semibold text-slate-600">
            <span>
              Showing Page <span className="font-bold text-slate-900">{currentPage}</span> of{' '}
              <span className="font-bold text-slate-900">{totalPages}</span> ({totalCount} total challenges)
            </span>
            
            <div className="flex items-center gap-1">
              <button
                disabled={currentPage <= 1}
                onClick={() => handlePageChange(1)}
                className="px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-100 disabled:opacity-40 transition text-[11px]"
              >
                First
              </button>
              <button
                disabled={currentPage <= 1}
                onClick={() => handlePageChange(currentPage - 1)}
                className="p-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-100 disabled:opacity-40 transition"
                title="Previous Page"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>

              <span className="px-3 py-1 font-bold text-emerald-800 bg-emerald-100 rounded-lg">
                {currentPage}
              </span>

              <button
                disabled={currentPage >= totalPages}
                onClick={() => handlePageChange(currentPage + 1)}
                className="p-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-100 disabled:opacity-40 transition"
                title="Next Page"
              >
                <ChevronRight className="w-4 h-4" />
              </button>
              <button
                disabled={currentPage >= totalPages}
                onClick={() => handlePageChange(totalPages)}
                className="px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-100 disabled:opacity-40 transition text-[11px]"
              >
                Last
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProblemsListPage;
