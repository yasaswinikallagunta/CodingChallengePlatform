export const advancedJsTopic = {
  id: 'advanced-javascript',
  title: 'Advanced JavaScript Concepts',
  shortTitle: 'Advanced JS',
  icon: 'Cpu',
  description: 'Master advanced JavaScript execution mechanics. Learn lexical scope, hoisting, closures, ES6+ features (destructuring, spread/rest), asynchronous patterns with Promises & async/await, error handling architectures, and the JavaScript Event Loop.',
  subtopics: [
    'Execution contexts, call stack & lexical scope chains',
    'Hoisting (function declarations vs var/let/const) & Temporal Dead Zone (TDZ)',
    'Closures: data privacy, factory functions, and memoization patterns',
    'Arrow functions vs traditional functions (lexical this, arguments, new keyword)',
    'Template literals & tagged template literals',
    'Destructuring: object & array destructuring, default values, aliases, nested extraction',
    'Spread & rest operators: shallow copying, function parameter gathering, immutable updates',
    'Promises: states, chaining (.then, .catch, .finally), static combinators (all, allSettled, race, any)',
    'Async/await: async function mechanics, sequential vs concurrent execution, try/catch/finally',
    'Error handling: custom Error classes, defensive propagation, unhandled rejections',
    'The JavaScript Event Loop: Call Stack, Web APIs, Task Queue (Macrotasks), Microtask Queue'
  ],
  theory: [
    {
      title: '1. Scopes, Closures & Lexical Environments',
      content: `A **closure** is the combination of a function bundled together with references to its surrounding lexical state. Closures give an inner function access to an outer function's scope even after the outer function has finished executing!

### Encapsulating Private State with Closures:
\`\`\`js
function createBankAccount(initialBalance = 0) {
  // Private variable inaccessible from outside!
  let balance = initialBalance;

  return {
    deposit(amount) {
      if (amount <= 0) throw new Error("Amount must be positive");
      balance += amount;
      return balance;
    },
    withdraw(amount) {
      if (amount > balance) throw new Error("Insufficient funds");
      balance -= amount;
      return balance;
    },
    getBalance() {
      return balance;
    }
  };
}

const account = createBankAccount(100);
account.deposit(50); // 150
console.log(account.balance); // undefined! Completely private!
\`\`\``
    },
    {
      title: '2. Modern ES6+: Destructuring, Spread & Rest',
      content: `Modern JavaScript provides syntax for clean, immutable data manipulation:

### Destructuring with Defaults & Aliasing:
\`\`\`js
const user = {
  id: 'u42',
  profile: { firstName: 'Sanya', lastName: 'Iyer' },
  role: 'admin'
};

// Nested destructuring with property alias and default value
const {
  profile: { firstName: givenName },
  role,
  status = 'active'
} = user;

console.log(givenName); // "Sanya"
console.log(status);    // "active" (used default)
\`\`\`

### Immutability with Spread:
\`\`\`js
// Updating nested state immutably (essential for React!)
const updatedUser = {
  ...user,
  role: 'superadmin',
  profile: {
    ...user.profile,
    lastName: 'Sharma'
  }
};
\`\`\``
    },
    {
      title: '3. Asynchronous JavaScript & The Event Loop',
      content: `JavaScript is single-threaded: it has one Call Stack and executes one command at a time. Concurrency is handled by the browser's **Event Loop**.

### Event Loop Priority:
1. **Call Stack**: Executes synchronous code line-by-line.
2. **Microtask Queue**: Processed immediately after the Call Stack empties (Promises \`.then()\`, \`async/await\`, \`queueMicrotask\`).
3. **Macrotask Queue**: Processed once all microtasks finish (\`setTimeout\`, \`setInterval\`, DOM events, I/O).

\`\`\`js
console.log('1: Sync Start');

setTimeout(() => {
  console.log('4: Macrotask (setTimeout)');
}, 0);

Promise.resolve().then(() => {
  console.log('3: Microtask (Promise)');
});

console.log('2: Sync End');

// Output Order:
// 1: Sync Start
// 2: Sync End
// 3: Microtask (Promise)
// 4: Macrotask (setTimeout)
\`\`\``
    }
  ],
  examples: [
    {
      title: 'Example: Async API Fetcher with Timeout & Error Recovery',
      code: `// Custom API error class
class ApiError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.name = 'ApiError';
    this.statusCode = statusCode;
  }
}

// Fetch with automatic timeout abort
async function fetchWithTimeout(resource, options = {}) {
  const { timeout = 5000, ...fetchOptions } = options;
  
  // Create an AbortController instance
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);
  
  try {
    // In real browser: const res = await fetch(resource, { ...fetchOptions, signal: controller.signal });
    // Simulated async fetch delay
    await new Promise(resolve => setTimeout(resolve, 300));
    
    // Simulate successful JSON response
    const data = {
      user: 'Developer #101',
      certifications: ['Modern Frontend', 'Algorithms'],
      timestamp: Date.now()
    };
    
    return data;
  } catch (error) {
    if (error.name === 'AbortError') {
      throw new ApiError('Request timed out after ' + timeout + 'ms', 408);
    }
    throw error;
  } finally {
    clearTimeout(timeoutId);
  }
}

// Executing async function with try/catch
async function run() {
  try {
    console.log('Fetching user credential data...');
    const result = await fetchWithTimeout('/api/profile', { timeout: 2000 });
    console.log('Data fetched successfully:', result.user);
    console.log('Earned certifications:', result.certifications.join(', '));
  } catch (err) {
    console.error('Fetch failed:', err.message, 'Status:', err.statusCode);
  }
}

run();`,
      explanation: `Line 2: Custom ApiError subclass preserves stack traces and carries custom HTTP status codes.
Line 11: AbortController allows canceling stalled network requests automatically.
Line 31: finally block guarantees clearTimeout is called regardless of success or failure.
Line 35: async/await converts asynchronous promise flows into readable synchronous-looking code.`,
      previewOutput: `Fetching user credential data...
Data fetched successfully: Developer #101
Earned certifications: Modern Frontend, Algorithms`
    }
  ],
  exercises: [
    {
      id: 'advjs-ex-1',
      title: 'Practice 1: Immutable State Updater with Spread & Rest',
      difficulty: 'Easy',
      type: 'javascript',
      problemStatement: 'Write a function updateStudentProfile(currentProfile, updates) that updates a nested student object immutably using the spread operator, without mutating the original object.',
      requirements: [
        'Do not mutate currentProfile (verify Object.is(returned, currentProfile) is false)',
        'Support updating top-level properties (e.g. name, email)',
        'Support shallow-merging nested preferences: updates.preferences should merge with currentProfile.preferences without erasing existing keys',
        'Support adding items to skills array: if updates.newSkills is provided, append new skills without duplicates',
        'Return the newly constructed updated profile object'
      ],
      starterCode: `function updateStudentProfile(currentProfile, updates) {
  // Return a new object with immutable updates
  
}

const original = {
  id: 101,
  name: 'Dev',
  preferences: { theme: 'light', emailNotifications: true },
  skills: ['HTML', 'CSS']
};

const updated = updateStudentProfile(original, {
  name: 'Dev Sharma',
  preferences: { theme: 'dark' },
  newSkills: ['JavaScript', 'HTML']
});

console.log('Updated:', updated);
console.log('Is Original Mutated?:', original.name === updated.name);`,
      expectedBehavior: 'Returns a cloned object with updated fields and merged preferences without mutating the input object.',
      hints: [
        'Use { ...currentProfile, ...updates } for shallow copies.',
        'For nested preferences: preferences: { ...currentProfile.preferences, ...updates.preferences }',
        'Use Array.from(new Set([...currentProfile.skills, ...updates.newSkills])) to combine arrays without duplicates.'
      ],
      solution: `function updateStudentProfile(currentProfile, updates = {}) {
  if (!currentProfile || typeof currentProfile !== 'object') {
    throw new Error('currentProfile must be a valid object');
  }

  const { preferences = {}, newSkills = [], ...topLevelUpdates } = updates;

  // Merge preferences immutably
  const mergedPreferences = {
    ...(currentProfile.preferences || {}),
    ...preferences
  };

  // Merge skills without duplicates
  const existingSkills = currentProfile.skills || [];
  const mergedSkills = Array.from(new Set([...existingSkills, ...newSkills]));

  return {
    ...currentProfile,
    ...topLevelUpdates,
    preferences: mergedPreferences,
    skills: mergedSkills,
    updatedAt: new Date().toISOString()
  };
}

const original = {
  id: 101,
  name: 'Dev',
  preferences: { theme: 'light', emailNotifications: true },
  skills: ['HTML', 'CSS']
};

const updated = updateStudentProfile(original, {
  name: 'Dev Sharma',
  preferences: { theme: 'dark' },
  newSkills: ['JavaScript', 'HTML']
});

console.log('Updated Profile:', updated);
console.log('Is original mutated?:', original === updated); // false`,
      solutionExplanation: `1. Uses object destructuring to extract preferences and newSkills while collecting remaining fields into topLevelUpdates.
2. Clones preferences with { ...currentProfile.preferences, ...preferences } so existing settings like emailNotifications are not erased.
3. new Set([...existing, ...newSkills]) cleanly removes duplicates when adding 'HTML' and 'JavaScript'.
4. Returns a new object reference, satisfying React's core immutability contract.`
    },
    {
      id: 'advjs-ex-2',
      title: 'Practice 2: Secure API Rate Limiter using Closures',
      difficulty: 'Easy',
      type: 'javascript',
      problemStatement: 'Write a higher-order function createRateLimiter(fn, limit, intervalMs) that uses closures to limit how many times an inner function can be called within a time window.',
      requirements: [
        'Function accepts fn (target function), limit (max calls), and intervalMs (time window in ms)',
        'Returns a wrapped function that tracks call timestamps inside its closure scope',
        'If the caller attempts more than limit calls within intervalMs, reject execution and return { success: false, error: "Rate limit exceeded" }',
        'If within limit, invoke fn(...args) and return { success: true, result: <returned value> }',
        'State (call count or timestamps) must be completely private to the closure'
      ],
      starterCode: `function createRateLimiter(fn, limit, intervalMs) {
  // Store private timestamp history in closure
  
  return function(...args) {
    // Check limit and execute fn or reject
  };
}

// Test function
const submitForm = (username) => \`Saved submission for \${username}\`;
const limitedSubmit = createRateLimiter(submitForm, 2, 1000);

console.log(limitedSubmit('Alice')); // success: true
console.log(limitedSubmit('Bob'));   // success: true
console.log(limitedSubmit('Charlie')); // success: false, rate limit exceeded`,
      expectedBehavior: 'First 2 calls within interval succeed; the 3rd call immediately returns rate limit exceeded.',
      hints: [
        'Store an array of timestamps inside createRateLimiter: const callTimestamps = [];',
        'On each invocation: filter timestamps older than Date.now() - intervalMs.',
        'If remaining timestamps length >= limit, return rate limit exceeded.'
      ],
      solution: `function createRateLimiter(fn, limit, intervalMs) {
  if (typeof fn !== 'function') {
    throw new Error('First argument must be a function');
  }

  // Private closure state
  const callTimestamps = [];

  return function rateLimitedWrapper(...args) {
    const now = Date.now();

    // Remove timestamps that have fallen outside the active sliding window
    while (callTimestamps.length > 0 && callTimestamps[0] <= now - intervalMs) {
      callTimestamps.shift();
    }

    if (callTimestamps.length >= limit) {
      const waitTimeMs = intervalMs - (now - callTimestamps[0]);
      return {
        success: false,
        error: 'Rate limit exceeded. Please try again in ' + Math.ceil(waitTimeMs / 1000) + 's.',
        limit,
        activeCalls: callTimestamps.length
      };
    }

    callTimestamps.push(now);
    const result = fn.apply(this, args);

    return {
      success: true,
      result,
      remainingCalls: limit - callTimestamps.length
    };
  };
}

const submitForm = (username) => \`Saved submission for \${username}\`;
const limitedSubmit = createRateLimiter(submitForm, 2, 1000);

console.log(limitedSubmit('Alice'));
console.log(limitedSubmit('Bob'));
console.log(limitedSubmit('Charlie'));`,
      solutionExplanation: `1. callTimestamps is stored in the lexical environment of createRateLimiter, inaccessible to outside tampering.
2. Uses a sliding window algorithm: timestamps older than now - intervalMs are evicted via shift().
3. If active calls reach limit, the wrapper intercepts execution before calling the underlying function.
4. Returns uniform outcome objects with success booleans and descriptive error messages.`
    },
    {
      id: 'advjs-ex-3',
      title: 'Practice 3: Asynchronous Data Fetcher with Exponential Backoff Retry',
      difficulty: 'Medium',
      type: 'javascript',
      problemStatement: 'Write an asynchronous function fetchWithRetry(taskFn, maxRetries, delayMs) that executes an async task, automatically retrying on failure with exponential backoff before throwing the final error.',
      requirements: [
        'taskFn is an async function that returns a Promise',
        'If taskFn succeeds, immediately return the resolved value',
        'If taskFn throws, retry up to maxRetries times (default: 3)',
        'Use exponential backoff: delay doubles after each failed attempt (delayMs * 2^attempt)',
        'Log each failed attempt: "Attempt {N} failed. Retrying in {X}ms..."',
        'If all retries fail, throw the error from the final attempt with message prefixed by "Operation failed after {maxRetries} retries:"'
      ],
      starterCode: `async function fetchWithRetry(taskFn, maxRetries = 3, delayMs = 100) {
  // Implement retry loop with exponential backoff
  
}

// Mock failing task
let attempts = 0;
const mockFlakyApi = async () => {
  attempts++;
  if (attempts < 3) throw new Error('Network timeout (503)');
  return { status: 200, data: 'Course catalog loaded!' };
};

fetchWithRetry(mockFlakyApi, 4, 50).then(console.log).catch(console.error);`,
      expectedBehavior: 'Function logs retry attempts with exponentially increasing pauses and recovers when taskFn eventually resolves.',
      hints: [
        'Use a for loop: for (let attempt = 1; attempt <= maxRetries; attempt++)',
        'Use await new Promise(r => setTimeout(r, currentDelay)) to pause execution.',
        'Calculate delay: delayMs * Math.pow(2, attempt - 1)'
      ],
      solution: `async function fetchWithRetry(taskFn, maxRetries = 3, delayMs = 100) {
  let lastError;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const result = await taskFn();
      return result;
    } catch (err) {
      lastError = err;
      
      if (attempt === maxRetries) {
        break;
      }

      // Calculate exponential backoff delay: delay * 2^(attempt - 1)
      const currentDelay = delayMs * Math.pow(2, attempt - 1);
      console.log(\`Attempt \${attempt} failed (\${err.message}). Retrying in \${currentDelay}ms...\`);

      await new Promise(resolve => setTimeout(resolve, currentDelay));
    }
  }

  const finalError = new Error(\`Operation failed after \${maxRetries} retries: \${lastError.message}\`);
  finalError.originalError = lastError;
  throw finalError;
}

// Demonstration
let attempts = 0;
const mockFlakyApi = async () => {
  attempts++;
  if (attempts < 3) throw new Error('503 Service Unavailable');
  return { status: 200, data: 'Course catalog loaded successfully!' };
};

fetchWithRetry(mockFlakyApi, 4, 50)
  .then(res => console.log('Resolved Result:', res))
  .catch(err => console.error('Caught Failure:', err.message));`,
      solutionExplanation: `1. The for-loop attempts execution up to maxRetries.
2. If taskFn resolves without error, it returns immediately, saving unnecessary latency.
3. On failure, it calculates Math.pow(2, attempt - 1) to implement exponential backoff (e.g. 50ms, 100ms, 200ms).
4. After exhausting all retries, it raises an informative Error carrying the original failure trace.`
    },
    {
      id: 'advjs-ex-4',
      title: 'Practice 4: Parallel Data Aggregator with Promise.allSettled()',
      difficulty: 'Medium',
      type: 'javascript',
      problemStatement: 'Write an asynchronous function aggregateDashboardData(promisesMap) that accepts an object mapping keys to Promises, executes them concurrently using Promise.allSettled, and returns a unified summary report.',
      requirements: [
        'Accepts an object of promises, e.g. { user: fetchUser(), stats: fetchStats(), notifications: fetchNotes() }',
        'Execute all promises in parallel without failing if one rejects (unlike Promise.all)',
        'Return an object with: { data: {}, errors: {}, summary: { total, succeeded, failed } }',
        'succeeded results are mapped by key into result.data',
        'rejected reasons are mapped by key into result.errors',
        'Summary accurately reports counts of total, succeeded, and failed promises'
      ],
      starterCode: `async function aggregateDashboardData(promisesMap) {
  // Execute promises concurrently with Promise.allSettled
  
}

// Sample tests
const tasks = {
  profile: Promise.resolve({ username: 'Maya' }),
  grades: Promise.reject(new Error('Grades service offline')),
  rank: Promise.resolve({ rank: 14 })
};

aggregateDashboardData(tasks).then(console.log);`,
      expectedBehavior: 'Returns an aggregated object separating fulfilled values from rejection errors with accurate summary metrics.',
      hints: [
        'Get keys and promises: const keys = Object.keys(promisesMap); const promises = Object.values(promisesMap);',
        'Use const results = await Promise.allSettled(promises);',
        'Inspect results[index].status === "fulfilled" (use .value) vs "rejected" (use .reason).'
      ],
      solution: `async function aggregateDashboardData(promisesMap = {}) {
  const keys = Object.keys(promisesMap);
  const promises = Object.values(promisesMap);

  const settledResults = await Promise.allSettled(promises);

  const data = {};
  const errors = {};
  let succeeded = 0;
  let failed = 0;

  settledResults.forEach((outcome, index) => {
    const key = keys[index];

    if (outcome.status === 'fulfilled') {
      data[key] = outcome.value;
      succeeded++;
    } else {
      errors[key] = outcome.reason instanceof Error 
        ? outcome.reason.message 
        : String(outcome.reason);
      failed++;
    }
  });

  return {
    data,
    errors,
    summary: {
      total: keys.length,
      succeeded,
      failed
    }
  };
}

// Test Demonstration
const tasks = {
  profile: Promise.resolve({ username: 'Maya', role: 'Student' }),
  grades: Promise.reject(new Error('Grades service database timeout')),
  rank: Promise.resolve({ globalRank: 14, percentile: 98.5 })
};

aggregateDashboardData(tasks).then(report => {
  console.log('Aggregated Report:', JSON.stringify(report, null, 2));
});`,
      solutionExplanation: `1. Promise.allSettled() prevents a single rejecting service from crashing the whole dashboard.
2. Iterates over settled outcomes, checking outcome.status ('fulfilled' vs 'rejected').
3. Normalizes errors into readable string messages.
4. Generates a breakdown with succeeded and failed metrics, enabling resilient UI component rendering.`
    },
    {
      id: 'advjs-ex-5',
      title: 'Practice 5: Custom EventEmitter & Microtask Event Queue',
      difficulty: 'Hard',
      type: 'javascript',
      problemStatement: 'Implement an enterprise-grade EventEmitter class supporting on(), once(), emit(), off(), and emitAsyncMicrotask() which dispatches events asynchronously on the JavaScript microtask queue using queueMicrotask.',
      requirements: [
        'Method on(event, callback): registers a listener and returns an unsubscribe function',
        'Method once(event, callback): listener is invoked at most once, then automatically unregisters itself',
        'Method emit(event, ...args): synchronously calls all registered listeners in registration order',
        'Method off(event, callback): removes a specific registered listener',
        'Method emitAsyncMicrotask(event, ...args): schedules execution of listeners using queueMicrotask() so they execute after current synchronous call stack clears',
        'Method listenerCount(event): returns the number of active listeners for that event'
      ],
      starterCode: `class EventEmitter {
  constructor() {
    this.events = new Map();
  }

  on(event, callback) {
    // Register listener and return unsubscribe function
  }

  once(event, callback) {
    // Register single-use listener
  }

  emit(event, ...args) {
    // Call listeners synchronously
  }

  emitAsyncMicrotask(event, ...args) {
    // Schedule listeners on microtask queue
  }

  off(event, callback) {
    // Remove listener
  }

  listenerCount(event) {
    // Return count of listeners
  }
}`,
      expectedBehavior: 'A robust event emitter class with support for one-time subscriptions, unsubscribe callbacks, and microtask queue scheduling.',
      hints: [
        'Use Map<string, Set<Function>> or Map<string, Array<Function>> to store event handlers.',
        'In once(), create a wrapper: const wrapper = (...args) => { this.off(event, wrapper); callback(...args); }',
        'Use queueMicrotask(() => this.emit(event, ...args)) for emitAsyncMicrotask.'
      ],
      solution: `class EventEmitter {
  constructor() {
    this._events = new Map();
  }

  on(event, callback) {
    if (typeof callback !== 'function') {
      throw new TypeError('Listener must be a function');
    }

    if (!this._events.has(event)) {
      this._events.set(event, []);
    }

    this._events.get(event).push(callback);

    // Return an unsubscribe function
    return () => this.off(event, callback);
  }

  once(event, callback) {
    if (typeof callback !== 'function') {
      throw new TypeError('Listener must be a function');
    }

    const onceWrapper = (...args) => {
      this.off(event, onceWrapper);
      callback.apply(this, args);
    };

    // Store reference to original callback for accurate off() removal
    onceWrapper.originalCallback = callback;
    return this.on(event, onceWrapper);
  }

  emit(event, ...args) {
    if (!this._events.has(event)) return false;

    // Clone array to safely handle listeners that call off() during emission
    const listeners = [...this._events.get(event)];
    for (const listener of listeners) {
      try {
        listener.apply(this, args);
      } catch (err) {
        console.error(\`Error in event listener for "\${event}":\`, err);
      }
    }

    return true;
  }

  emitAsyncMicrotask(event, ...args) {
    // Schedules event on the JavaScript microtask queue
    queueMicrotask(() => {
      this.emit(event, ...args);
    });
  }

  off(event, callback) {
    if (!this._events.has(event)) return this;

    const listeners = this._events.get(event);
    const filtered = listeners.filter(
      cb => cb !== callback && cb.originalCallback !== callback
    );

    if (filtered.length === 0) {
      this._events.delete(event);
    } else {
      this._events.set(event, filtered);
    }

    return this;
  }

  listenerCount(event) {
    if (!this._events.has(event)) return 0;
    return this._events.get(event).length;
  }
}

// Test verification
const emitter = new EventEmitter();
const unsubscribe = emitter.on('challengeSolved', (id) => console.log('Solved challenge:', id));
emitter.once('challengeSolved', () => console.log('First solve bonus badge unlocked!'));

emitter.emit('challengeSolved', 101);
emitter.emit('challengeSolved', 102);
unsubscribe();
emitter.emit('challengeSolved', 103); // Nothing logged!`,
      solutionExplanation: `1. Map<string, Array<Function>> stores listeners per event key with O(1) event lookups.
2. on() returns a closure unsubscribe function for clean lifecycle cleanup in components.
3. once() wraps the callback in a function that automatically calls off() prior to execution.
4. emit() clones the listener array [...listeners] to prevent mutation bugs if a listener unsubscribes while the loop executes.
5. queueMicrotask() leverages the JavaScript event loop microtask queue to defer execution until synchronous tasks complete.`
    }
  ]
};
