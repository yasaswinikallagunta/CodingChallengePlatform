import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../services/api';
import {
  Download,
  Printer,
  Copy,
  Check,
  ArrowLeft,
  ShieldCheck,
  Award,
  Sparkles,
  ExternalLink,
  Code2,
  AlertCircle,
  RefreshCw,
  Home
} from 'lucide-react';

const CertificatePreviewPage = () => {
  const { certificateId } = useParams();
  const [certificate, setCertificate] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [copied, setCopied] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);

  useEffect(() => {
    fetchCertificate();
  }, [certificateId]);

  const fetchCertificate = async () => {
    if (!certificateId || certificateId === 'undefined' || certificateId === 'null') {
      setError('No valid certificate ID was specified in the URL.');
      setIsLoading(false);
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const res = await api.get(`/certificates/${encodeURIComponent(certificateId)}/`);
      setCertificate(res.data);
    } catch (err) {
      console.error('Failed to load certificate:', err);
      const detail = err.response?.data?.detail;
      if (err.response?.status === 404) {
        setError(`Certificate "${certificateId}" could not be found. Please check the credential ID and try again.`);
      } else {
        setError(detail || 'Could not locate this certificate. Please check the ID or verify your network connection.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleCopyLink = () => {
    navigator.clipboard.writeText(window.location.href);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handlePrint = () => {
    window.print();
  };

  const handleDownloadPdf = async () => {
    if (!certificate?.certificate_id) return;
    setIsDownloading(true);

    try {
      const res = await api.get(`/certificates/${encodeURIComponent(certificate.certificate_id)}/download/`, {
        responseType: 'blob',
      });
      const blob = new Blob([res.data], { type: 'application/pdf' });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `Certificate_${certificate.certificate_id}.pdf`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (err) {
      console.error('Blob download failed, trying direct link fallback:', err);
      // Fallback: direct window download
      const fallbackUrl = `${api.defaults.baseURL}/certificates/${encodeURIComponent(certificate.certificate_id)}/download/`;
      window.open(fallbackUrl, '_blank');
    } finally {
      setIsDownloading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-24 text-center">
        <div className="w-12 h-12 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mx-auto mb-5" />
        <h2 className="text-lg font-bold text-slate-800 mb-1">Verifying Credential</h2>
        <p className="text-slate-500 text-sm">Validating cryptographic signature and generating certificate preview...</p>
      </div>
    );
  }

  if (error || !certificate) {
    return (
      <div className="max-w-xl mx-auto px-4 py-16 text-center">
        <div className="w-16 h-16 rounded-2xl bg-rose-50 text-rose-600 border border-rose-200 flex items-center justify-center mx-auto mb-4">
          <AlertCircle className="w-8 h-8" />
        </div>
        <h2 className="text-xl font-bold text-slate-900 mb-2">Certificate Unavailable</h2>
        <div className="p-4 rounded-xl bg-rose-50/80 border border-rose-200 text-rose-800 text-sm mb-6 max-w-md mx-auto leading-relaxed">
          {error || 'The requested technical certificate could not be retrieved.'}
        </div>
        <div className="flex flex-wrap items-center justify-center gap-3">
          <button
            onClick={fetchCertificate}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-sm transition"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Try Again</span>
          </button>
          <Link
            to="/exams"
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span>Back to Certifications</span>
          </Link>
          <Link
            to="/dashboard"
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition"
          >
            <Home className="w-3.5 h-3.5" />
            <span>Dashboard</span>
          </Link>
        </div>
      </div>
    );
  }

  // Format date cleanly
  const rawDate = certificate.issue_date || certificate.created_at;
  let formattedDate = 'Recent';
  if (rawDate) {
    try {
      const d = new Date(rawDate);
      if (!isNaN(d.getTime())) {
        formattedDate = d.toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        });
      } else {
        formattedDate = String(rawDate);
      }
    } catch {
      formattedDate = String(rawDate);
    }
  }

  const candidateDisplayName = (
    certificate.candidate_name ||
    certificate.user_full_name ||
    certificate.username ||
    'Candidate'
  );

  const examTitle = certificate.exam_title || 'Certification Assessment';
  const signatoryTitle = certificate.signatory_title || 'Platform Representative';

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8">
      {/* Action Header - Hidden when printing */}
      <div className="print:hidden flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8 bg-white p-4 sm:p-5 rounded-2xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <Link
            to="/exams"
            className="p-2 rounded-xl text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition"
            title="Back to Certifications Catalog"
          >
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
              <h2 className="text-sm font-bold text-slate-900">Verified Technical Credential</h2>
            </div>
            <div className="text-xs text-slate-500 font-mono mt-0.5">
              ID: {certificate.certificate_id}
            </div>
          </div>
        </div>

        {/* Toolbar Buttons */}
        <div className="flex flex-wrap items-center gap-2">
          <button
            onClick={handleCopyLink}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold transition"
            title="Copy verification link"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
            <span>{copied ? 'Link Copied!' : 'Share Credential'}</span>
          </button>

          <button
            onClick={handlePrint}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold transition"
            title="Print certificate"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>Print</span>
          </button>

          <button
            onClick={handleDownloadPdf}
            disabled={isDownloading}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-md shadow-emerald-600/20 transition disabled:opacity-50"
            title="Download official PDF vector document"
          >
            {isDownloading ? (
              <>
                <div className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                <span>Generating PDF...</span>
              </>
            ) : (
              <>
                <Download className="w-4 h-4" />
                <span>Download Certificate</span>
              </>
            )}
          </button>
        </div>
      </div>

      {/* Responsive helper for mobile */}
      <div className="print:hidden block md:hidden text-center text-xs text-slate-500 mb-3 bg-emerald-50/60 p-2.5 rounded-xl border border-emerald-100">
        Swipe horizontally or rotate your device to landscape for the full certificate view.
      </div>

      {/* A4 LANDSCAPE CERTIFICATE CONTAINER */}
      <div className="flex justify-center overflow-x-auto pb-8">
        <div
          id="certificate-frame"
          className="w-[900px] min-w-[900px] h-[636px] bg-[#FAFCF9] border-[10px] border-[#166534] rounded-2xl relative p-10 flex flex-col justify-between shadow-2xl select-none print:shadow-none print:border-[8px] print:m-0 print:w-full print:h-screen"
        >
          {/* Inner Emerald Thin Border */}
          <div className="absolute inset-3 border-2 border-[#16A34A] rounded-xl pointer-events-none" />

          {/* Corner Ornaments */}
          <div className="absolute top-4 left-4 w-5 h-5 bg-[#16A34A] rounded-sm pointer-events-none" />
          <div className="absolute top-4 right-4 w-5 h-5 bg-[#16A34A] rounded-sm pointer-events-none" />
          <div className="absolute bottom-4 left-4 w-5 h-5 bg-[#16A34A] rounded-sm pointer-events-none" />
          <div className="absolute bottom-4 right-4 w-5 h-5 bg-[#16A34A] rounded-sm pointer-events-none" />

          {/* Decorative Top and Bottom Bands */}
          <div className="absolute top-10 left-10 right-10 h-0.5 bg-[#DCFCE7] pointer-events-none" />
          <div className="absolute bottom-10 left-10 right-10 h-0.5 bg-[#DCFCE7] pointer-events-none" />

          {/* Watermark Logo Background */}
          <div className="absolute inset-0 flex items-center justify-center opacity-[0.03] pointer-events-none">
            <Award className="w-[450px] h-[450px] text-[#166534]" />
          </div>

          {/* Header Branding */}
          <div className="relative text-center pt-2">
            <div className="inline-flex items-center gap-2 mb-1">
              <div className="w-7 h-7 rounded-lg bg-[#166534] text-white flex items-center justify-center font-black text-xs shadow-sm">
                <Code2 className="w-4 h-4" />
              </div>
              <span className="font-extrabold text-[#166534] tracking-widest text-sm uppercase">
                Coding Challenge Platform
              </span>
            </div>
            <div className="text-[10px] tracking-widest uppercase font-bold text-[#16A34A]">
              Official Assessment &amp; Certification Authority
            </div>

            <div className="mt-4">
              <h1 className="text-3xl font-black text-[#172B21] tracking-tight uppercase">
                Certificate of Completion
              </h1>
              <div className="text-xs font-bold tracking-widest uppercase text-[#16A34A] mt-1">
                &mdash;&mdash; Verified Technical Credential &mdash;&mdash;
              </div>
            </div>
          </div>

          {/* Candidate Presentation */}
          <div className="relative text-center my-auto py-2">
            <div className="text-xs uppercase tracking-widest font-semibold text-slate-500 mb-2">
              This certificate is proudly conferred to
            </div>

            {/* Candidate Name */}
            <div className="text-3xl sm:text-4xl font-extrabold text-[#166534] uppercase tracking-wide border-b-2 border-emerald-200 inline-block px-10 pb-1 mb-3">
              {candidateDisplayName}
            </div>

            <p className="text-xs text-slate-600 max-w-xl mx-auto leading-relaxed mt-2">
              for successfully completing all required theoretical evaluations, hands-on programming challenges,
              and demonstrating recognized competence in
            </p>

            {/* Exam / Specialization Title */}
            <div className="text-2xl font-black text-[#172B21] mt-2 tracking-tight">
              {examTitle}
            </div>
          </div>

          {/* Footer Metadata & Signature */}
          <div className="relative pt-4 border-t border-emerald-100 grid grid-cols-3 items-end">
            {/* Left Column: Certificate ID & Security */}
            <div className="space-y-1 text-left">
              <div className="text-[9px] uppercase tracking-wider font-bold text-slate-400">Certificate ID</div>
              <div className="font-mono font-bold text-xs text-slate-900">{certificate.certificate_id}</div>
              <div className="text-[9px] text-emerald-700 font-semibold flex items-center gap-1 mt-1">
                <ShieldCheck className="w-3.5 h-3.5 text-[#16A34A]" />
                <span>Digitally Verified &amp; Validated</span>
              </div>
            </div>

            {/* Center Column: Official Date */}
            <div className="text-center">
              <div className="text-[9px] uppercase tracking-wider font-bold text-slate-400">Date of Issuance</div>
              <div className="font-semibold text-xs text-slate-900 mt-0.5">{formattedDate}</div>
              <div className="text-[9px] text-slate-400 font-medium">Coding Challenge Platform</div>
            </div>

            {/* Right Column: Signature */}
            <div className="text-right">
              <div className="font-serif italic text-lg text-[#166534] pr-2">
                C. C. Platform
              </div>
              <div className="w-36 ml-auto border-t border-slate-400 mt-1 mb-1" />
              <div className="text-[10px] font-bold text-slate-900 uppercase tracking-wide">
                {signatoryTitle}
              </div>
              <div className="text-[9px] text-slate-500">
                Coding Challenge Platform Certification Board
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CertificatePreviewPage;
