# 20 Official Exam Categories and Certification Exams Data

CATEGORIES_DATA = [
    {
        "order": 1,
        "name": "Python Programming",
        "slug": "python-programming",
        "icon": "Terminal",
        "description": "Master core Python syntax, OOP, generators, data manipulation, file I/O, and idiomatic Python algorithms.",
        "exam": {
            "title": "Python Professional Developer Certification",
            "slug": "python-professional-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Comprehensive assessment covering Python 3 language fundamentals, list comprehensions, dictionary operations, lambda functions, and algorithm implementation.",
            "instructions": "This exam consists of hands-on Python coding problems and conceptual questions. Your coding solutions will be executed in a sandboxed runtime against public and hidden test cases. You may navigate between questions freely. The exam will automatically submit when the timer expires.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Even Squares Filter",
                    "points": 25,
                    "problem_statement": "Write a Python program that reads a space-separated list of integers from standard input, filters out the even numbers, squares each even number, and prints them separated by single spaces. If there are no even numbers, print empty output.",
                    "input_format": "A single line containing space-separated integers.",
                    "output_format": "Space-separated squared even integers.",
                    "constraints": "1 <= N <= 1000, -1000 <= each number <= 1000",
                    "starter_code": {
                        "python": "import sys\n\ndef main():\n    line = sys.stdin.read().strip()\n    if not line:\n        return\n    nums = [int(x) for x in line.split()]\n    # Your logic here\n    \nif __name__ == '__main__':\n    main()\n"
                    },
                    "test_cases": [
                        {"input": "1 2 3 4 5 6", "expected_output": "4 16 36", "is_hidden": False},
                        {"input": "7 9 11", "expected_output": "", "is_hidden": False},
                        {"input": "2 4 8 10", "expected_output": "4 16 64 100", "is_hidden": True},
                        {"input": "-2 -4 5 6", "expected_output": "4 16 36", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "coding",
                    "title": "Count Character Frequencies",
                    "points": 25,
                    "problem_statement": "Given a lowercase string, count the frequency of each alphabetic character and print each character and its count formatted as `char:count` sorted in alphabetical order, separated by a comma and space (e.g., `a:2, b:1`). Ignore whitespace.",
                    "input_format": "A single string from stdin.",
                    "output_format": "Alphabetically sorted string of char:count pairs.",
                    "constraints": "Length of string <= 1000.",
                    "starter_code": {
                        "python": "import sys\n\ndef main():\n    text = sys.stdin.read().strip().replace(' ', '')\n    if not text:\n        return\n    # Count frequencies and print\n\nif __name__ == '__main__':\n    main()\n"
                    },
                    "test_cases": [
                        {"input": "banana", "expected_output": "a:3, b:1, n:2", "is_hidden": False},
                        {"input": "coding", "expected_output": "c:1, d:1, g:1, i:1, n:1, o:1", "is_hidden": False},
                        {"input": "mississippi", "expected_output": "i:4, m:1, p:2, s:4", "is_hidden": True}
                    ]
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Python List vs Tuple Immutability",
                    "points": 15,
                    "problem_statement": "What is the primary difference between a Python `list` and a Python `tuple`?",
                    "options": [
                        {"id": "A", "text": "Tuples can only contain integers, while lists can store any object."},
                        {"id": "B", "text": "Lists are mutable and can be modified after creation; tuples are immutable."},
                        {"id": "C", "text": "Lists use parentheses `()` while tuples use square brackets `[]`."},
                        {"id": "D", "text": "Tuples cannot be indexed or sliced, but lists can."}
                    ],
                    "correct_answer": "B",
                    "explanation": "In Python, lists are mutable (items can be added, removed, or changed in-place), whereas tuples are immutable once instantiated."
                },
                {
                    "order": 4,
                    "question_type": "single_choice",
                    "title": "Python GIL and Multithreading",
                    "points": 15,
                    "problem_statement": "What is the primary purpose and effect of the Global Interpreter Lock (GIL) in CPython?",
                    "options": [
                        {"id": "A", "text": "It speeds up CPU-bound tasks across multiple OS threads by eliminating thread context switches."},
                        {"id": "B", "text": "It ensures that only one native OS thread executes Python bytecode at any given time to protect CPython memory management."},
                        {"id": "C", "text": "It disables network socket concurrency completely in Python applications."},
                        {"id": "D", "text": "It automatically converts recursive functions into iterative loops."}
                    ],
                    "correct_answer": "B",
                    "explanation": "The GIL is a mutex that prevents multiple native threads from executing CPython bytecodes at once, ensuring thread-safe reference counting in CPython's memory management."
                },
                {
                    "order": 5,
                    "question_type": "multiple_choice",
                    "title": "Python Decorators & First-Class Functions",
                    "points": 20,
                    "problem_statement": "Which of the following statements about Python functions and decorators are true? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Functions in Python are first-class citizens and can be passed as arguments to other functions."},
                        {"id": "B", "text": "A decorator `@my_decorator` placed above `def foo():` is syntactic sugar for `foo = my_decorator(foo)`."},
                        {"id": "C", "text": "Decorators cannot accept their own custom arguments."},
                        {"id": "D", "text": "Using `functools.wraps` helps preserve the original function's name and docstring inside a wrapper function."}
                    ],
                    "correct_answer": ["A", "B", "D"],
                    "explanation": "Python functions are first-class objects. `@decorator` is syntactic sugar for `func = decorator(func)`. Decorators can take parameters by returning a decorator factory, and `functools.wraps` copies metadata like `__name__` and `__doc__`."
                }
            ]
        }
    },
    {
        "order": 2,
        "name": "C Programming",
        "slug": "c-programming",
        "icon": "Cpu",
        "description": "Low-level system architecture, manual memory management (malloc/free), pointers, structures, and standard I/O.",
        "exam": {
            "title": "C Systems Programming Certification",
            "slug": "c-systems-programming-certification",
            "difficulty": "Hard",
            "duration_minutes": 50,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Rigorous evaluation of C language proficiency, pointer arithmetic, dynamic memory allocation, string operations, and system-level debugging.",
            "instructions": "All code is compiled with GCC standard c99/c11. Write clean, memory-safe code. Handle standard input and output correctly.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "String Reversal in C",
                    "points": 30,
                    "problem_statement": "Write a complete C program that reads a string of up to 256 characters from standard input and prints the string reversed. Do not print extraneous spaces or newlines beyond the reversed string.",
                    "input_format": "A single word or string from stdin.",
                    "output_format": "The reversed string printed to stdout.",
                    "constraints": "String length <= 256 characters.",
                    "starter_code": {
                        "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    char str[300];\n    if (scanf(\"%299s\", str) != 1) return 0;\n    int len = strlen(str);\n    for (int i = len - 1; i >= 0; i--) {\n        putchar(str[i]);\n    }\n    printf(\"\\n\");\n    return 0;\n}\n"
                    },
                    "test_cases": [
                        {"input": "hello", "expected_output": "olleh", "is_hidden": False},
                        {"input": "world", "expected_output": "dlrow", "is_hidden": False},
                        {"input": "programming", "expected_output": "gnimmargorp", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Pointer Dereference and Null Pointers",
                    "points": 20,
                    "problem_statement": "What occurs in standard C when attempting to dereference a `NULL` pointer (e.g. `int *ptr = NULL; *ptr = 10;`)?",
                    "options": [
                        {"id": "A", "text": "The pointer automatically allocates 4 bytes on the heap."},
                        {"id": "B", "text": "It invokes Undefined Behavior (UB), commonly resulting in a Segmentation Fault."},
                        {"id": "C", "text": "The program safely skips the assignment without error."},
                        {"id": "D", "text": "The compiler replaces the pointer with the address of the main function."}
                    ],
                    "correct_answer": "B",
                    "explanation": "Dereferencing a null pointer is undefined behavior according to the C standard, which typically triggers a hardware memory protection fault (SIGSEGV)."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Dynamic Memory Allocation",
                    "points": 25,
                    "problem_statement": "Which function allocates memory on the heap and initializes all allocated bytes to zero?",
                    "options": [
                        {"id": "A", "text": "malloc()"},
                        {"id": "B", "text": "calloc()"},
                        {"id": "C", "text": "realloc()"},
                        {"id": "D", "text": "alloca()"}
                    ],
                    "correct_answer": "B",
                    "explanation": "calloc(num, size) allocates memory and clears all bits to zero, whereas malloc leaves memory uninitialized."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "C Storage Classes & Scope",
                    "points": 25,
                    "problem_statement": "Which of the following statements about C keywords and variables are correct? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "A variable declared with `static` inside a function retains its value between function calls."},
                        {"id": "B", "text": "The `const` qualifier guarantees that a variable is stored in read-only registers."},
                        {"id": "C", "text": "Applying `static` to a global variable or function restricts its linkage to that translation unit (.c file)."},
                        {"id": "D", "text": "The `sizeof` operator evaluates its operand's type at compile time in standard cases."}
                    ],
                    "correct_answer": ["A", "C", "D"],
                    "explanation": "Static local variables persist across calls. Static global variables have internal linkage. Sizeof is evaluated at compile time (except for variable-length arrays). `const` specifies immutability, not register placement."
                }
            ]
        }
    },
    {
        "order": 3,
        "name": "C++ Programming",
        "slug": "cpp-programming",
        "icon": "Code2",
        "description": "Modern C++ (C++17/20), Standard Template Library (STL), templates, smart pointers, RAII, and object-oriented architecture.",
        "exam": {
            "title": "C++ Advanced Concepts & OOP Certification",
            "slug": "cpp-advanced-certification",
            "difficulty": "Hard",
            "duration_minutes": 50,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Thorough assessment of C++ STL containers (vector, unordered_map), move semantics, RAII, templates, polymorphism, and memory management.",
            "instructions": "Solutions are compiled using G++ with modern C++ standards. Ensure code does not leak resources and adheres to standard I/O conventions.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Vector Duplicate Remover",
                    "points": 30,
                    "problem_statement": "Write a C++ program that reads an integer N followed by N integers from standard input, removes consecutive duplicates, and prints the unique sequence separated by spaces.",
                    "input_format": "First line: integer N. Second line: N space-separated integers.",
                    "output_format": "Space-separated sequence without consecutive duplicates.",
                    "constraints": "1 <= N <= 1000",
                    "starter_code": {
                        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    int n;\n    if (!(cin >> n)) return 0;\n    vector<int> v(n);\n    for (int i = 0; i < n; i++) cin >> v[i];\n    \n    // Remove consecutive duplicates and print\n    auto it = unique(v.begin(), v.end());\n    v.erase(it, v.end());\n    for (size_t i = 0; i < v.size(); i++) {\n        cout << v[i] << (i + 1 == v.size() ? \"\" : \" \");\n    }\n    cout << endl;\n    return 0;\n}\n"
                    },
                    "test_cases": [
                        {"input": "6\n1 1 2 2 3 1", "expected_output": "1 2 3 1", "is_hidden": False},
                        {"input": "5\n4 4 4 4 4", "expected_output": "4", "is_hidden": False},
                        {"input": "4\n1 2 3 4", "expected_output": "1 2 3 4", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "RAII and Smart Pointers",
                    "points": 25,
                    "problem_statement": "Which C++ smart pointer represents exclusive ownership of a dynamically allocated resource and cannot be copied, only moved?",
                    "options": [
                        {"id": "A", "text": "std::shared_ptr"},
                        {"id": "B", "text": "std::unique_ptr"},
                        {"id": "C", "text": "std::weak_ptr"},
                        {"id": "D", "text": "std::auto_ptr"}
                    ],
                    "correct_answer": "B",
                    "explanation": "`std::unique_ptr` enforces unique exclusive ownership with zero overhead over raw pointers. It prohibits copy construction and copy assignment, requiring `std::move`."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Virtual Destructors in C++",
                    "points": 20,
                    "problem_statement": "Why should a base class with virtual functions declare a virtual destructor?",
                    "options": [
                        {"id": "A", "text": "To speed up compilation time."},
                        {"id": "B", "text": "To allow the derived class destructor to be called when deleting an object through a base class pointer."},
                        {"id": "C", "text": "To make the class abstract so it cannot be instantiated."},
                        {"id": "D", "text": "To prevent other classes from inheriting from it."}
                    ],
                    "correct_answer": "B",
                    "explanation": "Deleting a derived class object through a pointer to base without a virtual destructor causes undefined behavior and resource leaks, as only the base destructor would be invoked."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "C++ STL Container Characteristics",
                    "points": 25,
                    "problem_statement": "Which of the following statements about C++ STL containers are accurate? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "`std::vector` provides contiguous memory storage and O(1) amortized push_back."},
                        {"id": "B", "text": "`std::map` is typically implemented as a self-balancing binary search tree (Red-Black Tree) with O(log N) lookup."},
                        {"id": "C", "text": "`std::unordered_map` has average O(1) lookup using hash tables."},
                        {"id": "D", "text": "`std::vector` iterator invalidation never happens when elements are pushed."}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "std::vector is contiguous with O(1) amortized push_back; std::map is an ordered red-black tree with O(log N); std::unordered_map has average O(1) hash lookup. Vector iterators can be invalidated upon reallocation."
                }
            ]
        }
    },
    {
        "order": 4,
        "name": "Java Programming",
        "slug": "java-programming",
        "icon": "Coffee",
        "description": "Java Collections Framework, Streams API, Concurrency, JVM memory model, and object-oriented principles.",
        "exam": {
            "title": "Java Enterprise Developer Certification",
            "slug": "java-enterprise-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Validate your enterprise Java skills including Collections, Streams, exception handling, polymorphism, and Java memory management.",
            "instructions": "All code is executed using OpenJDK. Ensure the class name is Solution or Main as indicated in the template.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Find Max Element in Java",
                    "points": 30,
                    "problem_statement": "Write a Java program that reads an integer N followed by N integers from standard input and prints the maximum value found. If N <= 0, print 0.",
                    "input_format": "N followed by N space-separated integers.",
                    "output_format": "The single maximum integer.",
                    "constraints": "1 <= N <= 1000",
                    "starter_code": {
                        "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int n = sc.nextInt();\n        int maxVal = Integer.MIN_VALUE;\n        for (int i = 0; i < n; i++) {\n            int val = sc.nextInt();\n            if (val > maxVal) maxVal = val;\n        }\n        System.out.println(maxVal);\n    }\n}\n"
                    },
                    "test_cases": [
                        {"input": "5\n3 8 2 10 5", "expected_output": "10", "is_hidden": False},
                        {"input": "3\n-5 -2 -9", "expected_output": "-2", "is_hidden": False},
                        {"input": "1\n42", "expected_output": "42", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Java String Pool and Equals",
                    "points": 20,
                    "problem_statement": "Given `String s1 = new String(\"hello\"); String s2 = new String(\"hello\");`, what are the results of `s1 == s2` and `s1.equals(s2)`?",
                    "options": [
                        {"id": "A", "text": "`s1 == s2` is true; `s1.equals(s2)` is true."},
                        {"id": "B", "text": "`s1 == s2` is false; `s1.equals(s2)` is true."},
                        {"id": "C", "text": "`s1 == s2` is true; `s1.equals(s2)` is false."},
                        {"id": "D", "text": "`s1 == s2` is false; `s1.equals(s2)` is false."}
                    ],
                    "correct_answer": "B",
                    "explanation": "`==` checks reference equality (heap memory addresses), which are distinct because both were created with `new`. `.equals()` compares character sequence values, which are equal."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Java Garbage Collection",
                    "points": 25,
                    "problem_statement": "In the HotSpot JVM, where are newly instantiated objects first allocated?",
                    "options": [
                        {"id": "A", "text": "Metaspace"},
                        {"id": "B", "text": "Eden space in the Young Generation"},
                        {"id": "C", "text": "Tenured (Old) Generation"},
                        {"id": "D", "text": "Thread Call Stack"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Newly created objects in Java are initially allocated in the Eden space of the Young Generation. Objects that survive multiple minor GC cycles are promoted to the Old/Tenured generation."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Java Interfaces vs Abstract Classes",
                    "points": 25,
                    "problem_statement": "Since Java 8 and beyond, which of the following are valid capabilities of a Java `interface`? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "An interface can provide default method implementations using the `default` keyword."},
                        {"id": "B", "text": "An interface can have instance fields with mutable state like normal classes."},
                        {"id": "C", "text": "An interface can define static helper methods."},
                        {"id": "D", "text": "A class can implement multiple interfaces simultaneously."}
                    ],
                    "correct_answer": ["A", "C", "D"],
                    "explanation": "Java 8 introduced default and static methods in interfaces. Multiple interface implementation is supported. Interfaces cannot hold mutable instance state (all fields are implicitly public static final)."
                }
            ]
        }
    },
    {
        "order": 5,
        "name": "JavaScript Programming",
        "slug": "javascript-programming",
        "icon": "Braces",
        "description": "Modern ECMAScript (ES6+), Event Loop, Promises, Async/Await, Closures, Prototypes, and Functional Programming.",
        "exam": {
            "title": "JavaScript Core & Modern ES6+ Certification",
            "slug": "javascript-core-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Prove your expertise in asynchronous JavaScript, the event loop, closures, scope chains, modern array methods, and object destructuring.",
            "instructions": "All coding challenges run in Node.js. Use modern ES6+ syntax and standard input/output formatting.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Chunk an Array in JavaScript",
                    "points": 30,
                    "problem_statement": "Write a JavaScript program that reads a chunk size K on the first line and a space-separated list of integers on the second line. Split the list into chunks of length K and print each chunk on a new line formatted as space-separated numbers.",
                    "input_format": "Line 1: integer K. Line 2: space-separated integers.",
                    "output_format": "Each chunk on its own line.",
                    "constraints": "1 <= K <= 100, list length <= 500",
                    "starter_code": {
                        "javascript": "const fs = require('fs');\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\n    if (input.length < 2) return;\n    const k = parseInt(input[0].trim(), 10);\n    const arr = input[1].trim().split(/\\s+/);\n    \n    for (let i = 0; i < arr.length; i += k) {\n        console.log(arr.slice(i, i + k).join(' '));\n    }\n}\n\nmain();\n"
                    },
                    "test_cases": [
                        {"input": "2\n1 2 3 4 5", "expected_output": "1 2\n3 4\n5", "is_hidden": False},
                        {"input": "3\n10 20 30 40 50 60", "expected_output": "10 20 30\n40 50 60", "is_hidden": False},
                        {"input": "1\n7 8 9", "expected_output": "7\n8\n9", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Event Loop Microtask vs Macrotask",
                    "points": 25,
                    "problem_statement": "In what order are the numbers logged by the following code?\n```js\nconsole.log(1);\nsetTimeout(() => console.log(2), 0);\nPromise.resolve().then(() => console.log(3));\nconsole.log(4);\n```",
                    "options": [
                        {"id": "A", "text": "1, 2, 3, 4"},
                        {"id": "B", "text": "1, 4, 3, 2"},
                        {"id": "C", "text": "1, 4, 2, 3"},
                        {"id": "D", "text": "3, 1, 4, 2"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Synchronous code executes first (1, 4). Microtasks (`Promise.then`) execute next before macrotasks (3). Macrotasks (`setTimeout`) execute in the next tick of the event loop (2). Result: 1, 4, 3, 2."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "JavaScript Closures",
                    "points": 20,
                    "problem_statement": "What is a closure in JavaScript?",
                    "options": [
                        {"id": "A", "text": "A function that immediately terminates the program after execution."},
                        {"id": "B", "text": "The combination of a function bundled together with references to its surrounding lexical environment."},
                        {"id": "C", "text": "An object that prevents properties from being modified using Object.freeze."},
                        {"id": "D", "text": "A syntax error that occurs when curly braces are left unclosed."}
                    ],
                    "correct_answer": "B",
                    "explanation": "A closure gives an inner function access to an outer enclosing function's scope even after the outer function has returned."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "var vs let vs const",
                    "points": 25,
                    "problem_statement": "Which of the following statements about JavaScript variable declarations are correct? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "`var` is function-scoped and hoisted with an initial value of `undefined`."},
                        {"id": "B", "text": "`let` and `const` are block-scoped and reside in the Temporal Dead Zone (TDZ) prior to declaration."},
                        {"id": "C", "text": "`const` prevents mutation of the internal properties of an assigned object or array."},
                        {"id": "D", "text": "`const` prevents reassignment of the variable identifier itself."}
                    ],
                    "correct_answer": ["A", "B", "D"],
                    "explanation": "var has function scope and hoists to undefined. let/const are block scoped with TDZ. const prevents reassigning the reference variable, but objects and arrays assigned to const can still have their internal properties mutated."
                }
            ]
        }
    },
    {
        "order": 6,
        "name": "React.js Development",
        "slug": "react-development",
        "icon": "Atom",
        "description": "Component architecture, hooks (useState, useEffect, useMemo, useCallback), Virtual DOM, state management, and modern React patterns.",
        "exam": {
            "title": "React.js Frontend Engineer Certification",
            "slug": "react-frontend-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Demonstrate mastery of modern React hooks, reconciliation algorithm, custom hooks, performance tuning, and declarative UI development.",
            "instructions": "Answer conceptual, architectural, and code analysis questions covering modern functional components and hooks.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "React Reconciliation and the Key Prop",
                    "points": 25,
                    "problem_statement": "Why does React require a unique `key` prop when rendering a dynamic list of elements?",
                    "options": [
                        {"id": "A", "text": "To enable CSS selector styling based on element index."},
                        {"id": "B", "text": "To identify which items have changed, been added, or been removed, optimizing the Virtual DOM diffing algorithm."},
                        {"id": "C", "text": "To bind each item to an automated Redux action dispatcher."},
                        {"id": "D", "text": "To prevent browser memory leaks during garbage collection."}
                    ],
                    "correct_answer": "B",
                    "explanation": "Keys help React distinguish elements across re-renders, enabling it to match virtual DOM subtrees efficiently without recreating DOM nodes unnecessarily."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "useEffect Dependency Array",
                    "points": 25,
                    "problem_statement": "What happens if a `useEffect` hook is declared with an empty dependency array `[]`?",
                    "options": [
                        {"id": "A", "text": "The effect runs on every single re-render of the component."},
                        {"id": "B", "text": "The effect runs only once after the initial render (mount) and cleans up on unmount."},
                        {"id": "C", "text": "The effect never runs at all."},
                        {"id": "D", "text": "The component throws an Uncaught ReferenceError."}
                    ],
                    "correct_answer": "B",
                    "explanation": "An empty dependency array indicates to React that the effect does not depend on any props or state, so it executes once after mounting and cleans up when unmounted."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "useMemo vs useCallback",
                    "points": 25,
                    "problem_statement": "What is the key difference between `useMemo` and `useCallback` in React?",
                    "options": [
                        {"id": "A", "text": "`useMemo` caches the calculated return value of a function, while `useCallback` caches the function instance itself."},
                        {"id": "B", "text": "`useCallback` only works with class components, whereas `useMemo` is for functional components."},
                        {"id": "C", "text": "`useMemo` runs asynchronously on a web worker, while `useCallback` runs on the main UI thread."},
                        {"id": "D", "text": "There is no difference; they are exact aliases."}
                    ],
                    "correct_answer": "A",
                    "explanation": "`useMemo(() => compute(), [deps])` memoizes the computed result, while `useCallback(fn, [deps])` memoizes the callback function reference between renders."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Rules of React Hooks",
                    "points": 25,
                    "problem_statement": "Which of the following follow the official Rules of React Hooks? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Only call hooks at the top level of React function components or custom hooks."},
                        {"id": "B", "text": "Never call hooks inside loops, conditions, or nested functions."},
                        {"id": "C", "text": "Hooks can be called inside standard helper utility functions that do not start with `use`."},
                        {"id": "D", "text": "Hooks ensure state stays tied to the same component instance across consecutive renders based on call order."}
                    ],
                    "correct_answer": ["A", "B", "D"],
                    "explanation": "React relies on consistent hook call order on every render. Hooks must only be called at the top level of React functions or custom hooks starting with 'use'."
                }
            ]
        }
    },
    {
        "order": 7,
        "name": "Full-Stack Development",
        "slug": "full-stack-development",
        "icon": "Layers",
        "description": "End-to-end web architecture, client-server lifecycle, REST APIs, database queries, and deployment pipeline.",
        "exam": {
            "title": "Full-Stack Web Development Certification",
            "slug": "full-stack-web-certification",
            "difficulty": "Hard",
            "duration_minutes": 50,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Assess complete full-stack software development skills: frontend rendering, backend routing, database transactions, CORS, and authentication token workflows.",
            "instructions": "Covers both frontend and backend concepts along with full-stack coding challenges.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "URL Query Parameter Parser",
                    "points": 30,
                    "problem_statement": "Write a program in Python or JavaScript that reads a full URL from standard input, parses the query parameters, and prints each parameter as `key=value` sorted alphabetically by key on separate lines.",
                    "input_format": "A single URL string.",
                    "output_format": "Alphabetically sorted key=value lines.",
                    "constraints": "URL length <= 500 characters.",
                    "starter_code": {
                        "python": "import sys\nfrom urllib.parse import urlparse, parse_qs\n\ndef main():\n    url = sys.stdin.read().strip()\n    if not url:\n        return\n    query = urlparse(url).query\n    params = parse_qs(query)\n    for k in sorted(params.keys()):\n        print(f\"{k}={params[k][0]}\")\n\nif __name__ == '__main__':\n    main()\n"
                    },
                    "test_cases": [
                        {"input": "https://api.example.com/search?q=fullstack&page=2&sort=desc", "expected_output": "page=2\nq=fullstack\nsort=desc", "is_hidden": False},
                        {"input": "https://test.io/?b=2&a=1", "expected_output": "a=1\nb=2", "is_hidden": False},
                        {"input": "https://app.dev/users?status=active&role=admin&city=ny", "expected_output": "city=ny\nrole=admin\nstatus=active", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "CORS Preflight Requests",
                    "points": 25,
                    "problem_statement": "What HTTP method is sent by a browser as a CORS preflight request to verify cross-origin permissions?",
                    "options": [
                        {"id": "A", "text": "GET"},
                        {"id": "B", "text": "HEAD"},
                        {"id": "C", "text": "OPTIONS"},
                        {"id": "D", "text": "TRACE"}
                    ],
                    "correct_answer": "C",
                    "explanation": "Before sending non-simple cross-origin requests (such as requests with custom Authorization headers or PUT/DELETE methods), browsers send an HTTP OPTIONS preflight request to check server permissions."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "JWT Token Authentication Structure",
                    "points": 20,
                    "problem_statement": "What are the three dot-separated components of a JSON Web Token (JWT)?",
                    "options": [
                        {"id": "A", "text": "Protocol, Domain, and Query"},
                        {"id": "B", "text": "Header, Payload, and Signature"},
                        {"id": "C", "text": "Issuer, Subject, and Audience"},
                        {"id": "D", "text": "Public Key, Private Key, and Salt"}
                    ],
                    "correct_answer": "B",
                    "explanation": "A JWT consists of three Base64URL encoded parts separated by dots: Header (algorithm & token type), Payload (claims and data), and Signature (verifies integrity)."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Full-Stack Security Practices",
                    "points": 25,
                    "problem_statement": "Which of the following are essential security best practices for full-stack web applications? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Sanitizing user inputs and escaping outputs to prevent Cross-Site Scripting (XSS)."},
                        {"id": "B", "text": "Storing database credentials directly in public frontend client bundles."},
                        {"id": "C", "text": "Using parameterized queries or ORM abstractions to prevent SQL injection."},
                        {"id": "D", "text": "Storing passwords hashed with slow, salted cryptographic functions like bcrypt or Argon2."}
                    ],
                    "correct_answer": ["A", "C", "D"],
                    "explanation": "Input sanitization prevents XSS, parameterized queries prevent SQL injection, and bcrypt/Argon2 securely hash passwords. Storing credentials in frontend code is a major security vulnerability."
                }
            ]
        }
    },
    {
        "order": 8,
        "name": "Frontend Development",
        "slug": "frontend-development",
        "icon": "Layout",
        "description": "DOM manipulation, responsive design, CSS Flexbox/Grid, web performance optimization, and accessibility (a11y).",
        "exam": {
            "title": "Frontend Architecture & UI Engineering Certification",
            "slug": "frontend-architecture-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Evaluate knowledge of browser rendering pipelines, CSS box model, responsive layouts, web accessibility, and client-side performance.",
            "instructions": "Demonstrate understanding of modern frontend standards, responsive design, and CSS layout algorithms.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "CSS Box Model: box-sizing",
                    "points": 25,
                    "problem_statement": "When `box-sizing: border-box;` is applied to an element with `width: 200px; padding: 20px; border: 5px solid black;`, what is the element's total rendered width?",
                    "options": [
                        {"id": "A", "text": "250px"},
                        {"id": "B", "text": "225px"},
                        {"id": "C", "text": "200px"},
                        {"id": "D", "text": "150px"}
                    ],
                    "correct_answer": "C",
                    "explanation": "Under `border-box`, padding and borders are absorbed inside the declared width, so the element's total width remains exactly 200px."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Browser Critical Rendering Path",
                    "points": 25,
                    "problem_statement": "In what order does a web browser construct page rendering structures from downloaded HTML and CSS?",
                    "options": [
                        {"id": "A", "text": "Render Tree -> DOM -> CSSOM -> Layout -> Paint"},
                        {"id": "B", "text": "DOM & CSSOM -> Render Tree -> Layout (Reflow) -> Paint"},
                        {"id": "C", "text": "Paint -> Layout -> DOM -> CSSOM"},
                        {"id": "D", "text": "Layout -> Render Tree -> DOM -> Paint"}
                    ],
                    "correct_answer": "B",
                    "explanation": "The browser parses HTML to build DOM and CSS to build CSSOM. These merge into the Render Tree, followed by Layout (calculating geometry) and Paint (rasterizing pixels)."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Web Accessibility (WCAG)",
                    "points": 25,
                    "problem_statement": "Which HTML attribute provides screen readers with accessible descriptive text for interactive UI elements that do not contain visible text?",
                    "options": [
                        {"id": "A", "text": "aria-label"},
                        {"id": "B", "text": "alt-text"},
                        {"id": "C", "text": "tabindex"},
                        {"id": "D", "text": "data-screenreader"}
                    ],
                    "correct_answer": "A",
                    "explanation": "`aria-label` provides an explicit string label for assistive technologies on elements without visible text."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "CSS Flexbox vs CSS Grid",
                    "points": 25,
                    "problem_statement": "Which of the following statements comparing CSS Flexbox and CSS Grid are correct? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Flexbox is primarily designed for one-dimensional layouts (row or column)."},
                        {"id": "B", "text": "CSS Grid is designed for two-dimensional layouts (rows and columns simultaneously)."},
                        {"id": "C", "text": "Flexbox cannot be nested inside CSS Grid containers."},
                        {"id": "D", "text": "CSS Grid supports `grid-template-areas` for expressive ASCII-style layout definition."}
                    ],
                    "correct_answer": ["A", "B", "D"],
                    "explanation": "Flexbox is 1D, Grid is 2D, and Grid supports `grid-template-areas`. Flexbox elements can easily be nested inside Grid items."
                }
            ]
        }
    },
    {
        "order": 9,
        "name": "Backend Development",
        "slug": "backend-development",
        "icon": "Server",
        "description": "Server architecture, API design, caching (Redis), message queues, database indexing, and microservices.",
        "exam": {
            "title": "Backend Architecture & RESTful API Certification",
            "slug": "backend-architecture-certification",
            "difficulty": "Hard",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Assess server-side design patterns, HTTP status codes, idempotency, caching tiers, connection pooling, and scalability principles.",
            "instructions": "Demonstrate knowledge of scalable server design and backend communication protocols.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "HTTP Idempotency",
                    "points": 25,
                    "problem_statement": "Which of the following HTTP methods is NOT idempotent according to RFC 7231?",
                    "options": [
                        {"id": "A", "text": "GET"},
                        {"id": "B", "text": "PUT"},
                        {"id": "C", "text": "DELETE"},
                        {"id": "D", "text": "POST"}
                    ],
                    "correct_answer": "D",
                    "explanation": "An idempotent method can be called multiple times with the exact same side effects. POST typically creates new records on each invocation, making it non-idempotent."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Cache Eviction Policies",
                    "points": 25,
                    "problem_statement": "In a high-throughput Redis caching layer, what does the LRU eviction policy do when maximum memory is exceeded?",
                    "options": [
                        {"id": "A", "text": "Evicts keys with the shortest expiration time first."},
                        {"id": "B", "text": "Evicts keys that have not been accessed for the longest duration (Least Recently Used)."},
                        {"id": "C", "text": "Evicts the keys with the largest data payload in bytes."},
                        {"id": "D", "text": "Randomly deletes keys regardless of access frequency."}
                    ],
                    "correct_answer": "B",
                    "explanation": "LRU (Least Recently Used) removes keys that have been idle the longest when memory reaches the configured threshold."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "HTTP 401 vs 403 Status Codes",
                    "points": 25,
                    "problem_statement": "What is the semantic distinction between HTTP status code 401 Unauthorized and 403 Forbidden?",
                    "options": [
                        {"id": "A", "text": "401 means the client is unauthenticated; 403 means the client is authenticated but lacks required permissions."},
                        {"id": "B", "text": "401 is for server-side crashes; 403 is for rate-limiting."},
                        {"id": "C", "text": "401 is for GET requests; 403 is only for POST requests."},
                        {"id": "D", "text": "There is no difference; they can be used interchangeably."}
                    ],
                    "correct_answer": "A",
                    "explanation": "401 indicates missing or invalid authentication credentials. 403 indicates that the user's identity is recognized, but access to the requested resource is denied."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Database Connection Pooling",
                    "points": 25,
                    "problem_statement": "Why do backend production applications employ database connection pooling? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Establishing a new TCP and TLS handshake to a database on every request is computationally expensive."},
                        {"id": "B", "text": "It limits the maximum number of concurrent database connections to prevent database exhaustion."},
                        {"id": "C", "text": "It eliminates the need for SQL queries by generating raw responses automatically."},
                        {"id": "D", "text": "It recycles established idle connections for reuse across multiple HTTP requests."}
                    ],
                    "correct_answer": ["A", "B", "D"],
                    "explanation": "Connection pools reduce socket handshake overhead, prevent DB connection starvation, and reuse active sockets. They do not replace SQL queries."
                }
            ]
        }
    },
    {
        "order": 10,
        "name": "SQL and Database Programming",
        "slug": "sql-database-programming",
        "icon": "Database",
        "description": "Complex SQL queries, joins, window functions, indexing strategies, normalization, and ACID transactions.",
        "exam": {
            "title": "SQL Querying & Database Modeling Certification",
            "slug": "sql-querying-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Validate proficiency with SQL joins, aggregation, grouping, subqueries, indexing, and ACID transaction isolation levels.",
            "instructions": "Demonstrate understanding of relational query optimization, database normalization, and relational algebra.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "SQL JOIN Types",
                    "points": 25,
                    "problem_statement": "Which SQL JOIN returns all rows from the left table, and matching rows from the right table (filling with NULL where no match exists)?",
                    "options": [
                        {"id": "A", "text": "INNER JOIN"},
                        {"id": "B", "text": "LEFT OUTER JOIN"},
                        {"id": "C", "text": "CROSS JOIN"},
                        {"id": "D", "text": "FULL OUTER JOIN"}
                    ],
                    "correct_answer": "B",
                    "explanation": "LEFT OUTER JOIN includes all rows from the left table and matched rows from the right table, populating unmatched right columns with NULL."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "ACID Properties: Isolation",
                    "points": 25,
                    "problem_statement": "In ACID relational databases, which phenomenon occurs when a transaction reads data modified by another concurrent uncommitted transaction?",
                    "options": [
                        {"id": "A", "text": "Dirty Read"},
                        {"id": "B", "text": "Non-Repeatable Read"},
                        {"id": "C", "text": "Phantom Read"},
                        {"id": "D", "text": "Deadlock"}
                    ],
                    "correct_answer": "A",
                    "explanation": "A dirty read occurs when a transaction reads changes made by another transaction before that transaction has committed."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "SQL Aggregate Functions and WHERE vs HAVING",
                    "points": 25,
                    "problem_statement": "When filtering rows based on an aggregate calculation like `COUNT(*) > 5`, which clause must be used?",
                    "options": [
                        {"id": "A", "text": "WHERE"},
                        {"id": "B", "text": "HAVING"},
                        {"id": "C", "text": "GROUP BY"},
                        {"id": "D", "text": "ORDER BY"}
                    ],
                    "correct_answer": "B",
                    "explanation": "`WHERE` filters individual rows before aggregation occurs; `HAVING` filters aggregated groups produced by `GROUP BY`."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Database B-Tree Indexing",
                    "points": 25,
                    "problem_statement": "Which of the following statements regarding B-Tree indexes in relational databases are true? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "A B-Tree index speeds up equality lookups (`=`) and range queries (`BETWEEN`, `<`)."},
                        {"id": "B", "text": "Adding indexes to a table has zero impact on `INSERT` or `UPDATE` performance."},
                        {"id": "C", "text": "A composite index on `(A, B)` can satisfy queries filtering on `A` alone due to the leftmost prefix rule."},
                        {"id": "D", "text": "Primary keys in InnoDB are clustered indexes that store row data in leaf nodes."}
                    ],
                    "correct_answer": ["A", "C", "D"],
                    "explanation": "B-Tree indexes support equality and range lookups. Leftmost prefix matching allows `(A, B)` to satisfy `A` queries. Clustered indexes store rows at leaves. Indexes add write overhead to INSERTs/UPDATEs."
                }
            ]
        }
    },
    {
        "order": 11,
        "name": "Data Structures",
        "slug": "data-structures",
        "icon": "Boxes",
        "description": "Arrays, Linked Lists, Stacks, Queues, Binary Search Trees, Heaps, Hash Tables, and Graphs.",
        "exam": {
            "title": "Data Structures Mastery Certification",
            "slug": "data-structures-certification",
            "difficulty": "Hard",
            "duration_minutes": 50,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Comprehensive evaluation of fundamental and advanced data structures, their asymptotic bounds, trade-offs, and optimal access patterns.",
            "instructions": "Demonstrate mastery of data structure implementations, pointer manipulation, and asymptotic analysis.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Valid Parentheses Checker",
                    "points": 30,
                    "problem_statement": "Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. A string is valid if open brackets are closed by the same type of brackets in the correct order. Print 'true' if valid or 'false' otherwise.",
                    "input_format": "A single string from stdin.",
                    "output_format": "'true' or 'false'.",
                    "constraints": "String length <= 1000",
                    "starter_code": {
                        "python": "import sys\n\ndef is_valid(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        elif char in mapping.values():\n            stack.append(char)\n    return not stack\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    print('true' if is_valid(s) else 'false')\n"
                    },
                    "test_cases": [
                        {"input": "()[]{}", "expected_output": "true", "is_hidden": False},
                        {"input": "(]", "expected_output": "false", "is_hidden": False},
                        {"input": "{[()]}", "expected_output": "true", "is_hidden": True},
                        {"input": "([)]", "expected_output": "false", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Binary Heap Extraction Complexity",
                    "points": 25,
                    "problem_statement": "What is the worst-case time complexity of extracting the minimum element from a Binary Min-Heap of N elements?",
                    "options": [
                        {"id": "A", "text": "O(1)"},
                        {"id": "B", "text": "O(log N)"},
                        {"id": "C", "text": "O(N)"},
                        {"id": "D", "text": "O(N log N)"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Extracting the root takes O(1) to inspect, but restoring the heap property (sift-down / bubble-down) traverses down the tree height of log N steps."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Hash Table Collisions",
                    "points": 20,
                    "problem_statement": "What technique resolves hash table collisions by storing collided elements in a linked list or dynamic bucket at that index?",
                    "options": [
                        {"id": "A", "text": "Linear Probing"},
                        {"id": "B", "text": "Separate Chaining"},
                        {"id": "C", "text": "Quadratic Probing"},
                        {"id": "D", "text": "Double Hashing"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Separate chaining stores all elements hashing to the same bucket in an auxiliary linked list or dynamic collection at that bucket index."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Binary Search Tree Properties",
                    "points": 25,
                    "problem_statement": "Which of the following statements about Binary Search Trees (BST) are true? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "An in-order traversal of a valid BST visits keys in strictly non-decreasing sorted order."},
                        {"id": "B", "text": "A standard unbalanced BST has worst-case search time complexity of O(N)."},
                        {"id": "C", "text": "Self-balancing BSTs like AVL trees guarantee O(log N) worst-case search, insertion, and deletion."},
                        {"id": "D", "text": "Every binary tree is automatically a binary search tree."}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "In-order traversal of a BST yields sorted order. An unbalanced degenerate BST degrades to a linked list O(N). Self-balancing BSTs guarantee O(log N). Not all binary trees satisfy the BST ordering property."
                }
            ]
        }
    },
    {
        "order": 12,
        "name": "Algorithms",
        "slug": "algorithms",
        "icon": "GitBranch",
        "description": "Sorting, Searching, Divide and Conquer, Greedy algorithms, Dynamic Programming, and Graph Traversals (BFS/DFS).",
        "exam": {
            "title": "Algorithms & Problem Solving Certification",
            "slug": "algorithms-problem-solving-certification",
            "difficulty": "Hard",
            "duration_minutes": 55,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Rigorous assessment of computational thinking, Big-O analysis, recurrence relations, Dijkstra's algorithm, and dynamic programming.",
            "instructions": "Implement algorithms within optimal time and space complexity constraints.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Binary Search Implementation",
                    "points": 30,
                    "problem_statement": "Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return -1. Write a program that reads target on line 1, and space-separated sorted integers on line 2.",
                    "input_format": "Line 1: target integer. Line 2: space-separated sorted integers.",
                    "output_format": "0-based index or -1.",
                    "constraints": "Array length <= 10000, target and values fit in 32-bit signed int.",
                    "starter_code": {
                        "python": "import sys\n\ndef binary_search(arr, target):\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().strip().split('\\n')\n    if len(lines) < 2:\n        return\n    target = int(lines[0].strip())\n    arr = [int(x) for x in lines[1].split()]\n    print(binary_search(arr, target))\n"
                    },
                    "test_cases": [
                        {"input": "9\n-1 0 3 5 9 12", "expected_output": "4", "is_hidden": False},
                        {"input": "2\n-1 0 3 5 9 12", "expected_output": "-1", "is_hidden": False},
                        {"input": "100\n10 20 30 40 50 100", "expected_output": "5", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Quicksort Worst-Case Time Complexity",
                    "points": 25,
                    "problem_statement": "What is the worst-case time complexity of standard Quicksort without randomized pivot selection on an already sorted array?",
                    "options": [
                        {"id": "A", "text": "O(N log N)"},
                        {"id": "B", "text": "O(N)"},
                        {"id": "C", "text": "O(N^2)"},
                        {"id": "D", "text": "O(log N)"}
                    ],
                    "correct_answer": "C",
                    "explanation": "If the pivot chosen is always the extreme element (first or last) on sorted data, the partition divides into N-1 and 0 elements, leading to O(N^2) comparisons."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Dijkstra's Algorithm Precondition",
                    "points": 20,
                    "problem_statement": "Which graph condition prevents Dijkstra's algorithm from finding the correct shortest paths?",
                    "options": [
                        {"id": "A", "text": "Cycles in the graph"},
                        {"id": "B", "text": "Negative edge weights"},
                        {"id": "C", "text": "Disconnected components"},
                        {"id": "D", "text": "Directed edges"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Dijkstra's greedy choice assumes that once a node's distance is finalized, no shorter path can be discovered later. Negative edge weights invalidate this assumption, requiring Bellman-Ford instead."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Dynamic Programming Principles",
                    "points": 25,
                    "problem_statement": "What two core properties must a problem exhibit to be solvable via Dynamic Programming? (Select the two correct options)",
                    "options": [
                        {"id": "A", "text": "Optimal Substructure"},
                        {"id": "B", "text": "Overlapping Subproblems"},
                        {"id": "C", "text": "NP-Completeness"},
                        {"id": "D", "text": "Greedy Choice Property"}
                    ],
                    "correct_answer": ["A", "B"],
                    "explanation": "Dynamic programming applies to problems possessing Optimal Substructure (an optimal solution contains optimal solutions to subproblems) and Overlapping Subproblems (the same subproblems are solved repeatedly)."
                }
            ]
        }
    },
    {
        "order": 13,
        "name": "Object-Oriented Programming",
        "slug": "object-oriented-programming",
        "icon": "Component",
        "description": "Encapsulation, Inheritance, Polymorphism, Abstraction, SOLID principles, and Gang of Four design patterns.",
        "exam": {
            "title": "Object-Oriented Design & Principles Certification",
            "slug": "oop-design-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Assess object-oriented architecture, SOLID design principles, inheritance hierarchies, runtime polymorphism, and creational/structural patterns.",
            "instructions": "Demonstrate understanding of object-oriented principles, interface contracts, and design pattern implementations.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "Liskov Substitution Principle (LSP)",
                    "points": 25,
                    "problem_statement": "According to the Liskov Substitution Principle in SOLID design, what must hold true for subtypes?",
                    "options": [
                        {"id": "A", "text": "A subtype must implement all public and private methods of the base class."},
                        {"id": "B", "text": "Objects of a superclass should be replaceable with objects of its subclasses without breaking program correctness."},
                        {"id": "C", "text": "Subclasses must always override every virtual method defined in the parent class."},
                        {"id": "D", "text": "Subclasses can never introduce new public methods not present in the superclass."}
                    ],
                    "correct_answer": "B",
                    "explanation": "LSP states that functions that use pointers or references to base classes must be able to use objects of derived classes without knowing the difference or altering desired correctness."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Singleton Design Pattern Trade-offs",
                    "points": 25,
                    "problem_statement": "What is a commonly cited architectural drawback of overusing the Singleton design pattern?",
                    "options": [
                        {"id": "A", "text": "It introduces global state and tight coupling, making unit testing and dependency mocking difficult."},
                        {"id": "B", "text": "It consumes double the memory of standard classes."},
                        {"id": "C", "text": "It cannot be compiled in statically typed languages."},
                        {"id": "D", "text": "It automatically causes database deadlocks."}
                    ],
                    "correct_answer": "A",
                    "explanation": "Singletons act as hidden global state, tightly coupling classes to a concrete implementation and making independent unit testing and mocking very challenging."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Compile-Time vs Runtime Polymorphism",
                    "points": 25,
                    "problem_statement": "Which of the following is an example of compile-time (static) polymorphism?",
                    "options": [
                        {"id": "A", "text": "Method overriding via virtual method table (vtable)"},
                        {"id": "B", "text": "Method overloading based on parameter count or parameter types"},
                        {"id": "C", "text": "Dynamic dispatch in interface calls"},
                        {"id": "D", "text": "Dependency injection at runtime"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Method overloading and operator overloading are resolved at compile time based on parameter signatures, making them static polymorphism."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "The Four Pillars of OOP",
                    "points": 25,
                    "problem_statement": "Which of the following comprise the four primary pillars of Object-Oriented Programming? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Encapsulation"},
                        {"id": "B", "text": "Inheritance"},
                        {"id": "C", "text": "Polymorphism"},
                        {"id": "D", "text": "Abstraction"}
                    ],
                    "correct_answer": ["A", "B", "C", "D"],
                    "explanation": "The four foundational pillars of OOP are Encapsulation (data hiding), Inheritance (code reuse), Polymorphism (multiple forms), and Abstraction (hiding implementation complexity)."
                }
            ]
        }
    },
    {
        "order": 14,
        "name": "HTML and CSS",
        "slug": "html-css",
        "icon": "FileCode",
        "description": "Semantic HTML5, CSS3 animations, Flexbox, Grid, CSS Variables, Typography, and cross-browser responsive layouts.",
        "exam": {
            "title": "HTML5 & Modern CSS3 Mastery Certification",
            "slug": "html-css-mastery-certification",
            "difficulty": "Easy",
            "duration_minutes": 40,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Demonstrate strong foundations in HTML5 semantic elements, CSS specificity rules, viewport units, modern layouts, and fluid typography.",
            "instructions": "Demonstrate knowledge of modern web styling standards, semantic document structures, and accessibility conventions.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "HTML5 Semantic Elements",
                    "points": 25,
                    "problem_statement": "Which HTML5 semantic element is best suited to encapsulate independent, self-contained content that could be distributed or syndicated on its own (e.g. a blog post or news story)?",
                    "options": [
                        {"id": "A", "text": "<section>"},
                        {"id": "B", "text": "<article>"},
                        {"id": "C", "text": "<aside>"},
                        {"id": "D", "text": "<div>"}
                    ],
                    "correct_answer": "B",
                    "explanation": "`<article>` specifies self-contained composition that is independently syndicatable or reusable (e.g., forum post, newspaper article, blog entry)."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "CSS Selector Specificity Calculation",
                    "points": 25,
                    "problem_statement": "Which of the following CSS selectors has the highest specificity?",
                    "options": [
                        {"id": "A", "text": "`.btn.primary:hover`"},
                        {"id": "B", "text": "`#nav .item`"},
                        {"id": "C", "text": "`div header nav ul li a`"},
                        {"id": "D", "text": "`#header #nav a`"}
                    ],
                    "correct_answer": "D",
                    "explanation": "Specificity is calculated as (Inline, ID, Class/Attribute/Pseudo-class, Element). `#header #nav a` has 2 IDs and 1 element (0, 2, 0, 1), which beats `#nav .item` (0, 1, 1, 0) and class selectors."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "CSS rem vs em Units",
                    "points": 25,
                    "problem_statement": "What is the difference between `em` and `rem` units in CSS font sizing?",
                    "options": [
                        {"id": "A", "text": "`rem` is relative to the root (`<html>`) element's font size, whereas `em` is relative to its immediate parent element's font size."},
                        {"id": "B", "text": "`em` is only for margins, while `rem` is only for paddings."},
                        {"id": "C", "text": "`rem` works in desktop browsers only; `em` is for mobile."},
                        {"id": "D", "text": "Both refer strictly to physical millimeters on display."}
                    ],
                    "correct_answer": "A",
                    "explanation": "`rem` stands for 'root em' and scales uniformly relative to the root html element (default 16px). `em` compounds relative to the parent element's font size."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Modern CSS Layout Features",
                    "points": 25,
                    "problem_statement": "Which of the following are native features of modern CSS3? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Native CSS custom properties (`--main-color: #16a34a;` and `var(--main-color)`)"},
                        {"id": "B", "text": "`clamp(MIN, VAL, MAX)` for responsive fluid typography without media queries"},
                        {"id": "C", "text": "`gap` property support inside Flexbox and Grid layouts"},
                        {"id": "D", "text": "Automatic compilation of Python scripts into CSS animations"}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "CSS variables, clamp(), and the gap property are native modern CSS features. Python is not natively compiled to CSS."
                }
            ]
        }
    },
    {
        "order": 15,
        "name": "Node.js Development",
        "slug": "nodejs-development",
        "icon": "Workflow",
        "description": "Server-side JavaScript, V8 engine, Libuv event loop, Streams, Buffers, EventEmitter, and Express.js APIs.",
        "exam": {
            "title": "Node.js Server-Side Engineering Certification",
            "slug": "nodejs-engineering-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Assess server-side Node.js capabilities: asynchronous I/O, Streams pipeline, EventEmitter architecture, clustering, and worker threads.",
            "instructions": "Demonstrate proficiency with Node.js runtime internals and standard modules.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Sum Line Numbers in Node.js",
                    "points": 30,
                    "problem_statement": "Write a Node.js program that reads all lines from standard input, parses each line as a float or integer, and prints their total sum rounded to two decimal places.",
                    "input_format": "Multiple lines of numbers from stdin.",
                    "output_format": "Sum rounded to 2 decimal places (e.g. 15.50).",
                    "constraints": "Number of lines <= 1000",
                    "starter_code": {
                        "javascript": "const fs = require('fs');\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf-8').trim();\n    if (!input) {\n        console.log('0.00');\n        return;\n    }\n    const lines = input.split(/\\r?\\n/);\n    let sum = 0;\n    for (const line of lines) {\n        const val = parseFloat(line.trim());\n        if (!isNaN(val)) sum += val;\n    }\n    console.log(sum.toFixed(2));\n}\n\nmain();\n"
                    },
                    "test_cases": [
                        {"input": "10.5\n4.25\n5.25", "expected_output": "20.00", "is_hidden": False},
                        {"input": "100\n200", "expected_output": "300.00", "is_hidden": False},
                        {"input": "0.1\n0.2", "expected_output": "0.30", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Node.js Libuv Threadpool",
                    "points": 25,
                    "problem_statement": "What library provides the underlying cross-platform asynchronous I/O and threadpool implementation in Node.js?",
                    "options": [
                        {"id": "A", "text": "V8 Engine"},
                        {"id": "B", "text": "Libuv"},
                        {"id": "C", "text": "Babel"},
                        {"id": "D", "text": "Webpack"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Libuv is the multi-platform C library that handles the event loop, threadpool (for filesystem, crypto, and DNS lookup), and async network I/O in Node.js."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Node.js Streams Backpressure",
                    "points": 25,
                    "problem_statement": "What problem does 'backpressure' address in Node.js stream processing?",
                    "options": [
                        {"id": "A", "text": "When a readable stream produces data faster than the writable stream can consume it, risking buffer memory exhaustion."},
                        {"id": "B", "text": "When a CPU runs out of registers during floating-point operations."},
                        {"id": "C", "text": "When HTTP headers exceed 8KB in size."},
                        {"id": "D", "text": "When an async function forgets to use `await`."}
                    ],
                    "correct_answer": "A",
                    "explanation": "Backpressure occurs when the data generation rate of a readable stream overwhelms the write rate of the destination, pausing reading until the write buffer drains."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Node.js Architecture & Concurrency",
                    "points": 20,
                    "problem_statement": "Which of the following statements about Node.js concurrency are true? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "JavaScript execution in Node.js runs on a single main thread."},
                        {"id": "B", "text": "CPU-intensive tasks can block the event loop and prevent other requests from being handled."},
                        {"id": "C", "text": "The `worker_threads` module enables true multi-threaded parallel CPU execution in Node.js."},
                        {"id": "D", "text": "Node.js automatically compiles all synchronous loops into GPU shaders."}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "Node.js executes JS on a single event loop thread, so long CPU loops block incoming I/O. The worker_threads module allows running parallel JS threads with shared memory."
                }
            ]
        }
    },
    {
        "order": 16,
        "name": "Django Development",
        "slug": "django-development",
        "icon": "Flame",
        "description": "MTV architecture, Django ORM, Django REST Framework, authentication, middlewares, signals, and migrations.",
        "exam": {
            "title": "Django Web Framework Certification",
            "slug": "django-framework-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Prove your capabilities in building enterprise web backends with Django and DRF, query optimization (`select_related`, `prefetch_related`), and secure authentication.",
            "instructions": "Demonstrate knowledge of Django architecture, ORM query patterns, serializer validations, and REST APIs.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "select_related vs prefetch_related",
                    "points": 25,
                    "problem_statement": "What is the primary difference in database queries executed between `select_related()` and `prefetch_related()` in Django ORM?",
                    "options": [
                        {"id": "A", "text": "`select_related` performs an SQL JOIN in a single query (for ForeignKey/OneToOne); `prefetch_related` executes separate queries and joins in Python memory (for ManyToMany/Reverse FK)."},
                        {"id": "B", "text": "`select_related` only works with SQLite, while `prefetch_related` works with PostgreSQL."},
                        {"id": "C", "text": "`select_related` caches results in Redis; `prefetch_related` does not."},
                        {"id": "D", "text": "There is no functional difference; they are aliases."}
                    ],
                    "correct_answer": "A",
                    "explanation": "`select_related` creates an SQL JOIN and includes the fields of the related object in the SELECT statement. `prefetch_related` executes a separate lookup for each relationship and does the joining in Python."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Django Middleware Request/Response Flow",
                    "points": 25,
                    "problem_statement": "In what order are middleware classes executed during an incoming HTTP request in Django?",
                    "options": [
                        {"id": "A", "text": "Top-to-bottom of the `MIDDLEWARE` list during the request phase, and bottom-to-top during the response phase."},
                        {"id": "B", "text": "Random order depending on server load."},
                        {"id": "C", "text": "Bottom-to-top during both request and response phases."},
                        {"id": "D", "text": "Alphabetically by middleware class name."}
                    ],
                    "correct_answer": "A",
                    "explanation": "Django middlewares act as onion layers: requests pass through top-to-bottom, view logic runs, and responses return bottom-to-top through the reverse list."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "DRF Serializer Validation",
                    "points": 25,
                    "problem_statement": "In Django REST Framework, which method should you override to implement field-level validation for a field named `username` on a Serializer?",
                    "options": [
                        {"id": "A", "text": "`validate()`"},
                        {"id": "B", "text": "`validate_username(self, value)`"},
                        {"id": "C", "text": "`clean_username()`"},
                        {"id": "D", "text": "`check_username()`"}
                    ],
                    "correct_answer": "B",
                    "explanation": "DRF uses the convention `validate_<field_name>(self, value)` for custom field-level validation, returning the cleaned value or raising `serializers.ValidationError`."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Django Security Defaults",
                    "points": 25,
                    "problem_statement": "Which of the following built-in security protections are provided automatically by Django out of the box? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "CSRF protection via middleware and tokens (`CsrfViewMiddleware`)"},
                        {"id": "B", "text": "SQL injection prevention via parameterized query compilation in the ORM"},
                        {"id": "C", "text": "Automatic HTML template escaping to prevent reflected XSS"},
                        {"id": "D", "text": "Automatic password hashing using PBKDF2 with SHA256"}
                    ],
                    "correct_answer": ["A", "B", "C", "D"],
                    "explanation": "Django includes enterprise security out of the box: CSRF tokens, ORM query parameterization, DTL auto-escaping, and strong cryptographic password hashing."
                }
            ]
        }
    },
    {
        "order": 17,
        "name": "Operating Systems",
        "slug": "operating-systems",
        "icon": "Binary",
        "description": "Process scheduling, Virtual Memory, Paging, Concurrency, Mutexes, Semaphores, Deadlocks, and File Systems.",
        "exam": {
            "title": "Operating Systems & Concurrency Certification",
            "slug": "operating-systems-certification",
            "difficulty": "Hard",
            "duration_minutes": 50,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Assess core concepts of modern operating systems: virtual memory, page replacement algorithms, deadlock conditions, context switching, and POSIX synchronization.",
            "instructions": "Demonstrate understanding of kernel space, process control blocks, scheduling algorithms, and memory management units.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "Coffman Conditions for Deadlock",
                    "points": 25,
                    "problem_statement": "Which of the following is NOT one of the four Coffman conditions necessary for a system deadlock to occur?",
                    "options": [
                        {"id": "A", "text": "Mutual Exclusion"},
                        {"id": "B", "text": "Hold and Wait"},
                        {"id": "C", "text": "Preemption Enabled (Resources can be forcibly taken from processes)"},
                        {"id": "D", "text": "Circular Wait"}
                    ],
                    "correct_answer": "C",
                    "explanation": "The condition is No Preemption (resources cannot be forcibly taken). If preemption is enabled, deadlocks can be broken."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Virtual Memory and Page Faults",
                    "points": 25,
                    "problem_statement": "What hardware component is responsible for translating virtual memory addresses to physical RAM addresses via page tables?",
                    "options": [
                        {"id": "A", "text": "ALU (Arithmetic Logic Unit)"},
                        {"id": "B", "text": "MMU (Memory Management Unit)"},
                        {"id": "C", "text": "DMA Controller"},
                        {"id": "D", "text": "BIOS ROM"}
                    ],
                    "correct_answer": "B",
                    "explanation": "The Memory Management Unit (MMU) is the CPU hardware component that translates virtual addresses into physical addresses, utilizing the TLB (Translation Lookaside Buffer)."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Process vs Thread Context Switching",
                    "points": 25,
                    "problem_statement": "Why is a thread context switch within the same process typically faster than a process context switch?",
                    "options": [
                        {"id": "A", "text": "Threads within the same process share the same virtual address space, avoiding TLB invalidation."},
                        {"id": "B", "text": "Threads do not have their own program counter or registers."},
                        {"id": "C", "text": "Threads bypass the OS kernel scheduler completely."},
                        {"id": "D", "text": "Threads only execute interpreted code."}
                    ],
                    "correct_answer": "A",
                    "explanation": "Because threads in the same process share memory space (page tables), the MMU does not need to flush and reload the Translation Lookaside Buffer (TLB), greatly reducing switch overhead."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "CPU Scheduling Algorithms",
                    "points": 25,
                    "problem_statement": "Which of the following are preemptive CPU scheduling algorithms? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Round Robin (RR)"},
                        {"id": "B", "text": "Shortest Remaining Time First (SRTF)"},
                        {"id": "C", "text": "First-Come, First-Served (FCFS)"},
                        {"id": "D", "text": "Multilevel Feedback Queue (MLFQ)"}
                    ],
                    "correct_answer": ["A", "B", "D"],
                    "explanation": "Round Robin uses time quantum slices (preemptive); SRTF preempts when a shorter job arrives; MLFQ dynamically preempts and adjusts priorities. Standard FCFS is non-preemptive."
                }
            ]
        }
    },
    {
        "order": 18,
        "name": "Database Management Systems (DBMS)",
        "slug": "dbms",
        "icon": "HardDrive",
        "description": "Relational algebra, ER modeling, Normal Forms (1NF through BCNF), transaction logging (WAL), and distributed databases.",
        "exam": {
            "title": "Database Management Systems (DBMS) Certification",
            "slug": "dbms-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Verify comprehensive mastery of relational theory, database normalization rules, functional dependencies, indexing, and WAL recovery mechanisms.",
            "instructions": "Demonstrate knowledge of database theory, normalization algorithms, and storage engines.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "Database Normalization (3NF)",
                    "points": 25,
                    "problem_statement": "A relation is in Third Normal Form (3NF) if it is in 2NF and has no:",
                    "options": [
                        {"id": "A", "text": "Primary keys"},
                        {"id": "B", "text": "Transitive functional dependencies between non-prime attributes"},
                        {"id": "C", "text": "Foreign keys"},
                        {"id": "D", "text": "Composite attributes"}
                    ],
                    "correct_answer": "B",
                    "explanation": "3NF requires the relation to be in 2NF and ensures that no non-prime attribute is transitively dependent on any candidate key (every determinant must be a candidate key, or the dependent is a prime attribute)."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Write-Ahead Logging (WAL)",
                    "points": 25,
                    "problem_statement": "What is the core principle of Write-Ahead Logging (WAL) in database storage engines?",
                    "options": [
                        {"id": "A", "text": "Log records describing a data modification must be flushed to stable disk storage before the corresponding modified data page is written to disk."},
                        {"id": "B", "text": "All user queries must be logged in plain text before execution."},
                        {"id": "C", "text": "Transactions are only committed at midnight."},
                        {"id": "D", "text": "Data is written directly into memory without any disk writes."}
                    ],
                    "correct_answer": "A",
                    "explanation": "WAL guarantees Atomicity and Durability: changes are appended sequentially to a transaction log on non-volatile storage before dirty data pages are flushed from the buffer pool to disk."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Two-Phase Locking (2PL)",
                    "points": 25,
                    "problem_statement": "What does Strict Two-Phase Locking (Strict 2PL) ensure regarding transaction concurrency?",
                    "options": [
                        {"id": "A", "text": "Deadlock impossibility"},
                        {"id": "B", "text": "Conflict serializability and avoidance of cascading aborts"},
                        {"id": "C", "text": "Instantaneous transaction commits without locks"},
                        {"id": "D", "text": "Unlimited simultaneous write access to the same record"}
                    ],
                    "correct_answer": "B",
                    "explanation": "Strict 2PL holds all exclusive locks until transaction commit/abort, guaranteeing conflict serializable schedules and preventing cascading rollbacks."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "CAP Theorem",
                    "points": 25,
                    "problem_statement": "According to Eric Brewer's CAP Theorem, which three properties cannot all be simultaneously guaranteed in a distributed data store in the presence of a network partition? (Select the three)",
                    "options": [
                        {"id": "A", "text": "Consistency"},
                        {"id": "B", "text": "Availability"},
                        {"id": "C", "text": "Partition Tolerance"},
                        {"id": "D", "text": "Performance"}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "The CAP theorem states that a distributed system can at most provide two out of three guarantees: Consistency (every read receives the most recent write), Availability (every request receives a non-error response), and Partition Tolerance (system tolerates network packet drops)."
                }
            ]
        }
    },
    {
        "order": 19,
        "name": "Software Engineering",
        "slug": "software-engineering",
        "icon": "ShieldCheck",
        "description": "SDLC methodologies, Agile/Scrum, CI/CD pipelines, Test-Driven Development (TDD), code reviews, and clean architecture.",
        "exam": {
            "title": "Software Engineering & Architecture Certification",
            "slug": "software-engineering-certification",
            "difficulty": "Medium",
            "duration_minutes": 45,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Assess software engineering practices: CI/CD automation, testing pyramid, refactoring patterns, clean architecture, and version control branching models.",
            "instructions": "Demonstrate understanding of professional software engineering practices and agile team workflows.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "single_choice",
                    "title": "The Testing Pyramid",
                    "points": 25,
                    "problem_statement": "According to the traditional Testing Pyramid proposed by Mike Cohn, which layer of automated tests should form the largest base with the highest test count?",
                    "options": [
                        {"id": "A", "text": "End-to-End (E2E) UI Tests"},
                        {"id": "B", "text": "Integration Tests"},
                        {"id": "C", "text": "Unit Tests"},
                        {"id": "D", "text": "Manual Acceptance Tests"}
                    ],
                    "correct_answer": "C",
                    "explanation": "Unit tests run fast, isolate faults precisely, and are cheap to maintain, forming the broad foundation of the testing pyramid, topped by fewer integration and UI tests."
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Continuous Integration (CI)",
                    "points": 25,
                    "problem_statement": "What is the primary objective of Continuous Integration (CI)?",
                    "options": [
                        {"id": "A", "text": "Automatically merge developers' working copies into a shared trunk several times a day, accompanied by automated building and testing to detect integration bugs early."},
                        {"id": "B", "text": "Eliminating the need for software developers by generating code from user stories."},
                        {"id": "C", "text": "Deploying directly to production hardware without automated testing."},
                        {"id": "D", "text": "Storing code exclusively on local flash drives."}
                    ],
                    "correct_answer": "A",
                    "explanation": "CI aims to prevent 'merge hell' by frequently integrating code changes into the main branch and validating them with automated build and test pipelines."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Semantic Versioning (SemVer)",
                    "points": 25,
                    "problem_statement": "Under Semantic Versioning (MAJOR.MINOR.PATCH), when should the MAJOR version number be incremented?",
                    "options": [
                        {"id": "A", "text": "When making backward-compatible bug fixes."},
                        {"id": "B", "text": "When adding new functionality in a backward-compatible manner."},
                        {"id": "C", "text": "When introducing incompatible API breaking changes."},
                        {"id": "D", "text": "Every calendar month."}
                    ],
                    "correct_answer": "C",
                    "explanation": "MAJOR version increments indicate breaking, backward-incompatible changes. MINOR indicates backward-compatible features, and PATCH indicates backward-compatible bug fixes."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Code Smell Identification",
                    "points": 25,
                    "problem_statement": "Which of the following are recognized architectural code smells in software development? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "God Object (a single class that knows too much or does too much)"},
                        {"id": "B", "text": "Feature Envy (a method that seems more interested in a class other than the one it is in)"},
                        {"id": "C", "text": "Shotgun Surgery (a single change requires small edits across many different classes)"},
                        {"id": "D", "text": "Writing comprehensive docstrings and unit tests"}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "God Object, Feature Envy, and Shotgun Surgery are classic Fowler code smells. Comprehensive docstrings and unit tests are recognized software engineering best practices."
                }
            ]
        }
    },
    {
        "order": 20,
        "name": "Programming Fundamentals",
        "slug": "programming-fundamentals",
        "icon": "BookOpen",
        "description": "Control flow, variables, data types, Boolean logic, functions, recursion, and algorithmic problem-solving basics.",
        "exam": {
            "title": "Programming Fundamentals & Logic Certification",
            "slug": "programming-fundamentals-certification",
            "difficulty": "Easy",
            "duration_minutes": 40,
            "passing_percentage": 70,
            "total_marks": 100,
            "description": "Foundational assessment of programming constructs: loops, conditional branching, recursion, operator precedence, and arithmetic algorithms.",
            "instructions": "Demonstrate clear logical problem solving across multiple languages and core computational principles.",
            "questions": [
                {
                    "order": 1,
                    "question_type": "coding",
                    "title": "Factorial Calculation",
                    "points": 30,
                    "problem_statement": "Write a program that reads a non-negative integer N (0 <= N <= 12) from standard input and prints its factorial N! (where 0! = 1).",
                    "input_format": "A single non-negative integer N.",
                    "output_format": "Factorial value of N.",
                    "constraints": "0 <= N <= 12",
                    "starter_code": {
                        "python": "import sys\n\ndef fact(n):\n    if n <= 1:\n        return 1\n    res = 1\n    for i in range(2, n + 1):\n        res *= i\n    return res\n\nif __name__ == '__main__':\n    inp = sys.stdin.read().strip()\n    if inp:\n        print(fact(int(inp)))\n"
                    },
                    "test_cases": [
                        {"input": "5", "expected_output": "120", "is_hidden": False},
                        {"input": "0", "expected_output": "1", "is_hidden": False},
                        {"input": "6", "expected_output": "720", "is_hidden": True},
                        {"input": "10", "expected_output": "3628800", "is_hidden": True}
                    ]
                },
                {
                    "order": 2,
                    "question_type": "single_choice",
                    "title": "Short-Circuit Logical Evaluation",
                    "points": 25,
                    "problem_statement": "In most modern programming languages (Python, C, JavaScript, Java), what does short-circuit evaluation mean for the expression `A && B` (or `A and B`)?",
                    "options": [
                        {"id": "A", "text": "If `A` evaluates to false, `B` is not evaluated because the overall expression is already guaranteed to be false."},
                        {"id": "B", "text": "Both `A` and `B` are always executed concurrently in separate threads."},
                        {"id": "C", "text": "If `A` is true, `B` is skipped."},
                        {"id": "D", "text": "The program crashes with a hardware short-circuit interrupt."}
                    ],
                    "correct_answer": "A",
                    "explanation": "With the logical AND operator, if the first operand is falsy, the result must be falsy, so the runtime short-circuits and skips evaluating the second operand."
                },
                {
                    "order": 3,
                    "question_type": "single_choice",
                    "title": "Recursion Base Case",
                    "points": 20,
                    "problem_statement": "What happens if a recursive function does not have a properly reachable base case?",
                    "options": [
                        {"id": "A", "text": "The function returns 0 automatically."},
                        {"id": "B", "text": "Infinite recursion occurs until the call stack memory is exhausted, throwing a Stack Overflow error."},
                        {"id": "C", "text": "The compiler transforms it into a GPU pipeline."},
                        {"id": "D", "text": "The operating system restarts."}
                    ],
                    "correct_answer": "B",
                    "explanation": "Every recursive invocation pushes a stack frame. Without a terminating base case, recursion continues until memory allocated for the call stack is exhausted, causing a stack overflow."
                },
                {
                    "order": 4,
                    "question_type": "multiple_choice",
                    "title": "Primitive vs Reference Types",
                    "points": 25,
                    "problem_statement": "Which of the following statements regarding primitive types and reference types are true? (Select all that apply)",
                    "options": [
                        {"id": "A", "text": "Primitive values (e.g. integers, booleans) typically store raw values directly."},
                        {"id": "B", "text": "Reference types store memory addresses pointing to objects allocated on the heap."},
                        {"id": "C", "text": "Passing an object reference to a function allows modifying the object's contents inside the function."},
                        {"id": "D", "text": "Primitive values in standard languages can have arbitrary dynamic methods attached at runtime."}
                    ],
                    "correct_answer": ["A", "B", "C"],
                    "explanation": "Primitives store literal values directly on the stack or inline. References store pointers to heap-allocated objects. Passing references by value allows modifying the underlying object."
                }
            ]
        }
    }
]
