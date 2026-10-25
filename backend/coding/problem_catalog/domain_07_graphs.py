# Domain 07: Algorithms - Graph & BFS/DFS (Problems 121 - 140)
from collections import deque, defaultdict
import heapq

def solver_121(s: str) -> str:
    # Number of Islands
    parts = s.strip().split()
    if not parts: return "0"
    r = int(parts[0])
    c = int(parts[1])
    grid = []
    idx = 2
    for _ in range(r):
        row = parts[idx:idx+c]
        grid.append(row)
        idx += c
    visited = set()
    islands = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1' and (i, j) not in visited:
                islands += 1
                q = deque([(i, j)])
                visited.add((i, j))
                while q:
                    ci, cj = q.popleft()
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == '1' and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            q.append((ni, nj))
    return str(islands)

def solver_122(s: str) -> str:
    # Flood Fill Algorithm
    parts = s.strip().split()
    sr = int(parts[0])
    sc = int(parts[1])
    new_color = parts[2]
    r = int(parts[3])
    c = int(parts[4])
    idx = 5
    grid = []
    for _ in range(r):
        grid.append(parts[idx:idx+c])
        idx += c
    orig_color = grid[sr][sc]
    if orig_color != new_color:
        q = deque([(sr, sc)])
        grid[sr][sc] = new_color
        while q:
            ci, cj = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == orig_color:
                    grid[ni][nj] = new_color
                    q.append((ni, nj))
    res = []
    for row in grid:
        res.append(" ".join(row))
    return " ".join(" ".join(row) for row in grid)

def solver_123(s: str) -> str:
    # Max Area of Island
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    idx = 2
    grid = []
    for _ in range(r):
        grid.append([int(x) for x in parts[idx:idx+c]])
        idx += c
    visited = set()
    max_area = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1 and (i, j) not in visited:
                area = 0
                q = deque([(i, j)])
                visited.add((i, j))
                while q:
                    ci, cj = q.popleft()
                    area += 1
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 1 and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            q.append((ni, nj))
                max_area = max(max_area, area)
    return str(max_area)

def solver_124(s: str) -> str:
    # Surrounded Regions Capture
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    idx = 2
    board = []
    for _ in range(r):
        board.append(parts[idx:idx+c])
        idx += c
    # BFS from borders
    q = deque()
    for i in range(r):
        for j in range(c):
            if (i in (0, r-1) or j in (0, c-1)) and board[i][j] == 'O':
                q.append((i, j))
                board[i][j] = 'E'
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < r and 0 <= nj < c and board[ni][nj] == 'O':
                board[ni][nj] = 'E'
                q.append((ni, nj))
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'
    return " ".join(" ".join(row) for row in board)

def solver_125(s: str) -> str:
    # Rotting Oranges Simulation
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    idx = 2
    grid = []
    q = deque()
    fresh = 0
    for i in range(r):
        row = [int(x) for x in parts[idx:idx+c]]
        grid.append(row)
        idx += c
        for j in range(c):
            if row[j] == 2:
                q.append((i, j, 0))
            elif row[j] == 1:
                fresh += 1
    mins = 0
    while q:
        ci, cj, t = q.popleft()
        mins = max(mins, t)
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh -= 1
                q.append((ni, nj, t + 1))
    return str(mins) if fresh == 0 else "-1"

def solver_126(s: str) -> str:
    # Clone Undirected Graph (return number of nodes cloned)
    parts = s.strip().split()
    n = int(parts[0])
    return str(n)

def solver_127(s: str) -> str:
    # Course Schedule Prerequisite Check
    parts = s.strip().split()
    num = int(parts[0])
    e = int(parts[1])
    adj = defaultdict(list)
    indeg = [0] * num
    idx = 2
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        adj[v].append(u)
        indeg[u] += 1
        idx += 2
    q = deque([i for i in range(num) if indeg[i] == 0])
    count = 0
    while q:
        curr = q.popleft()
        count += 1
        for nxt in adj[curr]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return "true" if count == num else "false"

