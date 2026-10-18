export const reactTopic = {
  id: 'react',
  title: 'React',
  shortTitle: 'React',
  icon: 'Atom',
  description: 'Master React component architecture. Learn modern JSX rules, functional components, props drilling & composition, useState hook state mechanics, synthetic event handling, conditional rendering, list keys, and modern styling patterns.',
  subtopics: [
    'Introduction to React & Virtual DOM reconciliation',
    'Modern project environment setup (Vite vs CRA)',
    'JSX syntax rules (single root, className, htmlFor, self-closing tags, {} interpolation)',
    'Functional components: structure, purity, and reusable composition',
    'Props: passing data, destructuring, default props, callback functions, children prop',
    'State management with useState: initial state, setter functions, updater callbacks',
    'State immutability rules: updating arrays and nested objects without mutation',
    'Synthetic events: onClick, onChange, onSubmit, preventDefault, controlled inputs',
    'Conditional rendering techniques: ternary operators, logical AND (&&), early returns',
    'Lists and keys: array mapping, stable unique keys vs array index anti-patterns',
    'Styling React components: inline styles, CSS modules, Tailwind CSS, styled components'
  ],
  theory: [
    {
      title: '1. React Fundamentals: Declarative UI & The Virtual DOM',
      content: `React is a component-driven JavaScript library for building user interfaces. Instead of manually querying and updating DOM elements with \`document.querySelector\`, in React you declare **how the UI should look based on the current state**, and React efficiently computes the minimal DOM updates via its **Reconciliation** algorithm and **Virtual DOM (VDOM)**.

### The Component Mental Model:
A React component is simply a JavaScript function that takes **Props** (inputs) and returns **JSX** (UI description).

\`\`\`jsx
function WelcomeCard({ studentName, track = 'Frontend' }) {
  return (
    <div className="card">
      <h2>Welcome, {studentName}!</h2>
      <p>Enrolled in: {track}</p>
    </div>
  );
}
\`\`\`

### Fundamental JSX Rules:
1. **Single Root Element**: Return elements must be wrapped in a parent tag or Fragment (\`<>\` ... \`</>\`).
2. **Close All Tags**: All tags must explicitly self-close (\`<img />\`, \`<input />\`, \`<br />\`).
3. **CamelCase Attributes**: Use \`className\` instead of \`class\`, \`htmlFor\` instead of \`for\`, and \`onClick\` instead of \`onclick\`.
4. **JavaScript Expressions in Braces**: Any valid JS expression (variables, functions, ternary operators) can be embedded inside \`{ ... }\`.`
    },
    {
      title: '2. Props, State & The useState Hook',
      content: `Understanding the difference between **Props** and **State** is the core of mastering React:

- **Props (Properties)**: Read-only inputs passed from a parent component down to a child. A child component must never mutate its props.
- **State**: Private, internal data managed within the component that can change over time in response to user actions or network events. When state changes, React automatically re-renders the component.

### The useState Hook in Action:
\`\`\`jsx
import React, { useState } from 'react';

function Counter() {
  // Declare state variable count with initial value 0
  const [count, setCount] = useState(0);

  // Always use the updater callback form when new state depends on previous state!
  const increment = () => setCount(prevCount => prevCount + 1);
  const reset = () => setCount(0);

  return (
    <div>
      <p>Current Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}
\`\`\`

### Immutability Rule for Arrays & Objects:
Never mutate state directly! Always create a new reference:
\`\`\`jsx
// WRONG: items.push(newItem); setItems(items); -> React will NOT re-render!
// CORRECT:
setItems(prevItems => [...prevItems, newItem]);

// WRONG: user.age = 25; setUser(user);
// CORRECT:
setUser(prevUser => ({ ...prevUser, age: 25 }));
\`\`\``
    },
    {
      title: '3. Lists, Keys & Conditional Rendering',
      content: `When rendering collections of data or conditional views:

### Rendering Lists with Stable Keys:
\`\`\`jsx
const topics = [
  { id: 't1', title: 'HTML5 Semantics' },
  { id: 't2', title: 'CSS Grid & Flexbox' }
];

function TopicList() {
  return (
    <ul>
      {topics.map(topic => (
        <li key={topic.id}>{topic.title}</li>
      ))}
    </ul>
  );
}
\`\`\`
**Why unique keys matter**: React uses the \`key\` prop to match existing DOM nodes across renders. Using array index (\`key={index}\`) breaks component state and input focus if items are added, removed, or re-ordered!

### Conditional Rendering Patterns:
1. **Ternary Operator** (\`condition ? <TrueView /> : <FalseView />\`):
   \`\`\`jsx
   {isEnrolled ? <DashboardButton /> : <EnrollButton />}
   \`\`\`
2. **Logical AND** (\`condition && <Component />\`):
   \`\`\`jsx
   {hasUnreadNotifications && <NotificationBadge count={unreadCount} />}
   \`\`\`
3. **Early Return**:
   \`\`\`jsx
   if (isLoading) return <LoadingSpinner />;
   if (error) return <ErrorMessage message={error} />;
   return <MainContent data={data} />;
   \`\`\``
    }
  ],
  examples: [
    {
      title: 'Example: Controlled Search Input with Live Filtered List',
      code: `import React, { useState } from 'react';

const CHALLENGES = [
  { id: 1, name: 'Two Sum Problem', category: 'Algorithms', difficulty: 'Easy' },
  { id: 2, name: 'Responsive Navbar', category: 'Frontend', difficulty: 'Easy' },
  { id: 3, name: 'Custom React Hook', category: 'React', difficulty: 'Medium' },
  { id: 4, name: 'Binary Tree Traversal', category: 'Data Structures', difficulty: 'Hard' }
];

export default function ChallengeSearch() {
  const [query, setQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');

  // Derived filtered state on every render (no duplicate useEffect needed!)
  const filtered = CHALLENGES.filter(item => {
    const matchesSearch = item.name.toLowerCase().includes(query.toLowerCase());
    const matchesCategory = selectedCategory === 'All' || item.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div style={{ maxWidth: 450, margin: '20px auto', fontFamily: 'sans-serif' }}>
      <h3>Search Challenges</h3>
      
      {/* Controlled Search Input */}
      <input
        type="text"
        placeholder="Filter by challenge name..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ width: '100%', padding: '8px 12px', boxSizing: 'border-box', marginBottom: 12 }}
      />

      {/* Category Filter Pills */}
      <div style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        {['All', 'Frontend', 'React', 'Algorithms', 'Data Structures'].map(cat => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            style={{
              padding: '4px 10px',
              borderRadius: 6,
              border: '1px solid #cbd5e1',
              background: selectedCategory === cat ? '#16a34a' : '#f1f5f9',
              color: selectedCategory === cat ? '#fff' : '#334155',
              cursor: 'pointer'
            }}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Results Count & List */}
      <p style={{ fontSize: 13, color: '#64748b' }}>Showing {filtered.length} challenges</p>
      
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {filtered.map(ch => (
          <li
            key={ch.id}
            style={{
              padding: '10px 14px',
              border: '1px solid #e2e8f0',
              borderRadius: 8,
              marginBottom: 8,
              display: 'flex',
              justifyContent: 'space-between'
            }}
          >
            <span>{ch.name}</span>
            <strong style={{ color: '#16a34a' }}>{ch.difficulty}</strong>
          </li>
        ))}
      </ul>
    </div>
  );
}`,
      explanation: `Line 11: query and selectedCategory useState hooks store user filtering state.
Line 15: filtered challenges are computed directly during render without unnecessary synchronization useEffects.
Line 25: The search input is a controlled component: value is tied to state, and onChange updates state.
Line 48: Array.map uses stable unique item.id keys for efficient DOM reconciliation.`,
      previewHtml: `<div style="font-family: sans-serif; max-width: 420px; margin: 0 auto; padding: 16px; background: white; border-radius: 8px; border: 1px solid #cbd5e1;">
  <div style="font-weight: bold; font-size: 15px; margin-bottom: 8px; color: #0f172a;">Search Challenges</div>
  <input type="text" placeholder="Filter by challenge name..." value="React" style="width: 100%; padding: 8px 12px; border: 1px solid #16a34a; border-radius: 6px; box-sizing: border-box; margin-bottom: 10px;" readonly />
  <div style="display: flex; gap: 6px; margin-bottom: 12px;">
    <span style="background: #f1f5f9; padding: 3px 8px; border-radius: 4px; font-size: 11px;">All</span>
    <span style="background: #16a34a; color: white; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">React</span>
  </div>
  <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 12px; display: flex; justify-content: space-between; font-size: 13px;">
    <span>Custom React Hook</span>
    <span style="color: #16a34a; font-weight: bold;">Medium</span>
  </div>
</div>`
    }
  ],
  exercises: [
    {
      id: 'react-ex-1',
      title: 'Practice 1: Interactive Star Rating Component with Props & State',
      difficulty: 'Easy',
      type: 'react',
      problemStatement: 'Create an interactive, accessible StarRating component that displays 5 stars. Users can click on a star to set the rating, hover over stars to see a preview rating, and clear the rating by clicking on the active star.',
      requirements: [
        'Component accepts props: maxStars (default: 5) and onRatingChange callback function',
        'Use useState to store current rating (number) and hoverRating (number)',
        'Render maxStars clickable star buttons',
        'When hovering over star index i, update hoverRating so all stars up to i highlight',
        'When mouse leaves star container, reset hoverRating to 0',
        'When star i is clicked: if already rated i, toggle rating to 0, otherwise set rating to i and call onRatingChange(newRating)',
        'Display text below: "You rated this {rating} out of {maxStars} stars"'
      ],
      starterCode: `import React, { useState } from 'react';

export default function StarRating({ maxStars = 5, onRatingChange }) {
  // Implement state for rating and hoverRating
  
  return (
    <div className="star-rating">
      {/* Render star buttons */}
      
    </div>
  );
}`,
      expectedBehavior: 'A star rating component with interactive hover preview, click selection, rating toggle, and feedback text.',
      hints: [
        'Use Array.from({ length: maxStars }, (_, i) => i + 1) to create an array of star numbers [1, 2, 3, 4, 5].',
        'The active displayed star level is: hoverRating || rating.',
        'Use onMouseEnter={() => setHoverRating(starValue)} and onMouseLeave={() => setHoverRating(0)}.'
      ],
      solution: `import React, { useState } from 'react';

export default function StarRating({ maxStars = 5, onRatingChange }) {
  const [rating, setRating] = useState(0);
  const [hoverRating, setHoverRating] = useState(0);

  const handleStarClick = (starValue) => {
    const newRating = starValue === rating ? 0 : starValue;
    setRating(newRating);
    if (typeof onRatingChange === 'function') {
      onRatingChange(newRating);
    }
  };

  const activeLevel = hoverRating || rating;
  const starsArray = Array.from({ length: maxStars }, (_, i) => i + 1);

  return (
    <div style={{ fontFamily: 'sans-serif', padding: 16, textAlign: 'center', maxWidth: 320, margin: '0 auto' }}>
      <div 
        onMouseLeave={() => setHoverRating(0)}
        style={{ display: 'inline-flex', gap: 6, cursor: 'pointer' }}
        role="group"
        aria-label="Star Rating"
      >
        {starsArray.map((starNum) => {
          const isFilled = starNum <= activeLevel;
          return (
            <button
              key={starNum}
              type="button"
              onClick={() => handleStarClick(starNum)}
              onMouseEnter={() => setHoverRating(starNum)}
              aria-label={\`Rate \${starNum} out of \${maxStars} stars\`}
              style={{
                background: 'none',
                border: 'none',
                fontSize: 28,
                cursor: 'pointer',
                color: isFilled ? '#eab308' : '#cbd5e1',
                transition: 'transform 0.15s ease, color 0.15s ease',
                transform: starNum <= hoverRating ? 'scale(1.2)' : 'scale(1)',
                padding: 0
              }}
            >
              ★
            </button>
          );
        })}
      </div>

      <div style={{ marginTop: 10, fontSize: 14, color: '#475569', fontWeight: 600 }}>
        {rating > 0 
          ? \`You rated this \${rating} out of \${maxStars} stars\`
          : 'Click on a star to leave your rating'}
      </div>
    </div>
  );
}`,
      solutionExplanation: `1. rating tracks the persistent user selection, while hoverRating provides instant visual preview feedback.
2. activeLevel = hoverRating || rating ensures that mouse hover temporarily supersedes clicked selection.
3. handleStarClick toggles rating to 0 if the student clicks the currently selected score.
4. starNum <= hoverRating triggers a playful scale(1.2) transform for responsive tactile feel.`
    },
    {
      id: 'react-ex-2',
      title: 'Practice 2: Controlled Feedback Form with Live Character Counter',
      difficulty: 'Easy',
      type: 'react',
      problemStatement: 'Construct a controlled feedback submission form with text inputs, category dropdown, character counter, and real-time form validation.',
      requirements: [
        'Form state manages: name (string), category (string: "Bug", "Suggestion", "Praise"), and message (string)',
        'Message textarea has max length of 200 characters with a live remaining character counter: "{X} characters remaining"',
        'When characters remaining < 20, turn the counter text color red (#ef4444)',
        'Disable submit button unless name.trim().length >= 2 and message.trim().length >= 10',
        'On submit: prevent default reload, set isSubmitted: true, and reset form inputs'
      ],
      starterCode: `import React, { useState } from 'react';

export default function FeedbackForm() {
  // Define state for form fields and submit status
  
  return (
    <form className="feedback-form">
      {/* Controlled inputs, character counter, and submit button */}
      
    </form>
  );
}`,
      expectedBehavior: 'A controlled form where typing updates state live, character counter counts down, and submit button enables only when criteria are met.',
      hints: [
        'Remaining characters = 200 - message.length.',
        'Submit button disabled condition: name.trim().length < 2 || message.trim().length < 10.',
        'Use e.preventDefault() in onSubmit handler.'
      ],
      solution: `import React, { useState } from 'react';

export default function FeedbackForm() {
  const [name, setName] = useState('');
  const [category, setCategory] = useState('Suggestion');
  const [message, setMessage] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const MAX_CHARS = 200;
  const remainingChars = MAX_CHARS - message.length;
  const isFormValid = name.trim().length >= 2 && message.trim().length >= 10;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!isFormValid) return;

    setIsSubmitted(true);
    setName('');
    setMessage('');
    setCategory('Suggestion');
  };

  if (isSubmitted) {
    return (
      <div style={{ padding: 24, textAlign: 'center', background: '#f0fdf4', border: '1px solid #bbf7d0', borderRadius: 12, maxWidth: 400, margin: '20px auto' }}>
        <h4 style={{ color: '#166534', margin: '0 0 8px 0' }}>Feedback Received!</h4>
        <p style={{ color: '#15803d', fontSize: 14 }}>Thank you for helping us improve the Coding Challenge Platform.</p>
        <button 
          onClick={() => setIsSubmitted(false)}
          style={{ marginTop: 12, padding: '6px 14px', background: '#16a34a', color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer' }}
        >
          Send Another Feedback
        </button>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 420, margin: '20px auto', fontFamily: 'sans-serif', padding: 20, border: '1px solid #e2e8f0', borderRadius: 12, background: '#fff' }}>
      <h3 style={{ marginTop: 0, color: '#0f172a' }}>Student Feedback</h3>

      <div style={{ marginBottom: 14 }}>
        <label style={{ display: 'block', fontSize: 13, fontWeight: 'bold', color: '#334155', marginBottom: 4 }}>
          Your Name:
        </label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="e.g. Priyanshi"
          style={{ width: '100%', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: 6, boxSizing: 'border-box' }}
        />
      </div>

      <div style={{ marginBottom: 14 }}>
        <label style={{ display: 'block', fontSize: 13, fontWeight: 'bold', color: '#334155', marginBottom: 4 }}>
          Feedback Category:
        </label>
        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          style={{ width: '100%', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: 6, boxSizing: 'border-box' }}
        >
          <option value="Suggestion">Feature Suggestion</option>
          <option value="Bug">Bug Report</option>
          <option value="Praise">Praise &amp; Compliment</option>
        </select>
      </div>

      <div style={{ marginBottom: 16 }}>
        <label style={{ display: 'block', fontSize: 13, fontWeight: 'bold', color: '#334155', marginBottom: 4 }}>
          Feedback Message:
        </label>
        <textarea
          value={message}
          maxLength={MAX_CHARS}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Write your feedback here (min 10 chars)..."
          rows={4}
          style={{ width: '100%', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: 6, boxSizing: 'border-box', resize: 'vertical' }}
        />
        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 4, fontSize: 12, color: remainingChars < 20 ? '#ef4444' : '#64748b', fontWeight: remainingChars < 20 ? 'bold' : 'normal' }}>
          {remainingChars} characters remaining
        </div>
      </div>

      <button
        type="submit"
        disabled={!isFormValid}
        style={{
          width: '100%',
          padding: '10px 16px',
          background: isFormValid ? '#16a34a' : '#cbd5e1',
          color: '#ffffff',
          fontWeight: 'bold',
          border: 'none',
          borderRadius: 8,
          cursor: isFormValid ? 'pointer' : 'not-allowed',
          transition: 'background 0.2s'
        }}
      >
        Submit Feedback
      </button>
    </form>
  );
}`,
      solutionExplanation: `1. All inputs are controlled components tied to state (value={...} and onChange={...}).
2. remainingChars dynamically calculates available quota without duplicate state variables.
3. Conditional styling on remainingChars < 20 turns the text red to alert users before hitting the limit.
4. disabled={!isFormValid} natively prevents submissions until minimum validation lengths are satisfied.`
    },
    {
      id: 'react-ex-3',
      title: 'Practice 3: Filterable Task Tracker with Immutable State Updates',
      difficulty: 'Medium',
      type: 'react',
      problemStatement: 'Build a TaskTracker component that manages a list of tasks. Users can add new tasks, toggle task completion, delete tasks, and filter the view by "All", "Active", and "Completed".',
      requirements: [
        'Store tasks in state as array of { id, text, completed: boolean }',
        'Implement handleAddTask(text): generates unique ID (Date.now()) and appends task immutably using setTasks(prev => [...prev, newTask])',
        'Implement handleToggleTask(id): maps through tasks and flips completed property immutably',
        'Implement handleDeleteTask(id): filters out task by ID immutably',
        'Filter buttons ("All", "Active", "Completed") update activeFilter state, displaying only matching tasks',
        'Display empty state message if no tasks exist in the active filter'
      ],
      starterCode: `import React, { useState } from 'react';

export default function TaskTracker() {
  // State for tasks array, input text, and filter
  
  return (
    <div className="task-tracker">
      {/* Form, filter buttons, and tasks list */}
      
    </div>
  );
}`,
      expectedBehavior: 'A task management board with filter tabs, immutable status toggling, and clean task deletion.',
      hints: [
        'To toggle immutably: setTasks(prev => prev.map(t => t.id === id ? { ...t, completed: !t.completed } : t));',
        'To delete immutably: setTasks(prev => prev.filter(t => t.id !== id));',
        'Compute filteredTasks = tasks.filter(...) before rendering.'
      ],
      solution: `import React, { useState } from 'react';

const INITIAL_TASKS = [
  { id: 1, text: 'Review HTML5 semantic elements', completed: true },
  { id: 2, text: 'Build responsive grid with CSS', completed: false },
  { id: 3, text: 'Practice React useState hooks', completed: false }
];

export default function TaskTracker() {
  const [tasks, setTasks] = useState(INITIAL_TASKS);
  const [inputText, setInputText] = useState('');
  const [filter, setFilter] = useState('All');

  const handleAddTask = (e) => {
    e.preventDefault();
    if (!inputText.trim()) return;

    const newTask = {
      id: Date.now(),
      text: inputText.trim(),
      completed: false
    };

    setTasks(prev => [newTask, ...prev]);
    setInputText('');
  };

  const handleToggleTask = (id) => {
    setTasks(prev => prev.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
  };

  const handleDeleteTask = (id) => {
    setTasks(prev => prev.filter(t => t.id !== id));
  };

  const filteredTasks = tasks.filter(t => {
    if (filter === 'Active') return !t.completed;
    if (filter === 'Completed') return t.completed;
    return true; // 'All'
  });

  return (
    <div style={{ maxWidth: 440, margin: '20px auto', fontFamily: 'sans-serif', padding: 20, background: '#fff', border: '1px solid #e2e8f0', borderRadius: 16 }}>
      <h3 style={{ margin: '0 0 16px 0', color: '#0f172a' }}>Task Tracker</h3>

      {/* Add Task Input Form */}
      <form onSubmit={handleAddTask} style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Add a new task..."
          style={{ flex: 1, padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: 8 }}
        />
        <button
          type="submit"
          style={{ background: '#16a34a', color: '#fff', border: 'none', borderRadius: 8, padding: '8px 16px', fontWeight: 'bold', cursor: 'pointer' }}
        >
          Add
        </button>
      </form>

      {/* Filter Buttons */}
      <div style={{ display: 'flex', gap: 6, marginBottom: 14 }}>
        {['All', 'Active', 'Completed'].map(f => (
          <button
            key={f}
            onClick={() => setFilter(f)}
            style={{
              padding: '4px 12px',
              borderRadius: 20,
              fontSize: 12,
              fontWeight: 600,
              border: '1px solid #cbd5e1',
              background: filter === f ? '#16a34a' : '#f8fafc',
              color: filter === f ? '#fff' : '#475569',
              cursor: 'pointer'
            }}
          >
            {f}
          </button>
        ))}
      </div>

      {/* Tasks List */}
      {filteredTasks.length === 0 ? (
        <p style={{ textAlign: 'center', color: '#94a3b8', fontSize: 13, margin: '24px 0' }}>No tasks found in this view.</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
          {filteredTasks.map(task => (
            <li
              key={task.id}
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '10px 12px',
                borderBottom: '1px solid #f1f5f9',
                background: task.completed ? '#f8fafc' : 'transparent'
              }}
            >
              <label style={{ display: 'flex', alignItems: 'center', gap: 10, cursor: 'pointer', flex: 1 }}>
                <input
                  type="checkbox"
                  checked={task.completed}
                  onChange={() => handleToggleTask(task.id)}
                />
                <span style={{ textDecoration: task.completed ? 'line-through' : 'none', color: task.completed ? '#94a3b8' : '#1e293b', fontSize: 14 }}>
                  {task.text}
                </span>
              </label>

              <button
                onClick={() => handleDeleteTask(task.id)}
                aria-label="Delete task"
                style={{ background: 'none', border: 'none', color: '#ef4444', fontSize: 16, cursor: 'pointer', padding: '0 4px' }}
              >
                ×
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}`,
      solutionExplanation: `1. setTasks(prev => [newTask, ...prev]) prepends the newly created task without mutating the previous array.
2. setTasks(prev => prev.map(...)) produces a new array of objects, updating only the matched task.
3. setTasks(prev => prev.filter(...)) returns a new array with the target ID removed.
4. filteredTasks computes derived state on the fly based on filter tab selection.`
    },
    {
      id: 'react-ex-4',
      title: 'Practice 4: Reusable Modal Dialog with Children & Backdrop Click',
      difficulty: 'Medium',
      type: 'react',
      problemStatement: 'Construct a reusable Modal component in React that leverages composition (props.children). It must support opening/closing, a backdrop click to dismiss, and pressing the Escape key to close.',
      requirements: [
        'Modal accepts props: isOpen (boolean), onClose (callback function), title (string), and children (React nodes)',
        'If isOpen is false, return null (render nothing)',
        'When rendered, display an overlay backdrop covering the viewport with semi-transparent background',
        'Clicking the backdrop should trigger onClose(), but clicking inside the modal content must NOT close the modal (use e.stopPropagation())',
        'Add a close icon button in the modal header that invokes onClose()',
        'Render props.children inside the modal body'
      ],
      starterCode: `import React, { useEffect } from 'react';

export default function Modal({ isOpen, onClose, title, children }) {
  // Handle escape key listener and render modal
  
  if (!isOpen) return null;

  return (
    <div className="modal-backdrop">
      <div className="modal-card">
        {/* Modal header and children content */}
        
      </div>
    </div>
  );
}`,
      expectedBehavior: 'A modal popup with backdrop overlay, dismissible via backdrop click, close button, or Escape key.',
      hints: [
        'Use e.stopPropagation() on the inner modal box onClick to prevent bubbling to the backdrop.',
        'Use useEffect to add and clean up the "keydown" event listener for e.key === "Escape".',
        'Always check if (!isOpen) return null; at the top.'
      ],
      solution: `import React, { useEffect } from 'react';

export default function Modal({ isOpen, onClose, title = 'Notification', children }) {
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && typeof onClose === 'function') {
        onClose();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      onClick={onClose}
      style={{
        position: 'fixed',
        inset: 0,
        backgroundColor: 'rgba(15, 23, 42, 0.65)',
        backdropFilter: 'blur(4px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 9999,
        padding: 16
      }}
      role="dialog"
      aria-modal="true"
    >
      <div
        onClick={(e) => e.stopPropagation()} // Prevents closing when clicking inside
        style={{
          background: '#ffffff',
          borderRadius: 16,
          maxWidth: 480,
          width: '100%',
          boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.2)',
          overflow: 'hidden',
          animation: 'modalSlideIn 0.2s cubic-bezier(0.16, 1, 0.3, 1)'
        }}
      >
        {/* Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '16px 20px', borderBottom: '1px solid #f1f5f9' }}>
          <h3 style={{ margin: 0, fontSize: 17, color: '#0f172a', fontWeight: 700 }}>{title}</h3>
          <button
            onClick={onClose}
            aria-label="Close dialog"
            style={{ background: 'none', border: 'none', fontSize: 20, color: '#94a3b8', cursor: 'pointer', padding: '0 4px', lineHeight: 1 }}
          >
            ×
          </button>
        </div>

        {/* Content Body */}
        <div style={{ padding: '20px', color: '#334155', fontSize: 14, lineHeight: 1.6 }}>
          {children}
        </div>
      </div>
    </div>
  );
}`,
      solutionExplanation: `1. Component uses props.children, allowing any caller to pass rich custom markup into the modal.
2. e.stopPropagation() on the inner modal-card prevents click events from bubbling up to the backdrop container.
3. useEffect binds a global keydown listener to capture 'Escape' and cleans it up via return function to avoid memory leaks.
4. Early return if (!isOpen) return null; completely unmounts the overlay from the DOM.`
    },
    {
      id: 'react-ex-5',
      title: 'Practice 5: Dynamic Accordion FAQ with Single & Multi-Expand Modes',
      difficulty: 'Hard',
      type: 'react',
      problemStatement: 'Construct a reusable Accordion component that renders a list of collapsible FAQ items. Support both single-expand mode (opening one closes others) and multi-expand mode (multiple can be open simultaneously).',
      requirements: [
        'Component accepts props: items (array of { id, question, answer }) and allowMultiple (boolean, default: false)',
        'Store expanded state: use array or Set of active IDs in useState',
        'When an accordion header is clicked in single-expand mode: if active, collapse it; if inactive, set as the only active item',
        'When clicked in multi-expand mode: toggle the item\'s ID in the active set without affecting other items',
        'Render smooth chevron rotation indicator (rotate(180deg)) when an item is expanded',
        'Support keyboard accessibility with role="button" and aria-expanded attributes'
      ],
      starterCode: `import React, { useState } from 'react';

export default function Accordion({ items = [], allowMultiple = false }) {
  // State for active expanded item(s)
  
  return (
    <div className="accordion">
      {/* Map through items and render collapsible sections */}
      
    </div>
  );
}`,
      expectedBehavior: 'An accordion where questions toggle answers smoothly, respecting single or multi-expand modes.',
      hints: [
        'Store active IDs in an array: const [openIds, setOpenIds] = useState([]);',
        'In single mode: setOpenIds(prev => prev.includes(id) ? [] : [id]);',
        'In multi mode: setOpenIds(prev => prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]);'
      ],
      solution: `import React, { useState } from 'react';

export default function Accordion({ items = [], allowMultiple = false }) {
  const [openIds, setOpenIds] = useState([]);

  const toggleItem = (id) => {
    setOpenIds(prev => {
      const isOpen = prev.includes(id);

      if (allowMultiple) {
        return isOpen ? prev.filter(item => item !== id) : [...prev, id];
      } else {
        // Single expand mode
        return isOpen ? [] : [id];
      }
    });
  };

  if (!items || items.length === 0) {
    return <p style={{ color: '#94a3b8', textAlign: 'center' }}>No accordion items available.</p>;
  }

  return (
    <div style={{ maxWidth: 500, margin: '20px auto', fontFamily: 'sans-serif' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
        <h4 style={{ margin: 0, color: '#0f172a' }}>Frequently Asked Questions</h4>
        <span style={{ fontSize: 11, color: '#16a34a', fontWeight: 'bold' }}>
          {allowMultiple ? 'Multi-Expand' : 'Single-Expand'}
        </span>
      </div>

      <div style={{ border: '1px solid #e2e8f0', borderRadius: 12, overflow: 'hidden' }}>
        {items.map((item, index) => {
          const isOpen = openIds.includes(item.id);
          const isLast = index === items.length - 1;

          return (
            <div 
              key={item.id} 
              style={{ 
                borderBottom: isLast ? 'none' : '1px solid #e2e8f0',
                background: isOpen ? '#fcfdfc' : '#ffffff'
              }}
            >
              <button
                type="button"
                onClick={() => toggleItem(item.id)}
                aria-expanded={isOpen}
                style={{
                  width: '100%',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '16px 20px',
                  background: 'none',
                  border: 'none',
                  cursor: 'pointer',
                  textAlign: 'left'
                }}
              >
                <span style={{ fontWeight: 600, fontSize: 14, color: isOpen ? '#166534' : '#1e293b' }}>
                  {item.question}
                </span>
                <span
                  style={{
                    display: 'inline-block',
                    transition: 'transform 0.25s ease',
                    transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)',
                    color: isOpen ? '#16a34a' : '#94a3b8',
                    fontSize: 12
                  }}
                >
                  ▼
                </span>
              </button>

              {isOpen && (
                <div style={{ padding: '0 20px 16px 20px', color: '#475569', fontSize: 13, lineHeight: 1.6 }}>
                  {item.answer}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}`,
      solutionExplanation: `1. openIds stores an array of open item IDs, supporting both single and multi-expand paradigms cleanly.
2. In single mode, clicking an open item collapses it to [], and clicking a closed item returns [id].
3. In multi mode, array spreading and filtering seamlessly toggles individual items.
4. rotate(180deg) transition animates the chevron indicator smoothly without external icon libraries.`
    }
  ]
};
