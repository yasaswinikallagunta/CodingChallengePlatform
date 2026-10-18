export const deploymentTopic = {
  id: 'deployment',
  title: 'Deployment',
  shortTitle: 'Deployment',
  icon: 'Rocket',
  description: 'Master the full modern frontend release cycle. Learn production build tooling, environment variables (.env), Single Page Application (SPA) routing on Netlify & Vercel, GitHub Actions CI/CD pipelines, DNS records, SSL/TLS certificates, and Core Web Vitals monitoring.',
  subtopics: [
    'Frontend build process: transpilation, bundling, minification & tree-shaking',
    'Development vs Production environments (HMR vs optimized static assets)',
    'Environment variables (.env, .env.production, VITE_ prefix & secret hygiene)',
    'Bundling & performance optimization: chunk splitting, dynamic import(), lazy loading',
    'Deploying to Netlify (netlify.toml, SPA redirects /* /index.html 200, build hooks)',
    'Deploying to Vercel (vercel.json, edge rewrites, preview deployments)',
    'Version control workflows & GitHub Actions CI/CD pipelines',
    'Custom domain setup, DNS records (A, CNAME, ALIAS) & SSL/TLS certificate automation',
    'Production error handling & monitoring (React Error Boundaries, Sentry)',
    'Performance monitoring: Core Web Vitals (LCP, INP, CLS) & Lighthouse audits'
  ],
  theory: [
    {
      title: '1. The Modern Frontend Build Pipeline',
      content: `In development, modern tools like **Vite** provide instantaneous updates using native ES Modules and Hot Module Replacement (HMR). However, browsers in production cannot fetch thousands of individual unbundled modules over high-latency mobile networks.

### The Production Build Process (\`npm run build\`):
1. **Transpilation**: Converts modern ECMAScript and JSX into backwards-compatible standard JavaScript using Rollup or esbuild.
2. **Tree-Shaking**: Dead-code elimination that removes unused library exports, significantly shrinking bundle weight.
3. **Minification**: Strips whitespace, removes comments, and mangles variable names (\`userCount\` &rarr; \`u\`).
4. **Content-Hash Asset Naming**: Generates files like \`index-BZHQ8ZYO.js\`. The cryptographic hash changes only when file content changes, allowing web servers to cache assets forever (\`Cache-Control: max-age=31536000, immutable\`).`
    },
    {
      title: '2. Environment Variables & Secret Safety',
      content: `Frontends run directly inside the end user's browser. Therefore, **any environment variable baked into a frontend build is 100% visible to anyone who opens Chrome DevTools!**

### Safe vs Unsafe Environment Variables:
- **SAFE for Frontend**: Public API base URLs (\`VITE_API_URL=https://api.example.com\`), public feature flags (\`VITE_ENABLE_ANALYTICS=true\`), public Stripe publishable keys.
- **NEVER in Frontend**: Database passwords, Stripe secret keys, JWT private keys, private server tokens. These must live strictly in your Django or Node.js backend!

### Vite Environment Variable Rules:
Vite exposes environment variables on the \`import.meta.env\` object, and **only** includes variables prefixed with \`VITE_\` to prevent accidental leakage of sensitive system environment variables:
\`\`\`env
# .env.production
VITE_API_BASE_URL=https://api.codechallenge.com
VITE_PLATFORM_NAME=Coding Challenge Platform
\`\`\`
\`\`\`js
const API_URL = import.meta.env.VITE_API_BASE_URL;
\`\`\``
    },
    {
      title: '3. Single Page Application (SPA) Routing on Netlify & Vercel',
      content: `In a React Single Page Application (using React Router), page navigation occurs purely in client-side JavaScript. When a user navigates to \`/course/modern-frontend-development\`, React updates the URL without contacting the server.

### The Infamous "404 Not Found" On Page Refresh:
If a user bookmarks \`https://mysite.com/course/modern-frontend\` and reloads their browser, the hosting server looks on its physical hard drive for a file named \`/course/modern-frontend/index.html\`, fails to find it, and throws a **404 Not Found**!

### The Solution: SPA Rewrite Rules
You must configure the host to route all paths back to the root \`/index.html\` with HTTP status 200, letting React Router handle the route:

**For Netlify (\`netlify.toml\`):**
\`\`\`toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
\`\`\`

**For Vercel (\`vercel.json\`):**
\`\`\`json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
\`\`\``
    },
    {
      title: '4. CI/CD Workflows, DNS & Production Monitoring',
      content: `Continuous Integration and Continuous Deployment (CI/CD) automates testing and deployment on every git commit.

### Standard GitHub Actions Pipeline (\`.github/workflows/deploy.yml\`):
\`\`\`yaml
name: Production Deployment

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Run Test Suite
        run: npm test

      - name: Build Production Bundle
        run: npm run build
\`\`\`

### DNS Records Primer:
- **A Record**: Points a root domain (\`example.com\`) to a static IPv4 address (e.g. \`76.76.21.21\`).
- **CNAME Record**: Points a subdomain (\`www.example.com\` or \`app.example.com\`) to another hostname (e.g. \`cname.vercel-dns.com\`).
- **SSL / HTTPS**: Modern hosts automatically provision free SSL certificates via Let's Encrypt, enforcing HTTPS redirection.`
    }
  ],
  examples: [
    {
      title: 'Example: Production netlify.toml & Environment Setup',
      code: `# Complete production netlify.toml configuration file
[build]
  # Directory where build output files are written
  publish = "dist"
  # Command to compile the project
  command = "npm run build"

# Single Page Application (SPA) Client-Side Routing Rewrite
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

# Security & Cache Control Headers
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"

# Cache immutable bundled assets forever (1 year)
[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"`,
      explanation: `Line 3: publish = "dist" specifies that Vite outputs static files to the dist directory.
Line 8: from = "/*" to = "/index.html" status = 200 guarantees deep page refreshes never 404 in React Router.
Line 13: Enterprise security headers protect against clickjacking (X-Frame-Options: DENY) and MIME-type sniffing.
Line 22: Max-age 1 year caching for hashed assets ensures lightning-fast repeat page loads without stale code bugs.`,
      previewOutput: `Configuration validation: PASS
- Build command: npm run build
- Publish folder: dist
- SPA Redirect: /* -> /index.html (Status: 200)
- Security headers: 4 rules active
- Asset caching: 31,536,000s (immutable)`
    }
  ],
  exercises: [
    {
      id: 'deploy-ex-1',
      title: 'Practice 1: Production Environment Variables & Security Audit',
      difficulty: 'Easy',
      type: 'deployment',
      problemStatement: 'Write a validation function parseAndValidateEnv(envContent) that parses a .env.production file, verifies that all frontend keys use the VITE_ prefix, and flags any dangerous secret leaks (such as database credentials or private API keys).',
      requirements: [
        'Parse multi-line KEY=VALUE environment strings, ignoring blank lines and comments starting with #',
        'Verify that all frontend environment variables start with "VITE_"',
        'Detect dangerous secrets: if any variable name contains "SECRET", "PRIVATE", "PASSWORD", or "DATABASE_URL", flag it as an illegal security violation',
        'Return an audit object: { valid: boolean, variables: {}, violations: [] }',
        'valid should be true only when violations.length === 0 and at least one valid VITE_ variable exists'
      ],
      starterCode: `function parseAndValidateEnv(envContent) {
  // Parse environment variables and perform security audit
  
}

const sampleEnv = \`
# Production Environment Config
VITE_API_URL=https://api.codingplatform.com
VITE_APP_NAME=CodingChallengePro
DATABASE_PASSWORD=super_secret_password_123
\`;

console.log(parseAndValidateEnv(sampleEnv));`,
      expectedBehavior: 'Flags DATABASE_PASSWORD as an unsafe secret leak and verifies that VITE_ variables are safely formatted.',
      hints: [
        'Split by newline: envContent.split("\\n").',
        'Filter out lines that are empty or start with "#".',
        'Check forbidden keywords: /(SECRET|PRIVATE|PASSWORD|DATABASE)/i.test(key).'
      ],
      solution: `function parseAndValidateEnv(envContent = '') {
  const lines = envContent.split('\\n');
  const variables = {};
  const violations = [];

  for (let line of lines) {
    line = line.trim();
    if (!line || line.startsWith('#')) continue;

    const eqIndex = line.indexOf('=');
    if (eqIndex === -1) continue;

    const key = line.slice(0, eqIndex).trim();
    const value = line.slice(eqIndex + 1).trim();

    // Check for dangerous sensitive secrets
    const hasSecretName = /(SECRET|PRIVATE|PASSWORD|DATABASE|TOKEN|KEY)/i.test(key);
    if (hasSecretName && !key.startsWith('VITE_PUBLIC_')) {
      violations.push(\`Security Risk: Sensitive secret "\${key}" detected in frontend environment file! Frontend variables are publicly exposed.\`);
    }

    // Check for missing VITE_ prefix
    if (!key.startsWith('VITE_')) {
      violations.push(\`Naming Violation: Variable "\${key}" must be prefixed with "VITE_" for Vite to recognize it.\`);
    }

    variables[key] = value;
  }

  const valid = violations.length === 0 && Object.keys(variables).length > 0;

  return {
    valid,
    variableCount: Object.keys(variables).length,
    variables,
    violations
  };
}

const sampleEnv = \`
# Production Environment Config
VITE_API_URL=https://api.codingplatform.com
VITE_APP_NAME=CodingChallengePro
DATABASE_PASSWORD=super_secret_password_123
\`;

console.log(parseAndValidateEnv(sampleEnv));`,
      solutionExplanation: `1. Splits environment text line-by-line while ignoring blank lines and comments.
2. Identifies dangerous secret keywords (PASSWORD, DATABASE, SECRET) to protect against accidental credentials leaks.
3. Enforces the VITE_ prefix required by modern Vite compilation to bundle variables safely.
4. Returns a comprehensive security audit report.`
    },
    {
      id: 'deploy-ex-2',
      title: 'Practice 2: SPA Client-Side Routing Configuration for Netlify & Vercel',
      difficulty: 'Easy',
      type: 'deployment',
      problemStatement: 'Write a function generateHostConfig(platform) that outputs the exact, validated configuration file content for either "netlify" (netlify.toml) or "vercel" (vercel.json) to solve the Single Page Application 404 page-refresh issue.',
      requirements: [
        'If platform is "netlify", return valid netlify.toml text configuring [build] publish = "dist", command = "npm run build", and [[redirects]] from = "/*" to = "/index.html" status = 200',
        'If platform is "vercel", return valid vercel.json string with rewrites array: [{ "source": "/(.*)", "destination": "/index.html" }]',
        'Include security headers (X-Frame-Options: DENY, X-Content-Type-Options: nosniff)',
        'If invalid platform is passed, throw an Error("Supported platforms: netlify, vercel")'
      ],
      starterCode: `function generateHostConfig(platform) {
  // Generate netlify.toml or vercel.json configuration string
  
}

console.log(generateHostConfig('netlify'));
console.log(generateHostConfig('vercel'));`,
      expectedBehavior: 'Generates syntactically correct TOML or JSON rewrite configurations that eliminate 404 errors on deep route refreshes.',
      hints: [
        'Netlify uses TOML syntax with [[redirects]].',
        'Vercel uses JSON with a rewrites array.',
        'Both must route to /index.html to let React Router take over page display.'
      ],
      solution: `function generateHostConfig(platform) {
  const target = String(platform).trim().toLowerCase();

  if (target === 'netlify') {
    return \`# Netlify Production Configuration
[build]
  publish = "dist"
  command = "npm run build"

# SPA Client-Side Routing Fallback
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

# Security Headers
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
\`.trim();
  } else if (target === 'vercel') {
    const vercelConfig = {
      version: 2,
      builds: [
        { src: "package.json", use: "@vercel/static-build", config: { distDir: "dist" } }
      ],
      rewrites: [
        { source: "/(.*)", destination: "/index.html" }
      ],
      headers: [
        {
          source: "/(.*)",
          headers: [
            { key: "X-Frame-Options", value: "DENY" },
            { key: "X-Content-Type-Options", value: "nosniff" }
          ]
        }
      ]
    };
    return JSON.stringify(vercelConfig, null, 2);
  } else {
    throw new Error('Supported platforms: "netlify", "vercel"');
  }
}

console.log('--- Netlify Config ---');
console.log(generateHostConfig('netlify'));
console.log('\\n--- Vercel Config ---');
console.log(generateHostConfig('vercel'));`,
      solutionExplanation: `1. Generates accurate netlify.toml with [[redirects]] from = "/*" to = "/index.html" status = 200.
2. Generates validated vercel.json with source = "/(.*)" and destination = "/index.html".
3. Adds standard defense-in-depth security headers (X-Frame-Options: DENY).
4. Solves the universal React Router 404 refresh bug on all major static hosts.`
    },
    {
      id: 'deploy-ex-3',
      title: 'Practice 3: Automated GitHub Actions CI/CD Pipeline Workflow',
      difficulty: 'Medium',
      type: 'deployment',
      problemStatement: 'Construct a complete GitHub Actions workflow YAML generator generateCiCdWorkflow(options) that outputs a production-ready .github/workflows/deploy.yml file.',
      requirements: [
        'Options accept: { branch: "main", nodeVersion: "20", testCommand: "npm test", buildCommand: "npm run build", deployTarget: "production" }',
        'Trigger workflow on: push to specified branch and pull_request to specified branch',
        'Workflow steps must include: actions/checkout@v4, actions/setup-node@v4 with cache: "npm", npm ci (clean install), run testCommand, and run buildCommand',
        'Return formatted YAML string with correct two-space indentation and clean step names'
      ],
      starterCode: `function generateCiCdWorkflow(options = {}) {
  // Generate GitHub Actions YAML workflow string
  
}

console.log(generateCiCdWorkflow({ branch: 'main', nodeVersion: '20' }));`,
      expectedBehavior: 'Outputs a valid, well-indented GitHub Actions YAML script capable of automating build and test pipelines.',
      hints: [
        'Use npm ci instead of npm install for reliable, deterministic CI builds.',
        'Include actions/checkout@v4 and actions/setup-node@v4.',
        'Keep YAML indentation consistent with 2 spaces per nesting level.'
      ],
      solution: `function generateCiCdWorkflow(options = {}) {
  const branch = options.branch || 'main';
  const nodeVersion = options.nodeVersion || '20';
  const testCommand = options.testCommand || 'npm test';
  const buildCommand = options.buildCommand || 'npm run build';

  return \`name: Frontend CI/CD Pipeline

on:
  push:
    branches:
      - \${branch}
  pull_request:
    branches:
      - \${branch}

jobs:
  validate-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: 1. Checkout Repository
        uses: actions/checkout@v4

      - name: 2. Set up Node.js \${nodeVersion} Environment
        uses: actions/setup-node@v4
        with:
          node-version: '\${nodeVersion}'
          cache: 'npm'

      - name: 3. Install Dependencies with Clean Lockfile
        run: npm ci

      - name: 4. Execute Automated Test Suite
        run: \${testCommand}

      - name: 5. Compile Optimized Production Bundle
        run: \${buildCommand}

      - name: 6. Verify Artifacts
        run: |
          echo "Build completed successfully."
          ls -la dist/
\`.trim();
}

console.log(generateCiCdWorkflow({ branch: 'main', nodeVersion: '20' }));`,
      solutionExplanation: `1. Configures automated triggers on push and pull_request to safeguard the main deployment branch.
2. actions/setup-node with cache: 'npm' caches ~/.npm to speed up pipeline execution by up to 70%.
3. npm ci installs exact versions from package-lock.json without modifying dependency trees.
4. Validates that tests pass and the bundle builds before allowing any production deployment.`
    },
    {
      id: 'deploy-ex-4',
      title: 'Practice 4: Custom Domain & DNS Records Mapping Validator',
      difficulty: 'Medium',
      type: 'deployment',
      problemStatement: 'Write a DNS configuration engine validateDnsConfiguration(domainName, dnsRecords) that validates whether a custom domain (e.g. "codechallenge.com" or "app.codechallenge.com") has the correct DNS record mappings for production hosting.',
      requirements: [
        'For apex domains (e.g. "example.com"): require an A record pointing to a valid IPv4 address (e.g. "76.76.21.21" for Vercel or "104.198.14.52" for Netlify)',
        'For subdomains (e.g. "app.example.com" or "www.example.com"): require a CNAME record pointing to a valid host alias (e.g. ends with ".vercel-dns.com" or ".netlify.app")',
        'Verify that no conflicting records exist (e.g. CNAME on apex domain without ALIAS support)',
        'Return validation report: { isValid: boolean, domainType: "apex" | "subdomain", errors: [], recommendations: [] }'
      ],
      starterCode: `function validateDnsConfiguration(domainName, dnsRecords) {
  // Validate A and CNAME records based on apex vs subdomain
  
}

const sampleApexRecords = [
  { type: 'A', host: '@', value: '76.76.21.21' },
  { type: 'CNAME', host: 'www', value: 'cname.vercel-dns.com' }
];

console.log(validateDnsConfiguration('codechallenge.com', sampleApexRecords));`,
      expectedBehavior: 'Correctly distinguishes between apex domains and subdomains and verifies the presence of required A and CNAME records.',
      hints: [
        'Apex domains typically have two dot parts (e.g. "site.com"), while subdomains have 3+ (e.g. "app.site.com").',
        'Apex domains require an A record pointing to an IPv4 address.',
        'Subdomains require a CNAME record pointing to the hosting platform domain.'
      ],
      solution: `function validateDnsConfiguration(domainName = '', dnsRecords = []) {
  const domain = String(domainName).trim().toLowerCase();
  const errors = [];
  const recommendations = [];

  const parts = domain.split('.');
  if (parts.length < 2) {
    return {
      isValid: false,
      domainType: 'invalid',
      errors: ['Invalid domain format. Domain must include extension (e.g. example.com).'],
      recommendations: []
    };
  }

  const isApex = parts.length === 2;
  const domainType = isApex ? 'apex' : 'subdomain';

  if (isApex) {
    // Apex domain: requires valid A record
    const aRecord = dnsRecords.find(r => r.type === 'A' && (r.host === '@' || r.host === domain || r.host === ''));
    if (!aRecord) {
      errors.push(\`Missing A Record for apex domain "\${domain}". Must point "@" to your hosting IP address.\`);
    } else {
      // Validate IP format
      const isIp = /^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$/.test(aRecord.value);
      if (!isIp) {
        errors.push(\`Invalid A Record IP: "\${aRecord.value}". Must be a valid IPv4 address.\`);
      }
    }

    // Recommendation for www
    const cnameWww = dnsRecords.find(r => r.type === 'CNAME' && r.host === 'www');
    if (!cnameWww) {
      recommendations.push('Recommended: Add a CNAME record for "www" pointing to your hosting alias to support www visitors.');
    }
  } else {
    // Subdomain: requires CNAME record
    const subLabel = parts[0];
    const cnameRecord = dnsRecords.find(r => r.type === 'CNAME' && (r.host === subLabel || r.host === domain));
    if (!cnameRecord) {
      errors.push(\`Missing CNAME Record for subdomain "\${domain}". Must point "\${subLabel}" to your hosting target.\`);
    }
  }

  recommendations.push('Enable automatic HTTPS & HSTS redirect once DNS propagation finishes.');

  return {
    isValid: errors.length === 0,
    domain,
    domainType,
    errors,
    recommendations
  };
}

const sampleApexRecords = [
  { type: 'A', host: '@', value: '76.76.21.21' },
  { type: 'CNAME', host: 'www', value: 'cname.vercel-dns.com' }
];

console.log(validateDnsConfiguration('codechallenge.com', sampleApexRecords));`,
      solutionExplanation: `1. Analyzes domain name parts to classify between root apex domains and subdomains.
2. For apex domains, enforces an 'A' record pointing to a valid IPv4 server address.
3. For subdomains, enforces a 'CNAME' record linking to the hosting provider's alias.
4. Supplies actionable recommendations including www redirects and SSL/HTTPS enforcement.`
    },
    {
      id: 'deploy-ex-5',
      title: 'Practice 5: Frontend Performance Audit & Dynamic Code-Splitting',
      difficulty: 'Hard',
      type: 'deployment',
      problemStatement: 'Write a bundle analysis function analyzeBundlePerformance(bundleChunks, budgetLimitKb) that audits bundle chunks, identifies oversized JavaScript chunks, flags un-split vendor dependencies, and calculates Core Web Vitals impact ratings.',
      requirements: [
        'Analyze array of chunks: [{ filename: "index.js", sizeKb: 650, isInitial: true }, ...]',
        'Flag chunks exceeding budgetLimitKb (default: 250 KB) as warnings or errors',
        'Identify whether initial critical JS exceeds 350 KB, which severely harms Largest Contentful Paint (LCP) and Interaction to Next Paint (INP)',
        'Calculate estimated Core Web Vitals rating ("Good", "Needs Improvement", "Poor")',
        'Provide actionable optimization recommendations (e.g. React.lazy, dynamic import(), vendor chunk splitting)'
      ],
      starterCode: `function analyzeBundlePerformance(bundleChunks, budgetLimitKb = 250) {
  // Analyze chunk sizes and generate performance diagnosis
  
}

const chunks = [
  { filename: 'index-BZHQ.js', sizeKb: 512, isInitial: true },
  { filename: 'vendor-react.js', sizeKb: 145, isInitial: true },
  { filename: 'workspace-chunk.js', sizeKb: 85, isInitial: false }
];

console.log(analyzeBundlePerformance(chunks));`,
      expectedBehavior: 'Produces an audit report diagnosing bundle bloat with specific recommendations to configure dynamic import() and code-splitting.',
      hints: [
        'Sum initial chunks: const initialSize = chunks.filter(c => c.isInitial).reduce((sum, c) => sum + c.sizeKb, 0);',
        'If initialSize <= 250 KB -> "Good", <= 400 KB -> "Needs Improvement", > 400 KB -> "Poor".',
        'Recommend React.lazy() for heavy non-initial routes.'
      ],
      solution: `function analyzeBundlePerformance(bundleChunks = [], budgetLimitKb = 250) {
  const totalSizeKb = bundleChunks.reduce((sum, c) => sum + (c.sizeKb || 0), 0);
  const initialChunks = bundleChunks.filter(c => c.isInitial);
  const initialSizeKb = initialChunks.reduce((sum, c) => sum + (c.sizeKb || 0), 0);

  const oversizedChunks = [];
  const recommendations = [];

  bundleChunks.forEach(chunk => {
    if (chunk.sizeKb > budgetLimitKb) {
      oversizedChunks.push({
        filename: chunk.filename,
        sizeKb: chunk.sizeKb,
        excessKb: chunk.sizeKb - budgetLimitKb
      });
    }
  });

  // Core Web Vitals assessment based on initial critical bundle
  let performanceRating = 'Good';
  if (initialSizeKb > 450) {
    performanceRating = 'Poor';
    recommendations.push('Critical: Initial JS bundle exceeds 450 KB. This will delay Largest Contentful Paint (LCP) on mobile 3G/4G connections.');
  } else if (initialSizeKb > 250) {
    performanceRating = 'Needs Improvement';
    recommendations.push('Warning: Initial JS bundle exceeds 250 KB recommended budget.');
  }

  if (oversizedChunks.length > 0) {
    recommendations.push('Use React.lazy() and dynamic import() to split heavy routes (e.g. Code Editor, Admin Dashboards) into separate on-demand chunks.');
    recommendations.push('Configure Vite/Rollup build.rollupOptions.output.manualChunks to split vendor dependencies into separate cacheable files.');
  }

  recommendations.push('Verify that text assets are compressed with Brotli or Gzip on your production CDN server.');

  return {
    totalBundleSizeKb: Math.round(totalSizeKb),
    initialBundleSizeKb: Math.round(initialSizeKb),
    chunkCount: bundleChunks.length,
    performanceRating,
    budgetLimitKb,
    oversizedChunkCount: oversizedChunks.length,
    oversizedChunks,
    recommendations
  };
}

const chunks = [
  { filename: 'index-BZHQ.js', sizeKb: 512, isInitial: true },
  { filename: 'vendor-react.js', sizeKb: 145, isInitial: true },
  { filename: 'workspace-chunk.js', sizeKb: 85, isInitial: false }
];

console.log(analyzeBundlePerformance(chunks, 250));`,
      solutionExplanation: `1. Analyzes bundle chunk sizes against performance budgets (250 KB per chunk).
2. Calculates total initial critical payload (657 KB in sample), highlighting direct impact on Core Web Vitals (LCP and INP).
3. Evaluates overall performance score as 'Poor' when initial JS exceeds 450 KB.
4. Generates concrete engineering recommendations: React.lazy() dynamic route splitting, manual vendor chunking, and CDN Brotli compression.`
    }
  ]
};
