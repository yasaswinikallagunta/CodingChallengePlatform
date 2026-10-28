import axios from 'axios';

// Detect whether we are running in a local development environment
const isLocalEnv =
  typeof window !== 'undefined' &&
  (window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1' ||
    window.location.hostname === '0.0.0.0');

// Production API Base URL
export const PRODUCTION_API_URL = 'https://codingchallengeplatform.onrender.com/api';

// Select API Base URL:
// 1. If running on local machine, allow localhost / 127.0.0.1 backend
// 2. If running deployed (e.g. on Render), always strictly route to the deployed backend
export const API_BASE_URL = (() => {
  const envUrl = import.meta.env.VITE_API_URL;
  if (!isLocalEnv) {
    // In production/deployed environment, guarantee the deployed Render backend URL is used
    if (envUrl && !envUrl.includes('localhost') && !envUrl.includes('127.0.0.1')) {
      return envUrl.replace(/\/+$/, '');
    }
    return PRODUCTION_API_URL;
  }
  // Local environment
  return envUrl || 'http://localhost:8000/api';
})();

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});
// Attach access token to outgoing requests if available
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Intercept response to catch 401s and handle logout
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // If token expired, clear localStorage if not already on auth page
      if (!window.location.pathname.startsWith('/auth')) {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user');
      }
    }
    return Promise.reject(error);
  }
);

export default api;
