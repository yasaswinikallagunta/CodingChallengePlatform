"""
Domain 3: Data Structures - Stack & Queue (20 problems)
"""

def solve_balanced_parentheses(s):
    s = s.strip()
    st = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            st.append(c)
        elif c in pairs:
            if not st or st[-1] != pairs[c]:
                return "false"
            st.pop()
    return "true" if not st else "false"

def solve_min_stack(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    stack, min_stack = [], []
    res = []
    idx = 1
    for _ in range(n):
        op = toks[idx]
        if op == "push":
            val = int(toks[idx+1])
            idx += 2
            stack.append(val)
            min_stack.append(val if not min_stack else min(val, min_stack[-1]))
        elif op == "pop":
            idx += 1
            if stack:
                stack.pop()
                min_stack.pop()
        elif op == "top":
            idx += 1
            res.append(str(stack[-1]) if stack else "null")
        elif op == "getMin":
            idx += 1
            res.append(str(min_stack[-1]) if min_stack else "null")
    return " ".join(res)

def solve_eval_rpn(s):
    toks = s.strip().split()
    if not toks: return "0"
    st = []
    for t in toks:
        if t in ("+", "-", "*", "/"):
            b = st.pop()
            a = st.pop()
            if t == "+": st.append(a + b)
            elif t == "-": st.append(a - b)
            elif t == "*": st.append(a * b)
            elif t == "/": st.append(int(a / b))
        else:
            st.append(int(t))
    return str(st[-1])

def solve_daily_temperatures(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    temps = [int(x) for x in toks[1:1+n]]
    ans = [0] * n
    st = []
    for i, t in enumerate(temps):
        while st and temps[st[-1]] < t:
            prev = st.pop()
            ans[prev] = i - prev
        st.append(i)
    return " ".join(map(str, ans))

def solve_next_greater_1(s):
    toks = s.strip().split()
    if not toks: return ""
    n1 = int(toks[0])
    nums1 = [int(x) for x in toks[1:1+n1]]
    n2 = int(toks[1+n1])
    nums2 = [int(x) for x in toks[2+n1:2+n1+n2]]
    st = []
    nxt = {}
    for x in nums2:
        while st and st[-1] < x:
            nxt[st.pop()] = x
        st.append(x)
    res = [str(nxt.get(x, -1)) for x in nums1]
    return " ".join(res)

def solve_next_greater_2(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    ans = [-1] * n
    st = []
    for i in range(2 * n):
        idx = i % n
        while st and nums[st[-1]] < nums[idx]:
            ans[st.pop()] = nums[idx]
        if i < n:
            st.append(i)
    return " ".join(map(str, ans))

def solve_queue_using_stacks(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    q = []
    res = []
    idx = 1
    for _ in range(n):
        op = toks[idx]
        if op == "push":
            val = int(toks[idx+1])
            idx += 2
            q.append(val)
        elif op == "pop":
            idx += 1
            if q: q.pop(0)
        elif op == "peek":
            idx += 1
            res.append(str(q[0]) if q else "null")
        elif op == "empty":
            idx += 1
            res.append("true" if not q else "false")
    return " ".join(res)

def solve_stack_using_queues(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    st = []
    res = []
    idx = 1
    for _ in range(n):
        op = toks[idx]
        if op == "push":
            val = int(toks[idx+1])
            idx += 2
            st.append(val)
        elif op == "pop":
            idx += 1
            if st: st.pop()
        elif op == "top":
            idx += 1
            res.append(str(st[-1]) if st else "null")
        elif op == "empty":
            idx += 1
            res.append("true" if not st else "false")
    return " ".join(res)

def solve_remove_adjacent_duplicates(s):
    s = s.strip()
    st = []
    for c in s:
        if st and st[-1] == c:
            st.pop()
        else:
            st.append(c)
    return "".join(st) if st else "empty"

def solve_simplify_path(s):
    path = s.strip()
    parts = path.split('/')
    st = []
    for p in parts:
        if p == '' or p == '.':
            continue
        if p == '..':
            if st: st.pop()
        else:
            st.append(p)
    return '/' + '/'.join(st)

def solve_basic_calculator(s):
    # Evaluates basic integer expressions with +, -, ()
    expr = s.strip().replace(" ", "")
    st = []
    num = 0
    sign = 1
    ans = 0
    for c in expr:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in ('+', '-'):
            ans += sign * num
            num = 0
            sign = 1 if c == '+' else -1
        elif c == '(':
            st.append(ans)
            st.append(sign)
            ans = 0
            sign = 1
        elif c == ')':
            ans += sign * num
            num = 0
            ans *= st.pop()
            ans += st.pop()
    ans += sign * num
    return str(ans)

def solve_asteroid_collision(s):
    toks = s.strip().split()
    if not toks: return "empty"
    n = int(toks[0])
    asteroids = [int(x) for x in toks[1:1+n]]
    st = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and st and st[-1] > 0:
            if st[-1] < -a:
                st.pop()
            elif st[-1] == -a:
                st.pop()
                alive = False
            else:
                alive = False
        if alive:
            st.append(a)
    return " ".join(map(str, st)) if st else "empty"

def solve_circular_queue(s):
    toks = s.strip().split()
    if not toks: return ""
    k = int(toks[0])
    n_ops = int(toks[1])
    q = []
    res = []
    idx = 2
    for _ in range(n_ops):
        op = toks[idx]
        if op == "enq":
            v = int(toks[idx+1])
            idx += 2
            if len(q) < k:
                q.append(v)
                res.append("true")
            else:
                res.append("false")
        elif op == "deq":
            idx += 1
            if q:
                q.pop(0)
                res.append("true")
            else:
                res.append("false")
        elif op == "front":
            idx += 1
            res.append(str(q[0]) if q else "-1")
        elif op == "rear":
            idx += 1
            res.append(str(q[-1]) if q else "-1")
    return " ".join(res)

def solve_circular_deque(s):
    toks = s.strip().split()
    if not toks: return ""
    k = int(toks[0])
    n_ops = int(toks[1])
    q = []
    res = []
    idx = 2
    for _ in range(n_ops):
        op = toks[idx]
        if op == "insertFront":
            v = int(toks[idx+1])
            idx += 2
            if len(q) < k:
                q.insert(0, v)
                res.append("true")
            else: res.append("false")
        elif op == "insertLast":
            v = int(toks[idx+1])
            idx += 2
            if len(q) < k:
                q.append(v)
                res.append("true")
            else: res.append("false")
        elif op == "deleteFront":
            idx += 1
            if q: q.pop(0); res.append("true")
            else: res.append("false")
        elif op == "deleteLast":
            idx += 1
            if q: q.pop(); res.append("true")
            else: res.append("false")
        elif op == "getFront":
            idx += 1
            res.append(str(q[0]) if q else "-1")
        elif op == "getRear":
            idx += 1
            res.append(str(q[-1]) if q else "-1")
    return " ".join(res)

def solve_sliding_window_max(s):
    toks = s.strip().split()
    if not toks: return ""
    k = int(toks[0])
    n = int(toks[1])
    nums = [int(x) for x in toks[2:2+n]]
    from collections import deque
    q = deque()
    res = []
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return " ".join(map(str, res))

def solve_trapping_rain_stack(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    h = [int(x) for x in toks[1:1+n]]
    st = []
    ans = 0
    for i, x in enumerate(h):
        while st and h[st[-1]] < x:
            top = st.pop()
            if not st: break
            dist = i - st[-1] - 1
            bounded = min(x, h[st[-1]]) - h[top]
            ans += dist * bounded
        st.append(i)
    return str(ans)

def solve_maximal_rectangle(s):
    toks = s.strip().split()
    if not toks: return "0"
    R = int(toks[0])
    C = int(toks[1])
    grid = []
    idx = 2
    for r in range(R):
        grid.append([int(toks[idx+c]) for c in range(C)])
        idx += C
    heights = [0] * C
    max_area = 0
    for row in grid:
        for c in range(C):
            heights[c] = heights[c] + 1 if row[c] == 1 else 0
        st = []
        for i, h in enumerate(heights + [0]):
            while st and (i == C or heights[st[-1]] >= h):
                height = heights[st.pop()]
                width = i if not st else i - st[-1] - 1
                max_area = max(max_area, height * width)
            st.append(i)
    return str(max_area)

def solve_validate_stack_seq(s):
    toks = s.strip().split()
    if not toks: return "false"
    n = int(toks[0])
    pushed = [int(x) for x in toks[1:1+n]]
    popped = [int(x) for x in toks[1+n:1+2*n]]
    st = []
    j = 0
    for x in pushed:
        st.append(x)
        while st and j < n and st[-1] == popped[j]:
            st.pop()
            j += 1
    return "true" if j == n else "false"

def solve_online_stock_span(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    prices = [int(x) for x in toks[1:1+n]]
    st = []
    res = []
    for p in prices:
        span = 1
        while st and st[-1][0] <= p:
            span += st.pop()[1]
        st.append((p, span))
        res.append(span)
    return " ".join(map(str, res))

def solve_sum_subarray_mins(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    arr = [int(x) for x in toks[1:1+n]]
    MOD = 10**9 + 7
    st = []
    ans = 0
    arr = [0] + arr + [0]
    for i, x in enumerate(arr):
        while st and arr[st[-1]] > x:
            j = st.pop()
            k = st[-1]
            ans = (ans + arr[j] * (i - j) * (j - k)) % MOD
        st.append(i)
    return str(ans)

PROBLEMS = [
    {
        "title_base": "Balanced Parentheses Validation",
        "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Open brackets must be closed by the same type of brackets in the correct order.",
        "input_format": "Line 1: A string containing parentheses characters",
        "output_format": "Output 'true' if the sequence is valid, or 'false' otherwise.",
        "constraints": "1 <= s.length <= 10^5",
        "io_type": "single_string",
        "sample_input": "()[]{}",
        "sample_output": "true",
        "explanation": "Brackets are closed in correct sequence.",
        "test_inputs": [
            "()[]{}",
            "(]",
            "([{}])",
            "((("
        ],
        "variant_inputs": [
            "{[]}",
            "({[)]}",
            "((()))[]",
            ")("
        ],
        "solver": solve_balanced_parentheses
    },
    {
        "title_base": "Min Stack Design",
        "description": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time O(1). Output the results of top and getMin operations.",
        "input_format": "Line 1: Number of operations N\nLine 2..N+1: Operations (e.g. 'push X', 'pop', 'top', 'getMin')",
        "output_format": "Output space-separated results of 'top' and 'getMin' queries.",
        "constraints": "1 <= N <= 10^4",
        "io_type": "general",
        "sample_input": "6\npush -2\npush 0\npush -3\ngetMin\npop\ngetMin",
        "sample_output": "-3 -2",
        "explanation": "getMin returns -3. After popping -3, next getMin returns -2.",
        "test_inputs": [
            "6\npush -2\npush 0\npush -3\ngetMin\npop\ngetMin",
            "4\npush 5\npush 3\ngetMin\ntop",
            "3\npush 10\ntop\ngetMin",
            "5\npush 1\npush 2\npop\ntop\ngetMin"
        ],
        "variant_inputs": [
            "5\npush 5\npush 5\ngetMin\npop\ngetMin",
            "4\npush -10\npush -5\ngetMin\ntop",
            "6\npush 8\npush 2\npush 4\ngetMin\ntop\ngetMin",
            "3\npush 100\ngetMin\ntop"
        ],
        "solver": solve_min_stack
    },
    {
        "title_base": "Evaluate Reverse Polish Notation",
        "description": "Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, and /. Each operand may be an integer or another expression. Division truncates toward zero.",
        "input_format": "Line 1: Space-separated tokens in postfix notation",
        "output_format": "Output the evaluated integer value.",
        "constraints": "1 <= tokens.length <= 10^4",
        "io_type": "single_string",
        "sample_input": "2 1 + 3 *",
        "sample_output": "9",
        "explanation": "((2 + 1) * 3) = 9.",
        "test_inputs": [
            "2 1 + 3 *",
            "4 13 5 / +",
            "10 6 9 3 + -11 * / * 17 + 5 +",
            "3 4 -"
        ],
        "variant_inputs": [
            "5 2 /",
            "15 7 1 1 + - / 3 * 2 1 1 + + -",
            "4 2 + 3 *",
            "10 5 -"
        ],
        "solver": solve_eval_rpn
    },
    {
        "title_base": "Daily Temperatures Span",
        "description": "Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated daily temperatures",
        "output_format": "Output N space-separated integers representing waiting days.",
        "constraints": "1 <= N <= 10^5\n30 <= temperatures[i] <= 100",
        "io_type": "array",
        "sample_input": "8\n73 74 75 71 69 72 76 73",
        "sample_output": "1 1 4 2 1 1 0 0",
        "explanation": "Day 0 has 73, next warmer is day 1 (74), wait = 1. Day 2 has 75, next warmer is day 6 (76), wait = 4.",
        "test_inputs": [
            "8\n73 74 75 71 69 72 76 73",
            "4\n30 40 50 60",
            "3\n30 60 90",
            "3\n80 70 60"
        ],
        "variant_inputs": [
            "5\n55 60 58 65 70",
            "6\n40 35 30 45 50 55",
            "4\n90 85 80 95",
            "2\n50 50"
        ],
        "solver": solve_daily_temperatures
    },
    {
        "title_base": "Next Greater Element I",
        "description": "The next greater element of some element x in an array is the first greater element that is to the right of x in the same array. Given array nums1 and array nums2, find next greater element for each item in nums1 within nums2.",
        "input_format": "Line 1: N1 (size of nums1)\nLine 2: N1 space-separated integers\nLine 3: N2 (size of nums2)\nLine 4: N2 space-separated integers",
        "output_format": "Output N1 space-separated next greater elements, or -1 if none exists.",
        "constraints": "1 <= N1 <= N2 <= 1000",
        "io_type": "two_arrays",
        "sample_input": "3\n4 1 2\n4\n1 3 4 2",
        "sample_output": "-1 3 -1",
        "explanation": "4 has no greater element to right (-1). 1 has next greater 3. 2 has none (-1).",
        "test_inputs": [
            "3\n4 1 2\n4\n1 3 4 2",
            "2\n2 4\n4\n1 2 3 4",
            "1\n5\n3\n5 2 6",
            "2\n1 2\n2\n2 1"
        ],
        "variant_inputs": [
            "3\n3 1 4\n5\n5 3 2 1 4",
            "2\n10 20\n3\n20 10 30",
            "1\n1\n2\n1 2",
            "3\n2 4 6\n3\n2 4 6"
        ],
        "solver": solve_next_greater_1
    },
    {
        "title_base": "Next Greater Element II",
        "description": "Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums. If it doesn't exist, return -1.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output N space-separated next greater numbers.",
        "constraints": "1 <= N <= 10^4\n-10^9 <= nums[i] <= 10^9",
        "io_type": "array",
        "sample_input": "3\n1 2 1",
        "sample_output": "2 -1 2",
        "explanation": "Next greater for 1 is 2. 2 is max, so -1. Next greater for last 1 wraps to 2.",
        "test_inputs": [
            "3\n1 2 1",
            "5\n1 2 3 4 3",
            "1\n42",
            "4\n5 4 3 2"
        ],
        "variant_inputs": [
            "4\n3 8 4 1",
            "5\n2 1 2 4 3",
            "3\n1 1 1",
            "4\n10 5 1 20"
        ],
        "solver": solve_next_greater_2
    },
    {
        "title_base": "Implement Queue using Stacks",
        "description": "Implement a first-in-first-out (FIFO) queue using only two stacks. Support operations: push x, pop, peek, empty.",
        "input_format": "Line 1: Number of operations N\nLine 2..N+1: Operations (e.g. 'push X', 'pop', 'peek', 'empty')",
        "output_format": "Output space-separated results of peek and empty queries.",
        "constraints": "1 <= N <= 100",
        "io_type": "general",
        "sample_input": "5\npush 1\npush 2\npeek\npop\nempty",
        "sample_output": "1 false",
        "explanation": "peek returns 1. After popping 1, queue has 2, so empty is false.",
        "test_inputs": [
            "5\npush 1\npush 2\npeek\npop\nempty",
            "3\npush 5\npeek\nempty",
            "4\npush 10\npop\nempty\nempty",
            "4\npush 3\npush 4\npeek\npeek"
        ],
        "variant_inputs": [
            "5\npush 10\npush 20\npop\npeek\nempty",
            "3\npush 7\npeek\npop",
            "4\npush 1\npush 2\npeek\nempty",
            "2\npush 99\npeek"
        ],
        "solver": solve_queue_using_stacks
    },
    {
        "title_base": "Implement Stack using Queues",
        "description": "Implement a last-in-first-out (LIFO) stack using standard queues. Support operations: push x, pop, top, empty.",
        "input_format": "Line 1: Number of operations N\nLine 2..N+1: Operations (e.g. 'push X', 'pop', 'top', 'empty')",
        "output_format": "Output space-separated results of top and empty queries.",
        "constraints": "1 <= N <= 100",
        "io_type": "general",
        "sample_input": "5\npush 1\npush 2\ntop\npop\nempty",
        "sample_output": "2 false",
        "explanation": "top returns 2. After popping 2, stack has 1, so empty is false.",
        "test_inputs": [
            "5\npush 1\npush 2\ntop\npop\nempty",
            "3\npush 5\ntop\nempty",
            "4\npush 10\npop\nempty\nempty",
            "3\npush 1\npush 2\ntop"
        ],
        "variant_inputs": [
            "5\npush 10\npush 20\npop\ntop\nempty",
            "3\npush 8\ntop\npop",
            "4\npush 4\npush 5\ntop\nempty",
            "2\npush 50\ntop"
        ],
        "solver": solve_stack_using_queues
    },
    {
        "title_base": "Remove All Adjacent Duplicates",
        "description": "You are given a string s. A duplicate removal consists of choosing two adjacent and equal letters and removing them. Repeatedly make duplicate removals until no adjacent pairs remain. If empty, return 'empty'.",
        "input_format": "Line 1: A lowercase string s",
        "output_format": "Output the final string after all duplicate removals, or 'empty'.",
        "constraints": "1 <= s.length <= 10^5",
        "io_type": "single_string",
        "sample_input": "abbaca",
        "sample_output": "ca",
        "explanation": "Remove 'bb' -> 'aaca'. Remove 'aa' -> 'ca'.",
        "test_inputs": [
            "abbaca",
            "azxxzy",
            "aa",
            "a"
        ],
        "variant_inputs": [
            "abccba",
            "mississippi",
            "repaper",
            "aabbcc"
        ],
        "solver": solve_remove_adjacent_duplicates
    },
    {
        "title_base": "Simplify File Path",
        "description": "Given an absolute path for a Unix-style file system, simplify it to its canonical path. In a canonical path, '.' is ignored, '..' goes up one directory, and multiple slashes are treated as a single slash.",
        "input_format": "Line 1: A string representing Unix path",
        "output_format": "Output the simplified canonical path.",
        "constraints": "1 <= path.length <= 3000",
        "io_type": "single_string",
        "sample_input": "/home//foo/",
        "sample_output": "/home/foo",
        "explanation": "Multiple consecutive slashes are reduced to single slash, trailing slash removed.",
        "test_inputs": [
            "/home//foo/",
            "/../",
            "/home/user/Documents/../Pictures",
            "/a/./b/../../c/"
        ],
        "variant_inputs": [
            "/a/../../b/../c//.//",
            "/a//b////c/d//././/..",
            "/...",
            "/home/foo/bar/../baz"
        ],
        "solver": solve_simplify_path
    },
    {
        "title_base": "Basic Calculator Evaluation",
        "description": "Given a string s representing a valid expression containing integers, '+', '-', '(', ')', and spaces, evaluate the expression and return its value.",
        "input_format": "Line 1: Arithmetic expression string",
        "output_format": "Output the integer result.",
        "constraints": "1 <= s.length <= 3 * 10^5",
        "io_type": "single_string",
        "sample_input": "(1+(4+5+2)-3)+(6+8)",
        "sample_output": "23",
        "explanation": "(1 + 11 - 3) + 14 = 9 + 14 = 23.",
        "test_inputs": [
            "(1+(4+5+2)-3)+(6+8)",
            "1 + 1",
            " 2-1 + 2 ",
            "- (3 + (4 + 5))"
        ],
        "variant_inputs": [
            "1-(     -2)",
            "(5-(1+2))+4",
            "10 - 20 + 30",
            "0"
        ],
        "solver": solve_basic_calculator
    },
    {
        "title_base": "Asteroid Collision Simulation",
        "description": "We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive = right, negative = left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output remaining asteroids separated by spaces, or 'empty' if none survive.",
        "constraints": "2 <= N <= 10^4\n-1000 <= asteroids[i] <= 1000, asteroids[i] != 0",
        "io_type": "array",
        "sample_input": "3\n5 10 -5",
        "sample_output": "5 10",
        "explanation": "10 and -5 collide resulting in 10. 5 and 10 never collide.",
        "test_inputs": [
            "3\n5 10 -5",
            "2\n8 -8",
            "3\n10 2 -5",
            "4\n-2 -1 1 2"
        ],
        "variant_inputs": [
            "4\n-2 -2 1 -2",
            "3\n1 -1 -2",
            "5\n1 2 3 -4 5",
            "2\n-5 5"
        ],
        "solver": solve_asteroid_collision
    },
    {
        "title_base": "Design Circular Queue",
        "description": "Design circular queue buffer of size k. Operations: enq X, deq, front, rear. Output true/false for enq/deq, and element value for front/rear (-1 if empty).",
        "input_format": "Line 1: Buffer capacity k and number of operations N\nLine 2..N+1: Operations ('enq X', 'deq', 'front', 'rear')",
        "output_format": "Output space-separated results.",
        "constraints": "1 <= k <= 1000",
        "io_type": "general",
        "sample_input": "3 6\nenq 1\nenq 2\nenq 3\nenq 4\nrear\ndeq",
        "sample_output": "true true true false 3 true",
        "explanation": "Capacity is 3. Fourth enq fails (false). rear is 3. deq succeeds (true).",
        "test_inputs": [
            "3 6\nenq 1\nenq 2\nenq 3\nenq 4\nrear\ndeq",
            "2 4\nenq 10\nfront\nrear\ndeq",
            "1 3\nenq 5\nenq 6\nfront",
            "2 3\ndeq\nfront\nrear"
        ],
        "variant_inputs": [
            "3 5\nenq 7\nenq 8\ndeq\nfront\nrear",
            "2 4\nenq 1\ndeq\ndeq\nfront",
            "4 4\nenq 10\nenq 20\nenq 30\nrear",
            "1 2\nenq 99\nrear"
        ],
        "solver": solve_circular_queue
    },
    {
        "title_base": "Design Circular Deque",
        "description": "Design double-ended circular queue buffer of size k. Operations: insertFront, insertLast, deleteFront, deleteLast, getFront, getRear.",
        "input_format": "Line 1: Capacity k and number of operations N\nLine 2..N+1: Operations",
        "output_format": "Output space-separated results.",
        "constraints": "1 <= k <= 1000",
        "io_type": "general",
        "sample_input": "3 5\ninsertLast 1\ninsertLast 2\ninsertFront 3\ninsertFront 4\ngetRear",
        "sample_output": "true true true false 2",
        "explanation": "3 items inserted. Fourth fails (false). Rear item is 2.",
        "test_inputs": [
            "3 5\ninsertLast 1\ninsertLast 2\ninsertFront 3\ninsertFront 4\ngetRear",
            "2 3\ninsertFront 5\ngetFront\ngetRear",
            "1 3\ndeleteFront\ninsertLast 10\ngetFront",
            "2 4\ninsertLast 1\ndeleteLast\ngetFront\ngetRear"
        ],
        "variant_inputs": [
            "3 4\ninsertFront 9\ninsertLast 8\ngetFront\ngetRear",
            "2 3\ninsertLast 4\ndeleteFront\ngetFront",
            "4 3\ninsertFront 1\ninsertFront 2\ngetRear",
            "1 2\ninsertLast 50\ngetRear"
        ],
        "solver": solve_circular_deque
    },
    {
        "title_base": "Sliding Window Maximum",
        "description": "You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Return the max sliding window values.",
        "input_format": "Line 1: Window size k\nLine 2: An integer N\nLine 3: N space-separated integers",
        "output_format": "Output space-separated maximum values.",
        "constraints": "1 <= k <= N <= 10^5\n-10^4 <= nums[i] <= 10^4",
        "io_type": "target_and_array",
        "sample_input": "3\n8\n1 3 -1 -3 5 3 6 7",
        "sample_output": "3 3 5 5 6 7",
        "explanation": "Window moves across array: max([1,3,-1])=3, max([3,-1,-3])=3, etc.",
        "test_inputs": [
            "3\n8\n1 3 -1 -3 5 3 6 7",
            "1\n1\n1",
            "1\n2\n1 -1",
            "2\n4\n9 11 8 5 7"
        ],
        "variant_inputs": [
            "4\n6\n1 2 3 4 5 6",
            "2\n5\n10 5 2 7 8",
            "3\n4\n4 3 2 1",
            "1\n3\n5 2 7"
        ],
        "solver": solve_sliding_window_max
    },
    {
        "title_base": "Trapping Rain Water with Stack",
        "description": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining using a monotonic stack.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated bar heights",
        "output_format": "Output total trapped rainwater.",
        "constraints": "1 <= N <= 10^5\n0 <= height[i] <= 10^5",
        "io_type": "array",
        "sample_input": "6\n4 2 0 3 2 5",
        "sample_output": "9",
        "explanation": "Total 9 units of trapped rainwater.",
        "test_inputs": [
            "6\n4 2 0 3 2 5",
            "12\n0 1 0 2 1 0 1 3 2 1 2 1",
            "3\n2 0 2",
            "2\n3 2"
        ],
        "variant_inputs": [
            "5\n3 0 1 0 2",
            "4\n2 1 1 2",
            "6\n5 4 1 2 3 6",
            "3\n1 1 1"
        ],
        "solver": solve_trapping_rain_stack
    },
    {
        "title_base": "Maximal Rectangle in Binary Matrix",
        "description": "Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.",
        "input_format": "Line 1: Two integers R and C\nNext R lines: C space-separated integers (0 or 1)",
        "output_format": "Output the maximum rectangle area.",
        "constraints": "1 <= R, C <= 200",
        "io_type": "matrix",
        "sample_input": "4 5\n1 0 1 0 0\n1 0 1 1 1\n1 1 1 1 1\n1 0 0 1 0",
        "sample_output": "6",
        "explanation": "The maximal rectangle has area = 6 (rows 1-2, cols 2-4).",
        "test_inputs": [
            "4 5\n1 0 1 0 0\n1 0 1 1 1\n1 1 1 1 1\n1 0 0 1 0",
            "1 1\n0",
            "1 1\n1",
            "2 2\n1 1\n1 1"
        ],
        "variant_inputs": [
            "3 3\n1 1 0\n1 1 1\n1 1 1",
            "2 3\n0 1 1\n1 1 1",
            "3 2\n1 0\n1 0\n1 0",
            "2 2\n0 0\n0 0"
        ],
        "solver": solve_maximal_rectangle
    },
    {
        "title_base": "Validate Stack Sequences",
        "description": "Given two integer arrays pushed and popped each with distinct values, return 'true' if this could have been the result of a sequence of push and pop operations on an initially empty stack, or 'false' otherwise.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers (pushed)\nLine 3: N space-separated integers (popped)",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "1 <= N <= 1000",
        "io_type": "two_arrays",
        "sample_input": "5\n1 2 3 4 5\n4 5 3 2 1",
        "sample_output": "true",
        "explanation": "We might do: push(1), push(2), push(3), push(4), pop() -> 4, push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1.",
        "test_inputs": [
            "5\n1 2 3 4 5\n4 5 3 2 1",
            "5\n1 2 3 4 5\n4 3 5 1 2",
            "1\n1\n1",
            "2\n1 2\n2 1"
        ],
        "variant_inputs": [
            "4\n1 2 3 4\n1 2 3 4",
            "3\n1 2 3\n3 1 2",
            "4\n2 1 0 3\n1 2 3 0",
            "2\n1 2\n1 2"
        ],
        "solver": solve_validate_stack_seq
    },
    {
        "title_base": "Online Stock Span Tracker",
        "description": "Calculate the span of stock prices representing the number of consecutive days (including today) the price was less than or equal to today's price.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated stock prices",
        "output_format": "Output N space-separated stock spans.",
        "constraints": "1 <= N <= 10^5\n1 <= prices[i] <= 10^5",
        "io_type": "array",
        "sample_input": "7\n100 80 60 70 60 75 85",
        "sample_output": "1 1 1 2 1 4 6",
        "explanation": "Spans for each day in order.",
        "test_inputs": [
            "7\n100 80 60 70 60 75 85",
            "4\n10 20 30 40",
            "4\n40 30 20 10",
            "1\n50"
        ],
        "variant_inputs": [
            "5\n31 41 48 59 79",
            "6\n60 50 70 40 80 90",
            "3\n25 25 25",
            "4\n10 5 15 20"
        ],
        "solver": solve_online_stock_span
    },
    {
        "title_base": "Sum of Subarray Minimums",
        "description": "Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output the sum modulo 10^9 + 7.",
        "constraints": "1 <= N <= 3 * 10^4\n1 <= arr[i] <= 3 * 10^4",
        "io_type": "array",
        "sample_input": "4\n3 1 2 4",
        "sample_output": "17",
        "explanation": "Subarrays: [3]->3, [1]->1, [2]->2, [4]->4, [3,1]->1, [1,2]->1, [2,4]->2, [3,1,2]->1, [1,2,4]->1, [3,1,2,4]->1. Sum = 17.",
        "test_inputs": [
            "4\n3 1 2 4",
            "5\n11 81 94 43 3",
            "1\n7",
            "3\n1 2 3"
        ],
        "variant_inputs": [
            "4\n71 55 82 55",
            "3\n2 1 2",
            "5\n1 3 2 4 1",
            "2\n5 10"
        ],
        "solver": solve_sum_subarray_mins
    }
]
