# Domain 08: Algorithms - Dynamic Programming (Problems 141 - 160)
from collections import defaultdict

def solver_141(s: str) -> str:
    # Climbing Stairs Ways
    n = int(s.strip().split()[0])
    if n <= 2: return str(n)
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return str(b)

def solver_142(s: str) -> str:
    # Min Cost Climbing Stairs
    parts = s.strip().split()
    n = int(parts[0])
    cost = [int(x) for x in parts[1:1+n]]
    dp0, dp1 = 0, 0
    for i in range(2, n + 1):
        dp0, dp1 = dp1, min(dp1 + cost[i - 1], dp0 + cost[i - 2])
    return str(dp1)

def solver_143(s: str) -> str:
    # House Robber Max Loot
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    if not nums: return "0"
    if len(nums) <= 2: return str(max(nums))
    rob1, rob2 = 0, 0
    for num in nums:
        rob1, rob2 = rob2, max(rob2, rob1 + num)
    return str(rob2)

def solver_144(s: str) -> str:
    # House Robber II Circular
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    if not nums: return "0"
    if len(nums) == 1: return str(nums[0])
    def simple_rob(arr):
        r1, r2 = 0, 0
        for x in arr:
            r1, r2 = r2, max(r2, r1 + x)
        return r2
    return str(max(simple_rob(nums[:-1]), simple_rob(nums[1:])))

def solver_145(s: str) -> str:
    # Coin Change Minimum Coins
    parts = s.strip().split()
    amount = int(parts[0])
    n = int(parts[1])
    coins = [int(x) for x in parts[2:2+n]]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] = min(dp[x], dp[x - c] + 1)
    return str(dp[amount]) if dp[amount] != float('inf') else "-1"

def solver_146(s: str) -> str:
    # Coin Change Total Combinations
    parts = s.strip().split()
    amount = int(parts[0])
    n = int(parts[1])
    coins = [int(x) for x in parts[2:2+n]]
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] += dp[x - c]
    return str(dp[amount])

def solver_147(s: str) -> str:
    # Longest Increasing Subsequence
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    import bisect
    sub = []
    for x in nums:
        idx = bisect.bisect_left(sub, x)
        if idx < len(sub):
            sub[idx] = x
        else:
            sub.append(x)
    return str(len(sub))

def solver_148(s: str) -> str:
    # Maximum Subarray Product
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    if not nums: return "0"
    max_so_far = min_so_far = result = nums[0]
    for x in nums[1:]:
        candidates = (x, max_so_far * x, min_so_far * x)
        max_so_far = max(candidates)
        min_so_far = min(candidates)
        result = max(result, max_so_far)
    return str(result)

def solver_149(s: str) -> str:
    # Unique Paths in Grid
    parts = s.strip().split()
    m = int(parts[0])
    n = int(parts[1])
    import math
    return str(math.comb(m + n - 2, m - 1))

def solver_150(s: str) -> str:
    # Unique Paths with Obstacles
    parts = s.strip().split()
    m = int(parts[0])
    n = int(parts[1])
    idx = 2
    grid = []
    for _ in range(m):
        grid.append([int(x) for x in parts[idx:idx+n]])
        idx += n
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return "0"
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0: dp[i][j] += dp[i-1][j]
                if j > 0: dp[i][j] += dp[i][j-1]
    return str(dp[m-1][n-1])

def solver_151(s: str) -> str:
    # Minimum Path Sum in Grid
    parts = s.strip().split()
    m = int(parts[0])
    n = int(parts[1])
    idx = 2
    grid = []
    for _ in range(m):
        grid.append([int(x) for x in parts[idx:idx+n]])
        idx += n
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return str(dp[m-1][n-1])

