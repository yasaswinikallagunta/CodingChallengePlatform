# Domain 13: Algorithms - Backtracking & Recursion (Problems 241 - 260)

def solver_241(s: str) -> str:
    # Subsets Power Set Generation (number of subsets and lexicographically sorted subsets)
    parts = s.strip().split()
    n = int(parts[0])
    nums = sorted(int(x) for x in parts[1:1+n])
    res = []
    def backtrack(start, path):
        res.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    # format as [1,2] [1] etc
    formatted = ["[" + ",".join(str(x) for x in sub) + "]" for sub in res]
    return " ".join(formatted)

def solver_242(s: str) -> str:
    # Subsets II with Duplicates
    parts = s.strip().split()
    n = int(parts[0])
    nums = sorted(int(x) for x in parts[1:1+n])
    res = []
    def backtrack(start, path):
        res.append(list(path))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    formatted = ["[" + ",".join(str(x) for x in sub) + "]" for sub in res]
    return " ".join(formatted)

def solver_243(s: str) -> str:
    # Permutations Array Permute
    parts = s.strip().split()
    n = int(parts[0])
    nums = sorted(int(x) for x in parts[1:1+n])
    res = []
    visited = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(list(path))
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False
    backtrack([])
    formatted = ["[" + ",".join(str(x) for x in p) + "]" for p in res]
    return " ".join(formatted)

