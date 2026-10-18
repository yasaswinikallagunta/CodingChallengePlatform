import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { 
  History, 
  Search, 
  Filter, 
  CheckCircle2, 
  XCircle, 
  Clock, 
  ChevronRight, 
  ChevronLeft, 
  Code2, 
  Eye, 
  X 
} from 'lucide-react';

const SubmissionsPage = () => {
  const [submissions, setSubmissions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [totalCount, setTotalCount] = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const [page, setPage] = useState(1);

  // Filters
  const [statusFilter, setStatusFilter] = useState('all');
  const [langFilter, setLangFilter] = useState('all');

  // Modal for viewing submitted code
  const [selectedSubmission, setSelectedSubmission] = useState(null);

  const fetchSubmissions = async (targetPage = 1) => {
    setLoading(true);
    try {
      const params = {
        page: targetPage,
        page_size: 10,
        status: statusFilter === 'all' ? '' : statusFilter,
        language: langFilter === 'all' ? '' : langFilter,
      };
      const res = await api.get('/submissions/', { params });
      setSubmissions(res.data.results || []);
      setTotalCount(res.data.count || 0);
      setTotalPages(res.data.total_pages || 1);
      setPage(res.data.page || 1);
    } catch (err) {
      console.error("Error loading submissions:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSubmissions(1);
  }, [statusFilter, langFilter]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200">
        <div>
          <h1 className="text-3xl font-black text-slate-900 tracking-tight flex items-center gap-3">
            <History className="w-8 h-8 text-emerald-600" />
            <span>Submission History</span>
          </h1>
          <p className="text-sm text-slate-500 mt-1">
            Review all your past code executions, evaluations, runtimes, and verdicts.
          </p>
        </div>

        {/* Filters */}
        <div className="flex items-center gap-3">
          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="py-2 px-3 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 bg-white focus:ring-2 focus:ring-emerald-500 shadow-sm"
          >
            <option value="all">All Verdicts</option>
            <option value="Accepted">Accepted</option>
            <option value="Wrong Answer">Wrong Answer</option>
            <option value="Runtime Error">Runtime Error</option>
            <option value="Compilation Error">Compilation Error</option>
          </select>

          <select
            value={langFilter}
            onChange={(e) => setLangFilter(e.target.value)}
            className="py-2 px-3 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 bg-white focus:ring-2 focus:ring-emerald-500 shadow-sm"
          >
            <option value="all">All Languages</option>
            <option value="python">Python</option>
            <option value="javascript">JavaScript</option>
            <option value="cpp">C++</option>
            <option value="c">C</option>
            <option value="java">Java</option>
            <option value="sql">SQL</option>
          </select>
        </div>
      </div>

      {/* Submissions Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        {loading ? (
          <div className="p-12 text-center">
            <div className="inline-block w-8 h-8 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mb-3" />
            <p className="text-sm font-semibold text-slate-500">Retrieving submission logs...</p>
          </div>
        ) : submissions.length === 0 ? (
          <div className="p-16 text-center">
            <div className="w-12 h-12 rounded-full bg-slate-100 text-slate-400 flex items-center justify-center mx-auto mb-3">
              <History className="w-6 h-6" />
            </div>
            <h3 className="font-bold text-slate-800 text-base">No submissions found</h3>
            <p className="text-xs text-slate-500 mt-1 max-w-sm mx-auto">
              You haven't submitted any code matching these filters yet.
            </p>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 uppercase font-bold text-[11px] tracking-wider">
                <tr>
                  <th className="py-3.5 px-4">Problem</th>
                  <th className="py-3.5 px-4">Verdict</th>
                  <th className="py-3.5 px-4">Language</th>
                  <th className="py-3.5 px-4">Test Cases</th>
                  <th className="py-3.5 px-4">Runtime</th>
                  <th className="py-3.5 px-4">Submitted At</th>
                  <th className="py-3.5 px-4 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 font-medium text-slate-700">
                {submissions.map((sub) => {
                  const isAccepted = sub.status === 'Accepted';
                  return (
                    <tr key={sub.id} className="hover:bg-slate-50/70 transition">
                      <td className="py-4 px-4 font-bold text-slate-900">
                        <Link to={`/workspace/${sub.problem_slug}`} className="hover:text-emerald-600 transition">
                          {sub.problem_title}
                        </Link>
                      </td>
                      <td className="py-4 px-4">
                        <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full font-bold text-[11px] ${
                          isAccepted
                            ? 'bg-emerald-100 text-emerald-800'
                            : 'bg-red-100 text-red-700'
                        }`}>
                          {isAccepted ? <CheckCircle2 className="w-3 h-3 text-emerald-600" /> : <XCircle className="w-3 h-3 text-red-500" />}
                          {sub.status}
                        </span>
                      </td>
                      <td className="py-4 px-4 font-mono font-semibold capitalize text-slate-600">
                        {sub.language}
                      </td>
                      <td className="py-4 px-4 font-semibold text-slate-600">
                        {sub.passed_test_cases} / {sub.total_test_cases} passed
                      </td>
                      <td className="py-4 px-4 text-slate-500">
                        {sub.execution_time != null ? `${sub.execution_time}s` : 'N/A'}
                      </td>
                      <td className="py-4 px-4 text-slate-500">
                        {new Date(sub.submitted_at).toLocaleString()}
                      </td>
                      <td className="py-4 px-4 text-right">
                        <button
                          onClick={() => setSelectedSubmission(sub)}
                          className="px-3 py-1.5 rounded-lg border border-slate-200 hover:border-emerald-300 hover:bg-emerald-50 text-slate-700 hover:text-emerald-700 font-semibold text-xs transition inline-flex items-center gap-1"
                        >
                          <Eye className="w-3.5 h-3.5" /> View Code
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}

        {/* Pagination Bar */}
        {totalPages > 1 && (
          <div className="p-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-slate-600">
            <span>
              Page {page} of {totalPages} ({totalCount} total submissions)
            </span>
            <div className="flex items-center gap-2">
              <button
                disabled={page <= 1}
                onClick={() => fetchSubmissions(page - 1)}
                className="p-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-100 disabled:opacity-40 transition"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>
              <button
                disabled={page >= totalPages}
                onClick={() => fetchSubmissions(page + 1)}
                className="p-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-100 disabled:opacity-40 transition"
              >
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Code Viewer Modal */}
      {selectedSubmission && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
          <div className="bg-white rounded-3xl max-w-2xl w-full max-h-[85vh] overflow-hidden flex flex-col shadow-2xl border border-slate-200">
            <div className="p-5 border-b border-slate-200 flex items-center justify-between bg-slate-50">
              <div>
                <h3 className="font-bold text-slate-900 text-base">{selectedSubmission.problem_title}</h3>
                <div className="flex items-center gap-2 text-xs text-slate-500 mt-0.5">
                  <span className="capitalize font-mono font-bold">{selectedSubmission.language}</span>
                  <span>•</span>
                  <span>{new Date(selectedSubmission.submitted_at).toLocaleString()}</span>
                  <span>•</span>
                  <span className={`font-bold ${selectedSubmission.status === 'Accepted' ? 'text-emerald-600' : 'text-red-600'}`}>
                    {selectedSubmission.status}
                  </span>
                </div>
              </div>
              <button
                onClick={() => setSelectedSubmission(null)}
                className="p-1.5 rounded-xl text-slate-400 hover:text-slate-700 hover:bg-slate-200 transition"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-6 overflow-y-auto space-y-4">
              <div>
                <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">Submitted Code:</span>
                <pre className="p-4 rounded-xl bg-slate-900 text-emerald-300 font-mono text-xs overflow-x-auto">
                  {selectedSubmission.code}
                </pre>
              </div>

              {selectedSubmission.output && (
                <div>
                  <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">Evaluation Output:</span>
                  <pre className="p-3 rounded-xl bg-slate-100 text-slate-800 font-mono text-xs overflow-x-auto whitespace-pre-wrap">
                    {selectedSubmission.output}
                  </pre>
                </div>
              )}
            </div>

            <div className="p-4 bg-slate-50 border-t border-slate-200 text-right">
              <button
                onClick={() => setSelectedSubmission(null)}
                className="px-4 py-2 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold text-xs transition"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default SubmissionsPage;
