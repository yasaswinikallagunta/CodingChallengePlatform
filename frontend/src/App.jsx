import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import AnimatedIntro from './components/AnimatedIntro';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ProtectedRoute from './components/ProtectedRoute';

import AuthPage from './pages/AuthPage';
import DashboardPage from './pages/DashboardPage';
import ProblemsListPage from './pages/ProblemsListPage';
import WorkspacePage from './pages/WorkspacePage';
import SubmissionsPage from './pages/SubmissionsPage';
import ProgressPage from './pages/ProgressPage';
import AchievementsPage from './pages/AchievementsPage';
import ExamsPage from './pages/ExamsPage';
import ExamInstructionsPage from './pages/ExamInstructionsPage';
import ExamSessionPage from './pages/ExamSessionPage';
import ExamResultPage from './pages/ExamResultPage';
import CertificatePreviewPage from './pages/CertificatePreviewPage';
import ModernFrontendPage from './pages/ModernFrontendPage';

const RootRedirect = () => {
  const { isAuthenticated, isLoading } = useAuth();
  if (isLoading) return null;
  return <Navigate to={isAuthenticated ? '/dashboard' : '/auth'} replace />;
};

function App() {
  const [showIntro, setShowIntro] = useState(() => {
    // Only show on first visit of the session
    return !sessionStorage.getItem('ccp_has_seen_intro');
  });

  return (
    <AuthProvider>
      <Router>
        {showIntro && <AnimatedIntro onComplete={() => setShowIntro(false)} />}
        <div className="flex flex-col min-h-screen bg-brand-bg text-brand-text">
          <Navbar />
          <main className="flex-1">
            <Routes>
              {/* Public Auth */}
              <Route path="/auth" element={<AuthPage />} />

              {/* Protected Routes */}
              <Route
                path="/dashboard"
                element={
                  <ProtectedRoute>
                    <DashboardPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/problems"
                element={
                  <ProtectedRoute>
                    <ProblemsListPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/workspace/:slug"
                element={
                  <ProtectedRoute>
                    <WorkspacePage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/submissions"
                element={
                  <ProtectedRoute>
                    <SubmissionsPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/progress"
                element={
                  <ProtectedRoute>
                    <ProgressPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/achievements"
                element={
                  <ProtectedRoute>
                    <AchievementsPage />
                  </ProtectedRoute>
                }
              />

              {/* Exams & Certifications Routes */}
              <Route
                path="/exams"
                element={
                  <ProtectedRoute>
                    <ExamsPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/exams/:slug"
                element={
                  <ProtectedRoute>
                    <ExamInstructionsPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/exams/:slug/session/:attemptId"
                element={
                  <ProtectedRoute>
                    <ExamSessionPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/exams/attempts/:attemptId/result"
                element={
                  <ProtectedRoute>
                    <ExamResultPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/certificates/:certificateId"
                element={<CertificatePreviewPage />}
              />

              {/* Modern Frontend Development Course Routes */}
              <Route
                path="/course/modern-frontend-development"
                element={
                  <ProtectedRoute>
                    <ModernFrontendPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/course/modern-frontend-development/:topicSlug"
                element={
                  <ProtectedRoute>
                    <ModernFrontendPage />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/courses"
                element={<Navigate to="/course/modern-frontend-development" replace />}
              />
              <Route
                path="/course"
                element={<Navigate to="/course/modern-frontend-development" replace />}
              />

              {/* Fallbacks */}
              <Route path="/" element={<RootRedirect />} />
              <Route path="*" element={<RootRedirect />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