def solver_128(s: str) -> str:
    # Course Schedule Order Ordering
    parts = s.strip().split()
    num = int(parts[0])
    e = int(parts[1])
    adj = defaultdict(list)
    indeg = [0] * num
    idx = 2
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        adj[v].append(u)
        indeg[u] += 1
        idx += 2
    q = deque([i for i in range(num) if indeg[i] == 0])
    res = []
    while q:
        curr = q.popleft()
        res.append(str(curr))
        for nxt in adj[curr]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return " ".join(res) if len(res) == num else "none"

def solver_129(s: str) -> str:
    # Pacific Atlantic Water Flow (count of points)
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    idx = 2
    h = []
    for _ in range(r):
        h.append([int(x) for x in parts[idx:idx+c]])
        idx += c
    pac = set()
    atl = set()
    def bfs(starts, visited):
        q = deque(starts)
        for p in starts: visited.add(p)
        while q:
            ci, cj = q.popleft()
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in visited and h[ni][nj] >= h[ci][cj]:
                    visited.add((ni, nj))
                    q.append((ni, nj))
    bfs([(i, 0) for i in range(r)] + [(0, j) for j in range(c)], pac)
    bfs([(i, c-1) for i in range(r)] + [(r-1, j) for j in range(c)], atl)
    common = pac & atl
    return str(len(common))

def solver_130(s: str) -> str:
    # Number of Connected Components
    parts = s.strip().split()
    n = int(parts[0])
    e = int(parts[1])
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    idx = 2
    comps = n
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        idx += 2
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            comps -= 1
    return str(comps)

def solver_131(s: str) -> str:
    # Graph Valid Tree Check
    parts = s.strip().split()
    n = int(parts[0])
    e = int(parts[1])
    if e != n - 1:
        return "false"
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    idx = 2
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        idx += 2
        ru, rv = find(u), find(v)
        if ru == rv:
            return "false"
        parent[ru] = rv
    return "true"

def solver_132(s: str) -> str:
    # Redundant Connection Finder
    parts = s.strip().split()
    n = int(parts[0])
    e = int(parts[1])
    parent = list(range(n + 1))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    idx = 2
    ans = ""
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        idx += 2
        ru, rv = find(u), find(v)
        if ru == rv:
            ans = f"{u} {v}"
        else:
            parent[ru] = rv
    return ans

def solver_133(s: str) -> str:
    # Is Graph Bipartite
    parts = s.strip().split()
    n = int(parts[0])
    e = int(parts[1])
    adj = defaultdict(list)
    idx = 2
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    color = {}
    for node in range(n):
        if node not in color:
            color[node] = 0
            q = deque([node])
            while q:
                curr = q.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[curr]
                        q.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return "false"
    return "true"

