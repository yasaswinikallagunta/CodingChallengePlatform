import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../services/api';
import {
  GraduationCap,
  Award,
  Search,
  Filter,
  Clock,
  HelpCircle,
  CheckCircle2,
  AlertCircle,
  ArrowRight,
  Download,
  ExternalLink,
  BookOpen,
  Sparkles,
  ShieldCheck,
  Flame,
  FileCheck2,
  Terminal,
  Cpu,
  Code2,
  Layers,
  Database,
  Server,
  Play
} from 'lucide-react';

const ExamsPage = () => {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('exams'); // 'exams' | 'certificates'
  const [categories, setCategories] = useState([]);
  const [exams, setExams] = useState([]);
  const [myCertificates, setMyCertificates] = useState([]);
  const [downloadingCertId, setDownloadingCertId] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Filters
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState('all');
  const [selectedStatus, setSelectedStatus] = useState('all');

  useEffect(() => {
    fetchInitialData();
  }, []);

  const fetchInitialData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const [catsRes, examsRes, certsRes] = await Promise.all([
        api.get('/exams/categories/').catch(() => ({ data: [] })),
        api.get('/exams/').catch(() => ({ data: [] })),
        api.get('/certificates/').catch(() => ({ data: [] }))
      ]);

      setCategories(Array.isArray(catsRes.data) ? catsRes.data : []);
      setExams(Array.isArray(examsRes.data) ? examsRes.data : []);
      setMyCertificates(Array.isArray(certsRes.data) ? certsRes.data : []);
    } catch (err) {
      console.error('Failed to load exams data:', err);
      setError('Failed to load examination catalog. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownloadPdf = async (certId) => {
    if (!certId) return;
    setDownloadingCertId(certId);
    try {
      const res = await api.get(`/certificates/${encodeURIComponent(certId)}/download/`, {
        responseType: 'blob',
      });
      const blob = new Blob([res.data], { type: 'application/pdf' });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `Certificate_${certId}.pdf`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (err) {
      console.error('Download failed, trying direct link fallback:', err);
      const fallbackUrl = `${api.defaults.baseURL}/certificates/${encodeURIComponent(certId)}/download/`;
      window.open(fallbackUrl, '_blank');
    } finally {
      setDownloadingCertId(null);
    }
  };

  // Filtered exams
  const filteredExams = exams.filter((exam) => {
    // Search
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      const matchTitle = exam.title.toLowerCase().includes(q);
      const matchCat = (exam.category_name || '').toLowerCase().includes(q);
      const matchDesc = (exam.description || '').toLowerCase().includes(q);
      if (!matchTitle && !matchCat && !matchDesc) return false;
    }

    // Category
    if (selectedCategory !== 'all' && exam.category_slug !== selectedCategory) {
      return false;
    }

    // Difficulty
    if (selectedDifficulty !== 'all' && exam.difficulty.toLowerCase() !== selectedDifficulty.toLowerCase()) {
      return false;
    }

    // Status
    if (selectedStatus !== 'all') {
      if (selectedStatus === 'passed' && exam.user_status !== 'passed') return false;
      if (selectedStatus === 'in_progress' && exam.user_status !== 'in_progress') return false;
      if (selectedStatus === 'not_started' && exam.user_status !== 'not_started') return false;
    }

    return true;
  });

  const getDifficultyBadge = (difficulty) => {
    switch (difficulty?.toLowerCase()) {
      case 'easy':
        return 'bg-emerald-100 text-emerald-800 border-emerald-200';
      case 'medium':
        return 'bg-amber-100 text-amber-800 border-amber-200';
      case 'hard':
        return 'bg-rose-100 text-rose-800 border-rose-200';
      default:
        return 'bg-slate-100 text-slate-800 border-slate-200';
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Hero Header */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-emerald-800 via-emerald-700 to-green-900 text-white p-8 md:p-12 mb-8 shadow-xl shadow-emerald-900/10">
        <div className="absolute top-0 right-0 -mt-10 -mr-10 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-emerald-200 text-xs font-semibold uppercase tracking-wider mb-4">
            <Sparkles className="w-3.5 h-3.5 text-emerald-300" />
            Verified Technical Credentials
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight">
            Exams & <span className="text-emerald-300">Certifications</span>
          </h1>
          <p className="mt-4 text-emerald-100 text-base sm:text-lg leading-relaxed">
            Validate your software engineering mastery across 20 specialized domains.
            Complete rigorous timed assessments, pass with 70% or higher, and earn digitally verifiable credentials.
          </p>

          {/* Quick Metrics Bar */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8 pt-6 border-t border-white/15">
            <div>
              <span className="block text-2xl font-black text-white">{categories.length || 20}</span>
              <span className="text-xs text-emerald-200 font-medium">Domain Categories</span>
            </div>
            <div>
              <span className="block text-2xl font-black text-white">{exams.length || 20}</span>
              <span className="text-xs text-emerald-200 font-medium">Certification Exams</span>
            </div>
            <div>
              <span className="block text-2xl font-black text-white">70%</span>
              <span className="text-xs text-emerald-200 font-medium">Passing Threshold</span>
            </div>
            <div>
              <span className="block text-2xl font-black text-emerald-300">{myCertificates.length}</span>
              <span className="text-xs text-emerald-200 font-medium">Earned Certificates</span>
            </div>
          </div>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <div className="flex items-center gap-3 border-b border-slate-200 mb-8">
        <button
          onClick={() => setActiveTab('exams')}
          className={`flex items-center gap-2.5 px-5 py-3.5 font-bold text-sm transition-all border-b-2 -mb-px ${
            activeTab === 'exams'
              ? 'border-emerald-600 text-emerald-700 bg-emerald-50/50 rounded-t-xl'
              : 'border-transparent text-slate-600 hover:text-emerald-600 hover:border-slate-300'
          }`}
        >
          <GraduationCap className="w-4 h-4" />
          <span>Certification Catalog</span>
          <span className="ml-1 px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">
            {exams.length}
          </span>
        </button>

        <button
          onClick={() => setActiveTab('certificates')}
          className={`flex items-center gap-2.5 px-5 py-3.5 font-bold text-sm transition-all border-b-2 -mb-px ${
            activeTab === 'certificates'
              ? 'border-emerald-600 text-emerald-700 bg-emerald-50/50 rounded-t-xl'
              : 'border-transparent text-slate-600 hover:text-emerald-600 hover:border-slate-300'
          }`}
        >
          <Award className="w-4 h-4" />
          <span>My Earned Certificates</span>
          <span className="ml-1 px-2 py-0.5 rounded-full text-xs font-semibold bg-slate-200 text-slate-700">
            {myCertificates.length}
          </span>
        </button>
      </div>

      {/* TAB 1: EXAMS CATALOG */}
      {activeTab === 'exams' && (
        <div className="space-y-6">
          {/* Search and Filters Toolbar */}
          <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">
            <div className="flex flex-col md:flex-row gap-3">
              {/* Search */}
              <div className="relative flex-1">
                <Search className="w-4 h-4 absolute left-3.5 top-3.5 text-slate-400" />
                <input
                  type="text"
                  placeholder="Search certifications by title, topic, or keyword..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition"
                />
              </div>

              {/* Difficulty Filter */}
              <div className="flex items-center gap-2">
                <select
                  value={selectedDifficulty}
                  onChange={(e) => setSelectedDifficulty(e.target.value)}
                  className="px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm font-medium text-slate-700 focus:outline-none focus:ring-2 focus:ring-emerald-500"
                >
                  <option value="all">All Difficulties</option>
                  <option value="easy">Easy</option>
                  <option value="medium">Medium</option>
                  <option value="hard">Hard</option>
                </select>

                {/* Status Filter */}
                <select
                  value={selectedStatus}
                  onChange={(e) => setSelectedStatus(e.target.value)}
                  className="px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm font-medium text-slate-700 focus:outline-none focus:ring-2 focus:ring-emerald-500"
                >
                  <option value="all">All Statuses</option>
                  <option value="passed">Passed</option>
                  <option value="in_progress">In Progress</option>
                  <option value="not_started">Not Started</option>
                </select>
              </div>
            </div>

            {/* Category Pills Slider */}
            <div className="flex items-center gap-2 overflow-x-auto pb-1 pt-1 no-scrollbar">
              <button
                onClick={() => setSelectedCategory('all')}
                className={`px-3.5 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition ${
                  selectedCategory === 'all'
                    ? 'bg-emerald-600 text-white shadow-sm'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                All 20 Categories
              </button>
              {categories.map((cat) => (
                <button
                  key={cat.id}
                  onClick={() => setSelectedCategory(cat.slug)}
                  className={`px-3.5 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition ${
                    selectedCategory === cat.slug
                      ? 'bg-emerald-600 text-white shadow-sm'
                      : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                  }`}
                >
                  {cat.name}
                </button>
              ))}
            </div>
          </div>

          {/* Loading / Error States */}
          {isLoading && (
            <div className="text-center py-20 bg-white rounded-2xl border border-slate-200">
              <div className="w-10 h-10 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
              <p className="text-slate-600 font-medium">Loading certification catalog...</p>
            </div>
          )}

          {error && (
            <div className="p-4 rounded-xl bg-red-50 border border-red-200 text-red-700 text-sm flex items-center gap-3">
              <AlertCircle className="w-5 h-5 flex-shrink-0" />
              <span>{error}</span>
            </div>
          )}

          {/* Exams Grid */}
          {!isLoading && !error && (
            <>
              <div className="flex items-center justify-between text-xs font-semibold text-slate-500 px-1">
                <span>Showing {filteredExams.length} of {exams.length} certifications</span>
                {selectedCategory !== 'all' && (
                  <button
                    onClick={() => {
                      setSelectedCategory('all');
                      setSearchQuery('');
                      setSelectedDifficulty('all');
                      setSelectedStatus('all');
                    }}
                    className="text-emerald-600 hover:underline"
                  >
                    Clear Filters
                  </button>
                )}
              </div>

              {filteredExams.length === 0 ? (
                <div className="text-center py-16 bg-white rounded-2xl border border-slate-200 p-8">
                  <BookOpen className="w-12 h-12 text-slate-300 mx-auto mb-3" />
                  <h3 className="text-base font-bold text-slate-800">No certifications found</h3>
                  <p className="text-sm text-slate-500 mt-1 max-w-sm mx-auto">
                    Try adjusting your search query or clear the category filters to browse all exams.
                  </p>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {filteredExams.map((exam) => {
                    const isPassed = exam.user_status === 'passed';
                    const isInProgress = exam.user_status === 'in_progress';

                    return (
                      <div
                        key={exam.id}
                        className="bg-white rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-all flex flex-col justify-between overflow-hidden group hover:border-emerald-300"
                      >
                        {/* Top Accent Strip */}
                        <div
                          className={`h-1.5 w-full ${
                            isPassed
                              ? 'bg-emerald-500'
                              : isInProgress
                              ? 'bg-amber-500'
                              : 'bg-slate-200 group-hover:bg-emerald-400'
                          }`}
                        />

                        <div className="p-6 flex-1 flex flex-col">
                          {/* Badges row */}
                          <div className="flex items-center justify-between gap-2 mb-3">
                            <span className="px-2.5 py-1 rounded-md text-[11px] font-bold tracking-wide uppercase bg-emerald-50 text-emerald-800 border border-emerald-200">
                              {exam.category_name}
                            </span>
                            <span className={`px-2.5 py-0.5 rounded-full text-xs font-semibold border ${getDifficultyBadge(exam.difficulty)}`}>
                              {exam.difficulty}
                            </span>
                          </div>

                          {/* Title */}
                          <h3 className="text-lg font-bold text-slate-900 group-hover:text-emerald-700 transition leading-snug mb-2">
                            {exam.title}
                          </h3>

                          {/* Description */}
                          <p className="text-xs text-slate-600 line-clamp-3 mb-5 leading-relaxed">
                            {exam.description}
                          </p>

                          {/* Exam Metrics Cards */}
                          <div className="mt-auto grid grid-cols-2 gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs text-slate-600 mb-5">
                            <div className="flex items-center gap-1.5">
                              <Clock className="w-3.5 h-3.5 text-slate-400" />
                              <span><b>{exam.duration_minutes}</b> mins</span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <HelpCircle className="w-3.5 h-3.5 text-slate-400" />
                              <span><b>{exam.questions_count}</b> questions</span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <ShieldCheck className="w-3.5 h-3.5 text-slate-400" />
                              <span><b>{exam.total_marks}</b> marks</span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                              <span><b>{exam.passing_percentage}%</b> pass</span>
                            </div>
                          </div>

                          {/* Status Badge */}
                          {isPassed && (
                            <div className="mb-4 flex items-center gap-2 p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-semibold">
                              <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                              <span>Certification Earned!</span>
                            </div>
                          )}

                          {isInProgress && (
                            <div className="mb-4 flex items-center gap-2 p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs font-semibold">
                              <Clock className="w-4 h-4 text-amber-600 flex-shrink-0 animate-pulse" />
                              <span>Session currently in progress</span>
                            </div>
                          )}

                          {/* Action Button */}
                          <div className="flex items-center gap-2">
                            {(() => {
                              const matchingCert = myCertificates.find((c) => c.exam_slug === exam.slug);
                              const targetCertId = exam.user_certificate_id || matchingCert?.certificate_id;

                              if (isPassed && targetCertId) {
                                return (
                                  <>
                                    <Link
                                      to={`/certificates/${targetCertId}`}
                                      className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-sm transition"
                                    >
                                      <Award className="w-3.5 h-3.5" />
                                      <span>View Certificate</span>
                                    </Link>
                                    <Link
                                      to={`/exams/${exam.slug}`}
                                      className="px-3 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs transition"
                                      title="Retake Exam"
                                    >
                                      Retake
                                    </Link>
                                  </>
                                );
                              }

                              return (
                                <Link
                                  to={`/exams/${exam.slug}`}
                                  className={`w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl font-bold text-xs shadow-sm transition ${
                                    isInProgress
                                      ? 'bg-amber-600 hover:bg-amber-700 text-white'
                                      : 'bg-emerald-600 hover:bg-emerald-700 text-white shadow-emerald-600/20'
                                  }`}
                                >
                                  {isInProgress ? (
                                    <>
                                      <Clock className="w-3.5 h-3.5" />
                                      <span>Resume Session</span>
                                    </>
                                  ) : (
                                    <>
                                      <Play className="w-3.5 h-3.5 fill-current" />
                                      <span>Take Certification Exam</span>
                                    </>
                                  )}
                                </Link>
                              );
                            })()}
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </>
          )}
        </div>
      )}

      {/* TAB 2: MY CERTIFICATES */}
      {activeTab === 'certificates' && (
        <div className="space-y-6">
          {myCertificates.length === 0 ? (
            <div className="text-center py-20 bg-white rounded-3xl border border-slate-200 p-8 shadow-sm">
              <div className="w-16 h-16 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center mx-auto mb-4">
                <Award className="w-8 h-8" />
              </div>
              <h3 className="text-xl font-bold text-slate-900">No Certificates Earned Yet</h3>
              <p className="text-sm text-slate-500 mt-2 max-w-md mx-auto leading-relaxed">
                Take any of our 20 official certification exams, score 70% or above, and your verified credential will be automatically issued here.
              </p>
              <button
                onClick={() => setActiveTab('exams')}
                className="mt-6 inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-md shadow-emerald-600/20 transition"
              >
                <GraduationCap className="w-4 h-4" />
                <span>Browse Certification Catalog</span>
              </button>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {myCertificates.map((cert) => (
                <div
                  key={cert.certificate_id}
                  className="bg-white rounded-2xl border border-emerald-200/80 p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
                >
                  <div>
                    {/* Header with verified badge */}
                    <div className="flex items-center justify-between gap-2 mb-4">
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 text-[11px] font-bold border border-emerald-200">
                        <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                        Verified Credential
                      </span>
                      <span className="text-[11px] font-semibold text-slate-500">
                        {cert.issue_date}
                      </span>
                    </div>

                    <h3 className="text-lg font-bold text-slate-900 leading-snug mb-1">
                      {cert.exam_title}
                    </h3>
                    <p className="text-xs font-semibold text-emerald-700 mb-4">
                      {cert.category_name} Specialization
                    </p>

                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-100 space-y-1.5 text-xs text-slate-600 mb-6">
                      <div className="flex items-center justify-between">
                        <span className="text-slate-400 font-medium">Candidate:</span>
                        <span className="font-bold text-slate-800">{cert.candidate_name}</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-slate-400 font-medium">Credential ID:</span>
                        <span className="font-mono font-bold text-slate-800">{cert.certificate_id}</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-slate-400 font-medium">Signatory:</span>
                        <span className="font-medium text-slate-700">{cert.signatory_title}</span>
                      </div>
                    </div>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-2 pt-2 border-t border-slate-100">
                    <Link
                      to={`/certificates/${cert.certificate_id}`}
                      className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-sm transition"
                    >
                      <Award className="w-3.5 h-3.5" />
                      <span>View Certificate</span>
                    </Link>

                    <button
                      onClick={() => handleDownloadPdf(cert.certificate_id)}
                      disabled={downloadingCertId === cert.certificate_id}
                      className="inline-flex items-center justify-center p-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition disabled:opacity-50"
                      title="Download Official Certificate PDF"
                    >
                      {downloadingCertId === cert.certificate_id ? (
                        <div className="w-4 h-4 border-2 border-emerald-600 border-t-transparent rounded-full animate-spin" />
                      ) : (
                        <Download className="w-4 h-4 text-emerald-700" />
                      )}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ExamsPage;
