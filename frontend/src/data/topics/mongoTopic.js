export const mongoTopic = {
  id: 'mongodb',
  title: 'MongoDB',
  shortTitle: 'MongoDB',
  icon: 'Database',
  description: 'Master modern NoSQL document databases. Learn JSON/BSON structures, collections, rich CRUD query operations, update operators, aggregation pipelines, indexing, schema design, and connecting frontend applications via REST APIs.',
  subtopics: [
    'Introduction to NoSQL & document-oriented databases vs relational SQL',
    'BSON (Binary JSON) format and core data types (ObjectId, Date, Arrays, Nested Objects)',
    'Databases, Collections, and Documents hierarchy',
    'Create operations: insertOne() and insertMany()',
    'Read operations: find(), findOne(), projections, sorting (sort()), and pagination (skip(), limit())',
    'Comparison operators ($eq, $ne, $gt, $gte, $lt, $lte, $in, $nin)',
    'Logical operators ($and, $or, $not, $nor) and element operators ($exists, $type)',
    'Update operations: updateOne(), updateMany(), $set, $unset, $inc, $push, $pull, $addToSet',
    'Delete operations: deleteOne() and deleteMany()',
    'Aggregation Framework ($match, $group, $sort, $project, $unwind, $lookup)',
    'Schema design patterns (Embedding vs Referencing) and Indexing for performance',
    'Connecting React frontend applications to MongoDB through REST/JSON APIs'
  ],
  theory: [
    {
      title: '1. NoSQL Architecture: Collections & The Document Model',
      content: `MongoDB is a document-oriented NoSQL database designed for high scalability and flexible data structures. Instead of rigid tables with fixed rows and foreign keys like SQL databases, MongoDB stores data in flexible, JSON-like **BSON (Binary JSON)** documents organized into **Collections**.

### Relational SQL vs. MongoDB Terminology:
| Relational (SQL) | MongoDB (NoSQL) | Description |
| :--- | :--- | :--- |
| Database | **Database** | Container of data |
| Table | **Collection** | Grouping of related documents (no rigid schema enforced) |
| Row / Record | **Document** | Individual JSON/BSON record with key-value pairs |
| Column | **Field** | Key in a document |
| Primary Key | **\`_id\`** | Unique identifier (automatically an \`ObjectId\`) |
| JOIN | **\`$lookup\` / Embedding** | Linking related data |

### Anatomical Anatomy of a BSON Document:
\`\`\`json
{
  "_id": "671289abc1234567890defab",
  "title": "Modern Frontend Development",
  "category": "Frontend",
  "rating": 4.9,
  "enrolledStudents": 1420,
  "tags": ["React", "HTML5", "CSS3", "JavaScript"],
  "instructor": {
    "name": "Dr. Sarah Lin",
    "verified": true
  },
  "createdAt": "2026-10-18T10:00:00Z"
}
\`\`\``
    },
    {
      title: '2. CRUD Operations & Query Syntax',
      content: `MongoDB queries are expressed as JSON objects specifying matching criteria:

### 1. Create (Insert):
\`\`\`js
db.developers.insertOne({
  name: "Arjun Verma",
  role: "Frontend Engineer",
  skills: ["React", "CSS3"],
  status: "active"
});
\`\`\`

### 2. Read (Query, Project, Sort):
\`\`\`js
// Find active developers with rating >= 4.5, sort by rating descending
db.developers.find(
  {
    status: "active",
    rating: { $gte: 4.5 }
  },
  { name: 1, skills: 1, _id: 0 } // Projection: include only name & skills
).sort({ rating: -1 }).limit(10);
\`\`\`

### 3. Update (Atomic Modifiers):
Never overwrite an entire document! Use atomic update operators:
\`\`\`js
db.developers.updateOne(
  { name: "Arjun Verma" },
  {
    $set: { status: "Senior Developer" },
    $inc: { projectsCompleted: 1 },
    $push: { skills: "TypeScript" }
  }
);
\`\`\`

### 4. Delete:
\`\`\`js
db.developers.deleteOne({ _id: targetId });
\`\`\``
    },
    {
      title: '3. Aggregation Pipelines & Connecting to Frontend APIs',
      content: `The **Aggregation Pipeline** is a framework for data transformation modeled on the concept of data processing pipelines. Documents enter a multi-stage pipeline that transforms the documents into aggregated results:

\`\`\`js
// Calculate average course rating grouped by category
db.courses.aggregate([
  { $match: { isPublished: true } },
  { 
    $group: {
      _id: "$category",
      avgRating: { $avg: "$rating" },
      courseCount: { $sum: 1 }
    }
  },
  { $sort: { avgRating: -1 } }
]);
\`\`\`

### Connecting Frontend Applications via REST:
Frontend React applications do not connect directly to MongoDB (which would expose database credentials to the browser). Instead:
1. **React Client**: Dispatches an authenticated HTTP \`fetch('/api/courses')\`.
2. **Backend API (Django / Express)**: Validates authentication, queries MongoDB via PyMongo or Mongoose (\`db.courses.find()\`).
3. **Database**: Returns BSON documents.
4. **Backend**: Serializes documents to standard JSON and sends HTTP response.
5. **React**: Receives JSON data and renders components with \`.map()\`.`
    }
  ],
  examples: [
    {
      title: 'Example: Course Catalog Filter, Projection & Sorting',
      code: `// Sample collection documents
const coursesCollection = [
  { _id: 'c1', title: 'HTML5 & Responsive Web Design', category: 'Frontend', price: 29.99, rating: 4.8, isPublished: true },
  { _id: 'c2', title: 'Advanced CSS Animations', category: 'Frontend', price: 19.99, rating: 4.3, isPublished: true },
  { _id: 'c3', title: 'React Hooks & State Architecture', category: 'Frontend', price: 49.99, rating: 4.9, isPublished: true },
  { _id: 'c4', title: 'Unpublished Draft Course', category: 'Backend', price: 39.99, rating: 3.5, isPublished: false }
];

// Query: Find published Frontend courses with rating >= 4.5, sort by rating desc
function queryCourses(collection) {
  return collection
    .filter(course => course.isPublished === true && course.category === 'Frontend' && course.rating >= 4.5)
    .sort((a, b) => b.rating - a.rating)
    .map(({ title, rating, price }) => ({ title, rating, price })); // Projection
}

const results = queryCourses(coursesCollection);
console.log('Query Match Count:', results.length);
console.log('Top Rated Courses:', JSON.stringify(results, null, 2));`,
      explanation: `Line 11: .filter() implements MongoDB query criteria { isPublished: true, category: 'Frontend', rating: { $gte: 4.5 } }.
Line 12: .sort((a, b) => b.rating - a.rating) simulates MongoDB .sort({ rating: -1 }).
Line 13: Object destructuring and mapping simulates MongoDB projection { title: 1, rating: 1, price: 1, _id: 0 }.`,
      previewOutput: `Query Match Count: 2
Top Rated Courses: [
  {
    "title": "React Hooks & State Architecture",
    "rating": 4.9,
    "price": 49.99
  },
  {
    "title": "HTML5 & Responsive Web Design",
    "rating": 4.8,
    "price": 29.99
  }
]`
    }
  ],
  exercises: [
    {
      id: 'mongo-ex-1',
      title: 'Practice 1: Developer Document Insertion & Status Query',
      difficulty: 'Easy',
      type: 'mongodb',
      problemStatement: 'Given a collection of developer records, write a query function that inserts a new developer document and queries all active developers who possess "React" in their skills array.',
      requirements: [
        'Document to insert: { name: "Ananya Das", role: "Frontend Engineer", skills: ["HTML5", "CSS3", "React"], status: "active", rating: 4.8 }',
        'Insert document into collection using an immutable push/clone',
        'Query the updated collection for documents where: status === "active" AND skills includes "React"',
        'Project only { name, role, skills, rating }',
        'Return array of matching developer profiles'
      ],
      sampleData: [
        { _id: 'd1', name: 'Rohan Sharma', role: 'Full-Stack Developer', skills: ['Python', 'Django', 'React'], status: 'active', rating: 4.9 },
        { _id: 'd2', name: 'Kavita Rao', role: 'Backend Developer', skills: ['Java', 'Spring', 'SQL'], status: 'inactive', rating: 4.2 },
        { _id: 'd3', name: 'Manish Kumar', role: 'UI Engineer', skills: ['HTML5', 'CSS3', 'Vue'], status: 'active', rating: 4.4 }
      ],
      starterCode: `function insertAndQueryDevelopers(developers) {
  const newDeveloper = {
    _id: 'd4',
    name: "Ananya Das",
    role: "Frontend Engineer",
    skills: ["HTML5", "CSS3", "React"],
    status: "active",
    rating: 4.8
  };

  // 1. Insert new developer into array
  
  // 2. Query for active developers with "React" skill
  
  // 3. Project name, role, skills, rating
  
}`,
      expectedBehavior: 'Returns matching active developers including Rohan Sharma and the newly inserted Ananya Das.',
      hints: [
        'To clone and insert: const updatedCollection = [...developers, newDeveloper];',
        'Use dev.status === "active" && dev.skills.includes("React") in the filter.',
        'Use .map(({ name, role, skills, rating }) => ({ name, role, skills, rating })) for projection.'
      ],
      solution: `function insertAndQueryDevelopers(developers = []) {
  const newDeveloper = {
    _id: 'd4',
    name: "Ananya Das",
    role: "Frontend Engineer",
    skills: ["HTML5", "CSS3", "React"],
    status: "active",
    rating: 4.8
  };

  // Simulate db.developers.insertOne(newDeveloper)
  const collection = [...developers, newDeveloper];

  // Simulate db.developers.find({ status: "active", skills: "React" }, { name: 1, role: 1, skills: 1, rating: 1, _id: 0 })
  const results = collection
    .filter(doc => doc.status === 'active' && Array.isArray(doc.skills) && doc.skills.includes('React'))
    .map(doc => ({
      name: doc.name,
      role: doc.role,
      skills: doc.skills,
      rating: doc.rating
    }));

  return results;
}

const sampleDevs = [
  { _id: 'd1', name: 'Rohan Sharma', role: 'Full-Stack Developer', skills: ['Python', 'Django', 'React'], status: 'active', rating: 4.9 },
  { _id: 'd2', name: 'Kavita Rao', role: 'Backend Developer', skills: ['Java', 'Spring', 'SQL'], status: 'inactive', rating: 4.2 },
  { _id: 'd3', name: 'Manish Kumar', role: 'UI Engineer', skills: ['HTML5', 'CSS3', 'Vue'], status: 'active', rating: 4.4 }
];

console.log(insertAndQueryDevelopers(sampleDevs));`,
      solutionExplanation: `1. Clones the array to insert the new developer document without mutating input data.
2. In MongoDB, querying an array field like { skills: "React" } automatically checks if the element exists in the array.
3. The projection filters out internal identifiers like _id, delivering clean JSON for frontend display.`
    },
    {
      id: 'mongo-ex-2',
      title: 'Practice 2: Course Catalog Filter, Projection & Sorting Query',
      difficulty: 'Easy',
      type: 'mongodb',
      problemStatement: 'Write a query function findHighRatedCourses(courses, minRating, maxPrice) that implements MongoDB query operators ($gte, $lte) with custom sorting and field projection.',
      requirements: [
        'Filter for courses matching: isPublished === true, rating >= minRating, and price <= maxPrice',
        'Sort matching courses by rating in descending order (highest first); if ratings are equal, sort by price in ascending order',
        'Project fields: { courseId: doc._id, title: doc.title, rating: doc.rating, price: doc.price }',
        'Return the sorted, projected results array'
      ],
      sampleData: [
        { _id: 'c101', title: 'Modern Frontend Development', category: 'Web', price: 49.99, rating: 4.9, isPublished: true },
        { _id: 'c102', title: 'Advanced Algorithms in Python', category: 'CS', price: 79.99, rating: 4.9, isPublished: true },
        { _id: 'c103', title: 'Legacy jQuery Guide', category: 'Web', price: 19.99, rating: 3.8, isPublished: false },
        { _id: 'c104', title: 'Docker & Kubernetes Basics', category: 'DevOps', price: 59.99, rating: 4.7, isPublished: true }
      ],
      starterCode: `function findHighRatedCourses(courses, minRating = 4.5, maxPrice = 80) {
  // Implement filter, sort, and projection
  
}`,
      expectedBehavior: 'Returns published courses within price budget sorted by rating descending and price ascending.',
      hints: [
        'Use .filter(c => c.isPublished && c.rating >= minRating && c.price <= maxPrice).',
        'In sort(): b.rating - a.rating || a.price - b.price provides secondary sort order!',
        'Map the output to the specified projected shape.'
      ],
      solution: `function findHighRatedCourses(courses = [], minRating = 4.5, maxPrice = 80) {
  // Simulates:
  // db.courses.find(
  //   { isPublished: true, rating: { $gte: minRating }, price: { $lte: maxPrice } },
  //   { title: 1, rating: 1, price: 1 }
  // ).sort({ rating: -1, price: 1 })

  return courses
    .filter(doc => doc.isPublished === true && doc.rating >= minRating && doc.price <= maxPrice)
    .sort((a, b) => (b.rating - a.rating) || (a.price - b.price))
    .map(doc => ({
      courseId: doc._id,
      title: doc.title,
      rating: doc.rating,
      price: doc.price
    }));
}

const sampleCatalog = [
  { _id: 'c101', title: 'Modern Frontend Development', category: 'Web', price: 49.99, rating: 4.9, isPublished: true },
  { _id: 'c102', title: 'Advanced Algorithms in Python', category: 'CS', price: 79.99, rating: 4.9, isPublished: true },
  { _id: 'c103', title: 'Legacy jQuery Guide', category: 'Web', price: 19.99, rating: 3.8, isPublished: false },
  { _id: 'c104', title: 'Docker & Kubernetes Basics', category: 'DevOps', price: 59.99, rating: 4.7, isPublished: true }
];

console.log(findHighRatedCourses(sampleCatalog, 4.7, 80));`,
      solutionExplanation: `1. Implements compound criteria { rating: { $gte: 4.7 }, price: { $lte: 80 } }.
2. (b.rating - a.rating) || (a.price - b.price) elegantly applies tie-breaking secondary sort order.
3. Formats documents with clean field projection matching API requirements.`
    },
    {
      id: 'mongo-ex-3',
      title: 'Practice 3: Inventory Update with $inc, $push, and $set',
      difficulty: 'Medium',
      type: 'mongodb',
      problemStatement: 'Write an updateProduct(products, productId, updateOps) function that simulates MongoDB atomic update operators: $inc (increments a number), $set (updates field values), and $push (appends an item to an array).',
      requirements: [
        'Find the target document by _id matching productId',
        'Apply $inc: for each field in updateOps.$inc, add the numeric value to existing value (e.g. stock: -1, salesCount: +1)',
        'Apply $set: for each field in updateOps.$set, overwrite the field value',
        'Apply $push: for each field in updateOps.$push, append the item into the array without replacing the array',
        'Update updatedAt timestamp to current ISO string',
        'Return the updated document; throw Error if document not found'
      ],
      sampleData: [
        {
          _id: 'prod-99',
          title: 'Mechanical Coding Keyboard',
          stock: 15,
          salesCount: 120,
          status: 'in-stock',
          reviews: [
            { user: 'Siddharth', rating: 5, comment: 'Great tactile switches!' }
          ]
        }
      ],
      starterCode: `function updateProduct(products, productId, updateOps) {
  // Simulate MongoDB updateOne with $inc, $set, and $push
  
}`,
      expectedBehavior: 'Document correctly has stock decremented, salesCount incremented, status updated, and a new review appended to reviews array.',
      hints: [
        'Find the product index: const idx = products.findIndex(p => p._id === productId);',
        'Handle $inc: doc[key] = (doc[key] || 0) + val;',
        'Handle $push: doc[key] = [...(doc[key] || []), item];'
      ],
      solution: `function updateProduct(products = [], productId, updateOps = {}) {
  const targetDoc = products.find(p => p._id === productId);
  if (!targetDoc) {
    throw new Error(\`Document with _id "\${productId}" not found\`);
  }

  // Clone document to avoid unexpected mutations
  const updatedDoc = JSON.parse(JSON.stringify(targetDoc));

  // 1. Handle $inc (atomic increment)
  if (updateOps.$inc) {
    for (const [field, incVal] of Object.entries(updateOps.$inc)) {
      updatedDoc[field] = (updatedDoc[field] || 0) + incVal;
    }
  }

  // 2. Handle $set (overwrite fields)
  if (updateOps.$set) {
    for (const [field, val] of Object.entries(updateOps.$set)) {
      updatedDoc[field] = val;
    }
  }

  // 3. Handle $push (append to array)
  if (updateOps.$push) {
    for (const [field, item] of Object.entries(updateOps.$push)) {
      if (!Array.isArray(updatedDoc[field])) {
        updatedDoc[field] = [];
      }
      updatedDoc[field].push(item);
    }
  }

  updatedDoc.updatedAt = new Date().toISOString();
  return updatedDoc;
}

const sampleInventory = [
  {
    _id: 'prod-99',
    title: 'Mechanical Coding Keyboard',
    stock: 15,
    salesCount: 120,
    status: 'in-stock',
    reviews: [{ user: 'Siddharth', rating: 5, comment: 'Great switches!' }]
  }
];

const updateOperation = {
  $inc: { stock: -1, salesCount: 1 },
  $set: { status: 'low-stock' },
  $push: { reviews: { user: 'Pooja', rating: 5, comment: 'Super fast delivery!' } }
};

const updatedResult = updateProduct(sampleInventory, 'prod-99', updateOperation);
console.log('Updated Document:', updatedResult);`,
      solutionExplanation: `1. Replicates MongoDB updateOne({ _id: productId }, { $inc: ..., $set: ..., $push: ... }) semantics.
2. $inc handles negative and positive increments (stock decremented from 15 to 14, salesCount incremented to 121).
3. $push safely appends the review object to the array without overwriting existing reviews.
4. Updates timestamps to keep track of modifications.`
    },
    {
      id: 'mongo-ex-4',
      title: 'Practice 4: Aggregation Pipeline ($match, $group, and $sort)',
      difficulty: 'Medium',
      type: 'mongodb',
      problemStatement: 'Implement an aggregateCategoryStats(challenges) function that simulates a MongoDB Aggregation Pipeline with $match, $group, and $sort stages to calculate statistics for verified coding challenges.',
      requirements: [
        'Stage 1 ($match): filter for challenges where isActive === true',
        'Stage 2 ($group): group by category. Compute: totalChallenges ($sum: 1), totalPoints ($sum: "$points"), and avgPoints ($avg: "$points")',
        'Round avgPoints to 1 decimal place using Number(avg.toFixed(1))',
        'Stage 3 ($sort): sort groups by totalPoints descending; if equal, sort alphabetically by category',
        'Return array of grouped objects: [ { category, totalChallenges, totalPoints, avgPoints }, ... ]'
      ],
      sampleData: [
        { _id: 1, title: 'Two Sum', category: 'Algorithms', points: 10, isActive: true },
        { _id: 2, title: 'QuickSort', category: 'Algorithms', points: 20, isActive: true },
        { _id: 3, title: 'Draft Problem', category: 'Algorithms', points: 15, isActive: false },
        { _id: 4, title: 'Flexbox Navbar', category: 'Frontend', points: 10, isActive: true },
        { _id: 5, title: 'Grid Gallery', category: 'Frontend', points: 15, isActive: true }
      ],
      starterCode: `function aggregateCategoryStats(challenges) {
  // Simulate MongoDB aggregation pipeline: $match -> $group -> $sort
  
}`,
      expectedBehavior: 'Returns grouped summary objects per active category sorted by total points descending.',
      hints: [
        'Filter first: const active = challenges.filter(c => c.isActive);',
        'Group with an object accumulator: groups[category] = groups[category] || { totalChallenges: 0, totalPoints: 0 }',
        'Map groups into an array and sort by totalPoints descending.'
      ],
      solution: `function aggregateCategoryStats(challenges = []) {
  // 1. $match stage: filter active challenges
  const matched = challenges.filter(ch => ch.isActive === true);

  // 2. $group stage: group by category
  const groupMap = {};
  for (const item of matched) {
    const cat = item.category || 'Uncategorized';
    if (!groupMap[cat]) {
      groupMap[cat] = {
        category: cat,
        totalChallenges: 0,
        totalPoints: 0,
        pointsList: []
      };
    }
    groupMap[cat].totalChallenges += 1;
    groupMap[cat].totalPoints += (item.points || 0);
    groupMap[cat].pointsList.push(item.points || 0);
  }

  // 3. Compute $avg and format
  const groupedArray = Object.values(groupMap).map(g => {
    const avg = g.totalPoints / g.totalChallenges;
    return {
      category: g.category,
      totalChallenges: g.totalChallenges,
      totalPoints: g.totalPoints,
      avgPoints: Number(avg.toFixed(1))
    };
  });

  // 4. $sort stage: sort by totalPoints desc, then category asc
  return groupedArray.sort((a, b) => 
    (b.totalPoints - a.totalPoints) || a.category.localeCompare(b.category)
  );
}

const challengeData = [
  { _id: 1, title: 'Two Sum', category: 'Algorithms', points: 10, isActive: true },
  { _id: 2, title: 'QuickSort', category: 'Algorithms', points: 20, isActive: true },
  { _id: 3, title: 'Draft Problem', category: 'Algorithms', points: 15, isActive: false },
  { _id: 4, title: 'Flexbox Navbar', category: 'Frontend', points: 10, isActive: true },
  { _id: 5, title: 'Grid Gallery', category: 'Frontend', points: 15, isActive: true }
];

console.log(aggregateCategoryStats(challengeData));`,
      solutionExplanation: `1. Stage 1 ($match) filters out inactive drafts prior to aggregation, optimizing downstream compute.
2. Stage 2 ($group) accumulates counts and sums using category as group key.
3. Computes average points and formats to 1 decimal place.
4. Stage 3 ($sort) orders categories by total points descending to highlight the highest-value tracks.`
    },
    {
      id: 'mongo-ex-5',
      title: 'Practice 5: Relational Lookup & Complex Multi-Condition Filter',
      difficulty: 'Hard',
      type: 'mongodb',
      problemStatement: 'Simulate a MongoDB $lookup join between an Orders collection and a Users collection. Join customer details into each order, filter for orders placed in 2026 with total >= 50, and project customer name and order items.',
      requirements: [
        'Simulate $lookup: from users collection where localField: "userId" matches foreignField: "_id", storing joined user in customer field',
        'Filter orders where order.status === "completed" AND order.total >= 50 AND order.orderDate starts with "2026"',
        'If joined customer is not found, default customer to { name: "Guest User", email: "N/A" }',
        'Project: { orderId: doc._id, customerName: customer.name, customerEmail: customer.email, total: doc.total, itemCount: doc.items.length, orderDate: doc.orderDate }',
        'Sort output by total descending'
      ],
      sampleData: [
        { _id: 'ord-1', userId: 'usr-1', total: 75.00, status: 'completed', orderDate: '2026-03-15', items: ['React Pro', 'CSS Guide'] },
        { _id: 'ord-2', userId: 'usr-2', total: 30.00, status: 'completed', orderDate: '2026-02-10', items: ['Python Basics'] },
        { _id: 'ord-3', userId: 'usr-1', total: 120.00, status: 'completed', orderDate: '2026-04-01', items: ['Fullstack Track', 'Certification'] },
        { _id: 'ord-4', userId: 'usr-3', total: 95.00, status: 'pending', orderDate: '2026-01-20', items: ['Algorithms'] }
      ],
      starterCode: `function lookupOrdersWithCustomers(orders, users) {
  // Simulate MongoDB $lookup, $match, and $project pipeline
  
}`,
      expectedBehavior: 'Returns orders with matched user details, filtered to completed 2026 orders with total >= 50, sorted by total descending.',
      hints: [
        'Build a user map for O(1) lookups: const userMap = new Map(users.map(u => [u._id, u]));',
        'For each order: const user = userMap.get(order.userId) || { name: "Guest User", email: "N/A" };',
        'Filter: order.status === "completed" && order.total >= 50 && order.orderDate.startsWith("2026").'
      ],
      solution: `function lookupOrdersWithCustomers(orders = [], users = []) {
  // Create quick lookup map for users
  const userMap = new Map();
  users.forEach(u => userMap.set(u._id, u));

  // 1. $lookup stage & 2. $match stage
  const matchedOrders = orders.filter(order => {
    const isCompleted = order.status === 'completed';
    const isSufficientAmount = (order.total || 0) >= 50;
    const isYear2026 = typeof order.orderDate === 'string' && order.orderDate.startsWith('2026');

    return isCompleted && isSufficientAmount && isYear2026;
  });

  // 3. $project stage with joined customer details
  const projected = matchedOrders.map(order => {
    const customer = userMap.get(order.userId) || { name: 'Guest User', email: 'N/A' };

    return {
      orderId: order._id,
      customerName: customer.name,
      customerEmail: customer.email,
      total: order.total,
      itemCount: Array.isArray(order.items) ? order.items.length : 0,
      orderDate: order.orderDate
    };
  });

  // 4. $sort by total descending
  return projected.sort((a, b) => b.total - a.total);
}

const sampleOrders = [
  { _id: 'ord-1', userId: 'usr-1', total: 75.00, status: 'completed', orderDate: '2026-03-15', items: ['React Pro', 'CSS Guide'] },
  { _id: 'ord-2', userId: 'usr-2', total: 30.00, status: 'completed', orderDate: '2026-02-10', items: ['Python Basics'] },
  { _id: 'ord-3', userId: 'usr-1', total: 120.00, status: 'completed', orderDate: '2026-04-01', items: ['Fullstack Track', 'Certification'] },
  { _id: 'ord-4', userId: 'usr-3', total: 95.00, status: 'pending', orderDate: '2026-01-20', items: ['Algorithms'] }
];

const sampleUsers = [
  { _id: 'usr-1', name: 'Tanvi Mehra', email: 'tanvi@example.com' },
  { _id: 'usr-2', name: 'Kabir Singh', email: 'kabir@example.com' }
];

console.log(lookupOrdersWithCustomers(sampleOrders, sampleUsers));`,
      solutionExplanation: `1. Replicates MongoDB $lookup stage by mapping the foreign key (userId) to the referenced collection (_id).
2. The $match stage filters out pending orders, low-value orders (< $50), and orders from previous years.
3. The $project stage shapes the document for client presentation without leaking unneeded user credentials.
4. Sorts output by total in descending order.`
    }
  ]
};
