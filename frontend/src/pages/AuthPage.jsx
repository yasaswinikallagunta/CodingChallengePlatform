import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { 
  Code2, 
  Terminal, 
  Eye, 
  EyeOff, 
  Lock, 
  Mail, 
  User, 
  ArrowRight, 
  CheckCircle2, 
  AlertCircle, 
  Sparkles, 
  ShieldCheck 
} from 'lucide-react';

const AuthPage = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  // Form states
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  // Status & error states
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const { login, register } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  // Password strength calculation
  const getPasswordStrength = (pass) => {
    if (!pass) return { score: 0, text: '', color: '' };
    let score = 0;
    if (pass.length >= 6) score++;
    if (pass.length >= 8) score++;
    if (/[A-Z]/.test(pass) && /[a-z]/.test(pass)) score++;
    if (/[0-9]/.test(pass) || /[^A-Za-z0-9]/.test(pass)) score++;

    if (score <= 1) return { score: 1, text: 'Weak', color: 'bg-red-500 text-red-600' };
    if (score <= 3) return { score: 2, text: 'Medium', color: 'bg-amber-500 text-amber-600' };
    return { score: 3, text: 'Strong', color: 'bg-emerald-600 text-emerald-600' };
  };

  const strength = getPasswordStrength(password);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage('');
    setSuccessMessage('');

    if (isLogin) {
      if (!username.trim() || !password) {
        setErrorMessage('Please provide both username/email and password.');
        return;
      }

      setLoading(true);
      try {
        await login(username.trim(), password);
        const destination = location.state?.from?.pathname || '/dashboard';
        navigate(destination, { replace: true });
      } catch (err) {
        const detail = err.response?.data?.detail || 'Authentication failed. Please check your credentials.';
        setErrorMessage(detail);
      } finally {
        setLoading(false);
      }
    } else {
      // Sign Up validation
      if (!fullName.trim() || !email.trim() || !username.trim() || !password || !confirmPassword) {
        setErrorMessage('All fields are required.');
        return;
      }

      // Email format check
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email.trim())) {
        setErrorMessage('Please enter a valid email address.');
        return;
      }

      if (password.length < 6) {
        setErrorMessage('Password must be at least 6 characters long.');
        return;
      }

      if (password !== confirmPassword) {
        setErrorMessage('Passwords do not match.');
        return;
      }

      setLoading(true);
      try {
        await register(fullName.trim(), email.trim(), username.trim(), password, confirmPassword);
        setSuccessMessage('Account created successfully! Redirecting to dashboard...');
        setTimeout(() => {
          navigate('/dashboard', { replace: true });
        }, 800);
      } catch (err) {
        const errorData = err.response?.data?.errors;
        if (errorData) {
          const firstKey = Object.keys(errorData)[0];
          const val = errorData[firstKey];
          setErrorMessage(Array.isArray(val) ? val[0] : String(val));
        } else {
          setErrorMessage(err.response?.data?.detail || 'Registration failed. Username or email may already be taken.');
        }
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="min-h-[calc(100vh-4rem)] flex flex-col md:flex-row bg-[#F7FCF8]">
      {/* Left side: Premium Animated Coding Hero */}
      <div className="w-full md:w-1/2 p-8 sm:p-12 lg:p-16 flex flex-col justify-between bg-gradient-to-br from-emerald-900 via-emerald-800 to-green-950 text-white relative overflow-hidden">
        {/* Subtle decorative glowing shapes */}
        <div className="absolute top-0 left-0 w-72 h-72 bg-emerald-500/20 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 right-0 w-80 h-80 bg-green-400/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10">
          <div className="flex items-center gap-2.5 mb-8">
            <div className="w-10 h-10 rounded-xl bg-white text-emerald-800 flex items-center justify-center font-bold shadow-lg">
              <Code2 className="w-6 h-6 text-emerald-700" />
            </div>
            <span className="font-extrabold text-xl tracking-tight">CODING CHALLENGE</span>
          </div>

          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-700/60 border border-emerald-500/40 text-emerald-200 text-xs font-semibold mb-6">
            <Sparkles className="w-3.5 h-3.5" /> Empower Your Engineering Journey
          </div>

          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight leading-tight">
            Level up your algorithmic mastery with <span className="text-emerald-300">every test case</span>.
          </h2>

          <p className="mt-4 text-emerald-100/90 text-sm sm:text-base leading-relaxed max-w-lg">
            Solve curated challenges across Python, JavaScript, C++, Java, and SQL. 
            Evaluate live with instant compilation and earn achievements along your path to technical excellence.
          </p>

          {/* Animated code snippet preview */}
          <div className="mt-8 rounded-2xl bg-black/40 border border-emerald-500/30 p-4 font-mono text-xs text-emerald-300 backdrop-blur-md shadow-2xl">
            <div className="flex items-center gap-1.5 pb-2 border-b border-emerald-900/60 mb-2.5">
              <span className="w-2.5 h-2.5 rounded-full bg-red-500/80" />
              <span className="w-2.5 h-2.5 rounded-full bg-amber-500/80" />
              <span className="w-2.5 h-2.5 rounded-full bg-green-500/80" />
              <span className="ml-2 text-[10px] text-emerald-400/80">challenge_runner.py</span>
            </div>
            <p className="text-slate-400"># Continuous practice brings mastery</p>
            <p><span className="text-purple-300">def</span> <span className="text-emerald-400">reach_breakthrough</span>(skills, dedication):</p>
            <p className="pl-4">streak = skills.practice_daily()</p>
            <p className="pl-4"><span className="text-purple-300">return</span> streak.achieve_goals()</p>
          </div>
        </div>

        {/* Left footer assurance */}
        <div className="relative z-10 pt-8 flex items-center gap-4 text-xs text-emerald-200/80 border-t border-emerald-700/50">
          <span className="flex items-center gap-1">
            <ShieldCheck className="w-4 h-4 text-emerald-400" /> Secure Sandboxed Code Runner
          </span>
          <span>•</span>
          <span>Instant Performance Feedback</span>
        </div>
      </div>

      {/* Right side: Authentication Form */}
      <div className="w-full md:w-1/2 p-6 sm:p-10 lg:p-16 flex items-center justify-center">
        <div className="w-full max-w-md bg-white rounded-3xl p-8 sm:p-10 border border-slate-200 shadow-xl shadow-emerald-900/5">
          {/* Toggle buttons */}
          <div className="flex rounded-xl bg-slate-100 p-1 mb-8">
            <button
              type="button"
              onClick={() => {
                setIsLogin(true);
                setErrorMessage('');
                setSuccessMessage('');
              }}
              className={`flex-1 py-2.5 text-xs font-bold rounded-lg transition-all ${
                isLogin
                  ? 'bg-white text-emerald-700 shadow-sm'
                  : 'text-slate-500 hover:text-slate-900'
              }`}
            >
              Sign In
            </button>
            <button
              type="button"
              onClick={() => {
                setIsLogin(false);
                setErrorMessage('');
                setSuccessMessage('');
              }}
              className={`flex-1 py-2.5 text-xs font-bold rounded-lg transition-all ${
                !isLogin
                  ? 'bg-white text-emerald-700 shadow-sm'
                  : 'text-slate-500 hover:text-slate-900'
              }`}
            >
              Create Account
            </button>
          </div>

          <div className="mb-6">
            <h3 className="text-2xl font-black text-slate-900">
              {isLogin ? 'Welcome back!' : 'Join the Platform'}
            </h3>
            <p className="text-xs text-slate-500 mt-1">
              {isLogin
                ? 'Enter your credentials to access your coding dashboard.'
                : 'Start tracking your algorithmic progress and unlock badges.'}
            </p>
          </div>

          {/* Feedback messages */}
          {errorMessage && (
            <div className="mb-5 p-3.5 rounded-xl bg-red-50 border border-red-200 text-xs text-red-700 flex items-start gap-2.5 animate-pulse-subtle">
              <AlertCircle className="w-4 h-4 text-red-500 shrink-0 mt-0.5" />
              <span>{errorMessage}</span>
            </div>
          )}

          {successMessage && (
            <div className="mb-5 p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 text-xs text-emerald-700 flex items-start gap-2.5">
              <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
              <span>{successMessage}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            {!isLogin && (
              <>
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1.5">
                    Full Name
                  </label>
                  <div className="relative">
                    <User className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                    <input
                      type="text"
                      required
                      placeholder="Ada Lovelace"
                      value={fullName}
                      onChange={(e) => setFullName(e.target.value)}
                      className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1.5">
                    Email Address
                  </label>
                  <div className="relative">
                    <Mail className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                    <input
                      type="email"
                      required
                      placeholder="developer@example.com"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition"
                    />
                  </div>
                </div>
              </>
            )}

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                {isLogin ? 'Username or Email' : 'Choose a Username'}
              </label>
              <div className="relative">
                <Terminal className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="text"
                  required
                  placeholder={isLogin ? 'username or your email' : 'coder123'}
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                Password
              </label>
              <div className="relative">
                <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full pl-10 pr-10 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3.5 top-3 text-slate-400 hover:text-slate-600"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>

              {!isLogin && password && (
                <div className="mt-2">
                  <div className="flex items-center justify-between text-[11px] mb-1">
                    <span className="text-slate-500">Password strength:</span>
                    <span className={`font-bold ${strength.color}`}>{strength.text}</span>
                  </div>
                  <div className="h-1.5 w-full bg-slate-100 rounded-full overflow-hidden flex gap-1">
                    <div className={`h-full rounded-full transition-all ${strength.score >= 1 ? strength.color.split(' ')[0] : 'bg-slate-200'}`} style={{ width: '33%' }} />
                    <div className={`h-full rounded-full transition-all ${strength.score >= 2 ? strength.color.split(' ')[0] : 'bg-slate-200'}`} style={{ width: '33%' }} />
                    <div className={`h-full rounded-full transition-all ${strength.score >= 3 ? strength.color.split(' ')[0] : 'bg-slate-200'}`} style={{ width: '34%' }} />
                  </div>
                </div>
              )}
            </div>

            {!isLogin && (
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1.5">
                  Confirm Password
                </label>
                <div className="relative">
                  <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                  <input
                    type={showConfirmPassword ? 'text' : 'password'}
                    required
                    placeholder="••••••••"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    className="w-full pl-10 pr-10 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition"
                  />
                  <button
                    type="button"
                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                    className="absolute right-3.5 top-3 text-slate-400 hover:text-slate-600"
                  >
                    {showConfirmPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                  </button>
                </div>
              </div>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-6 py-3 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-md shadow-emerald-600/25 flex items-center justify-center gap-2 transition disabled:opacity-50"
            >
              {loading ? (
                <span>Connecting to Server...</span>
              ) : isLogin ? (
                <>
                  <span>Sign In to Dashboard</span>
                  <ArrowRight className="w-4 h-4" />
                </>
              ) : (
                <>
                  <span>Create Account</span>
                  <CheckCircle2 className="w-4 h-4" />
                </>
              )}
            </button>
          </form>

          {/* Quick toggle footer */}
          <div className="mt-6 text-center text-xs text-slate-500">
            {isLogin ? (
              <p>
                Don't have an account yet?{' '}
                <button
                  onClick={() => {
                    setIsLogin(false);
                    setErrorMessage('');
                  }}
                  className="font-bold text-emerald-600 hover:text-emerald-700 underline"
                >
                  Create one now
                </button>
              </p>
            ) : (
              <p>
                Already have an account?{' '}
                <button
                  onClick={() => {
                    setIsLogin(true);
                    setErrorMessage('');
                  }}
                  className="font-bold text-emerald-600 hover:text-emerald-700 underline"
                >
                  Sign in here
                </button>
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AuthPage;
