export const jsBasicsTopic = {
  id: 'javascript-basics',
  title: 'JavaScript Basics',
  shortTitle: 'JavaScript Basics',
  icon: 'Zap',
  description: 'Master core JavaScript programming fundamentals. Learn variable declarations, primitive & reference data types, operators, conditional control flow, functions, array & object manipulation, DOM selection, and browser event listeners.',
  subtopics: [
    'Variables: var, let, and const differences & best practices',
    'Primitive data types (string, number, boolean, null, undefined, symbol, bigint)',
    'Reference types: objects, arrays, and functions in memory',
    'Operators (arithmetic, strict equality === vs ==, logical &&, ||, ?? nullish coalescing, ternary)',
    'Conditional statements (if/else if/else, switch case statements)',
    'Loops (for, while, do...while, for...of for arrays, for...in for objects)',
    'Functions: declarations, expressions, parameters, return values, default parameters',
    'Arrays and methods: push, pop, shift, unshift, slice, splice, map, filter, reduce',
    'Objects: property access, methods, Object.keys(), Object.values(), Object.entries()',
    'DOM Selection & Manipulation: querySelector, createElement, appendChild, classList, innerText',
    'Event listeners (addEventListener, click, input, submit, preventDefault, event delegation)',
    'Form validation & DOM user feedback'
  ],
  theory: [
    {
      title: '1. Variables, Data Types & Memory Storage',
      content: `JavaScript is a dynamically typed, prototype-based language. In modern development, we declare variables using \`const\` by default and \`let\` when reassignment is required. Never use legacy \`var\` due to function scoping and hoisting bugs.

### Variable Declarations Compared:
| Keyword | Scope | Hoisting Behavior | Can Be Reassigned? |
| :--- | :--- | :--- | :--- |
| **\`const\`** | Block (\`{}\`) | Temporal Dead Zone (TDZ) | No (Immutable binding) |
| **\`let\`** | Block (\`{}\`) | Temporal Dead Zone (TDZ) | Yes |
| **\`var\`** | Function / Global | Hoisted with \`undefined\` | Yes (Avoid in modern code) |

### Primitive vs Reference Types:
- **Primitives** (Stored directly on the Call Stack by value): \`String\`, \`Number\`, \`Boolean\`, \`Null\`, \`Undefined\`, \`Symbol\`, \`BigInt\`.
  \`\`\`js
  let a = 10;
  let b = a; // Copy of value
  b = 20;    // a remains 10
  \`\`\`
- **Reference Types** (Stored in Heap memory; variable holds memory pointer): \`Objects\`, \`Arrays\`, \`Functions\`.
  \`\`\`js
  const user1 = { name: "Aarav" };
  const user2 = user1; // Copies pointer address!
  user2.name = "Vikram"; // Modifies user1.name too!
  \`\`\``
    },
    {
      title: '2. Functions, Control Flow & Data Manipulation',
      content: `Functions are first-class citizens in JavaScript—they can be stored in variables, passed into arguments, and returned from other functions.

### Functions:
\`\`\`js
// Function Declaration (Hoisted)
function calculateTotal(subtotal, taxRate = 0.08) {
  return subtotal + (subtotal * taxRate);
}

// Arrow Function Expression (Lexical this)
const applyDiscount = (price, percentage) => price * (1 - percentage / 100);
\`\`\`

### Powerful Array Methods:
\`\`\`js
const products = [
  { id: 1, title: 'Mechanical Keyboard', price: 90, inStock: true },
  { id: 2, title: 'USB-C Cable', price: 15, inStock: true },
  { id: 3, title: 'UltraWide Monitor', price: 450, inStock: false },
];

// filter(): keep items meeting condition
const available = products.filter(p => p.inStock);

// map(): transform each item
const titles = products.map(p => p.title);

// reduce(): accumulate items into a single value
const totalInventoryValue = products.reduce((acc, p) => acc + p.price, 0);
\`\`\``
    },
    {
      title: '3. DOM Manipulation & Event-Driven Architecture',
      content: `The Document Object Model (DOM) is an object-oriented representation of the HTML document. JavaScript manipulates DOM nodes to create interactive user experiences.

### Selecting & Creating Elements:
\`\`\`js
// Selecting elements
const submitBtn = document.querySelector('#submit-btn');
const cards = document.querySelectorAll('.card');

// Creating and inserting elements
const badge = document.createElement('span');
badge.classList.add('badge', 'active');
badge.textContent = 'Verified User';
document.querySelector('.profile').appendChild(badge);
\`\`\`

### Event Handling & Event Delegation:
Instead of adding individual event listeners to hundreds of child items, **event delegation** attaches a single listener to the parent element, taking advantage of event bubbling (\`e.target\`):

\`\`\`js
const list = document.querySelector('#todo-list');

list.addEventListener('click', (e) => {
  // Check if the clicked element was a delete button
  if (e.target.matches('.delete-btn')) {
    const item = e.target.closest('li');
    item.remove();
  }
});
\`\`\``
    }
  ],
  examples: [
    {
      title: 'Example: Dynamic Cart Calculator & DOM Renderer',
      code: `// Sample shopping cart items
const cartItems = [
  { id: 'p1', name: 'Wireless Ergonomic Mouse', price: 49.99, quantity: 2 },
  { id: 'p2', name: 'Mechanical Keycaps Set', price: 24.50, quantity: 1 },
  { id: 'p3', name: 'Desk Mat (Extended)', price: 19.99, quantity: 3 }
];

// Calculate totals using array methods
function calculateCartSummary(items, discountCode = '') {
  const subtotal = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  
  let discountPercentage = 0;
  if (discountCode.trim().toUpperCase() === 'DEV2026') {
    discountPercentage = 15; // 15% discount
  }
  
  const discountAmount = subtotal * (discountPercentage / 100);
  const taxAmount = (subtotal - discountAmount) * 0.08; // 8% sales tax
  const finalTotal = subtotal - discountAmount + taxAmount;
  
  return {
    itemCount: items.reduce((cnt, item) => cnt + item.quantity, 0),
    subtotal: subtotal.toFixed(2),
    discount: discountAmount.toFixed(2),
    tax: taxAmount.toFixed(2),
    finalTotal: finalTotal.toFixed(2)
  };
}

const summary = calculateCartSummary(cartItems, 'DEV2026');
console.log('Cart Items Count:', summary.itemCount);
console.log('Subtotal: $' + summary.subtotal);
console.log('Discount applied: -$' + summary.discount);
console.log('Tax (8%): $' + summary.tax);
console.log('Grand Total: $' + summary.finalTotal);`,
      explanation: `Line 10: Array.reduce() computes subtotal by multiplying unit price by quantity for each product.
Line 13: String methods .trim() and .toUpperCase() normalize the coupon input before validation.
Line 23: .toFixed(2) formats floats to exactly 2 decimal currency places.
Line 27: Function returns a clean JavaScript object representing the invoice.`,
      previewOutput: `Cart Items Count: 6
Subtotal: $184.45
Discount applied: -$27.67
Tax (8%): $12.54
Grand Total: $169.32`
    }
  ],
  exercises: [
    {
      id: 'js-ex-1',
      title: 'Practice 1: Temperature Converter & Weather Formatter',
      difficulty: 'Easy',
      type: 'javascript',
      problemStatement: 'Write a JavaScript function convertTemperature(value, unit) that converts temperature between Celsius and Fahrenheit. Return a formatted string with classification.',
      requirements: [
        'If scale is "C", convert Celsius to Fahrenheit: (value * 9/5) + 32',
        'If scale is "F", convert Fahrenheit to Celsius: (value - 32) * 5/9',
        'Round the converted value to 1 decimal place using Number(result.toFixed(1))',
        'Return an object with: { originalValue, originalUnit, convertedValue, targetUnit, advisory }',
        'Advisory rules in Celsius: <= 0 is "Freezing", 1 to 20 is "Moderate", >= 21 is "Warm"',
        'If invalid scale is passed, throw an Error with message "Invalid temperature unit"'
      ],
      starterCode: `function convertTemperature(value, unit) {
  // Write your conversion logic here
  
}

// Test cases
console.log(convertTemperature(100, 'C'));
console.log(convertTemperature(32, 'F'));
console.log(convertTemperature(25, 'C'));`,
      expectedBehavior: 'Function returns conversion objects with numerical converted value and weather advisory strings.',
      hints: [
        'Standard formulas: C to F is (C * 9/5) + 32; F to C is (F - 32) * 5/9.',
        'Convert unit to uppercase: unit.toUpperCase() to handle both "c" and "C".',
        'Use if (unit !== "C" && unit !== "F") throw new Error(...)'
      ],
      solution: `function convertTemperature(value, unit) {
  if (typeof value !== 'number' || isNaN(value)) {
    throw new Error('Temperature value must be a valid number');
  }

  const normalizedUnit = String(unit).trim().toUpperCase();
  if (normalizedUnit !== 'C' && normalizedUnit !== 'F') {
    throw new Error('Invalid temperature unit. Must be "C" or "F"');
  }

  let convertedValue;
  let targetUnit;
  let tempInCelsius;

  if (normalizedUnit === 'C') {
    convertedValue = (value * 9 / 5) + 32;
    targetUnit = 'F';
    tempInCelsius = value;
  } else {
    convertedValue = (value - 32) * 5 / 9;
    targetUnit = 'C';
    tempInCelsius = convertedValue;
  }

  let advisory = '';
  if (tempInCelsius <= 0) {
    advisory = 'Freezing';
  } else if (tempInCelsius <= 20) {
    advisory = 'Moderate';
  } else {
    advisory = 'Warm';
  }

  return {
    originalValue: value,
    originalUnit: normalizedUnit,
    convertedValue: Number(convertedValue.toFixed(1)),
    targetUnit: targetUnit,
    advisory: advisory
  };
}

console.log(convertTemperature(100, 'C'));
console.log(convertTemperature(32, 'F'));
console.log(convertTemperature(25, 'C'));`,
      solutionExplanation: `1. Validates that value is a numeric type and scale is normalized to uppercase.
2. Applies the standard thermodynamic conversion formulas for Celsius and Fahrenheit.
3. Calculates advisory status by checking temperature in Celsius against specified thresholds.
4. Returns an object with numerical results rounded cleanly with Number(convertedValue.toFixed(1)).`
    },
    {
      id: 'js-ex-2',
      title: 'Practice 2: Dynamic E-Commerce Cart & Discount Calculator',
      difficulty: 'Easy',
      type: 'javascript',
      problemStatement: 'Write a function calculateCartInvoice(cart, couponCode) that calculates the subtotal, applies coupon discounts, calculates tiered shipping costs, and returns the final receipt.',
      requirements: [
        'Calculate subtotal = sum of (price * quantity) for all items in cart array',
        'Support coupon codes: "WELCOME10" (10% off subtotal), "FLAT20" ($20 off subtotal if subtotal >= 50)',
        'Shipping rules: Free shipping ($0) if subtotal after discount >= 100, otherwise flat $10 shipping',
        'Sales tax: 7% on the discounted subtotal',
        'Return formatted object: { itemCount, subtotal, discount, tax, shipping, grandTotal } with all monetary values rounded to 2 decimals'
      ],
      starterCode: `function calculateCartInvoice(cart, couponCode = '') {
  // Write your cart calculation logic below
  
}

const sampleCart = [
  { title: 'Full-Stack Book', price: 35.00, quantity: 2 },
  { title: 'USB-C Adapter', price: 15.50, quantity: 1 }
];

console.log(calculateCartInvoice(sampleCart, 'WELCOME10'));`,
      expectedBehavior: 'Returns a detailed invoice object with accurately calculated discount, shipping, tax, and grand total.',
      hints: [
        'Use cart.reduce() to sum item counts and subtotal.',
        'Make sure discount cannot exceed subtotal (Math.min(discount, subtotal)).',
        'Calculate tax on subtotal - discount before adding shipping.'
      ],
      solution: `function calculateCartInvoice(cart, couponCode = '') {
  if (!Array.isArray(cart) || cart.length === 0) {
    return {
      itemCount: 0,
      subtotal: 0,
      discount: 0,
      tax: 0,
      shipping: 0,
      grandTotal: 0
    };
  }

  const itemCount = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
  const subtotal = cart.reduce((sum, item) => sum + ((item.price || 0) * (item.quantity || 1)), 0);

  let discount = 0;
  const code = String(couponCode).trim().toUpperCase();

  if (code === 'WELCOME10') {
    discount = subtotal * 0.10;
  } else if (code === 'FLAT20' && subtotal >= 50) {
    discount = 20.00;
  }

  discount = Math.min(discount, subtotal);
  const discountedSubtotal = subtotal - discount;

  const tax = discountedSubtotal * 0.07;
  const shipping = discountedSubtotal >= 100 ? 0 : 10.00;
  const grandTotal = discountedSubtotal + tax + shipping;

  return {
    itemCount,
    subtotal: Number(subtotal.toFixed(2)),
    discount: Number(discount.toFixed(2)),
    tax: Number(tax.toFixed(2)),
    shipping: Number(shipping.toFixed(2)),
    grandTotal: Number(grandTotal.toFixed(2))
  };
}

const sampleCart = [
  { title: 'Full-Stack Book', price: 35.00, quantity: 2 },
  { title: 'USB-C Adapter', price: 15.50, quantity: 1 }
];

console.log(calculateCartInvoice(sampleCart, 'WELCOME10'));`,
      solutionExplanation: `1. Array.reduce() computes total quantity and raw subtotal.
2. The coupon code validator checks conditions: "WELCOME10" provides 10% off, and "FLAT20" requires subtotal >= $50.
3. Math.min(discount, subtotal) protects against negative values.
4. Free shipping applies when discounted subtotal reaches or exceeds $100.`
    },
    {
      id: 'js-ex-3',
      title: 'Practice 3: Interactive Todo List Manager with DOM Manipulation',
      difficulty: 'Medium',
      type: 'javascript',
      problemStatement: 'Write a TodoListManager class in JavaScript that manipulates the DOM to add tasks, toggle completion states, delete tasks, and update a live counter of remaining items.',
      requirements: [
        'TodoListManager constructor accepts containerElement reference',
        'Method addTask(text): creates <li> with task text, a toggle checkbox, and a delete button',
        'When checkbox is clicked, toggle .completed class on the <li> and update remaining counter',
        'When delete button is clicked, remove the <li> from the DOM and update remaining counter',
        'Method getRemainingCount(): returns integer of uncompleted tasks',
        'Method clearCompleted(): removes all <li> items with class .completed'
      ],
      starterCode: `class TodoListManager {
  constructor(container) {
    this.container = container;
    this.list = document.createElement('ul');
    this.counterEl = document.createElement('span');
    this.init();
  }

  init() {
    // Append list and counter to container
  }

  addTask(text) {
    // Create task item, checkbox, and delete button
  }

  getRemainingCount() {
    // Return count of uncompleted tasks
  }

  clearCompleted() {
    // Remove completed tasks
  }
}`,
      expectedBehavior: 'A fully functional Todo List manager that dynamically modifies DOM nodes, attaches event listeners, and tracks live pending task counts.',
      hints: [
        'Use document.createElement("li"), document.createElement("input"), and document.createElement("button").',
        'Attach a change listener to the checkbox to toggle "completed" on the parent <li>.',
        'Use this.list.querySelectorAll("li:not(.completed)").length to compute remaining count.'
      ],
      solution: `class TodoListManager {
  constructor(container) {
    this.container = container;
    this.list = document.createElement('ul');
    this.list.className = 'todo-items-list';
    this.counterEl = document.createElement('div');
    this.counterEl.className = 'todo-counter';
    this.init();
  }

  init() {
    this.container.appendChild(this.list);
    this.container.appendChild(this.counterEl);
    this.updateCounter();
  }

  addTask(text) {
    if (!text || !text.trim()) return;

    const li = document.createElement('li');
    li.className = 'todo-item';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', () => {
      li.classList.toggle('completed', checkbox.checked);
      this.updateCounter();
    });

    const span = document.createElement('span');
    span.className = 'todo-text';
    span.textContent = text.trim();

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = '×';
    deleteBtn.setAttribute('aria-label', 'Delete task');
    deleteBtn.addEventListener('click', () => {
      li.remove();
      this.updateCounter();
    });

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);

    this.list.appendChild(li);
    this.updateCounter();
    return li;
  }

  getRemainingCount() {
    return this.list.querySelectorAll('li:not(.completed)').length;
  }

  clearCompleted() {
    const completedItems = this.list.querySelectorAll('li.completed');
    completedItems.forEach(item => item.remove());
    this.updateCounter();
  }

  updateCounter() {
    const remaining = this.getRemainingCount();
    const total = this.list.querySelectorAll('li').length;
    this.counterEl.textContent = \`\${remaining} of \${total} tasks remaining\`;
  }
}`,
      solutionExplanation: `1. The class encapsulates DOM node creation and event listeners cleanly.
2. addEventListener on checkbox toggles the 'completed' class and immediately recalculates the counter.
3. deleteBtn.addEventListener calls li.remove() to cleanly unmount the element from the DOM tree.
4. querySelectorAll('li:not(.completed)') reliably calculates remaining active tasks using modern CSS selector syntax.`
    },
    {
      id: 'js-ex-4',
      title: 'Practice 4: Real-Time Password Strength Validator with DOM Feedback',
      difficulty: 'Medium',
      type: 'javascript',
      problemStatement: 'Build a real-time password strength evaluation function and DOM inspector that checks minimum length, uppercase, lowercase, numbers, and special characters.',
      requirements: [
        'Write evaluatePasswordStrength(password): tests 5 criteria: length >= 8, lowercase letter, uppercase letter, number, and special symbol (!@#$%^&*)',
        'Score calculation: 1 criteria passed = "Weak", 2-3 passed = "Medium", 4 passed = "Strong", all 5 passed = "Very Strong"',
        'Return result object: { score: 1-5, strength: string, passedCriteria: [], missingCriteria: [], isValid: boolean }',
        'isValid is true only if length >= 8 AND score >= 4'
      ],
      starterCode: `function evaluatePasswordStrength(password) {
  // Define regex rules and calculate score
  
}

// Test cases
console.log(evaluatePasswordStrength('secret'));
console.log(evaluatePasswordStrength('P@ssword2026!'));`,
      expectedBehavior: 'Accurately scores passwords from 1 to 5, listing fulfilled and unfulfilled requirements along with strength labels.',
      hints: [
        'Use regex: /[a-z]/ for lowercase, /[A-Z]/ for uppercase, /[0-9]/ for numbers, /[^A-Za-z0-9]/ for symbols.',
        'Push passing rules into an array to compute score = passedCriteria.length.',
        'Use switch or if/else to translate numerical score into string labels.'
      ],
      solution: `function evaluatePasswordStrength(password) {
  const pwd = String(password || '');
  
  const rules = [
    { id: 'min_length', label: 'At least 8 characters', test: (s) => s.length >= 8 },
    { id: 'lowercase', label: 'Contains a lowercase letter', test: (s) => /[a-z]/.test(s) },
    { id: 'uppercase', label: 'Contains an uppercase letter', test: (s) => /[A-Z]/.test(s) },
    { id: 'number', label: 'Contains a number (0-9)', test: (s) => /[0-9]/.test(s) },
    { id: 'symbol', label: 'Contains a special symbol (!@#$%^&*)', test: (s) => /[^A-Za-z0-9]/.test(s) }
  ];

  const passedCriteria = [];
  const missingCriteria = [];

  for (const rule of rules) {
    if (rule.test(pwd)) {
      passedCriteria.push(rule.label);
    } else {
      missingCriteria.push(rule.label);
    }
  }

  const score = passedCriteria.length;
  let strength = 'Very Weak';

  if (score === 5) {
    strength = 'Very Strong';
  } else if (score === 4) {
    strength = 'Strong';
  } else if (score >= 2) {
    strength = 'Medium';
  } else if (score === 1) {
    strength = 'Weak';
  }

  const isValid = pwd.length >= 8 && score >= 4;

  return {
    score,
    strength,
    passedCriteria,
    missingCriteria,
    isValid
  };
}

console.log(evaluatePasswordStrength('secret'));
console.log(evaluatePasswordStrength('P@ssword2026!'));`,
      solutionExplanation: `1. Organizes password requirements as an array of rule objects with test functions.
2. Regex tests verify character diversity (lowercase, uppercase, digit, non-alphanumeric symbol).
3. Compiles passed and missing criteria lists for live user UI feedback.
4. Determines isValid requiring both minimum length and at least 4 out of 5 criteria met.`
    },
    {
      id: 'js-ex-5',
      title: 'Practice 5: Multi-Filter Product Catalog with Event Delegation',
      difficulty: 'Hard',
      type: 'javascript',
      problemStatement: 'Build a complete ProductCatalogEngine that filters an array of products by category, search text, and price range, rendering the filtered items dynamically with an event delegation click handler for cart actions.',
      requirements: [
        'Store an array of at least 5 products with id, title, category, price, and rating',
        'Method filterProducts(criteria): filters products matching criteria.category (if specified and not "all"), criteria.maxPrice (if specified), and criteria.search (case-insensitive substring in title)',
        'Method sortProducts(products, sortBy): supports sorting by "price_asc", "price_desc", "rating_desc", and "title_asc"',
        'Method attachCartHandler(container, onAddToCart): uses event delegation to listen for clicks on button.add-to-cart, extracting data-product-id and calling onAddToCart(productId)'
      ],
      starterCode: `class ProductCatalogEngine {
  constructor(products) {
    this.products = products;
  }

  filterProducts(criteria) {
    // Filter by category, maxPrice, and search keyword
  }

  sortProducts(products, sortBy) {
    // Sort products based on sortBy key
  }

  attachCartHandler(container, onAddToCart) {
    // Use event delegation on container
  }
}`,
      expectedBehavior: 'A robust catalog engine capable of multi-criteria filtering, multi-order sorting, and memory-efficient event delegation.',
      hints: [
        'Array.filter() can check multiple conditions sequentially.',
        'In sortProducts, use .slice() first to avoid mutating the original array: [...products].sort(...)',
        'In attachCartHandler, check e.target.closest("button.add-to-cart") to handle clicks on child icons.'
      ],
      solution: `class ProductCatalogEngine {
  constructor(products = []) {
    this.products = [...products];
  }

  filterProducts(criteria = {}) {
    const { category, maxPrice, search } = criteria;
    const query = search ? search.trim().toLowerCase() : '';

    return this.products.filter(item => {
      // Category filter
      if (category && category !== 'all' && item.category !== category) {
        return false;
      }

      // Max price filter
      if (typeof maxPrice === 'number' && item.price > maxPrice) {
        return false;
      }

      // Search keyword filter
      if (query && !item.title.toLowerCase().includes(query)) {
        return false;
      }

      return true;
    });
  }

  sortProducts(products, sortBy = 'price_asc') {
    const sorted = [...products];

    switch (sortBy) {
      case 'price_asc':
        return sorted.sort((a, b) => a.price - b.price);
      case 'price_desc':
        return sorted.sort((a, b) => b.price - a.price);
      case 'rating_desc':
        return sorted.sort((a, b) => b.rating - a.rating);
      case 'title_asc':
        return sorted.sort((a, b) => a.title.localeCompare(b.title));
      default:
        return sorted;
    }
  }

  attachCartHandler(container, onAddToCart) {
    if (!container || typeof onAddToCart !== 'function') return;

    container.addEventListener('click', (event) => {
      const button = event.target.closest('button.add-to-cart');
      if (button && container.contains(button)) {
        const productId = button.dataset.productId || button.getAttribute('data-product-id');
        if (productId) {
          onAddToCart(productId);
        }
      }
    });
  }
}

// Sample usage
const items = [
  { id: '101', title: 'React Pro Course', category: 'frontend', price: 89.99, rating: 4.9 },
  { id: '102', title: 'CSS Mastery Guide', category: 'frontend', price: 29.99, rating: 4.7 },
  { id: '103', title: 'Python Backend Systems', category: 'backend', price: 99.99, rating: 4.8 }
];

const engine = new ProductCatalogEngine(items);
const filtered = engine.filterProducts({ category: 'frontend', maxPrice: 50 });
console.log('Filtered Products:', filtered);`,
      solutionExplanation: `1. Implements non-mutating filtering using Array.filter() and spreading [...products].
2. localeCompare guarantees correct alphabetical sorting for international titles.
3. Event delegation on the parent container intercepts clicks using event.target.closest('button.add-to-cart'), removing the need to bind individual event listeners when products are added or removed dynamically.
4. Reads dataset.productId safely for seamless integration with frontend rendering.`
    }
  ]
};
