export const advancedCssTopic = {
  id: 'advanced-css',
  title: 'Advanced CSS',
  shortTitle: 'Advanced CSS',
  icon: 'Layers',
  description: 'Master advanced modern layout systems, dynamic micro-interactions, hardware-accelerated animations, custom CSS properties, architectural methodologies, and cross-browser resilience.',
  subtopics: [
    'Flexbox deep-dive: axes, alignment, flex-grow, flex-shrink, flex-basis & gap',
    'CSS Grid architecture: explicit vs implicit grids, template areas, minmax(), auto-fit vs auto-fill',
    'Hybrid responsive layouts combining CSS Grid and Flexbox',
    'Transitions, timing functions (cubic-bezier, steps) and GPU-accelerated properties',
    'Keyframe animations (@keyframes, animation-fill-mode, iteration-count, alternate)',
    'Modern pseudo-classes (:is(), :where(), :has(), :not(), :focus-visible)',
    'Advanced pseudo-elements (::before, ::after, ::marker, ::selection)',
    'CSS Custom Properties (CSS variables) for dynamic system theming',
    'CSS architecture best practices (BEM naming, utility classes, specificity reduction)',
    'Browser compatibility, vendor prefixes, and @supports feature queries'
  ],
  theory: [
    {
      title: '1. Flexbox vs. CSS Grid: Choosing the Right Layout Engine',
      content: `Modern CSS provides two complementary two-dimensional and one-dimensional layout engines:

### Quick Comparison Matrix:
| Feature | Flexbox (\`display: flex\`) | CSS Grid (\`display: grid\`) |
| :--- | :--- | :--- |
| **Primary Dimension** | 1-Dimensional (Row OR Column) | 2-Dimensional (Rows AND Columns simultaneously) |
| **Content vs. Layout** | Content-first (items dictate size) | Layout-first (grid tracks dictate item placement) |
| **Best Used For** | Navbars, button groups, card headers, aligning items | Entire page layouts, image galleries, complex dashboards |

### Essential Flexbox Properties:
- **Container**: \`flex-direction\` (row/column), \`justify-content\` (main axis), \`align-items\` (cross axis), \`flex-wrap\`, \`gap\`.
- **Item**: \`flex: 1 1 auto\` (shorthand for \`flex-grow\`, \`flex-shrink\`, \`flex-basis\`), \`align-self\`, \`order\`.

### Essential CSS Grid Superpowers:
\`\`\`css
/* Automatic responsive grid without media queries! */
.responsive-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
\`\`\`
- **\`auto-fit\`**: Expands columns to fill the full container width.
- **\`minmax(280px, 1fr)\`**: Never lets a column shrink below 280px; when space allows, grows equally (\`1fr\`).`
    },
    {
      title: '2. Hardware-Accelerated Transitions & Keyframe Animations',
      content: `Smooth 60fps animations enhance user experience without introducing browser jank or high CPU usage.

### Performance Rule: The Composite-Only Properties
To avoid triggering expensive browser **Layout (Reflow)** and **Paint (Repaint)** stages, animate only properties handled directly by the GPU Compositor thread:
- \`transform\` (translate, scale, rotate)
- \`opacity\`

\`\`\`css
/* DO THIS: GPU accelerated */
.card {
  transition: transform 0.25s ease, opacity 0.25s ease;
}
.card:hover {
  transform: translateY(-6px);
  opacity: 0.95;
}

/* AVOID THIS: Triggers layout reflow on every single frame! */
.card-bad:hover {
  top: -6px; /* BAD */
  margin-top: -6px; /* BAD */
}
\`\`\`

### Defining Keyframe Sequences:
\`\`\`css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton-loader {
  background: linear-gradient(90deg, #f1f5f9 25%, #e2e8f0 50%, #f1f5f9 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
}
\`\`\``
    },
    {
      title: '3. CSS Variables & Real-Time Multi-Theme Systems',
      content: `CSS Custom Properties (Variables) allow dynamic values to cascade through the DOM hierarchy and update instantly via JavaScript or media queries.

\`\`\`css
:root {
  --color-primary: #16a34a;
  --color-primary-dark: #166534;
  --bg-surface: #ffffff;
  --text-main: #0f172a;
  --border-color: #e2e8f0;
}

/* Dark mode theme variables */
[data-theme="dark"] {
  --color-primary: #22c55e;
  --color-primary-dark: #15803d;
  --bg-surface: #0f172a;
  --text-main: #f8fafc;
  --border-color: #334155;
}

.theme-card {
  background-color: var(--bg-surface);
  color: var(--text-main);
  border: 1px solid var(--border-color);
  transition: background-color 0.3s ease, color 0.3s ease;
}
\`\`\``
    },
    {
      title: '4. Modern Selectors: :has(), :is(), and Feature Queries',
      content: `Modern CSS selectors simplify complex style rules and eliminate boilerplate JavaScript:

- **\`:has()\` (The Parent Selector)**: Styles a parent element based on its descendants!
  \`\`\`css
  /* Give card an emerald border if it contains an active checkbox */
  .card:has(input[type="checkbox"]:checked) {
    border-color: #16a34a;
    background-color: #f0fdf4;
  }
  \`\`\`
- **\`:is()\` & \`:where()\`**: Consolidate repetitive selector lists:
  \`\`\`css
  /* Instead of h1 a, h2 a, h3 a */
  :is(h1, h2, h3) a {
    color: #166534;
  }
  \`\`\`
- **\`@supports\` (Feature Queries)**: Provide progressive enhancement:
  \`\`\`css
  @supports (backdrop-filter: blur(10px)) {
    .glass-nav {
      backdrop-filter: blur(10px);
      background: rgba(255, 255, 255, 0.7);
    }
  }
  \`\`\``
    }
  ],
  examples: [
    {
      title: 'Example: Responsive Grid with Themed CSS Variables',
      code: `:root {
  --brand-green: #16a34a;
  --brand-dark: #166534;
  --card-bg: #ffffff;
  --text-primary: #0f172a;
  --text-secondary: #64748b;
  --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.grid-dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.metric-card {
  background: var(--card-bg);
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 20px;
  box-shadow: var(--card-shadow);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.metric-card:hover {
  transform: translateY(-4px);
  border-color: var(--brand-green);
}

.metric-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.metric-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background-color: #dcfce7;
  color: var(--brand-dark);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}`,
      explanation: `Line 1: :root defines reusable variables across the layout.
Line 10: grid-template-columns with auto-fit and minmax(260px, 1fr) creates an intrinsically responsive grid that re-flows across all screens without media queries.
Line 22: flex-direction: column with justify-content: space-between distributes content vertically.
Line 25: Hardware-accelerated transform: translateY with cubic-bezier easing provides smooth interactive feedback.`,
      previewHtml: `<div style="font-family: sans-serif; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; padding: 16px; background: #f8fafc; border-radius: 8px;">
  <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <span style="font-size: 12px; color: #64748b; font-weight: bold;">CHALLENGES SOLVED</span>
      <span style="background: #dcfce7; color: #166534; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: bold;">+14%</span>
    </div>
    <div style="font-size: 24px; font-weight: 800; color: #0f172a;">342</div>
  </div>
  <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <span style="font-size: 12px; color: #64748b; font-weight: bold;">GLOBAL RANK</span>
      <span style="background: #dcfce7; color: #166534; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: bold;">Top 5%</span>
    </div>
    <div style="font-size: 24px; font-weight: 800; color: #16a34a;">#128</div>
  </div>
</div>`
    }
  ],
  exercises: [
    {
      id: 'advcss-ex-1',
      title: 'Practice 1: Responsive Navigation Bar with Flexbox',
      difficulty: 'Easy',
      type: 'css',
      problemStatement: 'Construct a responsive application header navigation bar using Flexbox alignment. Align logo on the far left, menu links centered, and user actions on the far right.',
      requirements: [
        'Set .nav-container to display: flex, justify-content: space-between, and align-items: center',
        'Add padding of 14px 24px, background-color: #ffffff, and border-bottom: 1px solid #e2e8f0',
        'Style the navigation links list (.nav-links) with display: flex, list-style: none, and gap: 24px',
        'Style .action-group with display: flex, align-items: center, and gap: 12px',
        'Add a hover state on links with color: #16a34a and transition: color 0.2s ease'
      ],
      starterCode: `/* Style the Flexbox navigation bar below */
.nav-container {
  /* Flex container properties */
}

.nav-links {
  /* Flex items list with gap */
}

.nav-links a {
  text-decoration: none;
  color: #334155;
  font-weight: 600;
  font-size: 0.9375rem;
}

.action-group {
  /* Action buttons flex alignment */
}`,
      expectedBehavior: 'A balanced header with logo on left, links in center, action buttons on right, with smooth hover transitions.',
      hints: [
        'justify-content: space-between pushes the outer flex items to the left and right edges.',
        'Use gap: 24px; on the flex container rather than applying right margins to individual items.',
        'align-items: center vertically aligns all items to the middle line.'
      ],
      solution: `.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 24px;
  background-color: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.logo-brand {
  font-size: 1.25rem;
  font-weight: 800;
  color: #166534;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 28px;
  margin: 0;
  padding: 0;
}

.nav-links a {
  text-decoration: none;
  color: #475569;
  font-weight: 600;
  font-size: 0.9375rem;
  transition: color 0.2s ease;
}

.nav-links a:hover {
  color: #16a34a;
}

.action-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-signin {
  padding: 8px 18px;
  background-color: #16a34a;
  color: #ffffff;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  font-size: 0.875rem;
  transition: background-color 0.2s ease;
}

.btn-signin:hover {
  background-color: #15803d;
}`,
      solutionExplanation: `1. display: flex with justify-content: space-between separates the three primary sections across the header bar.
2. align-items: center ensures consistent vertical baseline across text, logo, and button elements.
3. gap: 28px replaces legacy margin hacks and prevents wrapping margin bugs.
4. transition: color 0.2s ease provides smooth interaction feedback.`
    },
    {
      id: 'advcss-ex-2',
      title: 'Practice 2: Shimmering Skeleton Loader Animation',
      difficulty: 'Easy',
      type: 'css',
      problemStatement: 'Build a smooth, continuous loading skeleton animation using CSS @keyframes and background-position translation to represent content while data is being fetched.',
      requirements: [
        'Define a @keyframes animation named shimmer',
        'In @keyframes shimmer, animate from background-position: -200% 0 to background-position: 200% 0',
        'Style .skeleton-card with a linear-gradient background from #f1f5f9 through #e2e8f0 back to #f1f5f9',
        'Set background-size: 200% 100% so the highlight band spans across the element',
        'Apply animation: shimmer 1.6s infinite linear',
        'Add border-radius: 8px to rounded skeleton bars'
      ],
      starterCode: `/* Write your @keyframes shimmer and skeleton styling below */
@keyframes shimmer {
  /* Animate background-position */
}

.skeleton-box {
  /* Linear gradient and animation properties */
}

.skeleton-title {
  height: 24px;
  width: 60%;
  margin-bottom: 12px;
}

.skeleton-text {
  height: 16px;
  width: 100%;
  margin-bottom: 8px;
}`,
      expectedBehavior: 'A soft gray box with a continuous light shimmer wave sweeping across from left to right.',
      hints: [
        'Use linear-gradient(90deg, #f1f5f9 25%, #e2e8f0 50%, #f1f5f9 75%);',
        'background-size: 200% 100% gives the gradient enough track distance to travel.',
        'animation: shimmer 1.6s infinite linear guarantees smooth, non-stopping looping.'
      ],
      solution: `@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}

.skeleton-box {
  background: linear-gradient(
    90deg,
    #f1f5f9 20%,
    #e2e8f0 40%,
    #e2e8f0 60%,
    #f1f5f9 80%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
  border-radius: 8px;
}

.skeleton-card {
  padding: 20px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  max-width: 380px;
}

.skeleton-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-bottom: 16px;
}

.skeleton-title {
  height: 20px;
  width: 70%;
  margin-bottom: 12px;
}

.skeleton-text {
  height: 14px;
  width: 100%;
  margin-bottom: 8px;
}

.skeleton-text.short {
  width: 45%;
}`,
      solutionExplanation: `1. @keyframes shimmer translates background-position horizontally from -200% to 200%.
2. The 90-degree linear-gradient with lighter stops in the middle creates the illusion of moving light reflection.
3. animation: shimmer 1.5s infinite linear ensures that the wave travels at constant velocity with zero pauses between loops.
4. Using background-position instead of DOM movement prevents layout thrashing.`
    },
    {
      id: 'advcss-ex-3',
      title: 'Practice 3: Responsive Magazine Grid with Named Areas',
      difficulty: 'Medium',
      type: 'css',
      problemStatement: 'Construct a responsive magazine layout using CSS Grid and grid-template-areas. The layout must display a featured lead article, two sidebar stories, and bottom metric cards, re-arranging seamlessly for mobile screens.',
      requirements: [
        'On mobile (base styles), .magazine-grid should use a single column layout with grid-template-areas: "featured" "sidebar" "metrics"',
        'Add a media query for @media (min-width: 900px)',
        'Inside the media query, define a 3-column, 2-row layout with grid-template-columns: 2fr 1fr and grid-template-areas: "featured sidebar" "metrics sidebar"',
        'Assign grid-area: featured to .featured-story',
        'Assign grid-area: sidebar to .sidebar-stories',
        'Assign grid-area: metrics to .metrics-bar',
        'Use gap: 24px between all grid cells'
      ],
      starterCode: `/* Mobile-first single column named areas */
.magazine-grid {
  display: grid;
  gap: 20px;
  grid-template-areas:
    "featured"
    "sidebar"
    "metrics";
}

.featured-story { grid-area: featured; }
.sidebar-stories { grid-area: sidebar; }
.metrics-bar { grid-area: metrics; }

/* Desktop 2-column layout with named grid areas */
@media (min-width: 900px) {
  .magazine-grid {
    /* Define 2-column grid template areas */
  }
}`,
      expectedBehavior: 'Single stacked column on mobile; transforms to an editorial magazine grid on desktop where the sidebar spans across both rows.',
      hints: [
        'On desktop: grid-template-columns: 2fr 1fr; defines the relative column widths.',
        'To make the sidebar span both rows, repeat "sidebar" in the second row: "metrics sidebar".',
        'Each item must declare its corresponding grid-area name matching the template.'
      ],
      solution: `.magazine-grid {
  display: grid;
  gap: 20px;
  max-width: 1140px;
  margin: 0 auto;
  padding: 16px;
  grid-template-areas:
    "featured"
    "sidebar"
    "metrics";
}

.featured-story {
  grid-area: featured;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 28px;
}

.sidebar-stories {
  grid-area: sidebar;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 24px;
}

.metrics-bar {
  grid-area: metrics;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  gap: 16px;
}

@media (min-width: 900px) {
  .magazine-grid {
    grid-template-columns: 2fr 1fr;
    grid-template-rows: auto auto;
    grid-template-areas:
      "featured sidebar"
      "metrics  sidebar";
    gap: 24px;
    padding: 32px 16px;
  }
}`,
      solutionExplanation: `1. grid-template-areas visualizes the layout structure directly in CSS syntax.
2. Writing "sidebar" in both row definitions ("featured sidebar" and "metrics sidebar") causes the sidebar item to automatically span across both rows.
3. 2fr 1fr gives the featured story double the width of the secondary sidebar column.
4. On mobile screens, the single-word row definitions cleanly stack elements in reading order.`
    },
    {
      id: 'advcss-ex-4',
      title: 'Practice 4: Dynamic Theme Switcher with CSS Custom Properties',
      difficulty: 'Medium',
      type: 'css',
      problemStatement: 'Implement a complete multi-token CSS custom property theming system supporting seamless light and dark mode switching with smooth color transitions.',
      requirements: [
        'Define default light theme tokens on :root: --bg-page (#f8fafc), --bg-card (#ffffff), --text-main (#0f172a), --text-sub (#64748b), --border (#e2e8f0), and --accent (#16a34a)',
        'Define dark theme overrides on [data-theme="dark"]: --bg-page (#090d16), --bg-card (#111827), --text-main (#f9fafb), --text-sub (#9ca3af), --border (#1f2937), and --accent (#22c55e)',
        'Style body with background-color: var(--bg-page) and color: var(--text-main)',
        'Style .theme-box with background: var(--bg-card), border: 1px solid var(--border), and color: var(--text-main)',
        'Apply transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease to body and cards for smooth transition'
      ],
      starterCode: `/* Define :root light theme variables */
:root {
  /* Light theme tokens */
}

/* Define [data-theme="dark"] tokens */
[data-theme="dark"] {
  /* Dark theme overrides */
}

body {
  /* Use variables and smooth transition */
}

.theme-box {
  /* Card using themed variables */
}`,
      expectedBehavior: 'A theme system where switching the data-theme attribute on <html> instantly transitions card backgrounds, borders, and text colors smoothly.',
      hints: [
        'Use CSS var() function: background-color: var(--bg-card);',
        'Place [data-theme="dark"] on the same selector level or as an attribute selector on html/body.',
        'Add transitions to the styled elements to prevent abrupt color popping.'
      ],
      solution: `:root {
  --bg-page: #f8fafc;
  --bg-card: #ffffff;
  --text-main: #0f172a;
  --text-sub: #64748b;
  --border: #e2e8f0;
  --accent: #16a34a;
  --accent-light: #dcfce7;
}

[data-theme="dark"] {
  --bg-page: #090d16;
  --bg-card: #111827;
  --text-main: #f9fafb;
  --text-sub: #9ca3af;
  --border: #1f2937;
  --accent: #22c55e;
  --accent-light: #064e3b;
}

body {
  background-color: var(--bg-page);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  transition: background-color 0.3s ease, color 0.3s ease;
  margin: 0;
  padding: 40px 16px;
}

.theme-box {
  background-color: var(--bg-card);
  color: var(--text-main);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 28px;
  max-width: 440px;
  margin: 0 auto;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease;
}

.theme-box h3 {
  color: var(--text-main);
  margin-top: 0;
}

.theme-box p {
  color: var(--text-sub);
  line-height: 1.6;
}

.badge {
  display: inline-block;
  background-color: var(--accent-light);
  color: var(--accent);
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
}`,
      solutionExplanation: `1. :root establishes the base light palette with high-contrast semantics.
2. [data-theme="dark"] re-binds the variable tokens to deep slate and emerald colors when the attribute is applied by JavaScript.
3. Every component consumes var(--...) tokens, meaning components automatically adapt without declaring custom dark-mode selectors!
4. The 0.3s ease transition produces a silky smooth cross-fade when toggling themes.`
    },
    {
      id: 'advcss-ex-5',
      title: 'Practice 5: Interactive 3D Perspective Card with Ribbon & Shading',
      difficulty: 'Hard',
      type: 'css',
      problemStatement: 'Construct a 3D interactive product card using CSS perspective, preserve-3d, rotate transformations on hover, and an angular corner ribbon badge rendered using clip-path and pseudo-elements.',
      requirements: [
        'Set perspective: 1000px on the card container wrapper',
        'Set transform-style: preserve-3d and transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) on .card-3d',
        'On .card-3d:hover, apply transform: rotateY(8deg) rotateX(4deg) translateY(-8px)',
        'Style a corner ribbon badge (.ribbon) using position: absolute, top: 18px, right: -30px, transform: rotate(45deg), background: #16a34a, and color: #ffffff',
        'Give child text elements transform: translateZ(30px) so they visually float above the card surface in 3D space',
        'Add realistic ambient drop shadow on hover that shifts in depth'
      ],
      starterCode: `/* Setup 3D perspective and card transformation */
.card-wrapper {
  /* Perspective viewport */
}

.card-3d {
  /* 3D preserve and transition */
}

.card-3d:hover {
  /* 3D rotation and lift */
}

.floating-content {
  /* translateZ depth effect */
}

.ribbon {
  /* Rotated corner ribbon */
}`,
      expectedBehavior: 'A card that tilts dynamically in 3D space with subtle depth separation when hovered, featuring an angular corner ribbon.',
      hints: [
        'perspective: 1000px must be placed on the parent container of the transformed card.',
        'transform-style: preserve-3d ensures children with translateZ() render on separate z-depth planes.',
        'overflow: hidden on the card container prevents rotated ribbons from sticking out.'
      ],
      solution: `.card-wrapper {
  perspective: 1000px;
  max-width: 380px;
  margin: 40px auto;
}

.card-3d {
  position: relative;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 36px 28px;
  transform-style: preserve-3d;
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.card-3d:hover {
  transform: rotateY(8deg) rotateX(4deg) translateY(-8px);
  box-shadow: 0 25px 40px -10px rgba(22, 163, 74, 0.2);
  border-color: #86efac;
}

/* Floating content in 3D plane */
.card-content {
  transform: translateZ(30px);
  transform-style: preserve-3d;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 8px;
}

.card-desc {
  font-size: 0.9375rem;
  color: #64748b;
  line-height: 1.6;
}

/* Diagonal Corner Ribbon */
.ribbon {
  position: absolute;
  top: 18px;
  right: -32px;
  width: 120px;
  background: #16a34a;
  color: #ffffff;
  text-align: center;
  font-size: 0.6875rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  padding: 6px 0;
  transform: rotate(45deg);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
  text-transform: uppercase;
}`,
      solutionExplanation: `1. perspective: 1000px establishes the virtual distance between the viewer's eye and the z=0 plane.
2. transform-style: preserve-3d allows child elements (.card-content) to maintain their own 3D orientation.
3. translateZ(30px) pushes the text forward in virtual space, making it pop out physically when the card rotates!
4. The corner ribbon uses absolute positioning and rotate(45deg), while overflow: hidden clips the excess ribbon cleanly inside the card radius.`
    }
  ]
};