def solver_244(s: str) -> str:
    # Permutations II Unique
    parts = s.strip().split()
    n = int(parts[0])
    nums = sorted(int(x) for x in parts[1:1+n])
    res = []
    visited = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(list(path))
            return
        for i in range(len(nums)):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue
            visited[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            visited[i] = False
    backtrack([])
    formatted = ["[" + ",".join(str(x) for x in p) + "]" for p in res]
    return " ".join(formatted)

def solver_245(s: str) -> str:
    # Combination Sum Target
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    candidates = sorted(int(x) for x in parts[2:2+n])
    res = []
    def backtrack(start, remain, path):
        if remain == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain: break
            path.append(candidates[i])
            backtrack(i, remain - candidates[i], path)
            path.pop()
    backtrack(0, target, [])
    formatted = ["[" + ",".join(str(x) for x in c) + "]" for c in res]
    return " ".join(formatted) if formatted else "none"

def solver_246(s: str) -> str:
    # Combination Sum II No Reuse
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    candidates = sorted(int(x) for x in parts[2:2+n])
    res = []
    def backtrack(start, remain, path):
        if remain == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain: break
            if i > start and candidates[i] == candidates[i - 1]: continue
            path.append(candidates[i])
            backtrack(i + 1, remain - candidates[i], path)
            path.pop()
    backtrack(0, target, [])
    formatted = ["[" + ",".join(str(x) for x in c) + "]" for c in res]
    return " ".join(formatted) if formatted else "none"

def solver_247(s: str) -> str:
    # Letter Combinations of Phone
    digits = s.strip().split()[0]
    if not digits: return "none"
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = []
    def backtrack(idx, path):
        if idx == len(digits):
            res.append("".join(path))
            return
        for ch in mapping.get(digits[idx], ''):
            path.append(ch)
            backtrack(idx + 1, path)
            path.pop()
    backtrack(0, [])
    return " ".join(res) if res else "none"

def solver_248(s: str) -> str:
    # Generate Valid Parentheses
    n = int(s.strip().split()[0])
    res = []
    def backtrack(open_c, close_c, path):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_c < n:
            path.append('(')
            backtrack(open_c + 1, close_c, path)
            path.pop()
        if close_c < open_c:
            path.append(')')
            backtrack(open_c, close_c + 1, path)
            path.pop()
    backtrack(0, 0, [])
    return " ".join(res)

def solver_249(s: str) -> str:
    # Palindrome Partitioning Strings
    word = s.strip().split()[0]
    res = []
    def is_pal(sub): return sub == sub[::-1]
    def backtrack(start, path):
        if start == len(word):
            res.append(list(path))
            return
        for end in range(start + 1, len(word) + 1):
            sub = word[start:end]
            if is_pal(sub):
                path.append(sub)
                backtrack(end, path)
                path.pop()
    backtrack(0, [])
    formatted = ["[" + ",".join(p) + "]" for p in res]
    return " ".join(formatted)

def solver_250(s: str) -> str:
    # Word Search in Board Grid
    parts = s.strip().split()
    word = parts[0]
    r = int(parts[1])
    c = int(parts[2])
    idx = 3
    board = []
    for _ in range(r):
        board.append(parts[idx:idx+c])
        idx += c
    visited = set()
    def dfs(i, j, k):
        if k == len(word): return True
        if i < 0 or i >= r or j < 0 or j >= c or (i, j) in visited or board[i][j] != word[k]:
            return False
        visited.add((i, j))
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            if dfs(i + di, j + dj, k + 1):
                return True
        visited.remove((i, j))
        return False
    for i in range(r):
        for j in range(c):
            if dfs(i, j, 0):
                return "true"
    return "false"

def solver_251(s: str) -> str:
    # N-Queens Puzzle Solver (return number of distinct solutions)
    n = int(s.strip().split()[0])
    cols = set()
    pos_diag = set()
    neg_diag = set()
    count = 0
    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            backtrack(r + 1)
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
    backtrack(0)
    return str(count)

def solver_252(s: str) -> str:
    # N-Queens II Total Solutions
    n = int(s.strip().split()[0])
    cols = set()
    pos_diag = set()
    neg_diag = set()
    count = 0
    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            backtrack(r + 1)
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
    backtrack(0)
    return str(count)

def solver_253(s: str) -> str:
    # Sudoku Solver 9x9
    board = [list(row) for row in s.strip().split()]
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch: return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch: return False
        return True
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for d in '123456789':
                        if is_valid(i, j, d):
                            board[i][j] = d
                            if solve(): return True
                            board[i][j] = '.'
                    return False
        return True
    solve()
    return " ".join("".join(row) for row in board)

def solver_254(s: str) -> str:
    # Restore IP Addresses Validation
    raw = s.strip().split()[0]
    res = []
    def backtrack(start, dots, path):
        if dots == 4 and start == len(raw):
            res.append(".".join(path))
            return
        if dots > 4: return
        for length in range(1, 4):
            if start + length > len(raw): break
            segment = raw[start:start+length]
            if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                continue
            path.append(segment)
            backtrack(start + length, dots + 1, path)
            path.pop()
    backtrack(0, 0, [])
    return " ".join(sorted(res)) if res else "none"

def solver_255(s: str) -> str:
    # Word Search II Trie Lookup
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    idx = 2
    board = []
    for _ in range(r):
        board.append(parts[idx:idx+c])
        idx += c
    num_words = int(parts[idx])
    idx += 1
    words = parts[idx:idx+num_words]
    # Simple word search
    found = []
    for w in words:
        # search w in board
        visited = set()
        def dfs(i, j, k):
            if k == len(w): return True
            if i < 0 or i >= r or j < 0 or j >= c or (i, j) in visited or board[i][j] != w[k]:
                return False
            visited.add((i, j))
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                if dfs(i + di, j + dj, k + 1): return True
            visited.remove((i, j))
            return False
        w_found = False
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    w_found = True
                    break
            if w_found: break
        if w_found:
            found.append(w)
    return " ".join(sorted(found)) if found else "none"

def solver_256(s: str) -> str:
    # Combination Sum III Fixed Size (k numbers adding up to n using 1..9)
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    res = []
    def backtrack(start, remain, path):
        if len(path) == k:
            if remain == 0:
                res.append(list(path))
            return
        for i in range(start, 10):
            if i > remain: break
            path.append(i)
            backtrack(i + 1, remain - i, path)
            path.pop()
    backtrack(1, n, [])
    formatted = ["[" + ",".join(str(x) for x in c) + "]" for c in res]
    return " ".join(formatted) if formatted else "none"

def solver_257(s: str) -> str:
    # Combinations n Choose k
    parts = s.strip().split()
    n = int(parts[0])
    k = int(parts[1])
    res = []
    def backtrack(start, path):
        if len(path) == k:
            res.append(list(path))
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    formatted = ["[" + ",".join(str(x) for x in c) + "]" for c in res]
    return " ".join(formatted)

def solver_258(s: str) -> str:
    # Split String into Descending Values
    raw = s.strip().split()[0]
    def backtrack(index, prev):
        if index == len(raw):
            return True
        for j in range(index, len(raw)):
            val = int(raw[index:j+1])
            if prev is None:
                if j < len(raw) - 1:
                    if backtrack(j + 1, val): return True
            elif val == prev - 1:
                if backtrack(j + 1, val): return True
        return False
    return "true" if backtrack(0, None) else "false"

def solver_259(s: str) -> str:
    # Matchsticks to Square Partition
    parts = s.strip().split()
    n = int(parts[0])
    matchsticks = [int(x) for x in parts[1:1+n]]
    total = sum(matchsticks)
    if total % 4 != 0: return "false"
    side = total // 4
    matchsticks.sort(reverse=True)
    if matchsticks[0] > side: return "false"
    sides = [0] * 4
    def backtrack(idx):
        if idx == len(matchsticks):
            return True
        for i in range(4):
            if sides[i] + matchsticks[idx] <= side:
                sides[i] += matchsticks[idx]
                if backtrack(idx + 1): return True
                sides[i] -= matchsticks[idx]
            if sides[i] == 0: break
        return False
    return "true" if backtrack(0) else "false"

def solver_260(s: str) -> str:
    # Target Sum Expression Evaluator (count of valid expressions)
    parts = s.strip().split()
    target = int(parts[0])
    num = parts[1]
    count = 0
    def backtrack(index, prev_operand, current_val):
        nonlocal count
        if index == len(num):
            if current_val == target:
                count += 1
            return
        for i in range(index, len(num)):
            if i != index and num[index] == '0': break
            curr_str = num[index:i+1]
            curr_val = int(curr_str)
            if index == 0:
                backtrack(i + 1, curr_val, curr_val)
            else:
                backtrack(i + 1, curr_val, current_val + curr_val)
                backtrack(i + 1, -curr_val, current_val - curr_val)
                backtrack(i + 1, prev_operand * curr_val, current_val - prev_operand + (prev_operand * curr_val))
    backtrack(0, 0, 0)
    return str(count)

PROBLEMS = [
    {
        "index": 241,
        "title_base": "Subsets Power Set Generation",
        "description": "Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print all subsets formatted as [elem1,elem2] separated by spaces.",
        "constraints": "1 <= nums.length <= 10, -10 <= nums[i] <= 10",
        "sample_input": "3\n1 2 3",
        "sample_output": "[] [1] [1,2] [1,2,3] [1,3] [2] [2,3] [3]",
        "explanation": "All 8 subsets of [1, 2, 3] generated via backtracking.",
        "test_inputs": ["1\n0", "2\n1 2"],
        "variant_inputs": ["3\n4 5 6", "2\n10 20"],
        "starter_archetype": "array",
        "solver": solver_241
    },
    {
        "index": 242,
        "title_base": "Subsets II with Duplicates",
        "description": "Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print unique subsets formatted as [elem1,elem2] separated by spaces.",
        "constraints": "1 <= nums.length <= 10, -10 <= nums[i] <= 10",
        "sample_input": "3\n1 2 2",
        "sample_output": "[] [1] [1,2] [1,2,2] [2] [2,2]",
        "explanation": "Duplicate subsets are pruned during backtracking.",
        "test_inputs": ["1\n0", "2\n2 2"],
        "variant_inputs": ["3\n1 1 1", "3\n1 2 3"],
        "starter_archetype": "array",
        "solver": solver_242
    },
    {
        "index": 243,
        "title_base": "Permutations Array Permute",
        "description": "Given an array nums of distinct integers, return all the possible permutations.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print all permutations formatted as [elem1,elem2] separated by spaces.",
        "constraints": "1 <= nums.length <= 6, -10 <= nums[i] <= 10",
        "sample_input": "3\n1 2 3",
        "sample_output": "[1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]",
        "explanation": "All 3! = 6 permutations generated in order.",
        "test_inputs": ["2\n0 1", "1\n1"],
        "variant_inputs": ["3\n4 5 6", "2\n10 20"],
        "starter_archetype": "array",
        "solver": solver_243
    },
    {
        "index": 244,
        "title_base": "Permutations II Unique",
        "description": "Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print all unique permutations formatted as [elem1,elem2] separated by spaces.",
        "constraints": "1 <= nums.length <= 8, -10 <= nums[i] <= 10",
        "sample_input": "3\n1 1 2",
        "sample_output": "[1,1,2] [1,2,1] [2,1,1]",
        "explanation": "There are 3 unique permutations of [1, 1, 2].",
        "test_inputs": ["3\n1 2 3", "2\n2 2"],
        "variant_inputs": ["3\n3 3 1", "1\n5"],
        "starter_archetype": "array",
        "solver": solver_244
    },
    {
        "index": 245,
        "title_base": "Combination Sum Target",
        "description": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print all valid combinations formatted as [c1,c2] separated by spaces, or 'none'.",
        "constraints": "1 <= candidates.length <= 30, 2 <= candidates[i] <= 40, 1 <= target <= 40",
        "sample_input": "7 4\n2 3 6 7",
        "sample_output": "[2,2,3] [7]",
        "explanation": "2 and 3 can be used repeatedly: 2+2+3=7 and 7=7.",
        "test_inputs": ["8 3\n2 3 5", "2 1\n2"],
        "variant_inputs": ["6 3\n2 4 6", "5 2\n2 3"],
        "starter_archetype": "target_and_array",
        "solver": solver_245
    },
    {
        "index": 246,
        "title_base": "Combination Sum II No Reuse",
        "description": "Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print valid combinations formatted as [c1,c2] separated by spaces, or 'none'.",
        "constraints": "1 <= candidates.length <= 100, 1 <= candidates[i] <= 50, 1 <= target <= 30",
        "sample_input": "8 7\n10 1 2 7 6 1 5",
        "sample_output": "[1,1,6] [1,2,5] [1,7] [2,6]",
        "explanation": "Unique combinations without reusing an index: [1,1,6], [1,2,5], [1,7], [2,6].",
        "test_inputs": ["5 5\n2 5 2 1 2", "3 2\n1 2"],
        "variant_inputs": ["4 4\n1 1 2 2", "6 3\n2 4 6"],
        "starter_archetype": "target_and_array",
        "solver": solver_246
    },
    {
        "index": 247,
        "title_base": "Letter Combinations of Phone",
        "description": "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.",
        "input_format": "A single line containing the digit string.",
        "output_format": "Print all letter combinations separated by spaces, or 'none'.",
        "constraints": "0 <= digits.length <= 4, digits[i] is a digit in the range ['2', '9'].",
        "sample_input": "23",
        "sample_output": "ad ae af bd be bf cd ce cf",
        "explanation": "Keypad mapping yields 3 * 3 = 9 combinations.",
        "test_inputs": ["2", "7"],
        "variant_inputs": ["34", "9"],
        "starter_archetype": "single_string",
        "solver": solver_247
    },
    {
        "index": 248,
        "title_base": "Generate Valid Parentheses",
        "description": "Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print all well-formed parentheses strings separated by spaces.",
        "constraints": "1 <= n <= 8",
        "sample_input": "3",
        "sample_output": "((())) (()()) (())() ()(()) ()()()",
        "explanation": "All 5 valid combinations of 3 pairs of parentheses.",
        "test_inputs": ["1", "2"],
        "variant_inputs": ["4", "5"],
        "starter_archetype": "single_number",
        "solver": solver_248
    },
    {
        "index": 249,
        "title_base": "Palindrome Partitioning Strings",
        "description": "Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.",
        "input_format": "A single line containing string s.",
        "output_format": "Print all partitions formatted as [sub1,sub2] separated by spaces.",
        "constraints": "1 <= s.length <= 16, s contains only lowercase English letters.",
        "sample_input": "aab",
        "sample_output": "[a,a,b] [aa,b]",
        "explanation": "'a','a','b' and 'aa','b' are all palindromes.",
        "test_inputs": ["a", "racecar"],
        "variant_inputs": ["aba", "bb"],
        "starter_archetype": "single_string",
        "solver": solver_249
    },
    {
        "index": 250,
        "title_base": "Word Search in Board Grid",
        "description": "Given an m x n grid of characters board and a string word, return 'true' if word exists in the grid, or 'false' otherwise.",
        "input_format": "First line contains word, rows, and cols. Following lines contain grid characters.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= m, n <= 6, 1 <= word.length <= 15",
        "sample_input": "ABCCED 3 4\nA B C E\nS F C S\nA D E E",
        "sample_output": "true",
        "explanation": "ABCCED traces from (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,1).",
        "test_inputs": ["SEE 3 4\nA B C E\nS F C S\nA D E E", "ABCB 3 4\nA B C E\nS F C S\nA D E E"],
        "variant_inputs": ["CAT 2 2\nC A\nT S", "DOG 2 2\nD A\nB G"],
        "starter_archetype": "general",
        "solver": solver_250
    },
    {
        "index": 251,
        "title_base": "N-Queens Puzzle Solver",
        "description": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Return the number of distinct solutions.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the number of distinct solutions.",
        "constraints": "1 <= n <= 9",
        "sample_input": "4",
        "sample_output": "2",
        "explanation": "There are 2 distinct configurations to place 4 queens safely.",
        "test_inputs": ["1", "5"],
        "variant_inputs": ["6", "8"],
        "starter_archetype": "single_number",
        "solver": solver_251
    },
    {
        "index": 252,
        "title_base": "N-Queens II Total Solutions",
        "description": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an integer n, return the number of distinct solutions to the n-queens puzzle.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the total number of solutions.",
        "constraints": "1 <= n <= 9",
        "sample_input": "4",
        "sample_output": "2",
        "explanation": "There are two distinct solutions to the 4-queens puzzle.",
        "test_inputs": ["1", "2"],
        "variant_inputs": ["7", "3"],
        "starter_archetype": "single_number",
        "solver": solver_252
    },
    {
        "index": 253,
        "title_base": "Sudoku Solver 9x9",
        "description": "Write a program to solve a Sudoku puzzle by filling the empty cells (marked with '.'). A sudoku solution must satisfy all row, column, and 3x3 subgrid uniqueness rules.",
        "input_format": "9 lines of 9 characters each, where '.' represents empty cells.",
        "output_format": "Print 9 lines of 9 digits each representing the solved board.",
        "constraints": "The given board is always valid and has a unique solution.",
        "sample_input": "53..7....\n6..195...\n.98....6.\n8...6...3\n4..8.3..1\n7...2...6\n.6....28.\n...419..5\n....8..79",
        "sample_output": "534678912 672195348 198342567 859761423 426853791 713924856 961537284 287419635 345286179",
        "explanation": "The solved 9x9 sudoku board meets all Sudoku rules.",
        "test_inputs": [
            "534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n287419635\n34528617.",
            "53..7....\n6..195...\n.98....6.\n8...6...3\n4..8.3..1\n7...2...6\n.6....28.\n...419..5\n....8..7."
        ],
        "variant_inputs": [
            "534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n28741963.\n345286179",
            "534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n96153728.\n287419635\n345286179"
        ],
        "starter_archetype": "general",
        "solver": solver_253
    },
    {
        "index": 254,
        "title_base": "Restore IP Addresses Validation",
        "description": "A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 and cannot have leading zeros. Given a string s containing only digits, return all possible valid IP addresses in sorted order, or 'none'.",
        "input_format": "A single line containing digit string s.",
        "output_format": "Print all valid IP addresses separated by spaces, or 'none'.",
        "constraints": "1 <= s.length <= 20",
        "sample_input": "25525511135",
        "sample_output": "255.255.11.135 255.255.111.35",
        "explanation": "Two valid IP addresses can be restored.",
        "test_inputs": ["0000", "101023"],
        "variant_inputs": ["1111", "010010"],
        "starter_archetype": "single_string",
        "solver": solver_254
    },
    {
        "index": 255,
        "title_base": "Word Search II Trie Lookup",
        "description": "Given an m x n board of characters and a list of strings words, return all words on the board in sorted order, or 'none'.",
        "input_format": "First line contains rows and cols. Following lines contain the board. Next line contains words_count followed by the words.",
        "output_format": "Print found words in alphabetical order separated by spaces, or 'none'.",
        "constraints": "1 <= m, n <= 12, 1 <= words.length <= 3 * 10^4",
        "sample_input": "4 4\no a a n\ne t a e\ni h k r\ni f l v\n4 oath pea eat rain",
        "sample_output": "eat oath",
        "explanation": "'eat' and 'oath' are present on the board.",
        "test_inputs": ["2 2\na b\nc d\n1 abcd", "1 1\na\n1 a"],
        "variant_inputs": ["2 2\no a\ne t\n2 oat tea", "2 2\nx y\nz w\n1 hi"],
        "starter_archetype": "general",
        "solver": solver_255
    },
    {
        "index": 256,
        "title_base": "Combination Sum III Fixed Size",
        "description": "Find all valid combinations of k numbers that sum up to n such that only numbers 1 through 9 are used and each number is used at most once.",
        "input_format": "A single line containing k and n.",
        "output_format": "Print valid combinations formatted as [c1,c2] separated by spaces, or 'none'.",
        "constraints": "2 <= k <= 9, 1 <= n <= 60",
        "sample_input": "3 7",
        "sample_output": "[1,2,4]",
        "explanation": "1 + 2 + 4 = 7, with 3 distinct numbers.",
        "test_inputs": ["3 9", "4 1"],
        "variant_inputs": ["3 15", "2 5"],
        "starter_archetype": "two_numbers",
        "solver": solver_256
    },
    {
        "index": 257,
        "title_base": "Combinations n Choose k",
        "description": "Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].",
        "input_format": "A single line containing n and k.",
        "output_format": "Print all combinations formatted as [c1,c2] separated by spaces.",
        "constraints": "1 <= n <= 20, 1 <= k <= n",
        "sample_input": "4 2",
        "sample_output": "[1,2] [1,3] [1,4] [2,3] [2,4] [3,4]",
        "explanation": "4 choose 2 gives 6 combinations.",
        "test_inputs": ["1 1", "3 1"],
        "variant_inputs": ["3 2", "5 3"],
        "starter_archetype": "two_numbers",
        "solver": solver_257
    },
    {
        "index": 258,
        "title_base": "Split String into Descending Values",
        "description": "You are given a string s that consists of only digits. Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between consecutive values is 1.",
        "input_format": "A single line containing digit string s.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= s.length <= 20",
        "sample_input": "050043",
        "sample_output": "true",
        "explanation": "Can be split into [05, 004, 3] with values 5, 4, 3 (each difference is 1).",
        "test_inputs": ["10009998", "1234"],
        "variant_inputs": ["9080701", "21"],
        "starter_archetype": "single_string",
        "solver": solver_258
    },
    {
        "index": 259,
        "title_base": "Matchsticks to Square Partition",
        "description": "You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up. Return 'true' if you can make this square and 'false' otherwise.",
        "input_format": "First line contains N. Second line contains N matchstick lengths.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= matchsticks.length <= 15, 1 <= matchsticks[i] <= 10^8",
        "sample_input": "5\n1 1 2 2 2",
        "sample_output": "true",
        "explanation": "We can form a square with side length 2: (1, 1), 2, 2, 2.",
        "test_inputs": ["5\n3 3 3 3 4", "4\n1 1 1 1"],
        "variant_inputs": ["4\n2 2 2 2", "4\n5 5 5 6"],
        "starter_archetype": "array",
        "solver": solver_259
    },
    {
        "index": 260,
        "title_base": "Target Sum Expression Evaluator",
        "description": "Given a string num that contains only digits and an integer target, return the number of distinct expressions formed by adding binary operators ('+', '-', '*') between digits that evaluate to the target value.",
        "input_format": "A single line containing target and num.",
        "output_format": "Print the count of valid expressions.",
        "constraints": "1 <= num.length <= 10, -2^31 <= target <= 2^31 - 1",
        "sample_input": "6 123",
        "sample_output": "2",
        "explanation": "'1+2+3' and '1*2*3' both evaluate to 6.",
        "test_inputs": ["8 232", "5 105"],
        "variant_inputs": ["0 00", "2 11"],
        "starter_archetype": "general",
        "solver": solver_260
    }
]