def solver_134(s: str) -> str:
    # Word Ladder Shortest Transformation
    parts = s.strip().split()
    begin = parts[0]
    end = parts[1]
    n = int(parts[2])
    word_set = set(parts[3:3+n])
    if end not in word_set:
        return "0"
    q = deque([(begin, 1)])
    visited = {begin}
    while q:
        w, dist = q.popleft()
        if w == end:
            return str(dist)
        for i in range(len(w)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nw = w[:i] + c + w[i+1:]
                if nw in word_set and nw not in visited:
                    visited.add(nw)
                    q.append((nw, dist + 1))
    return "0"

def solver_135(s: str) -> str:
    # Alien Dictionary Order
    parts = s.strip().split()
    n = int(parts[0])
    words = parts[1:1+n]
    adj = defaultdict(set)
    in_degree = {c: 0 for w in words for c in w}
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    in_degree[c2] += 1
                break
        else:
            if len(w1) > len(w2):
                return "invalid"
    q = deque([c for c, deg in in_degree.items() if deg == 0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    return "".join(res) if len(res) == len(in_degree) else "invalid"

def solver_136(s: str) -> str:
    # Shortest Path in Binary Matrix
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    idx = 2
    grid = []
    for _ in range(r):
        grid.append([int(x) for x in parts[idx:idx+c]])
        idx += c
    if grid[0][0] != 0 or grid[r-1][c-1] != 0:
        return "-1"
    q = deque([(0, 0, 1)])
    grid[0][0] = 1
    while q:
        ci, cj, dist = q.popleft()
        if ci == r - 1 and cj == c - 1:
            return str(dist)
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0: continue
                ni, nj = ci + di, cj + dj
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    q.append((ni, nj, dist + 1))
    return "-1"

def solver_137(s: str) -> str:
    # Open the Lock BFS
    parts = s.strip().split()
    target = parts[0]
    n = int(parts[1])
    dead = set(parts[2:2+n])
    if "0000" in dead: return "-1"
    if target == "0000": return "0"
    q = deque([("0000", 0)])
    visited = {"0000"} | dead
    while q:
        state, turns = q.popleft()
        if state == target:
            return str(turns)
        for i in range(4):
            digit = int(state[i])
            for delta in (-1, 1):
                new_digit = (digit + delta) % 10
                new_state = state[:i] + str(new_digit) + state[i+1:]
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, turns + 1))
    return "-1"

def solver_138(s: str) -> str:
    # Evaluate Division Expressions
    # input: N (eqs) then N pairs (A B) then N values, then Q queries
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    adj = defaultdict(dict)
    for _ in range(n):
        a = parts[idx]
        b = parts[idx+1]
        val = float(parts[idx+2])
        idx += 3
        adj[a][b] = val
        adj[b][a] = 1.0 / val
    q_count = int(parts[idx])
    idx += 1
    res = []
    for _ in range(q_count):
        src = parts[idx]
        dst = parts[idx+1]
        idx += 2
        if src not in adj or dst not in adj:
            res.append("-1.0")
            continue
        # BFS
        q = deque([(src, 1.0)])
        visited = {src}
        ans = -1.0
        while q:
            curr, acc = q.popleft()
            if curr == dst:
                ans = acc
                break
            for neighbor, weight in adj[curr].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, acc * weight))
        res.append(f"{ans:.1f}")
    return " ".join(res)

def solver_139(s: str) -> str:
    # Reconstruct Itinerary Euler Path
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    adj = defaultdict(list)
    for _ in range(n):
        u = parts[idx]
        v = parts[idx+1]
        idx += 2
        adj[u].append(v)
    for u in adj:
        adj[u].sort(reverse=True)
    stack = ["JFK"]
    route = []
    while stack:
        while adj[stack[-1]]:
            stack.append(adj[stack[-1]].pop())
        route.append(stack.pop())
    return " ".join(reversed(route))

def solver_140(s: str) -> str:
    # Cheapest Flights within K Stops
    parts = s.strip().split()
    n = int(parts[0])
    src = int(parts[1])
    dst = int(parts[2])
    k = int(parts[3])
    e = int(parts[4])
    idx = 5
    flights = []
    for _ in range(e):
        u = int(parts[idx])
        v = int(parts[idx+1])
        w = int(parts[idx+2])
        flights.append((u, v, w))
        idx += 3
    prices = [float('inf')] * n
    prices[src] = 0
    for _ in range(k + 1):
        temp = list(prices)
        for u, v, w in flights:
            if prices[u] != float('inf') and prices[u] + w < temp[v]:
                temp[v] = prices[u] + w
        prices = temp
    return str(prices[dst]) if prices[dst] != float('inf') else "-1"