def solver_152(s: str) -> str:
    # Triangle Minimum Total
    parts = s.strip().split()
    num_rows = int(parts[0])
    idx = 1
    triangle = []
    for r in range(1, num_rows + 1):
        triangle.append([int(x) for x in parts[idx:idx+r]])
        idx += r
    for r in range(num_rows - 2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
    return str(triangle[0][0])

def solver_153(s: str) -> str:
    # Partition Equal Subset Sum
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    total = sum(nums)
    if total % 2 != 0: return "false"
    target = total // 2
    dp = {0}
    for x in nums:
        dp |= {val + x for val in dp if val + x <= target}
    return "true" if target in dp else "false"

def solver_154(s: str) -> str:
    # Target Sum Sign Assignment
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    dp = {0: 1}
    for x in nums:
        nxt = defaultdict(int)
        for cur, cnt in dp.items():
            nxt[cur + x] += cnt
            nxt[cur - x] += cnt
        dp = nxt
    return str(dp.get(target, 0))

def solver_155(s: str) -> str:
    # 0-1 Knapsack Optimization
    parts = s.strip().split()
    w_cap = int(parts[0])
    n = int(parts[1])
    idx = 2
    weights = [int(x) for x in parts[idx:idx+n]]
    idx += n
    values = [int(x) for x in parts[idx:idx+n]]
    dp = [0] * (w_cap + 1)
    for w, v in zip(weights, values):
        for j in range(w_cap, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return str(dp[w_cap])

def solver_156(s: str) -> str:
    # Edit Distance Levenshtein
    parts = s.strip().split()
    w1 = parts[0] if len(parts) > 0 else ""
    w2 = parts[1] if len(parts) > 1 else ""
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return str(dp[m][n])

def solver_157(s: str) -> str:
    # Longest Common Subsequence
    parts = s.strip().split()
    t1 = parts[0] if len(parts) > 0 else ""
    t2 = parts[1] if len(parts) > 1 else ""
    m, n = len(t1), len(t2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if t1[i - 1] == t2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return str(dp[m][n])

def solver_158(s: str) -> str:
    # Interleaving String Checker
    parts = s.strip().split()
    s1 = parts[0] if len(parts) > 0 else ""
    s2 = parts[1] if len(parts) > 1 else ""
    s3 = parts[2] if len(parts) > 2 else ""
    if len(s1) + len(s2) != len(s3):
        return "false"
    dp = [False] * (len(s2) + 1)
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
            elif j == 0:
                dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
            else:
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
    return "true" if dp[len(s2)] else "false"

def solver_159(s: str) -> str:
    # Distinct Subsequences Total
    parts = s.strip().split()
    s_str = parts[0]
    t_str = parts[1]
    m, n = len(s_str), len(t_str)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if s_str[i - 1] == t_str[j - 1]:
                dp[j] += dp[j - 1]
    return str(dp[n])

def solver_160(s: str) -> str:
    # Burst Balloons Maximum Coins
    parts = s.strip().split()
    n = int(parts[0])
    nums = [1] + [int(x) for x in parts[1:1+n]] + [1]
    L = len(nums)
    dp = [[0] * L for _ in range(L)]
    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for k in range(left, right + 1):
                coins = nums[left - 1] * nums[k] * nums[right + 1] + dp[left][k - 1] + dp[k + 1][right]
                dp[left][right] = max(dp[left][right], coins)
    return str(dp[1][n])

PROBLEMS = [
    {
        "index": 141,
        "title_base": "Climbing Stairs Ways",
        "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the number of distinct ways.",
        "constraints": "1 <= n <= 45",
        "sample_input": "2",
        "sample_output": "2",
        "explanation": "There are two ways: 1 step + 1 step, or 2 steps.",
        "test_inputs": ["3", "5"],
        "variant_inputs": ["4", "10"],
        "starter_archetype": "single_number",
        "solver": solver_141
    },
    {
        "index": 142,
        "title_base": "Min Cost Climbing Stairs",
        "description": "You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps. Return the minimum cost to reach the top of the floor starting from index 0 or index 1.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the minimum cost.",
        "constraints": "2 <= N <= 1000, 0 <= cost[i] <= 999",
        "sample_input": "3\n10 15 20",
        "sample_output": "15",
        "explanation": "Cheapest option: Start at index 1, pay 15 and climb two steps to the top.",
        "test_inputs": ["10\n1 100 1 1 1 100 1 1 100 1", "2\n10 20"],
        "variant_inputs": ["4\n1 2 3 4", "5\n5 10 15 20 25"],
        "starter_archetype": "array",
        "solver": solver_142
    },
    {
        "index": 143,
        "title_base": "House Robber Max Loot",
        "description": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. Adjacent houses have security systems connected that trigger an alarm if two adjacent houses are broken into. Determine maximum amount of money you can rob tonight without alerting the police.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the maximum loot.",
        "constraints": "1 <= N <= 100, 0 <= nums[i] <= 400",
        "sample_input": "4\n1 2 3 1",
        "sample_output": "4",
        "explanation": "Rob house 1 (money = 1) and rob house 3 (money = 3). Total amount = 4.",
        "test_inputs": ["5\n2 7 9 3 1", "1\n50"],
        "variant_inputs": ["6\n1 3 1 3 100 1", "3\n2 1 1"],
        "starter_archetype": "array",
        "solver": solver_143
    },
    {
        "index": 144,
        "title_base": "House Robber II Circular",
        "description": "All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Adjacent houses cannot be robbed. Return the maximum amount of money you can rob tonight without alerting the police.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the maximum circular loot.",
        "constraints": "1 <= N <= 100, 0 <= nums[i] <= 1000",
        "sample_input": "3\n2 3 2",
        "sample_output": "3",
        "explanation": "You cannot rob house 1 and house 3 because they are adjacent in a circle. Max is 3.",
        "test_inputs": ["4\n1 2 3 1", "1\n100"],
        "variant_inputs": ["5\n2 7 9 3 1", "4\n5 1 1 5"],
        "starter_archetype": "array",
        "solver": solver_144
    },
    {
        "index": 145,
        "title_base": "Coin Change Minimum Coins",
        "description": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.",
        "input_format": "First line contains amount and N. Second line contains N coin values.",
        "output_format": "Print the fewest number of coins or -1.",
        "constraints": "1 <= coins.length <= 12, 1 <= coins[i] <= 2^31 - 1, 0 <= amount <= 10^4",
        "sample_input": "11 3\n1 2 5",
        "sample_output": "3",
        "explanation": "11 = 5 + 5 + 1 (3 coins).",
        "test_inputs": ["3 1\n2", "0 1\n1"],
        "variant_inputs": ["7 2\n2 4", "10 2\n5 10"],
        "starter_archetype": "target_and_array",
        "solver": solver_145
    },
    {
        "index": 146,
        "title_base": "Coin Change Total Combinations",
        "description": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the number of combinations that make up that amount.",
        "input_format": "First line contains amount and N. Second line contains N coin values.",
        "output_format": "Print the total number of combinations.",
        "constraints": "1 <= coins.length <= 300, 1 <= coins[i] <= 5000, 0 <= amount <= 5000",
        "sample_input": "5 3\n1 2 5",
        "sample_output": "4",
        "explanation": "Four ways to make 5: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1.",
        "test_inputs": ["3 1\n2", "10 1\n10"],
        "variant_inputs": ["4 2\n1 2", "6 3\n1 2 3"],
        "starter_archetype": "target_and_array",
        "solver": solver_146
    },
    {
        "index": 147,
        "title_base": "Longest Increasing Subsequence",
        "description": "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the length of the LIS.",
        "constraints": "1 <= N <= 2500, -10^4 <= nums[i] <= 10^4",
        "sample_input": "8\n10 9 2 5 3 7 101 18",
        "sample_output": "4",
        "explanation": "The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.",
        "test_inputs": ["6\n0 1 0 3 2 3", "7\n7 7 7 7 7 7 7"],
        "variant_inputs": ["5\n1 2 3 4 5", "5\n5 4 3 2 1"],
        "starter_archetype": "array",
        "solver": solver_147
    },
    {
        "index": 148,
        "title_base": "Maximum Subarray Product",
        "description": "Given an integer array nums, find a subarray that has the largest product, and return the product.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the maximum subarray product.",
        "constraints": "1 <= N <= 2 * 10^4, -10 <= nums[i] <= 10",
        "sample_input": "4\n2 3 -2 4",
        "sample_output": "6",
        "explanation": "[2, 3] has the largest product 6.",
        "test_inputs": ["3\n-2 0 -1", "1\n-5"],
        "variant_inputs": ["4\n-2 3 -4 -1", "3\n2 -5 -2"],
        "starter_archetype": "array",
        "solver": solver_148
    },
    {
        "index": 149,
        "title_base": "Unique Paths in Grid",
        "description": "There is a robot on an m x n grid. The robot is initially located at the top-left corner and tries to move to the bottom-right corner. The robot can only move either down or right at any point in time. Return the number of possible unique paths.",
        "input_format": "A single line containing integers m and n.",
        "output_format": "Print the number of unique paths.",
        "constraints": "1 <= m, n <= 100",
        "sample_input": "3 7",
        "sample_output": "28",
        "explanation": "From (0,0) to (2,6) there are 28 unique paths.",
        "test_inputs": ["3 2", "1 1"],
        "variant_inputs": ["4 4", "5 3"],
        "starter_archetype": "two_numbers",
        "solver": solver_149
    },
    {
        "index": 150,
        "title_base": "Unique Paths with Obstacles",
        "description": "You are given an m x n integer array obstacleGrid. An obstacle and space are marked as 1 or 0 respectively in grid. Return the number of possible unique paths from top-left to bottom-right.",
        "input_format": "First line contains m and n. Following lines contain the obstacle grid values.",
        "output_format": "Print the number of unique paths.",
        "constraints": "1 <= m, n <= 100, obstacleGrid[i][j] is 0 or 1.",
        "sample_input": "3 3\n0 0 0\n0 1 0\n0 0 0",
        "sample_output": "2",
        "explanation": "There is one obstacle in the middle of the 3x3 grid resulting in 2 paths.",
        "test_inputs": ["2 2\n0 1\n0 0", "1 1\n1"],
        "variant_inputs": ["3 3\n0 0 0\n0 0 0\n0 0 0", "2 2\n0 0\n0 0"],
        "starter_archetype": "general",
        "solver": solver_150
    },
    {
        "index": 151,
        "title_base": "Minimum Path Sum in Grid",
        "description": "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move either down or right.",
        "input_format": "First line contains m and n. Following lines contain grid values.",
        "output_format": "Print the minimum path sum.",
        "constraints": "1 <= m, n <= 200, 0 <= grid[i][j] <= 200",
        "sample_input": "3 3\n1 3 1\n1 5 1\n4 2 1",
        "sample_output": "7",
        "explanation": "Path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum to 7.",
        "test_inputs": ["2 3\n1 2 3\n4 5 6", "1 1\n5"],
        "variant_inputs": ["2 2\n1 2\n1 1", "3 2\n1 2\n3 4\n5 6"],
        "starter_archetype": "general",
        "solver": solver_151
    },
    {
        "index": 152,
        "title_base": "Triangle Minimum Total",
        "description": "Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below.",
        "input_format": "First line contains numRows. Next rows contain 1, 2, ..., numRows values.",
        "output_format": "Print the minimum total.",
        "constraints": "1 <= triangle.length <= 200, -10^4 <= triangle[i][j] <= 10^4",
        "sample_input": "4\n2\n3 4\n6 5 7\n4 1 8 3",
        "sample_output": "11",
        "explanation": "The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.",
        "test_inputs": ["1\n-10", "2\n1\n2 3"],
        "variant_inputs": ["3\n1\n2 3\n4 5 6", "3\n5\n1 2\n3 4 5"],
        "starter_archetype": "general",
        "solver": solver_152
    },
    {
        "index": 153,
        "title_base": "Partition Equal Subset Sum",
        "description": "Given an integer array nums, return 'true' if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or 'false' otherwise.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= N <= 200, 1 <= nums[i] <= 100",
        "sample_input": "4\n1 5 11 5",
        "sample_output": "true",
        "explanation": "The array can be partitioned as [1, 5, 5] and [11].",
        "test_inputs": ["4\n1 2 3 5", "2\n1 2"],
        "variant_inputs": ["3\n1 2 3", "4\n2 2 2 2"],
        "starter_archetype": "array",
        "solver": solver_153
    },
    {
        "index": 154,
        "title_base": "Target Sum Sign Assignment",
        "description": "You are given an integer array nums and an integer target. You want to build an expression out of nums by adding '+' or '-' before each integer and then concatenate all integers. Return the number of different expressions that you can build, which evaluates to target.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print the number of ways.",
        "constraints": "1 <= N <= 20, 0 <= nums[i] <= 1000, -1000 <= target <= 1000",
        "sample_input": "3 5\n1 1 1 1 1",
        "sample_output": "5",
        "explanation": "There are 5 ways to assign symbols to make the sum 3.",
        "test_inputs": ["1 1\n1", "0 2\n1 1"],
        "variant_inputs": ["2 4\n1 1 1 1", "5 3\n2 3 4"],
        "starter_archetype": "target_and_array",
        "solver": solver_154
    },
    {
        "index": 155,
        "title_base": "0-1 Knapsack Optimization",
        "description": "Given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.",
        "input_format": "First line contains W and N. Second line contains N weights. Third line contains N values.",
        "output_format": "Print the maximum value.",
        "constraints": "1 <= N <= 1000, 1 <= W <= 1000",
        "sample_input": "4 3\n1 2 3\n10 15 40",
        "sample_output": "50",
        "explanation": "Take item 1 (weight 1, value 10) and item 3 (weight 3, value 40) for total weight 4 and maximum value 50.",
        "test_inputs": ["3 2\n1 2\n10 20", "5 3\n2 3 4\n3 4 5"],
        "variant_inputs": ["5 3\n1 2 3\n10 20 30", "10 2\n5 5\n50 50"],
        "starter_archetype": "general",
        "solver": solver_155
    },
    {
        "index": 156,
        "title_base": "Edit Distance Levenshtein",
        "description": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted on a word: Insert a character, Delete a character, Replace a character.",
        "input_format": "A single line containing word1 and word2.",
        "output_format": "Print the minimum edit distance.",
        "constraints": "0 <= word1.length, word2.length <= 500",
        "sample_input": "horse ros",
        "sample_output": "3",
        "explanation": "horse -> rorse (replace 'h' with 'r') -> rose (remove 'r') -> ros (remove 'e').",
        "test_inputs": ["intention execution", "a b"],
        "variant_inputs": ["kitten sitting", "sunday saturday"],
        "starter_archetype": "two_strings",
        "solver": solver_156
    },
    {
        "index": 157,
        "title_base": "Longest Common Subsequence",
        "description": "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
        "input_format": "A single line containing text1 and text2.",
        "output_format": "Print the LCS length.",
        "constraints": "1 <= text1.length, text2.length <= 1000",
        "sample_input": "abcde ace",
        "sample_output": "3",
        "explanation": "The longest common subsequence is 'ace' and its length is 3.",
        "test_inputs": ["abc abc", "abc def"],
        "variant_inputs": ["aggtab gxtxayb", "programming gaming"],
        "starter_archetype": "two_strings",
        "solver": solver_157
    },
    {
        "index": 158,
        "title_base": "Interleaving String Checker",
        "description": "Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.",
        "input_format": "A single line containing s1, s2, and s3.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "0 <= s1.length, s2.length <= 100, 0 <= s3.length <= 200",
        "sample_input": "aabcc dbbca aadbbcbcac",
        "sample_output": "true",
        "explanation": "s3 can be split into 'aa' (s1), 'dbbc' (s2), 'bc' (s1), 'a' (s2), 'c' (s1).",
        "test_inputs": ["aabcc dbbca aadbbbaccc", "a b ab"],
        "variant_inputs": ["abc def adbecf", "x y xy"],
        "starter_archetype": "general",
        "solver": solver_158
    },
    {
        "index": 159,
        "title_base": "Distinct Subsequences Total",
        "description": "Given two strings s and t, return the number of distinct subsequences of s which equals t.",
        "input_format": "A single line containing s and t.",
        "output_format": "Print the number of distinct subsequences.",
        "constraints": "1 <= s.length, t.length <= 1000",
        "sample_input": "rabbbit rabbit",
        "sample_output": "3",
        "explanation": "There are 3 ways you can generate 'rabbit' from 'rabbbit'.",
        "test_inputs": ["babgbag bag", "a a"],
        "variant_inputs": ["geeksforgeeks ge", "banana an"],
        "starter_archetype": "two_strings",
        "solver": solver_159
    },
    {
        "index": 160,
        "title_base": "Burst Balloons Maximum Coins",
        "description": "You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons. If you burst balloon i you will get nums[i - 1] * nums[i] * nums[i + 1] coins. Return the maximum coins you can collect by bursting the balloons wisely.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the maximum coins.",
        "constraints": "n == nums.length, 1 <= n <= 300, 0 <= nums[i] <= 100",
        "sample_input": "4\n3 1 5 8",
        "sample_output": "167",
        "explanation": "Burst 1 -> 5 -> 3 -> 8 yields 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15 + 120 + 24 + 8 = 167.",
        "test_inputs": ["2\n1 5", "1\n9"],
        "variant_inputs": ["3\n1 2 3", "3\n3 2 1"],
        "starter_archetype": "array",
        "solver": solver_160
    }
]
