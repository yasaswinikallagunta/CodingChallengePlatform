# Domain 11: Java - Priority Queue & Greedy (Problems 201 - 220)
from collections import Counter
import heapq

def solver_201(s: str) -> str:
    # Kth Largest Element in Array
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    nums.sort(reverse=True)
    return str(nums[k - 1])

def solver_202(s: str) -> str:
    # Top K Frequent Words
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    words = parts[2:2+n]
    counts = Counter(words)
    sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], w))
    return " ".join(sorted_words[:k])

def solver_203(s: str) -> str:
    # Merge K Sorted Integer Lists
    parts = s.strip().split()
    k = int(parts[0])
    idx = 1
    all_vals = []
    for _ in range(k):
        cnt = int(parts[idx])
        idx += 1
        all_vals.extend(int(x) for x in parts[idx:idx+cnt])
        idx += cnt
    all_vals.sort()
    return " ".join(str(x) for x in all_vals)

def solver_204(s: str) -> str:
    # Find Median from Data Stream (final median formatted to 1 decimal place)
    parts = s.strip().split()
    n = int(parts[0])
    nums = sorted(int(x) for x in parts[1:1+n])
    if n % 2 == 1:
        return f"{float(nums[n // 2]):.1f}"
    else:
        med = (nums[n // 2 - 1] + nums[n // 2]) / 2.0
        return f"{med:.1f}"

def solver_205(s: str) -> str:
    # Last Stone Weight Simulation
    parts = s.strip().split()
    n = int(parts[0])
    stones = [-int(x) for x in parts[1:1+n]]
    heapq.heapify(stones)
    while len(stones) > 1:
        s1 = -heapq.heappop(stones)
        s2 = -heapq.heappop(stones)
        if s1 != s2:
            heapq.heappush(stones, -(s1 - s2))
    return str(-stones[0]) if stones else "0"

def solver_206(s: str) -> str:
    # K Closest Points to Origin
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    idx = 2
    points = []
    for _ in range(n):
        x = int(parts[idx])
        y = int(parts[idx+1])
        points.append((x, y))
        idx += 2
    points.sort(key=lambda p: (p[0]**2 + p[1]**2, p[0], p[1]))
    res = [f"{p[0]} {p[1]}" for p in points[:k]]
    return " ".join(res)

def solver_207(s: str) -> str:
    # Sort Array by Increasing Frequency (ties in descending value)
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    counts = Counter(nums)
    nums.sort(key=lambda x: (counts[x], -x))
    return " ".join(str(x) for x in nums)

def solver_208(s: str) -> str:
    # Reorganize String No Adjacent
    word = s.strip().split()[0]
    counts = Counter(word)
    max_heap = [(-cnt, ch) for ch, cnt in counts.items()]
    heapq.heapify(max_heap)
    res = []
    prev_cnt, prev_ch = 0, ""
    while max_heap:
        cnt, ch = heapq.heappop(max_heap)
        res.append(ch)
        if prev_cnt < 0:
            heapq.heappush(max_heap, (prev_cnt, prev_ch))
        prev_cnt = cnt + 1
        prev_ch = ch
    ans = "".join(res)
    return ans if len(ans) == len(word) else "none"

def solver_209(s: str) -> str:
    # Task Scheduler CPU Cooldown
    parts = s.strip().split()
    n_cooldown = int(parts[0])
    num_tasks = int(parts[1])
    tasks = parts[2:2+num_tasks]
    counts = Counter(tasks)
    max_freq = max(counts.values())
    count_max_freq = sum(1 for v in counts.values() if v == max_freq)
    ans = (max_freq - 1) * (n_cooldown + 1) + count_max_freq
    return str(max(len(tasks), ans))

def solver_210(s: str) -> str:
    # Gas Station Circular Tour
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    gas = [int(x) for x in parts[idx:idx+n]]
    idx += n
    cost = [int(x) for x in parts[idx:idx+n]]
    if sum(gas) < sum(cost):
        return "-1"
    start = 0
    tank = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return str(start)

def solver_211(s: str) -> str:
    # Jump Game Can Reach End
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    max_reach = 0
    for i, x in enumerate(nums):
        if i > max_reach: return "false"
        max_reach = max(max_reach, i + x)
        if max_reach >= n - 1: return "true"
    return "true"

def solver_212(s: str) -> str:
    # Jump Game II Minimum Jumps
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    if n <= 1: return "0"
    jumps = 0
    cur_end = 0
    cur_farthest = 0
    for i in range(n - 1):
        cur_farthest = max(cur_farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_farthest
    return str(jumps)

def solver_213(s: str) -> str:
    # Assign Cookies to Children
    parts = s.strip().split()
    n = int(parts[0])
    m = int(parts[1])
    idx = 2
    g = sorted(int(x) for x in parts[idx:idx+n])
    idx += n
    s_cookies = sorted(int(x) for x in parts[idx:idx+m])
    i, j = 0, 0
    while i < len(g) and j < len(s_cookies):
        if s_cookies[j] >= g[i]:
            i += 1
        j += 1
    return str(i)

def solver_214(s: str) -> str:
    # Lemonade Change Register
    parts = s.strip().split()
    n = int(parts[0])
    bills = [int(x) for x in parts[1:1+n]]
    five = 0
    ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if five == 0: return "false"
            five -= 1
            ten += 1
        else: # 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return "false"
    return "true"

def solver_215(s: str) -> str:
    # Candy Distribution Optimal
    parts = s.strip().split()
    n = int(parts[0])
    ratings = [int(x) for x in parts[1:1+n]]
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return str(sum(candies))

def solver_216(s: str) -> str:
    # Minimum Number of Arrows
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    points = []
    for _ in range(n):
        points.append((int(parts[idx]), int(parts[idx+1])))
        idx += 2
    if not points: return "0"
    points.sort(key=lambda p: p[1])
    arrows = 1
    end = points[0][1]
    for p in points[1:]:
        if p[0] > end:
            arrows += 1
            end = p[1]
    return str(arrows)

def solver_217(s: str) -> str:
    # Non-overlapping Intervals
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    intervals = []
    for _ in range(n):
        intervals.append((int(parts[idx]), int(parts[idx+1])))
        idx += 2
    if not intervals: return "0"
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return str(count)

def solver_218(s: str) -> str:
    # Queue Reconstruction by Height
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    people = []
    for _ in range(n):
        h = int(parts[idx])
        k = int(parts[idx+1])
        people.append((h, k))
        idx += 2
    people.sort(key=lambda p: (-p[0], p[1]))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    res = [f"{p[0]} {p[1]}" for p in queue]
    return " ".join(res)

def solver_219(s: str) -> str:
    # Maximum Subsequence Score
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    idx = 2
    nums1 = [int(x) for x in parts[idx:idx+n]]
    idx += n
    nums2 = [int(x) for x in parts[idx:idx+n]]
    pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
    top_k = []
    total_sum = 0
    ans = 0
    for num1, num2 in pairs:
        heapq.heappush(top_k, num1)
        total_sum += num1
        if len(top_k) > k:
            total_sum -= heapq.heappop(top_k)
        if len(top_k) == k:
            ans = max(ans, total_sum * num2)
    return str(ans)

def solver_220(s: str) -> str:
    # Course Schedule III Max Courses
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    courses = []
    for _ in range(n):
        dur = int(parts[idx])
        last = int(parts[idx+1])
        courses.append((dur, last))
        idx += 2
    courses.sort(key=lambda c: c[1])
    max_heap = []
    total_time = 0
    for dur, last in courses:
        if total_time + dur <= last:
            heapq.heappush(max_heap, -dur)
            total_time += dur
        elif max_heap and -max_heap[0] > dur:
            total_time += dur + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -dur)
    return str(len(max_heap))

PROBLEMS = [
    {
        "index": 201,
        "title_base": "Kth Largest Element in Array",
        "description": "Given an integer array nums and an integer k, return the kth largest element in the array.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print the kth largest integer.",
        "constraints": "1 <= k <= N <= 10^5, -10^4 <= nums[i] <= 10^4",
        "sample_input": "2 6\n3 2 1 5 6 4",
        "sample_output": "5",
        "explanation": "Sorted in descending order: 6, 5, 4, 3, 2, 1. The 2nd largest is 5.",
        "test_inputs": ["4 9\n3 2 3 1 2 4 5 5 6", "1 1\n10"],
        "variant_inputs": ["3 5\n10 20 30 40 50", "2 4\n5 1 9 3"],
        "starter_archetype": "target_and_array",
        "solver": solver_201
    },
    {
        "index": 202,
        "title_base": "Top K Frequent Words",
        "description": "Given an array of strings words and an integer k, return the k most frequent strings sorted by their frequency from highest to lowest. Words with the same frequency are sorted by their lexicographical order.",
        "input_format": "First line contains k and N. Second line contains N words.",
        "output_format": "Print the top k words separated by spaces.",
        "constraints": "1 <= words.length <= 500, 1 <= k <= number of unique words.",
        "sample_input": "2 6\ni love leetcode i love coding",
        "sample_output": "i love",
        "explanation": "'i' and 'love' are the two most frequent words.",
        "test_inputs": ["4 6\nthe day is sunny the the", "1 2\na b"],
        "variant_inputs": ["2 4\ncat dog cat fish", "3 5\na a b b c"],
        "starter_archetype": "general",
        "solver": solver_202
    },
    {
        "index": 203,
        "title_base": "Merge K Sorted Integer Lists",
        "description": "You are given an array of k sorted lists of integers. Merge all the lists into one sorted list using a PriorityQueue.",
        "input_format": "First line contains k. The next k lines each start with count Ni followed by Ni sorted integers.",
        "output_format": "Print the merged sorted integers separated by spaces.",
        "constraints": "0 <= k <= 10^4, total elements <= 10^5",
        "sample_input": "3\n3 1 4 5\n3 1 3 4\n2 2 6",
        "sample_output": "1 1 2 3 4 4 5 6",
        "explanation": "Merging [1, 4, 5], [1, 3, 4], and [2, 6] produces 1 1 2 3 4 4 5 6.",
        "test_inputs": ["2\n2 1 2\n2 3 4", "1\n3 5 10 15"],
        "variant_inputs": ["3\n1 10\n1 20\n1 30", "2\n3 1 5 9\n3 2 6 8"],
        "starter_archetype": "general",
        "solver": solver_203
    },
    {
        "index": 204,
        "title_base": "Find Median from Data Stream",
        "description": "Design a data structure that calculates the median of a stream of numbers. Output the final median formatted to 1 decimal place.",
        "input_format": "First line contains N. Second line contains N numbers.",
        "output_format": "Print the final median with one decimal place.",
        "constraints": "1 <= N <= 5 * 10^4, -10^5 <= num <= 10^5",
        "sample_input": "3\n1 2 3",
        "sample_output": "2.0",
        "explanation": "Median of [1, 2, 3] is 2.0.",
        "test_inputs": ["2\n1 2", "1\n5"],
        "variant_inputs": ["4\n1 3 5 7", "5\n10 20 30 40 50"],
        "starter_archetype": "array",
        "solver": solver_204
    },
    {
        "index": 205,
        "title_base": "Last Stone Weight Simulation",
        "description": "You are given an array of integers stones where stones[i] is the weight of the ith stone. We play a game with the stones: each turn, we choose the heaviest two stones with weights x and y with x <= y. If x == y, both are destroyed. If x != y, stone of weight y - x is left. Return the weight of the last remaining stone, or 0 if none remain.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the weight of the last stone or 0.",
        "constraints": "1 <= stones.length <= 30, 1 <= stones[i] <= 1000",
        "sample_input": "6\n2 7 4 1 8 1",
        "sample_output": "1",
        "explanation": "Smash 7 and 8 -> 1 remaining. Eventually 1 stone of weight 1 remains.",
        "test_inputs": ["1\n1", "2\n2 2"],
        "variant_inputs": ["3\n1 3 5", "4\n10 20 30 40"],
        "starter_archetype": "array",
        "solver": solver_205
    },
    {
        "index": 206,
        "title_base": "K Closest Points to Origin",
        "description": "Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).",
        "input_format": "First line contains k and N. Following lines contain N points (x y).",
        "output_format": "Print the k closest points formatted as x y separated by spaces.",
        "constraints": "1 <= k <= N <= 10^4, -10^4 <= xi, yi <= 10^4",
        "sample_input": "1 2\n1 3\n-2 2",
        "sample_output": "-2 2",
        "explanation": "Distance of (-2, 2) is sqrt(8) < distance of (1, 3) which is sqrt(10).",
        "test_inputs": ["2 3\n3 3\n5 -1\n-2 4", "1 1\n0 0"],
        "variant_inputs": ["2 4\n1 1\n2 2\n3 3\n4 4", "1 2\n2 3\n1 2"],
        "starter_archetype": "general",
        "solver": solver_206
    },
    {
        "index": 207,
        "title_base": "Sort Array by Increasing Frequency",
        "description": "Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the sorted array separated by spaces.",
        "constraints": "1 <= nums.length <= 100, -100 <= nums[i] <= 100",
        "sample_input": "6\n1 1 2 2 2 3",
        "sample_output": "3 1 1 2 2 2",
        "explanation": "'3' has frequency 1, '1' has frequency 2, '2' has frequency 3.",
        "test_inputs": ["6\n2 3 1 3 2", "1\n5"],
        "variant_inputs": ["5\n-1 1 -6 4 5", "4\n1 2 2 3"],
        "starter_archetype": "array",
        "solver": solver_207
    },
    {
        "index": 208,
        "title_base": "Reorganize String No Adjacent",
        "description": "Given a string s, rearrange the characters of s so that any two adjacent characters are not the same. Return any possible rearrangement of s or 'none' if impossible.",
        "input_format": "A single line containing string s.",
        "output_format": "Print the reorganized string or 'none'.",
        "constraints": "1 <= s.length <= 500, s consists of lowercase English letters.",
        "sample_input": "aab",
        "sample_output": "aba",
        "explanation": "'aba' has no adjacent identical characters.",
        "test_inputs": ["aaab", "vvvlo"],
        "variant_inputs": ["abc", "aabbcc"],
        "starter_archetype": "single_string",
        "solver": solver_208
    },
    {
        "index": 209,
        "title_base": "Task Scheduler CPU Cooldown",
        "description": "You are given an array of CPU tasks and an integer n representing cooldown intervals. Return the minimum number of CPU intervals required to complete all tasks.",
        "input_format": "First line contains n and num_tasks. Second line contains space-separated task characters.",
        "output_format": "Print the minimum CPU intervals.",
        "constraints": "1 <= task.length <= 10^4, 0 <= n <= 100",
        "sample_input": "2 6\nA A A B B B",
        "sample_output": "8",
        "explanation": "Execution sequence: A -> B -> idle -> A -> B -> idle -> A -> B (8 units).",
        "test_inputs": ["0 6\nA A A B B B", "2 6\nA A A A A A"],
        "variant_inputs": ["1 4\nA A B B", "2 3\nA B C"],
        "starter_archetype": "general",
        "solver": solver_209
    },
    {
        "index": 210,
        "title_base": "Gas Station Circular Tour",
        "description": "There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.",
        "input_format": "First line contains N. Second line contains N gas amounts. Third line contains N costs.",
        "output_format": "Print starting station index or -1.",
        "constraints": "1 <= N <= 10^5, 0 <= gas[i], cost[i] <= 10^4",
        "sample_input": "5\n1 2 3 4 5\n3 4 5 1 2",
        "sample_output": "3",
        "explanation": "Start at station 3 (index 3). You can complete the circuit.",
        "test_inputs": ["3\n2 3 4\n3 4 3", "1\n2\n2"],
        "variant_inputs": ["4\n1 2 3 4\n2 2 2 2", "2\n3 1\n1 3"],
        "starter_archetype": "general",
        "solver": solver_210
    },
    {
        "index": 211,
        "title_base": "Jump Game Can Reach End",
        "description": "You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return 'true' if you can reach the last index, or 'false' otherwise.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= nums.length <= 10^4, 0 <= nums[i] <= 10^5",
        "sample_input": "5\n2 3 1 1 4",
        "sample_output": "true",
        "explanation": "Jump 1 step from index 0 to 1, then 3 steps to the last index.",
        "test_inputs": ["5\n3 2 1 0 4", "1\n0"],
        "variant_inputs": ["4\n2 0 0 1", "3\n1 2 3"],
        "starter_archetype": "array",
        "solver": solver_211
    },
    {
        "index": 212,
        "title_base": "Jump Game II Minimum Jumps",
        "description": "You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. Return the minimum number of jumps to reach nums[n - 1].",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the minimum number of jumps.",
        "constraints": "1 <= n <= 10^4, 0 <= nums[i] <= 1000",
        "sample_input": "5\n2 3 1 1 4",
        "sample_output": "2",
        "explanation": "Jump from index 0 to 1, then from index 1 to the last index. 2 jumps.",
        "test_inputs": ["5\n2 3 0 1 4", "1\n0"],
        "variant_inputs": ["4\n1 2 1 1", "3\n3 2 1"],
        "starter_archetype": "array",
        "solver": solver_212
    },
    {
        "index": 213,
        "title_base": "Assign Cookies to Children",
        "description": "Assume you are an awesome parent and want to give your children some cookies. Each child i has a greed factor g[i], and each cookie j has a size s[j]. Maximize the number of your content children.",
        "input_format": "First line contains N and M. Second line contains N greed values. Third line contains M cookie sizes.",
        "output_format": "Print the number of content children.",
        "constraints": "1 <= N, M <= 3 * 10^4, 1 <= g[i], s[j] <= 2^31 - 1",
        "sample_input": "3 2\n1 2 3\n1 1",
        "sample_output": "1",
        "explanation": "Only child with greed factor 1 can be content.",
        "test_inputs": ["2 3\n1 2\n1 2 3", "1 1\n2\n1"],
        "variant_inputs": ["3 3\n1 2 3\n3 2 1", "2 2\n3 4\n4 5"],
        "starter_archetype": "general",
        "solver": solver_213
    },
    {
        "index": 214,
        "title_base": "Lemonade Change Register",
        "description": "At a lemonade stand, each lemonade costs $5. Customers pay with a $5, $10, or $20 bill. Return 'true' if you can provide every customer with correct change, or 'false' otherwise.",
        "input_format": "First line contains N. Second line contains N bill values.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= bills.length <= 10^5, bills[i] is either 5, 10, or 20.",
        "sample_input": "5\n5 5 5 10 20",
        "sample_output": "true",
        "explanation": "All customers receive exact change.",
        "test_inputs": ["5\n5 5 10 10 20", "1\n5"],
        "variant_inputs": ["4\n5 10 5 20", "3\n10 10 10"],
        "starter_archetype": "array",
        "solver": solver_214
    },
    {
        "index": 215,
        "title_base": "Candy Distribution Optimal",
        "description": "There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings. Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. Return the minimum number of candies you need to distribute.",
        "input_format": "First line contains N. Second line contains N ratings.",
        "output_format": "Print the minimum candies.",
        "constraints": "n == ratings.length, 1 <= n <= 2 * 10^4, 0 <= ratings[i] <= 2 * 10^4",
        "sample_input": "3\n1 0 2",
        "sample_output": "5",
        "explanation": "Distribute candies [2, 1, 2] summing to 5.",
        "test_inputs": ["3\n1 2 2", "1\n10"],
        "variant_inputs": ["4\n1 3 2 1", "5\n1 2 3 4 5"],
        "starter_archetype": "array",
        "solver": solver_215
    },
    {
        "index": 216,
        "title_base": "Minimum Number of Arrows",
        "description": "There are some spherical balloons taped onto a flat wall. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]. Arrows can be shot vertically from points along the x-axis. Return the minimum number of arrows that must be shot to burst all balloons.",
        "input_format": "First line contains N. Following lines contain N interval pairs.",
        "output_format": "Print the minimum arrows.",
        "constraints": "1 <= points.length <= 10^5, points[i].length == 2",
        "sample_input": "4\n10 16\n2 8\n1 6\n7 12",
        "sample_output": "2",
        "explanation": "Shoot arrow at x = 6 (bursts [2,8] and [1,6]) and x = 11 (bursts [10,16] and [7,12]).",
        "test_inputs": ["4\n1 2\n3 4\n5 6\n7 8", "1\n1 2"],
        "variant_inputs": ["3\n1 5\n2 6\n3 7", "2\n1 10\n2 5"],
        "starter_archetype": "general",
        "solver": solver_216
    },
    {
        "index": 217,
        "title_base": "Non-overlapping Intervals",
        "description": "Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.",
        "input_format": "First line contains N. Following lines contain N interval pairs.",
        "output_format": "Print the minimum removals.",
        "constraints": "1 <= intervals.length <= 10^5, intervals[i].length == 2",
        "sample_input": "4\n1 2\n2 3\n3 4\n1 3",
        "sample_output": "1",
        "explanation": "[1,3] can be removed and the rest are non-overlapping.",
        "test_inputs": ["3\n1 2\n1 2\n1 2", "2\n1 2\n2 3"],
        "variant_inputs": ["3\n1 4\n2 5\n3 6", "1\n1 5"],
        "starter_archetype": "general",
        "solver": solver_217
    },
    {
        "index": 218,
        "title_base": "Queue Reconstruction by Height",
        "description": "You are given an array of people, people, which are the attributes of some people in a queue. Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi. Reconstruct the queue.",
        "input_format": "First line contains N. Following lines contain N pairs (h k).",
        "output_format": "Print the reconstructed queue pairs separated by spaces.",
        "constraints": "1 <= people.length <= 2000, 0 <= hi <= 10^6, 0 <= ki < people.length",
        "sample_input": "6\n7 0\n4 4\n7 1\n5 0\n6 1\n5 2",
        "sample_output": "5 0 7 0 5 2 6 1 4 4 7 1",
        "explanation": "Valid reconstructed queue satisfying all height constraints.",
        "test_inputs": ["2\n6 0\n5 0", "1\n1 0"],
        "variant_inputs": ["3\n2 0\n1 1\n3 0", "2\n4 0\n5 0"],
        "starter_archetype": "general",
        "solver": solver_218
    },
    {
        "index": 219,
        "title_base": "Maximum Subsequence Score",
        "description": "You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices of length k. The score is the sum of selected nums1 multiplied by the minimum selected nums2. Return the maximum possible score.",
        "input_format": "First line contains k and N. Second line contains N integers of nums1. Third line contains N integers of nums2.",
        "output_format": "Print the maximum score.",
        "constraints": "n == nums1.length == nums2.length, 1 <= n <= 10^5, 1 <= k <= n",
        "sample_input": "3 4\n1 3 3 2\n2 1 3 4",
        "sample_output": "12",
        "explanation": "Choose indices 0, 2, 3: (1 + 3 + 2) * min(2, 3, 4) = 6 * 2 = 12.",
        "test_inputs": ["1 3\n4 2 3\n1 2 3", "2 2\n1 1\n1 1"],
        "variant_inputs": ["2 3\n2 1 14\n11 4 3", "3 3\n1 2 3\n3 2 1"],
        "starter_archetype": "general",
        "solver": solver_219
    },
    {
        "index": 220,
        "title_base": "Course Schedule III Max Courses",
        "description": "There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi]. You will take courses one at a time and course i must be completed on or before lastDayi. Return the maximum number of courses that you can take.",
        "input_format": "First line contains N. Following lines contain N pairs (duration lastDay).",
        "output_format": "Print the maximum courses.",
        "constraints": "1 <= courses.length <= 10^4, 1 <= durationi, lastDayi <= 10^4",
        "sample_input": "4\n100 200\n200 1300\n1000 1250\n2000 3200",
        "sample_output": "3",
        "explanation": "You can take courses 1, 2, and 3 (3 courses in total).",
        "test_inputs": ["1\n1 2", "3\n3 2\n4 3\n2 1"],
        "variant_inputs": ["2\n100 200\n100 200", "3\n5 5\n4 6\n2 6"],
        "starter_archetype": "general",
        "solver": solver_220
    }
]
