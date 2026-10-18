export const htmlTopic = {
  id: 'html-html5',
  title: 'HTML & HTML5',
  shortTitle: 'HTML5',
  icon: 'FileCode',
  description: 'Master the fundamental building block of the Web. Learn semantic markup, accessible document architectures, modern forms with HTML5 validation, multimedia integration, and SEO best practices.',
  subtopics: [
    'Document structure & DOCTYPE declaration',
    'Semantic elements (header, nav, main, article, section, aside, footer)',
    'Headings, paragraphs, text formatting & typography hierarchy',
    'Ordered, unordered & definition lists',
    'Hyperlinks (relative, absolute, anchor jumps, target & rel attributes)',
    'Images (img, alt text, responsive picture element, figure & figcaption)',
    'Data tables (table, thead, tbody, tfoot, th scope, colspan & rowspan)',
    'Forms, input types (text, email, password, number, date, range, file)',
    'Form attributes & HTML5 validation (required, pattern, min/max, autocomplete)',
    'Multimedia (video, audio, source, track for captions/subtitles)',
    'Accessibility fundamentals (ARIA roles, labels, tabindex, screen-reader semantics)',
    'SEO-friendly HTML (meta tags, OpenGraph, title hierarchy, canonical links)'
  ],
  theory: [
    {
      title: '1. Document Structure & The Modern HTML5 Standard',
      content: `HTML (HyperText Markup Language) is the standard language that creates the structural backbone of every web page. HTML5 introduced a clean syntax, semantic tags, native multimedia support, and powerful form controls without requiring third-party plugins.

### The Standard HTML5 Boilerplate:
\`\`\`html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Modern Web Application</title>
  </head>
  <body>
    <!-- Visible content rendered to user goes here -->
  </body>
</html>
\`\`\`

### Core Components Explained:
- **\`<!DOCTYPE html>\`**: Tells modern browsers to render in standards-compliant mode rather than legacy quirks mode.
- **\`<html lang="en">\`**: Declares root element and specifies document language for search engines and screen readers.
- **\`<meta charset="UTF-8">\`**: Ensures universal character encoding supporting all world languages and symbols.
- **\`<meta name="viewport" content="width=device-width, initial-scale=1.0">\`**: Critical viewport tag for responsive design, instructing mobile browsers to set screen width to device width at 1:1 scale.`
    },
    {
      title: '2. Semantic HTML Elements & Accessible Landmarks',
      content: `Semantic elements clearly describe their meaning to both the browser and the developer. Instead of generic \`<div>\` containers, modern HTML provides meaningful landmark elements:

| Semantic Tag | Purpose & Usage | Real-World Example |
| :--- | :--- | :--- |
| **\`<header>\`** | Introduces a page or section, contains logo, branding, or titles | Site top bar or article banner |
| **\`<nav>\`** | Contains primary navigation links | Main navigation menu |
| **\`<main>\`** | Unique primary content of the document (only one per page) | Core article or app body |
| **\`<article>\`** | Self-contained, independently distributable content | Blog post, news story, comment |
| **\`<section>\`** | Thematic grouping of content with a heading | Features section, FAQ section |
| **\`<aside>\`** | Content tangentially related to surrounding content | Sidebar, related links, author bio |
| **\`<footer>\`** | Footer for nearest section or page | Copyright, sitemap, legal links |

### Why Semantics Matter:
1. **Accessibility (a11y)**: Screen readers allow visually impaired users to jump directly to landmarks like \`<nav>\` or \`<main>\`.
2. **Search Engine Optimization (SEO)**: Search crawlers index content hierarchy accurately.
3. **Maintainability**: Clean, readable markup that team members can understand immediately.`
    },
    {
      title: '3. Modern Forms, Input Types & Built-In Validation',
      content: `Forms allow users to submit data to web applications. HTML5 provides specialized input types with automatic browser validation, mobile-optimized keyboards, and accessible labeling.

### Standard Accessible Form Pattern:
\`\`\`html
<form action="/api/register" method="POST">
  <div class="form-group">
    <label for="user-email">Email Address <span aria-hidden="true">*</span></label>
    <input 
      type="email" 
      id="user-email" 
      name="email" 
      placeholder="you@example.com" 
      required 
      autocomplete="email"
    />
  </div>
  
  <div class="form-group">
    <label for="user-age">Age (18-99)</label>
    <input 
      type="number" 
      id="user-age" 
      name="age" 
      min="18" 
      max="99" 
    />
  </div>

  <button type="submit">Complete Registration</button>
</form>
\`\`\`

### Key Form Rules:
- **Always associate \`<label for="id">\` with \`<input id="id">\`**: Clicking the label focuses the input, which is essential for accessibility and mobile usability.
- **Built-in HTML5 attributes**: Use \`required\`, \`pattern\` (regex), \`min\`, \`max\`, \`minlength\`, and \`maxlength\` to catch invalid input before network requests are dispatched.`
    },
    {
      title: '4. Multimedia, Accessibility & SEO Best Practices',
      content: `Modern websites require fast-loading media and high search visibility.

### Responsive Images with \`<picture>\`:
\`\`\`html
<picture>
  <source media="(min-width: 800px)" srcset="hero-large.webp" type="image/webp" />
  <source srcset="hero-small.webp" type="image/webp" />
  <img src="hero-fallback.jpg" alt="Student coding in a collaborative software lab" loading="lazy" />
</picture>
\`\`\`

### Audio & Video with Subtitles:
\`\`\`html
<video controls poster="preview.jpg" width="640">
  <source src="tutorial.mp4" type="video/mp4" />
  <track kind="subtitles" src="subtitles_en.vtt" srclang="en" label="English" default />
  Your browser does not support the HTML5 video element.
</video>
\`\`\`

### SEO Essentials:
- Provide meaningful \`<title>\` tags under 60 characters.
- Include \`<meta name="description" content="...">\` under 160 characters.
- Add OpenGraph meta tags (\`og:title\`, \`og:description\`, \`og:image\`) for clean previews when shared on LinkedIn, Twitter, and Slack.`
    }
  ],
  examples: [
    {
      title: 'Example 1: Semantic Article with Media & Accessible Table',
      code: `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Frontend Engineering Insights</title>
</head>
<body>
  <header>
    <h1>Web Engineering Journal</h1>
    <nav aria-label="Main Navigation">
      <a href="#article">Article</a> | 
      <a href="#stats">Benchmarks</a>
    </nav>
  </header>

  <main>
    <article id="article">
      <header>
        <h2>The Architecture of Modern Web Applications</h2>
        <p>Published on <time datetime="2026-10-18">October 18, 2026</time> by Engineering Team</p>
      </header>

      <p>Modern frontend web development emphasizes <strong>semantic markup</strong>, accessible components, and fast rendering.</p>

      <section id="stats">
        <h3>Performance Metrics</h3>
        <table border="1" cellpadding="6">
          <caption>Core Web Vitals Comparison</caption>
          <thead>
            <tr>
              <th scope="col">Metric</th>
              <th scope="col">Target</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">LCP (Largest Contentful Paint)</th>
              <td>&lt; 2.5s</td>
              <td>Good</td>
            </tr>
            <tr>
              <th scope="row">CLS (Cumulative Layout Shift)</th>
              <td>&lt; 0.1</td>
              <td>Optimal</td>
            </tr>
          </tbody>
        </table>
      </section>
    </article>
  </main>

  <footer>
    <p>&copy; 2026 Coding Challenge Platform. All rights reserved.</p>
  </footer>
</body>
</html>`,
      explanation: `Line 1: DOCTYPE specifies HTML5 standards mode.
Line 8: <header> landmark houses the brand title and main navigation.
Line 10: <nav aria-label="..."> gives assistive tech an explicit accessible name.
Line 16: <article> groups the self-contained blog post.
Line 29: <table> includes <caption> for screen reader context.
Lines 33 & 41: <th scope="col"> and <th scope="row"> link table headers to data cells.`,
      previewHtml: `<div style="font-family: sans-serif; padding: 16px; border: 1px solid #cbd5e1; border-radius: 8px; background: #ffffff;">
  <div style="border-bottom: 2px solid #16a34a; padding-bottom: 8px; margin-bottom: 12px;">
    <h2 style="margin: 0; color: #166534; font-size: 20px;">Web Engineering Journal</h2>
    <div style="font-size: 13px; color: #64748b; margin-top: 4px;">Navigation: <a href="#" style="color: #16a34a;">Article</a> | <a href="#" style="color: #16a34a;">Benchmarks</a></div>
  </div>
  <h3 style="margin: 0 0 6px 0; color: #0f172a; font-size: 16px;">The Architecture of Modern Web Applications</h3>
  <p style="font-size: 12px; color: #64748b; margin: 0 0 10px 0;">Published on October 18, 2026</p>
  <p style="font-size: 13px; color: #334155; line-height: 1.5;">Modern frontend development emphasizes semantic markup, accessible components, and fast rendering.</p>
  <table style="width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 10px; border: 1px solid #cbd5e1;">
    <caption style="text-align: left; font-weight: bold; margin-bottom: 4px; font-size: 12px; color: #166534;">Core Web Vitals Comparison</caption>
    <thead>
      <tr style="background: #f0fdf4;">
        <th style="border: 1px solid #cbd5e1; padding: 6px; text-align: left;">Metric</th>
        <th style="border: 1px solid #cbd5e1; padding: 6px; text-align: left;">Target</th>
        <th style="border: 1px solid #cbd5e1; padding: 6px; text-align: left;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="border: 1px solid #cbd5e1; padding: 6px; font-weight: bold;">LCP</td>
        <td style="border: 1px solid #cbd5e1; padding: 6px;">&lt; 2.5s</td>
        <td style="border: 1px solid #cbd5e1; padding: 6px; color: #16a34a; font-weight: bold;">Good</td>
      </tr>
      <tr>
        <td style="border: 1px solid #cbd5e1; padding: 6px; font-weight: bold;">CLS</td>
        <td style="border: 1px solid #cbd5e1; padding: 6px;">&lt; 0.1</td>
        <td style="border: 1px solid #cbd5e1; padding: 6px; color: #16a34a; font-weight: bold;">Optimal</td>
      </tr>
    </tbody>
  </table>
</div>`
    }
  ],
  exercises: [
    {
      id: 'html-ex-1',
      title: 'Practice 1: Build a Semantic Developer Profile Article',
      difficulty: 'Easy',
      type: 'html',
      problemStatement: 'Construct a semantic HTML5 developer profile article card for a software engineer. Use proper structural elements instead of generic containers.',
      requirements: [
        'Use an <article> element as the main wrapper',
        'Include a <header> containing an <h1> for the developer name and a <p> with their title',
        'Add an <img> tag with src, alt description, width and height',
        'Add a <section> containing a brief bio paragraph and an unordered list (<ul>) of at least 3 technical skills',
        'Include a <footer> with a link (<a href="...">) to the developer\'s portfolio'
      ],
      starterCode: `<!-- Write your semantic profile article below -->
<article>
  <!-- 1. Header with developer name and title -->
  
  <!-- 2. Developer avatar image -->
  
  <!-- 3. Section with bio and skills list -->
  
  <!-- 4. Footer with portfolio link -->
</article>`,
      expectedBehavior: 'A well-structured HTML card showing the developer header, avatar image, skills list, and footer portfolio link with semantic tags.',
      hints: [
        'Use <article> for the outer wrapper rather than <div>.',
        'Always provide meaningful alt text on <img> (e.g., alt="Profile photo of Alex Chen").',
        'Wrap skills in <ul> and <li> elements.'
      ],
      solution: `<article class="profile-card">
  <header>
    <h1>Alex Chen</h1>
    <p>Full-Stack Software Engineer</p>
  </header>
  
  <img 
    src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150" 
    alt="Headshot of Alex Chen smiling in an engineering office" 
    width="150" 
    height="150" 
  />
  
  <section>
    <h2>About Me</h2>
    <p>Passionate developer specializing in React, TypeScript, and distributed web services with over 4 years of experience building scalable applications.</p>
    
    <h3>Core Technical Competencies</h3>
    <ul>
      <li>React.js &amp; Modern Frontend Tooling</li>
      <li>TypeScript &amp; JavaScript ES6+</li>
      <li>RESTful APIs &amp; Node.js</li>
    </ul>
  </section>
  
  <footer>
    <a href="https://example.com/portfolio" target="_blank" rel="noopener noreferrer">View Full Engineering Portfolio</a>
  </footer>
</article>`,
      solutionExplanation: `1. The <article> tag correctly designates this card as self-contained content.
2. The <header> houses the primary identity (<h1> and <p>).
3. The <img> has an informative alt attribute describing the image for screen readers.
4. The <section> groups the bio and technical skills list with hierarchical <h2> and <h3> headings.
5. The <footer> wraps the external portfolio link with security attributes target="_blank" and rel="noopener noreferrer".`
    },
    {
      id: 'html-ex-2',
      title: 'Practice 2: Student Course Registration Form with HTML5 Validations',
      difficulty: 'Easy',
      type: 'html',
      problemStatement: 'Create a clean, accessible student registration form for a coding bootcamp with native HTML5 input types and constraints.',
      requirements: [
        'Use a <form> with action="#" and method="POST"',
        'Include a text input for Full Name with required and minlength="3"',
        'Include an email input with type="email", required, and placeholder',
        'Include a telephone input with type="tel" and pattern="[0-9]{10}"',
        'Include a <select> dropdown for Course Selection with at least 3 course options',
        'Provide an associated <label> for every input field using matching for and id attributes',
        'Include a submit <button> with text "Register for Course"'
      ],
      starterCode: `<form action="#" method="POST">
  <!-- Create accessible form fields with labels and validations here -->

</form>`,
      expectedBehavior: 'A form that triggers native browser validation tooltips if fields are left blank or formatted improperly.',
      hints: [
        'Every <label for="xyz"> must match the id="xyz" of its corresponding input.',
        'Use type="email" and type="tel" to prompt mobile devices to display appropriate keyboards.',
        'Add the required attribute to prevent empty submissions.'
      ],
      solution: `<form action="#" method="POST" class="registration-form">
  <h2>Coding Bootcamp Registration</h2>
  
  <div class="form-group">
    <label for="student-name">Full Name (required):</label>
    <input 
      type="text" 
      id="student-name" 
      name="student_name" 
      minlength="3" 
      placeholder="e.g. Maya Patel" 
      required 
    />
  </div>

  <div class="form-group">
    <label for="student-email">Email Address (required):</label>
    <input 
      type="email" 
      id="student-email" 
      name="student_email" 
      placeholder="maya@example.com" 
      required 
    />
  </div>

  <div class="form-group">
    <label for="student-phone">Phone Number (10 digits):</label>
    <input 
      type="tel" 
      id="student-phone" 
      name="student_phone" 
      pattern="[0-9]{10}" 
      placeholder="9876543210" 
      required 
    />
  </div>

  <div class="form-group">
    <label for="course-select">Select Course Track:</label>
    <select id="course-select" name="course" required>
      <option value="">-- Choose a specialization --</option>
      <option value="frontend">Modern Frontend Development</option>
      <option value="fullstack">Full-Stack Engineering (React + Django)</option>
      <option value="backend">Cloud Backend Systems</option>
    </select>
  </div>

  <button type="submit">Register for Course</button>
</form>`,
      solutionExplanation: `1. Each input has an explicit <label> with a corresponding 'for' attribute matching the input 'id'.
2. type="email" automatically verifies that an '@' and valid domain structure are entered.
3. pattern="[0-9]{10}" validates that the phone number contains exactly 10 numeric digits.
4. The select dropdown requires a choice by providing an empty default option with required.`
    },
    {
      id: 'html-ex-3',
      title: 'Practice 3: Accessible Student Semester Grade Table',
      difficulty: 'Medium',
      type: 'html',
      problemStatement: 'Construct a data table displaying student exam marks and grades. The table must conform to WCAG accessibility guidelines with proper headers, scope, and summary captions.',
      requirements: [
        'Use <table> with a descriptive <caption> element',
        'Structure table using <thead>, <tbody>, and <tfoot>',
        'Column headers in <thead> must use <th scope="col">',
        'Row headers in <tbody> must use <th scope="row">',
        'Include at least 3 subjects with Credits, Internal Marks, and Final Grade',
        'Use <tfoot> to display GPA or Total Credits spanning multiple columns with colspan'
      ],
      starterCode: `<!-- Build the accessible table below -->
<table>
  <!-- Add caption, thead, tbody, and tfoot -->
</table>`,
      expectedBehavior: 'A structured, semantic table showing headers linked to columns and rows, and a summary footer with colspan.',
      hints: [
        '<caption> should be the first child element of <table>.',
        'Use scope="col" for vertical column headers and scope="row" for subject row titles.',
        'In <tfoot>, use colspan="2" or similar to span multiple columns.'
      ],
      solution: `<table class="grade-report" border="1" cellpadding="8">
  <caption>Semester 4 Academic Performance &amp; Grade Report</caption>
  <thead>
    <tr>
      <th scope="col">Course Code &amp; Title</th>
      <th scope="col">Credits</th>
      <th scope="col">Internal Marks (40)</th>
      <th scope="col">End Exam (60)</th>
      <th scope="col">Letter Grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">CS401: Data Structures &amp; Algorithms</th>
      <td>4</td>
      <td>38</td>
      <td>54</td>
      <td>A+</td>
    </tr>
    <tr>
      <th scope="row">CS402: Modern Frontend Web Development</th>
      <td>4</td>
      <td>39</td>
      <td>58</td>
      <td>O (Outstanding)</td>
    </tr>
    <tr>
      <th scope="row">CS403: Database Management Systems</th>
      <td>3</td>
      <td>35</td>
      <td>50</td>
      <td>A</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row" colspan="3">Cumulative Semester Credits &amp; GPA</th>
      <td colspan="2"><strong>11 Credits | SGPA: 9.42 / 10.0</strong></td>
    </tr>
  </tfoot>
</table>`,
      solutionExplanation: `1. <caption> provides an immediate title accessible to assistive technology.
2. <thead>, <tbody>, and <tfoot> separate header, data, and summary calculations logically.
3. <th scope="col"> and <th scope="row"> establish precise 2-dimensional relationships between headers and data cells.
4. colspan="3" merges the summary label cells cleanly in the <tfoot>.`
    },
    {
      id: 'html-ex-4',
      title: 'Practice 4: Responsive Media Gallery with Video, Audio & Fallbacks',
      difficulty: 'Medium',
      type: 'html',
      problemStatement: 'Build a responsive multimedia showcase containing both a video presentation with subtitle track and an audio interview with fallback messages.',
      requirements: [
        'Use a <section> element with an <h2> heading',
        'Include a <video> element with controls, poster image attribute, and width="100%"',
        'Add at least two <source> tags inside <video> with different formats (mp4 and webm)',
        'Add a <track> element for English closed captions (kind="subtitles" or "captions")',
        'Include an <audio> element with controls and at least two audio sources (mp3 and ogg)',
        'Provide a friendly fallback text message inside both media elements for unsupported browsers'
      ],
      starterCode: `<section class="media-showcase">
  <!-- Build your video and audio showcase with sources and captions -->

</section>`,
      expectedBehavior: 'A multimedia section with a video player displaying poster image and subtitle support, and an audio player with accessible controls.',
      hints: [
        '<source> elements must specify src and type attributes (e.g. type="video/mp4").',
        '<track> requires kind, src, srclang, and label attributes.',
        'Place fallback text directly before the closing </video> or </audio> tag.'
      ],
      solution: `<section class="media-showcase">
  <h2>Engineering Keynote &amp; Tech Podcast</h2>
  
  <article class="video-container">
    <h3>Keynote: The Future of Frontend Architectures</h3>
    <video controls poster="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600" width="100%">
      <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" type="video/mp4" />
      <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.webm" type="video/webm" />
      <track kind="subtitles" src="subtitles_en.vtt" srclang="en" label="English (CC)" default />
      <p>Your browser does not support HTML5 video. Please download the presentation file directly.</p>
    </video>
  </article>

  <article class="audio-container" style="margin-top: 20px;">
    <h3>Podcast Episode: Clean Code &amp; Component Design</h3>
    <audio controls style="width: 100%;">
      <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg" />
      <source src="podcast.ogg" type="audio/ogg" />
      <p>Your browser does not support the HTML5 audio element. <a href="podcast.mp3">Download audio MP3</a>.</p>
    </audio>
  </article>
</section>`,
      solutionExplanation: `1. The poster attribute gives the video a high-resolution preview image before playback begins.
2. Multiple <source> tags allow the browser to choose the most efficient supported codec (WebM vs MP4).
3. The <track> element ensures accessibility for hearing-impaired users and non-native speakers.
4. Fallback text provides a graceful degradation path if older browsers cannot render the HTML5 media engine.`
    },
    {
      id: 'html-ex-5',
      title: 'Practice 5: SEO-Optimized Product Landing Page Header & Metadata',
      difficulty: 'Hard',
      type: 'html',
      problemStatement: 'Construct an enterprise-grade HTML head document and semantic top-level landing page layout optimized for search engine crawlers, social sharing (OpenGraph), and screen-reader accessibility.',
      requirements: [
        'Include complete <head> metadata: charset, responsive viewport, title under 60 chars, meta description under 160 chars, canonical link',
        'Add OpenGraph meta tags: og:title, og:description, og:image, og:url, and og:type',
        'Add Twitter card meta tags: twitter:card, twitter:title, and twitter:description',
        'Structure the <body> using proper landmarks: <header>, <nav>, <main>, <aside>, and <footer>',
        'Add an accessible skip navigation link (<a href="#main-content">Skip to Content</a>) as the first element inside body',
        'Add ARIA landmarks and aria-labels where appropriate'
      ],
      starterCode: `<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Add all SEO and OpenGraph metadata here -->
</head>
<body>
  <!-- Add accessible skip link and landmark structure -->

</body>
</html>`,
      expectedBehavior: 'An industry-grade HTML document with comprehensive social preview metadata, skip links, and semantic landmark hierarchy.',
      hints: [
        'The skip link should point to id="main-content" on the <main> tag.',
        'OpenGraph meta tags use property="og:..." whereas standard meta tags use name="...".',
        'Ensure the <title> tag includes both product name and primary keyword.'
      ],
      solution: `<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DevChallenge Pro &mdash; Interactive Coding Platform for Engineers</title>
  <meta name="description" content="Master data structures, frontend frameworks, and cloud deployment with 500+ interactive coding challenges and verified certifications." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://codechallenge.example.com" />
  
  <!-- OpenGraph Metadata for Facebook, LinkedIn, Slack -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://codechallenge.example.com" />
  <meta property="og:title" content="DevChallenge Pro &mdash; Interactive Coding Platform" />
  <meta property="og:description" content="500+ verified coding challenges in React, Python, Java, and Algorithms with official certifications." />
  <meta property="og:image" content="https://codechallenge.example.com/assets/social-card.jpg" />
  <meta property="og:site_name" content="DevChallenge Platform" />

  <!-- Twitter Card Metadata -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="DevChallenge Pro &mdash; Interactive Coding Platform" />
  <meta name="twitter:description" content="Master coding challenges, earn verifiable technical credentials." />
  <meta name="twitter:image" content="https://codechallenge.example.com/assets/social-card.jpg" />
</head>
<body>
  <!-- Accessible Skip Navigation Link -->
  <a href="#main-content" class="skip-link" style="position: absolute; left: -9999px;">Skip to primary content</a>

  <header role="banner">
    <div class="logo">
      <a href="/" aria-label="DevChallenge Homepage"><strong>DevChallenge</strong> Pro</a>
    </div>
    <nav role="navigation" aria-label="Main Menu">
      <ul>
        <li><a href="/courses">Courses</a></li>
        <li><a href="/problems">Challenges</a></li>
        <li><a href="/certifications">Certificates</a></li>
      </ul>
    </nav>
  </header>

  <main id="main-content" role="main">
    <section aria-labelledby="hero-heading">
      <h1 id="hero-heading">Master Modern Frontend &amp; Full-Stack Engineering</h1>
      <p>Accelerate your software engineering career through practical challenges, hands-on sandboxes, and industry-recognized certifications.</p>
      <a href="/register" class="cta-button">Get Started Free</a>
    </section>
  </main>

  <aside role="complementary" aria-label="Platform Highlights">
    <h3>Quick Facts</h3>
    <p>Over 50,000 developers verified across 20 specialized engineering disciplines.</p>
  </aside>

  <footer role="contentinfo">
    <p>&copy; 2026 DevChallenge Platform Inc. Built with accessible semantic HTML5.</p>
  </footer>
</body>
</html>`,
      solutionExplanation: `1. The <head> contains complete OpenGraph and Twitter card protocols, ensuring that when the URL is shared on social networks or messaging apps, rich media previews render correctly.
2. The skip link allows keyboard-only and screen reader users to bypass repetitive header navigation links and jump directly to the primary content (#main-content).
3. The role attributes (banner, navigation, main, complementary, contentinfo) reinforce standard HTML5 semantic tags for older assistive technologies.
4. aria-labelledby connects the section to its descriptive heading element.`
    }
  ]
};
