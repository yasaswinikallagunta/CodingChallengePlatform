export const cssBasicsTopic = {
  id: 'css-styling-basics',
  title: 'CSS & CSS3 Styling Basics',
  shortTitle: 'CSS Basics',
  icon: 'Palette',
  description: 'Master core CSS rules and visual design fundamentals. Learn selector specificity, color models, typography, the CSS box model, display types, positioning strategies, and mobile-first responsive media queries.',
  subtopics: [
    'CSS syntax, declarations & selector specificity',
    'Inline, internal (<style>) and external stylesheet linking',
    'Color models (HEX, RGB, RGBA, HSL, HSLA)',
    'Backgrounds (solid, linear/radial gradients, background-size, background-position)',
    'Typography & font styling (font-family, font-weight, line-height, letter-spacing, text-transform)',
    'The CSS Box Model (content, padding, border, margin, box-sizing: border-box)',
    'Display modes (block, inline, inline-block, none) vs Visibility (visible, hidden, opacity)',
    'Positioning (static, relative, absolute, fixed, sticky) and z-index stacking context',
    'Float, clear, and clearfix micro-patterns',
    'Responsive design fundamentals & mobile-first media queries (@media screen and (min-width))',
    'Fluid sizing units (rem, em, %, vw, vh) and clamp() calculations'
  ],
  theory: [
    {
      title: '1. CSS Syntax, Rule Sets & Selector Specificity',
      content: `Cascading Style Sheets (CSS) dictate how HTML elements render visually. A CSS rule comprises a **selector** and a **declaration block**.

\`\`\`css
/* Selector */
.button-primary {
  /* Property: Value; */
  background-color: #16a34a;
  color: #ffffff;
  padding: 10px 20px;
  border-radius: 8px;
}
\`\`\`

### Selector Types:
- **Element Selector**: \`p { color: #334155; }\` targets all \`<p>\` tags.
- **Class Selector**: \`.card { border: 1px solid #e2e8f0; }\` targets elements with \`class="card"\`.
- **ID Selector**: \`#header { background: #ffffff; }\` targets the unique element with \`id="header"\`.
- **Attribute Selector**: \`input[type="email"] { border-color: #16a34a; }\`.
- **Combinators**:
  - Descendant: \`nav a\` (all links anywhere inside \`<nav>\`).
  - Child: \`ul > li\` (direct children only).
  - Adjacent Sibling: \`h2 + p\` (the immediate paragraph after an \`h2\`).

### The Specificity Cascade Hierarchy:
When multiple conflicting rules match an element, the browser resolves precedence using specificity weights:
1. **Inline styles** (\`style="..."\`) &rarr; 1,0,0,0
2. **IDs** (\`#id\`) &rarr; 0,1,0,0
3. **Classes, attributes, pseudo-classes** (\`.class\`, \`[type]\`, \`:hover\`) &rarr; 0,0,1,0
4. **Element tags & pseudo-elements** (\`h1\`, \`div\`, \`::before\`) &rarr; 0,0,0,1`
    },
    {
      title: '2. The CSS Box Model & Sizing Reset',
      content: `Every HTML element rendered on a web page is enclosed inside a rectangular box consisting of four concentric layers:

1. **Content**: The inner area where text, images, or child elements appear.
2. **Padding**: Transparent inner spacing around the content.
3. **Border**: The stroke encircling the padding and content.
4. **Margin**: Transparent outer clearance separating this element from sibling elements.

### The Standard \`box-sizing: border-box\` Universal Reset:
Under legacy \`content-box\` sizing, adding padding or borders expands the element's actual rendered width beyond its specified \`width\`! 
Modern professional web development universally applies the following reset so that \`width\` and \`height\` represent the complete outer edge including padding and border:

\`\`\`css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
\`\`\`

### Margin Collapse:
Top and bottom margins between adjacent block elements collapse into a single margin equal to the larger of the two values, preventing double spacing.`
    },
    {
      title: '3. Display Modes & Positioning Strategies',
      content: `The \`display\` and \`position\` properties govern layout flow.

### Display Modes:
- **\`block\`**: Takes up the full width available, starts on a new line (e.g. \`<div>\`, \`<p>\`, \`<h1>\`).
- **\`inline\`**: Only takes as much width as its content, respects left/right padding and margins, but ignores top/bottom height/width (e.g. \`<span>\`, \`<a>\`, \`<strong>\`).
- **\`inline-block\`**: Flows inline with text but respects explicit \`width\`, \`height\`, and vertical margins.
- **\`none\`**: Completely removes the element from document flow (unlike \`visibility: hidden\` which preserves the blank space).

### Positioning Values:
- **\`static\`** (Default): Follows normal document flow. \`top\`, \`left\`, \`right\`, \`bottom\`, and \`z-index\` have no effect.
- **\`relative\`**: Remains in normal document flow, but can be offset relative to its own default position. Crucially, it serves as the coordinate reference for child elements with \`position: absolute\`.
- **\`absolute\`**: Removed from normal flow and positioned relative to its nearest positioned ancestor (an ancestor with \`relative\`, \`absolute\`, or \`fixed\`).
- **\`fixed\`**: Removed from flow and positioned relative to the browser viewport. Remains locked in place when the user scrolls (e.g., floating chat buttons).
- **\`sticky\`**: Toggles between \`relative\` and \`fixed\` based on scroll position (ideal for table headers and sticky navigation bars).`
    },
    {
      title: '4. Responsive Design & Mobile-First Media Queries',
      content: `Responsive web design guarantees an optimal user experience across smartphones, tablets, laptops, and ultra-wide desktop monitors.

### Mobile-First Philosophy:
Write base CSS for mobile screens first (without media queries), then use \`@media (min-width: ...)\` to progressively enhance layouts as viewport real estate expands.

\`\`\`css
/* Base styles (Mobile: 0px and up) */
.grid-container {
  display: block;
  width: 100%;
}

/* Tablet screens (768px and up) */
@media screen and (min-width: 768px) {
  .grid-container {
    display: flex;
    gap: 20px;
  }
}

/* Desktop screens (1024px and up) */
@media screen and (min-width: 1024px) {
  .grid-container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
\`\`\`

### Fluid Units:
- **\`rem\`**: Root em. Equal to font size of \`<html>\` (default \`1rem = 16px\`). Changing root size scales the whole interface proportionately.
- **\`vw\` / \`vh\`**: Viewport width and height (1vw = 1% of screen width).`
    }
  ],
  examples: [
    {
      title: 'Example: Modern Card with Box Model & Sticky Header',
      code: `/* Modern Card & Header Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: #f8fafc;
  color: #1e293b;
  line-height: 1.6;
}

/* Sticky Header */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #ffffff;
  border-bottom: 2px solid #e2e8f0;
  padding: 12px 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

/* Profile Card */
.card {
  position: relative;
  max-width: 400px;
  margin: 32px auto;
  padding: 24px;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 16px;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* Status Badge positioned in top-right */
.badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background-color: #dcfce7;
  color: #166534;
  padding: 4px 10px;
  font-size: 0.75rem;
  font-weight: 700;
  border-radius: 9999px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.card h2 {
  font-size: 1.5rem;
  color: #0f172a;
  margin-bottom: 8px;
}

.card p {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 16px;
}

.btn-primary {
  display: inline-block;
  background: linear-gradient(135deg, #16a34a, #15803d);
  color: #ffffff;
  padding: 10px 18px;
  font-size: 0.875rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 8px;
  transition: opacity 0.2s ease;
}`,
      explanation: `Line 1: Universal box-sizing: border-box reset applied.
Line 12: position: sticky on .site-header locks the header to top: 0 as the page scrolls.
Line 22: position: relative on .card establishes a coordinate anchor for the absolute badge.
Line 33: position: absolute with top: 16px and right: 16px pins the badge cleanly to the card's corner.
Line 56: linear-gradient creates a modern visual depth without heavy external image assets.`,
      previewHtml: `<div style="font-family: sans-serif; background: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0;">
  <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 16px; padding: 24px; position: relative; max-width: 380px; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
    <span style="position: absolute; top: 16px; right: 16px; background: #dcfce7; color: #166534; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 999px; text-transform: uppercase;">Active Student</span>
    <h3 style="margin: 0 0 6px 0; color: #0f172a; font-size: 18px;">Frontend Specialization</h3>
    <p style="margin: 0 0 16px 0; color: #64748b; font-size: 13px; line-height: 1.5;">Master HTML5, modern CSS3 styling, and responsive layout architectures.</p>
    <a href="#" style="display: inline-block; background: #16a34a; color: white; padding: 8px 16px; border-radius: 8px; font-size: 13px; font-weight: 600; text-decoration: none;">Continue Curriculum</a>
  </div>
</div>`
    }
  ],
  exercises: [
    {
      id: 'css-ex-1',
      title: 'Practice 1: Developer Profile Card with the CSS Box Model',
      difficulty: 'Easy',
      type: 'css',
      problemStatement: 'Apply CSS Box Model rules to style an unstyled profile card. Set box-sizing, internal padding, borders, rounded corners, and subtle box shadows.',
      requirements: [
        'Apply box-sizing: border-box universally to all elements',
        'Set .profile-card max-width to 360px, center it horizontally with margin: 0 auto',
        'Add padding of 24px inside the card and a 1px solid border with color #e2e8f0',
        'Give the card a border-radius of 12px and background-color #ffffff',
        'Add a soft box-shadow (e.g. 0 4px 6px -1px rgba(0, 0, 0, 0.1))',
        'Style the avatar image with width: 80px, height: 80px, and border-radius: 50% for a circular shape'
      ],
      starterCode: `/* Write your CSS Box Model styling below */
* {
  /* Universal reset */
}

.profile-card {
  /* Card box model styling */
}

.avatar {
  /* Circular avatar image */
}

.dev-name {
  color: #0f172a;
  font-size: 1.25rem;
  margin-top: 12px;
}

.dev-role {
  color: #16a34a;
  font-size: 0.875rem;
  font-weight: 600;
}`,
      expectedBehavior: 'A centered, rounded card with circular avatar, clean interior padding, and elevated box-shadow.',
      hints: [
        'Use margin: 20px auto; to center a block element with a max-width.',
        'border-radius: 50% on a square element creates a perfect circle.',
        'box-sizing: border-box ensures padding is included within max-width.'
      ],
      solution: `* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: #f1f5f9;
  padding: 40px 16px;
}

.profile-card {
  max-width: 360px;
  margin: 0 auto;
  padding: 24px;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  text-align: center;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #16a34a;
}

.dev-name {
  color: #0f172a;
  font-size: 1.25rem;
  font-weight: 700;
  margin-top: 12px;
}

.dev-role {
  color: #16a34a;
  font-size: 0.875rem;
  font-weight: 600;
  margin-top: 4px;
}`,
      solutionExplanation: `1. box-sizing: border-box guarantees that padding (24px) doesn't cause the card to exceed max-width: 360px.
2. margin: 0 auto centers the card horizontally on the page.
3. border-radius: 50% turns the square 80px by 80px avatar into a clean circular profile badge.
4. box-shadow introduces visual depth with subtle ambient shading.`
    },
    {
      id: 'css-ex-2',
      title: 'Practice 2: Multi-Level Typography & Gradient Hero Banner',
      difficulty: 'Easy',
      type: 'css',
      problemStatement: 'Style an impactful hero banner featuring an emerald-green linear gradient background, high-contrast typography hierarchy with rem units, and custom line-height.',
      requirements: [
        'Style .hero-banner with a linear-gradient background from #166534 to #15803d at 135deg',
        'Add padding of 48px 24px and border-radius of 16px',
        'Set text color to #ffffff with text-align: center',
        'Style the <h1> with font-size: 2.25rem, line-height: 1.2, and letter-spacing: -0.02em',
        'Style the subtitle paragraph with font-size: 1.125rem, color: #dcfce7, and max-width: 600px centered with margin',
        'Style a .cta-btn with background #ffffff, color #166534, font-weight: 700, and border-radius: 8px'
      ],
      starterCode: `/* Style the gradient hero banner below */
.hero-banner {
  /* Gradient background, padding, text-align */
}

.hero-banner h1 {
  /* Large title with fluid rem units */
}

.hero-banner p {
  /* Subtitle styling */
}

.cta-btn {
  /* High contrast action button */
}`,
      expectedBehavior: 'A vibrant white-and-green gradient hero banner with crisp readable typography and centered action button.',
      hints: [
        'Linear gradient syntax: background: linear-gradient(135deg, #color1, #color2);',
        'To center the subtitle paragraph with a max-width, use margin: 0 auto 24px auto;',
        'Set display: inline-block on .cta-btn so vertical padding and margins work.'
      ],
      solution: `.hero-banner {
  background: linear-gradient(135deg, #166534 0%, #15803d 100%);
  padding: 48px 24px;
  border-radius: 16px;
  text-align: center;
  color: #ffffff;
  box-shadow: 0 10px 25px -5px rgba(22, 101, 52, 0.3);
}

.hero-banner h1 {
  font-size: 2.25rem;
  line-height: 1.2;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
}

.hero-banner p {
  font-size: 1.125rem;
  color: #dcfce7;
  line-height: 1.6;
  max-width: 600px;
  margin: 0 auto 24px auto;
}

.cta-btn {
  display: inline-block;
  background-color: #ffffff;
  color: #166534;
  padding: 12px 28px;
  font-size: 1rem;
  font-weight: 700;
  text-decoration: none;
  border-radius: 8px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px -2px rgba(0, 0, 0, 0.15);
}`,
      solutionExplanation: `1. linear-gradient(135deg, #166534, #15803d) creates the platform's signature green aesthetic.
2. 2.25rem with negative letter-spacing gives the heading high visual authority.
3. max-width: 600px with auto margins keeps text line lengths readable for human eyes.
4. :hover pseudo-class adds micro-interaction feedback with translateY.`
    },
    {
      id: 'css-ex-3',
      title: 'Practice 3: Sticky Navigation Bar with Absolute Notification Badge',
      difficulty: 'Medium',
      type: 'css',
      problemStatement: 'Construct a sticky top header with an avatar and an unread notification counter badge. Use relative and absolute positioning along with z-index to coordinate the stacking layer.',
      requirements: [
        'Style .navbar with position: sticky, top: 0, and z-index: 1000 so it stays visible during scroll',
        'Set .navbar background to #ffffff, border-bottom: 1px solid #e2e8f0, and padding: 12px 24px',
        'Wrap the bell icon inside a container with position: relative and display: inline-block',
        'Position .notification-badge with position: absolute, top: -6px, right: -8px',
        'Style .notification-badge with background-color: #ef4444 (red), color: #ffffff, font-size: 0.7rem, font-weight: bold, padding: 2px 6px, and border-radius: 9999px',
        'Add a white border around the badge to create visual separation from the icon'
      ],
      starterCode: `/* Style the sticky navbar and absolute badge below */
.navbar {
  /* Sticky positioning and stacking index */
}

.notification-container {
  /* Relative anchor for badge */
}

.notification-badge {
  /* Absolute coordinate positioning */
}`,
      expectedBehavior: 'A sticky header that locks to the top on scroll, displaying a bell icon with a red badge overlapping its top-right corner.',
      hints: [
        'position: absolute requires the parent container to have position: relative to establish the coordinate system.',
        'top: -6px and right: -8px offset the badge outward from the top-right corner.',
        'z-index ensures the sticky navbar renders on top of page content.'
      ],
      solution: `.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.brand {
  font-weight: 800;
  color: #166534;
  font-size: 1.125rem;
}

.notification-container {
  position: relative;
  display: inline-block;
  cursor: pointer;
  padding: 6px;
}

.bell-icon {
  font-size: 1.25rem;
}

.notification-badge {
  position: absolute;
  top: -4px;
  right: -6px;
  background-color: #ef4444;
  color: #ffffff;
  font-size: 0.6875rem;
  font-weight: 800;
  min-width: 18px;
  height: 18px;
  line-height: 14px;
  text-align: center;
  padding: 0 4px;
  border-radius: 9999px;
  border: 2px solid #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}`,
      solutionExplanation: `1. position: sticky; top: 0 keeps the header pinned to the top of the viewport when scrolling.
2. z-index: 1000 guarantees the navigation stays above other page layers.
3. .notification-container has position: relative, defining the boundary coordinates for the badge.
4. position: absolute on the badge with negative top and right offsets places it precisely over the bell icon.`
    },
    {
      id: 'css-ex-4',
      title: 'Practice 4: Responsive Mobile-First Pricing Table',
      difficulty: 'Medium',
      type: 'css',
      problemStatement: 'Design a mobile-first responsive pricing grid. On mobile phones, pricing cards stack vertically in a single column. On screens 768px and wider, cards display side-by-side in 3 columns.',
      requirements: [
        'Write mobile-first styles: .pricing-grid renders cards stacked in 1 column with a 20px vertical gap',
        'Style each .pricing-card with border: 1px solid #e2e8f0, padding: 24px, border-radius: 12px, background: #ffffff',
        'Add a media query for @media screen and (min-width: 768px)',
        'Inside the media query, set .pricing-grid to display: flex with flex-direction: row and gap: 24px',
        'Each card on desktop should take flex: 1 to ensure equal width distribution',
        'Add a .featured-card class that has a highlighted border: 2px solid #16a34a and elevated box-shadow'
      ],
      starterCode: `/* Mobile-first base styles (phones 0px and up) */
.pricing-grid {
  /* Stacked layout */
}

.pricing-card {
  /* Card aesthetics */
}

/* Tablet & Desktop enhancement (768px and up) */
@media screen and (min-width: 768px) {
  .pricing-grid {
    /* 3-column horizontal layout */
  }
}`,
      expectedBehavior: 'Single-column stacked view on mobile devices, transitioning to a balanced 3-column row on tablet and desktop screens.',
      hints: [
        'Use @media screen and (min-width: 768px) to trigger the desktop layout.',
        'flex: 1 1 0 ensures all three cards occupy identical widths regardless of content length.',
        'Use border: 2px solid #16a34a on .featured-card to make the recommended plan stand out.'
      ],
      solution: `/* Base Mobile Styles */
.pricing-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 1080px;
  margin: 0 auto;
  padding: 16px;
}

.pricing-card {
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.featured-card {
  border: 2px solid #16a34a;
  position: relative;
  box-shadow: 0 10px 15px -3px rgba(22, 163, 74, 0.15);
}

.price {
  font-size: 2rem;
  font-weight: 800;
  color: #0f172a;
  margin: 16px 0;
}

/* Responsive Tablet & Desktop Breakpoint */
@media screen and (min-width: 768px) {
  .pricing-grid {
    flex-direction: row;
    gap: 24px;
    padding: 32px 16px;
  }

  .pricing-card {
    flex: 1 1 0;
  }

  .featured-card {
    transform: scale(1.04);
  }
}`,
      solutionExplanation: `1. The mobile-first approach starts with flex-direction: column, requiring zero overrides for mobile devices.
2. The @media (min-width: 768px) query activates only on tablets and larger viewports, switching flex-direction to row.
3. flex: 1 1 0 forces all three pricing tiers to distribute available width equally.
4. transform: scale(1.04) slightly enlarges the featured card for instant visual hierarchy.`
    },
    {
      id: 'css-ex-5',
      title: 'Practice 5: Glassmorphic Metric Card with Pseudo-Elements & Shading',
      difficulty: 'Hard',
      type: 'css',
      problemStatement: 'Construct a modern glassmorphic dashboard statistics card using semi-transparent RGBA backgrounds, backdrop-filter blur, gradient borders, and custom ::before and ::after decorative pseudo-elements.',
      requirements: [
        'Style .glass-card with background: rgba(255, 255, 255, 0.85) and backdrop-filter: blur(12px)',
        'Add border: 1px solid rgba(22, 163, 74, 0.2) and border-radius: 20px',
        'Add position: relative and overflow: hidden so pseudo-elements stay contained',
        'Use .glass-card::before to render an accent strip at top: 0, left: 0, width: 100%, height: 4px with linear-gradient(#16a34a, #22c55e)',
        'Use .glass-card::after to place a subtle glowing green circle in the background with position: absolute, width: 120px, height: 120px, border-radius: 50%, filter: blur(40px), and opacity: 0.15',
        'Add smooth hover transition: transform: translateY(-4px) and increased shadow'
      ],
      starterCode: `/* Create the glassmorphic card with pseudo-elements below */
.glass-card {
  /* Semi-transparent background, blur, relative anchor */
}

.glass-card::before {
  /* Top accent gradient bar */
}

.glass-card::after {
  /* Ambient glowing blur circle */
}

.glass-card:hover {
  /* Hover elevation */
}`,
      expectedBehavior: 'A frosted glass effect card with a green top accent bar, ambient green background glow, and smooth hover lift.',
      hints: [
        'Pseudo-elements ::before and ::after must always define content: ""; to render.',
        'Use backdrop-filter: blur(...) to achieve the frosted glass aesthetic.',
        'overflow: hidden on the parent prevents blurred pseudo-elements from bleeding outside rounded corners.'
      ],
      solution: `.glass-card {
  position: relative;
  overflow: hidden;
  max-width: 420px;
  margin: 32px auto;
  padding: 32px 28px;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(22, 163, 74, 0.2);
  border-radius: 20px;
  box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
}

/* Top Gradient Accent Strip */
.glass-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #166534, #16a34a, #86efac);
}

/* Ambient Radial Glow */
.glass-card::after {
  content: "";
  position: absolute;
  top: -40px;
  right: -40px;
  width: 140px;
  height: 140px;
  background: #16a34a;
  border-radius: 50%;
  filter: blur(40px);
  opacity: 0.15;
  pointer-events: none;
}

.glass-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 35px -8px rgba(22, 163, 74, 0.15);
  border-color: rgba(22, 163, 74, 0.4);
}

.stat-label {
  font-size: 0.8125rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #64748b;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 900;
  color: #0f172a;
  margin: 8px 0;
}`,
      solutionExplanation: `1. backdrop-filter: blur(12px) blurs what is visible behind the card, producing the frosted glass aesthetic.
2. content: "" is required for ::before and ::after to be generated into the render tree.
3. ::before creates the sleek multi-tone green gradient stripe along the top edge.
4. ::after uses filter: blur(40px) with low opacity to cast an ambient brand glow without adding DOM nodes.
5. cubic-bezier curve provides a snappy, physics-based hover elevation.`
    }
  ]
};