PROBLEMS = [
    {
        "index": 121,
        "title_base": "Number of Islands",
        "description": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
        "input_format": "First line contains rows and cols. Following lines contain the grid values.",
        "output_format": "Print the number of islands.",
        "constraints": "1 <= m, n <= 300, grid[i][j] is '0' or '1'.",
        "sample_input": "4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0",
        "sample_output": "1",
        "explanation": "All connected 1s form a single island.",
        "test_inputs": ["4 5\n1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1", "1 1\n1"],
        "variant_inputs": ["3 3\n1 0 1\n0 1 0\n1 0 1", "2 2\n0 0\n0 0"],
        "starter_archetype": "general",
        "solver": solver_121
    },
    {
        "index": 122,
        "title_base": "Flood Fill Algorithm",
        "description": "An image is represented by an m x n integer grid image where image[i][j] represents the pixel value. Perform a flood fill on the image starting from pixel (sr, sc) with color color.",
        "input_format": "First line contains sr, sc, color, rows, cols. Following lines contain image rows.",
        "output_format": "Print the modified image elements separated by spaces.",
        "constraints": "1 <= m, n <= 50, 0 <= image[i][j], color < 65536, 0 <= sr < m, 0 <= sc < n.",
        "sample_input": "1 1 2 3 3\n1 1 1\n1 1 0\n1 0 1",
        "sample_output": "2 2 2 2 2 0 2 0 1",
        "explanation": "Starting at (1,1), all connected 1s are replaced with 2.",
        "test_inputs": ["0 0 0 2 2\n0 0\n0 0", "0 0 2 1 1\n1"],
        "variant_inputs": ["0 1 3 2 3\n1 1 1\n2 1 2", "1 0 5 2 2\n2 2\n2 2"],
        "starter_archetype": "general",
        "solver": solver_122
    },
    {
        "index": 123,
        "title_base": "Max Area of Island",
        "description": "You are given an m x n binary matrix grid. An island is a 4-directionally connected group of 1s. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid.",
        "input_format": "First line contains rows and cols. Following lines contain the grid elements.",
        "output_format": "Print the maximum area.",
        "constraints": "1 <= m, n <= 50, grid[i][j] is either 0 or 1.",
        "sample_input": "4 5\n0 0 1 0 0\n0 1 1 1 0\n0 0 1 0 0\n0 0 0 0 0",
        "sample_output": "5",
        "explanation": "The island formed by the central 1s has area 5.",
        "test_inputs": ["2 2\n0 0\n0 0", "1 1\n1"],
        "variant_inputs": ["3 3\n1 1 0\n1 1 0\n0 0 1", "2 3\n1 1 1\n1 1 1"],
        "starter_archetype": "general",
        "solver": solver_123
    },
    {
        "index": 124,
        "title_base": "Surrounded Regions Capture",
        "description": "Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.",
        "input_format": "First line contains rows and cols. Following lines contain the board characters.",
        "output_format": "Print the modified board elements separated by spaces.",
        "constraints": "1 <= m, n <= 200, board[i][j] is 'X' or 'O'.",
        "sample_input": "4 4\nX X X X\nX O O X\nX X O X\nX O X X",
        "sample_output": "X X X X X X X X X X X X X O X X",
        "explanation": "Surrounded 'O' cells are flipped to 'X', while border connected 'O' remains.",
        "test_inputs": ["1 1\nX", "2 2\nO O\nO O"],
        "variant_inputs": ["3 3\nX X X\nX O X\nX X X", "3 3\nO X X\nX O X\nX X O"],
        "starter_archetype": "general",
        "solver": solver_124
    },
    {
        "index": 125,
        "title_base": "Rotting Oranges Simulation",
        "description": "You are given an m x n grid where 0 represents empty cell, 1 represents fresh orange, and 2 represents rotten orange. Every minute, any fresh orange 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes until no cell has a fresh orange, or -1 if impossible.",
        "input_format": "First line contains rows and cols. Following lines contain grid elements.",
        "output_format": "Print the minimum minutes or -1.",
        "constraints": "1 <= m, n <= 10, grid[i][j] is 0, 1, or 2.",
        "sample_input": "3 3\n2 1 1\n1 1 0\n0 1 1",
        "sample_output": "4",
        "explanation": "All oranges rot after 4 minutes.",
        "test_inputs": ["3 3\n2 1 1\n0 1 1\n1 0 1", "1 2\n0 2"],
        "variant_inputs": ["2 2\n1 1\n1 2", "2 2\n2 2\n2 2"],
        "starter_archetype": "general",
        "solver": solver_125
    },
    {
        "index": 126,
        "title_base": "Clone Undirected Graph",
        "description": "Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Output the number of cloned nodes.",
        "input_format": "First line contains N, the number of nodes.",
        "output_format": "Print the number of cloned nodes.",
        "constraints": "The number of nodes in the graph is between [0, 100].",
        "sample_input": "4",
        "sample_output": "4",
        "explanation": "Graph with 4 nodes is completely cloned.",
        "test_inputs": ["1", "0"],
        "variant_inputs": ["5", "10"],
        "starter_archetype": "single_number",
        "solver": solver_126
    },
    {
        "index": 127,
        "title_base": "Course Schedule Prerequisite Check",
        "description": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given prerequisites [ai, bi] indicating you must take course bi first if you want to take course ai. Return 'true' if you can finish all courses, or 'false' otherwise.",
        "input_format": "First line contains numCourses and E (number of prerequisite pairs). The next E pairs are given as (ai, bi).",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= numCourses <= 2000, 0 <= prerequisites.length <= 5000",
        "sample_input": "2 1\n1 0",
        "sample_output": "true",
        "explanation": "To take course 1 you should have finished course 0. So it is possible.",
        "test_inputs": ["2 2\n1 0 0 1", "1 0"],
        "variant_inputs": ["3 2\n1 0 2 1", "3 3\n0 1 1 2 2 0"],
        "starter_archetype": "general",
        "solver": solver_127
    },
    {
        "index": 128,
        "title_base": "Course Schedule Order Ordering",
        "description": "Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return 'none'.",
        "input_format": "First line contains numCourses and E. Next E pairs are (ai, bi).",
        "output_format": "Print the course order separated by spaces.",
        "constraints": "1 <= numCourses <= 2000, 0 <= prerequisites.length <= numCourses * (numCourses - 1)",
        "sample_input": "4 4\n1 0 2 0 3 1 3 2",
        "sample_output": "0 1 2 3",
        "explanation": "Topological ordering allows all courses to be taken sequentially.",
        "test_inputs": ["2 1\n1 0", "1 0"],
        "variant_inputs": ["3 2\n1 0 2 1", "2 2\n0 1 1 0"],
        "starter_archetype": "general",
        "solver": solver_128
    },
    {
        "index": 129,
        "title_base": "Pacific Atlantic Water Flow",
        "description": "There is an m x n rectangular island bordered by both the Pacific Ocean and Atlantic Ocean. Rain water can flow to neighboring cells directly north, south, east, and west if neighboring height is less than or equal to current height. Return the count of grid coordinates where water can flow to both oceans.",
        "input_format": "First line contains rows and cols. Following lines contain grid heights.",
        "output_format": "Print the number of coordinates flowing to both oceans.",
        "constraints": "1 <= m, n <= 200, 0 <= heights[r][c] <= 10^5",
        "sample_input": "5 5\n1 2 2 3 5\n3 2 3 4 4\n2 4 5 3 1\n6 7 1 4 5\n5 1 1 2 4",
        "sample_output": "7",
        "explanation": "7 coordinates can flow into both the Pacific and Atlantic oceans.",
        "test_inputs": ["1 1\n1", "2 2\n1 1\n1 1"],
        "variant_inputs": ["3 3\n1 2 3\n4 5 6\n7 8 9", "2 3\n3 3 3\n3 1 3"],
        "starter_archetype": "general",
        "solver": solver_129
    },
    {
        "index": 130,
        "title_base": "Number of Connected Components",
        "description": "You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph. Return the number of connected components in the graph.",
        "input_format": "First line contains n and E. Next lines contain E edges.",
        "output_format": "Print the number of connected components.",
        "constraints": "1 <= n <= 2000, 0 <= edges.length <= 5000",
        "sample_input": "5 4\n0 1 1 2 3 4 2 0",
        "sample_output": "2",
        "explanation": "Component 1: {0, 1, 2}, Component 2: {3, 4}.",
        "test_inputs": ["5 4\n0 1 1 2 2 3 3 4", "3 0"],
        "variant_inputs": ["4 2\n0 1 2 3", "4 1\n0 1"],
        "starter_archetype": "general",
        "solver": solver_130
    },
    {
        "index": 131,
        "title_base": "Graph Valid Tree Check",
        "description": "Given n nodes labeled from 0 to n-1 and a list of undirected edges, write a function to check whether these edges make up a valid tree.",
        "input_format": "First line contains n and E. Next lines contain E edges.",
        "output_format": "Print 'true' if valid tree, otherwise 'false'.",
        "constraints": "1 <= n <= 2000, 0 <= edges.length <= 5000",
        "sample_input": "5 4\n0 1 0 2 0 3 1 4",
        "sample_output": "true",
        "explanation": "Graph is connected and has no cycles, hence a valid tree.",
        "test_inputs": ["5 5\n0 1 1 2 2 3 1 3 1 4", "1 0"],
        "variant_inputs": ["4 3\n0 1 1 2 2 3", "4 2\n0 1 2 3"],
        "starter_archetype": "general",
        "solver": solver_131
    },
    {
        "index": 132,
        "title_base": "Redundant Connection Finder",
        "description": "In this problem, a tree is an undirected graph that is connected and has no cycles. Given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. Return an edge that can be removed so that the resulting graph is a tree of n nodes.",
        "input_format": "First line contains n and E. Next lines contain E edges.",
        "output_format": "Print the redundant edge endpoints separated by a space.",
        "constraints": "n == edges.length, 3 <= n <= 1000",
        "sample_input": "3 3\n1 2 1 3 2 3",
        "sample_output": "2 3",
        "explanation": "Edge [2, 3] creates a cycle and is redundant.",
        "test_inputs": ["5 5\n1 2 2 3 3 4 1 4 1 5", "4 4\n1 2 2 3 3 4 1 3"],
        "variant_inputs": ["4 4\n1 2 2 3 3 1 1 4", "3 3\n1 2 2 3 1 3"],
        "starter_archetype": "general",
        "solver": solver_132
    },
    {
        "index": 133,
        "title_base": "Is Graph Bipartite",
        "description": "There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. Return 'true' if and only if it is bipartite.",
        "input_format": "First line contains n and E. Next lines contain E edges.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= n <= 100, 0 <= E <= n * (n - 1) / 2",
        "sample_input": "4 4\n0 1 0 3 1 2 2 3",
        "sample_output": "true",
        "explanation": "Nodes can be partitioned into two sets {0, 2} and {1, 3}.",
        "test_inputs": ["4 5\n0 1 0 2 0 3 1 2 2 3", "2 1\n0 1"],
        "variant_inputs": ["3 3\n0 1 1 2 2 0", "4 2\n0 1 2 3"],
        "starter_archetype": "general",
        "solver": solver_133
    },
    {
        "index": 134,
        "title_base": "Word Ladder Shortest Transformation",
        "description": "Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.",
        "input_format": "First line contains beginWord, endWord, and N. Second line contains N words.",
        "output_format": "Print the sequence length.",
        "constraints": "1 <= beginWord.length <= 10, 1 <= wordList.length <= 5000",
        "sample_input": "hit cog 6\nhot dot dog lot log cog",
        "sample_output": "5",
        "explanation": "Shortest transformation is hit -> hot -> dot -> dog -> cog (5 words).",
        "test_inputs": ["hit cog 5\nhot dot dog lot log", "a c 3\na b c"],
        "variant_inputs": ["hot dog 3\nhot dot dog", "red tax 5\nted tex red tax tad"],
        "starter_archetype": "general",
        "solver": solver_134
    },
    {
        "index": 135,
        "title_base": "Alien Dictionary Order",
        "description": "There is a new alien language that uses the English alphabet. Given a list of words from the alien language's dictionary, sorted lexicographically by the rules of this new language, return a string of the unique letters in the new alien language sorted in lexicographically increasing order. If the order is invalid, return 'invalid'.",
        "input_format": "First line contains N. Following line contains N words.",
        "output_format": "Print the alien alphabet order as a string.",
        "constraints": "1 <= words.length <= 100, 1 <= words[i].length <= 100",
        "sample_input": "5\nwrt wrf er ett rftt",
        "sample_output": "wertf",
        "explanation": "The order of unique characters is w -> e -> r -> t -> f.",
        "test_inputs": ["2\nz x", "3\nz x z"],
        "variant_inputs": ["3\nabc abcd abd", "2\nbaa abcd"],
        "starter_archetype": "general",
        "solver": solver_135
    },
    {
        "index": 136,
        "title_base": "Shortest Path in Binary Matrix",
        "description": "Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1. An 8-directional move is allowed.",
        "input_format": "First line contains rows and cols. Following lines contain grid cells.",
        "output_format": "Print the shortest path length or -1.",
        "constraints": "1 <= n <= 100, grid[i][j] is 0 or 1.",
        "sample_input": "2 2\n0 1\n1 0",
        "sample_output": "2",
        "explanation": "Shortest clear path from (0,0) to (1,1) has length 2.",
        "test_inputs": ["3 3\n0 0 0\n1 1 0\n1 1 0", "2 2\n1 0\n0 0"],
        "variant_inputs": ["3 3\n0 1 0\n1 1 0\n1 1 0", "1 1\n0"],
        "starter_archetype": "general",
        "solver": solver_136
    },
    {
        "index": 137,
        "title_base": "Open the Lock BFS",
        "description": "You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0' to '9'. The lock starts at '0000'. Given a target and deadends, return the minimum total number of turns required to open the lock, or -1 if impossible.",
        "input_format": "First line contains target and deadends_count. Second line contains deadend combinations.",
        "output_format": "Print the minimum turns or -1.",
        "constraints": "1 <= deadends.length <= 500",
        "sample_input": "0202 5\n0201 0101 0102 1212 2002",
        "sample_output": "6",
        "explanation": "Path: 0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202 takes 6 turns.",
        "test_inputs": ["0009 1\n8888", "8888 1\n0000"],
        "variant_inputs": ["0001 2\n0002 0003", "1000 1\n0000"],
        "starter_archetype": "general",
        "solver": solver_137
    },
    {
        "index": 138,
        "title_base": "Evaluate Division Expressions",
        "description": "You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Given queries, evaluate each query and return the answers.",
        "input_format": "First line contains N (number of equations). The next N lines contain Ai Bi value. Then Q line with queries.",
        "output_format": "Print the query answers separated by spaces formatted to 1 decimal place.",
        "constraints": "1 <= equations.length <= 20, 1 <= queries.length <= 20",
        "sample_input": "2\na b 2.0\nb c 3.0\n3\na c\nb a\na e",
        "sample_output": "6.0 0.5 -1.0",
        "explanation": "a / c = 2.0 * 3.0 = 6.0, b / a = 0.5, a / e = -1.0.",
        "test_inputs": ["1\na b 0.5\n1\na b", "1\nx y 4.0\n1\ny x"],
        "variant_inputs": ["2\na b 1.5\nb c 2.5\n2\na c\nc b", "1\nm n 2.0\n1\nm m"],
        "starter_archetype": "general",
        "solver": solver_138
    },
    {
        "index": 139,
        "title_base": "Reconstruct Itinerary Euler Path",
        "description": "You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it. All tickets start from JFK and itinerary must be smallest lexical order.",
        "input_format": "First line contains N. Following line contains N ticket pairs.",
        "output_format": "Print the itinerary airports separated by spaces.",
        "constraints": "1 <= tickets.length <= 300",
        "sample_input": "4\nMUC LHR JFK MUC SFO SJC LHR SFO",
        "sample_output": "JFK MUC LHR SFO SJC",
        "explanation": "Valid itinerary in smallest lexical order starting from JFK.",
        "test_inputs": ["2\nJFK SFO SFO JFK", "1\nJFK ATL"],
        "variant_inputs": ["3\nJFK KUL JFK NRT NRT JFK", "2\nJFK ORD ORD JFK"],
        "starter_archetype": "general",
        "solver": solver_139
    },
    {
        "index": 140,
        "title_base": "Cheapest Flights within K Stops",
        "description": "There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei]. Return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.",
        "input_format": "First line contains n, src, dst, k, and E (flight count). Following line contains E triplets (u v price).",
        "output_format": "Print the cheapest price or -1.",
        "constraints": "1 <= n <= 100, 0 <= flights.length <= (n * (n - 1) / 2), 0 <= k < n",
        "sample_input": "4 0 3 1 5\n0 1 100 1 2 100 2 0 100 1 3 600 2 3 200",
        "sample_output": "700",
        "explanation": "The optimal path with at most 1 stop is 0 -> 1 -> 3 costing 100 + 600 = 700.",
        "test_inputs": ["3 0 2 1 3\n0 1 100 1 2 100 0 2 500", "3 0 2 0 3\n0 1 100 1 2 100 0 2 500"],
        "variant_inputs": ["4 0 3 1 4\n0 1 10 1 3 15 0 2 5 2 3 50", "2 0 1 0 1\n0 1 50"],
        "starter_archetype": "general",
        "solver": solver_140
    }
]
