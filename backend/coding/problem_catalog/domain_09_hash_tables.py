# Domain 09: JavaScript - Hash Table & Maps (Problems 161 - 180)
from collections import Counter, defaultdict

def solver_161(s: str) -> str:
    # Two Sum Hash Lookup
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return f"{seen[diff]} {i}"
        seen[num] = i
    return "-1 -1"

def solver_162(s: str) -> str:
    # First Unique Character
    word = s.strip().split()[0]
    count = Counter(word)
    for i, ch in enumerate(word):
        if count[ch] == 1:
            return str(i)
    return "-1"

def solver_163(s: str) -> str:
    # Intersection of Two Arrays
    parts = s.strip().split()
    n = int(parts[0])
    m = int(parts[1])
    idx = 2
    a = set(int(x) for x in parts[idx:idx+n])
    idx += n
    b = set(int(x) for x in parts[idx:idx+m])
    inter = sorted(a & b)
    return " ".join(str(x) for x in inter)

def solver_164(s: str) -> str:
    # Happy Number Cycle
    n = int(s.strip().split()[0])
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return "true" if n == 1 else "false"

def solver_165(s: str) -> str:
    # Word Pattern Matching
    lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
    if len(lines) == 1:
        parts = lines[0].split()
        pattern = parts[0]
        words = parts[1:]
    else:
        pattern = lines[0].strip()
        words = lines[1].strip().split()
    if len(pattern) != len(words):
        return "false"
    p_to_w = {}
    w_to_p = {}
    for p, w in zip(pattern, words):
        if p in p_to_w and p_to_w[p] != w: return "false"
        if w in w_to_p and w_to_p[w] != p: return "false"
        p_to_w[p] = w
        w_to_p[w] = p
    return "true"

def solver_166(s: str) -> str:
    # Subarray Sum Equals K
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    count = 0
    cur_sum = 0
    prefix_counts = {0: 1}
    for x in nums:
        cur_sum += x
        count += prefix_counts.get(cur_sum - k, 0)
        prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1
    return str(count)

def solver_167(s: str) -> str:
    # Longest Consecutive Sequence
    parts = s.strip().split()
    n = int(parts[0])
    nums = set(int(x) for x in parts[1:1+n])
    max_streak = 0
    for num in nums:
        if num - 1 not in nums:
            cur_num = num
            cur_streak = 1
            while cur_num + 1 in nums:
                cur_num += 1
                cur_streak += 1
            max_streak = max(max_streak, cur_streak)
    return str(max_streak)

def solver_168(s: str) -> str:
    # Top K Frequent Elements
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    counts = Counter(nums)
    top = [str(item[0]) for item in counts.most_common(k)]
    return " ".join(top)

def solver_169(s: str) -> str:
    # Sort Characters by Frequency
    word = s.strip().split()[0]
    counts = Counter(word)
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return "".join(ch * cnt for ch, cnt in sorted_chars)

def solver_170(s: str) -> str:
    # Four Sum Quadruplets (count of unique quadruplets)
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    nums = sorted(int(x) for x in parts[2:2+n])
    quads = set()
    L = len(nums)
    for i in range(L - 3):
        for j in range(i + 1, L - 2):
            left, right = j + 1, L - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    quads.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return str(len(quads))

def solver_171(s: str) -> str:
    # Contiguous Array Zero One Balance
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    max_len = 0
    cur = 0
    first_seen = {0: -1}
    for i, x in enumerate(nums):
        cur += 1 if x == 1 else -1
        if cur in first_seen:
            max_len = max(max_len, i - first_seen[cur])
        else:
            first_seen[cur] = i
    return str(max_len)

def solver_172(s: str) -> str:
    # Brick Wall Least Cuts
    parts = s.strip().split()
    num_rows = int(parts[0])
    idx = 1
    gap_counts = defaultdict(int)
    for _ in range(num_rows):
        k = int(parts[idx])
        idx += 1
        pos = 0
        row_bricks = [int(x) for x in parts[idx:idx+k]]
        idx += k
        for b in row_bricks[:-1]:
            pos += b
            gap_counts[pos] += 1
    max_gaps = max(gap_counts.values()) if gap_counts else 0
    return str(num_rows - max_gaps)

def solver_173(s: str) -> str:
    # Insert Delete GetRandom O(1)
    parts = s.strip().split()
    num_ops = int(parts[0])
    idx = 1
    s_set = set()
    res = []
    for _ in range(num_ops):
        op = parts[idx]
        val = int(parts[idx+1])
        idx += 2
        if op == "insert":
            if val not in s_set:
                s_set.add(val)
                res.append("true")
            else:
                res.append("false")
        elif op == "remove":
            if val in s_set:
                s_set.remove(val)
                res.append("true")
            else:
                res.append("false")
    return " ".join(res)

def solver_174(s: str) -> str:
    # Insert Delete GetRandom Duplicates
    parts = s.strip().split()
    num_ops = int(parts[0])
    idx = 1
    counts = Counter()
    res = []
    for _ in range(num_ops):
        op = parts[idx]
        val = int(parts[idx+1])
        idx += 2
        if op == "insert":
            not_present = (counts[val] == 0)
            counts[val] += 1
            res.append("true" if not_present else "false")
        elif op == "remove":
            if counts[val] > 0:
                counts[val] -= 1
                res.append("true")
            else:
                res.append("false")
    return " ".join(res)

def solver_175(s: str) -> str:
    # All O`one Data Structure
    parts = s.strip().split()
    num_ops = int(parts[0])
    idx = 1
    counts = Counter()
    res = []
    for _ in range(num_ops):
        op = parts[idx]
        idx += 1
        if op == "inc":
            key = parts[idx]
            idx += 1
            counts[key] += 1
        elif op == "dec":
            key = parts[idx]
            idx += 1
            counts[key] -= 1
            if counts[key] <= 0:
                del counts[key]
        elif op == "getMaxKey":
            if not counts:
                res.append('""')
            else:
                max_val = max(counts.values())
                keys = [k for k, v in counts.items() if v == max_val]
                res.append(sorted(keys)[0])
        elif op == "getMinKey":
            if not counts:
                res.append('""')
            else:
                min_val = min(counts.values())
                keys = [k for k, v in counts.items() if v == min_val]
                res.append(sorted(keys)[0])
    return " ".join(res)

def solver_176(s: str) -> str:
    # LRU Cache Architecture
    from collections import OrderedDict
    parts = s.strip().split()
    cap = int(parts[0])
    num_ops = int(parts[1])
    idx = 2
    cache = OrderedDict()
    res = []
    for _ in range(num_ops):
        op = parts[idx]
        idx += 1
        if op == "put":
            k = int(parts[idx])
            v = int(parts[idx+1])
            idx += 2
            if k in cache:
                cache.move_to_end(k)
            cache[k] = v
            if len(cache) > cap:
                cache.popitem(last=False)
        elif op == "get":
            k = int(parts[idx])
            idx += 1
            if k in cache:
                cache.move_to_end(k)
                res.append(str(cache[k]))
            else:
                res.append("-1")
    return " ".join(res)

def solver_177(s: str) -> str:
    # LFU Cache Architecture
    parts = s.strip().split()
    cap = int(parts[0])
    num_ops = int(parts[1])
    idx = 2
    # Simple simulation
    val_map = {}
    freq_map = {}
    time_map = {}
    timer = 0
    res = []
    for _ in range(num_ops):
        op = parts[idx]
        idx += 1
        timer += 1
        if op == "put":
            k = int(parts[idx])
            v = int(parts[idx+1])
            idx += 2
            if cap <= 0: continue
            if k in val_map:
                val_map[k] = v
                freq_map[k] += 1
                time_map[k] = timer
            else:
                if len(val_map) >= cap:
                    # Evict min freq, then min time
                    lfu_key = min(val_map.keys(), key=lambda x: (freq_map[x], time_map[x]))
                    del val_map[lfu_key]
                    del freq_map[lfu_key]
                    del time_map[lfu_key]
                val_map[k] = v
                freq_map[k] = 1
                time_map[k] = timer
        elif op == "get":
            k = int(parts[idx])
            idx += 1
            if k in val_map:
                freq_map[k] += 1
                time_map[k] = timer
                res.append(str(val_map[k]))
            else:
                res.append("-1")
    return " ".join(res)

def solver_178(s: str) -> str:
    # Contains Duplicate Check
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    return "true" if len(nums) != len(set(nums)) else "false"

def solver_179(s: str) -> str:
    # Contains Duplicate II Distance
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    last_idx = {}
    for i, x in enumerate(nums):
        if x in last_idx and i - last_idx[x] <= k:
            return "true"
        last_idx[x] = i
    return "false"

def solver_180(s: str) -> str:
    # Subarray Product Less Than K
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    if k <= 1: return "0"
    prod = 1
    left = 0
    ans = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k and left <= right:
            prod //= nums[left]
            left += 1
        ans += right - left + 1
    return str(ans)

PROBLEMS = [
    {
        "index": 161,
        "title_base": "Two Sum Hash Lookup",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target using a one-pass hash map.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print the 0-based indices separated by a space.",
        "constraints": "2 <= N <= 10^4, -10^9 <= nums[i] <= 10^9",
        "sample_input": "9 4\n2 7 11 15",
        "sample_output": "0 1",
        "explanation": "nums[0] + nums[1] == 9, we return 0 1.",
        "test_inputs": ["6 3\n3 2 4", "6 2\n3 3"],
        "variant_inputs": ["10 4\n1 2 8 9", "7 3\n1 4 6"],
        "starter_archetype": "target_and_array",
        "solver": solver_161
    },
    {
        "index": 162,
        "title_base": "First Unique Character",
        "description": "Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.",
        "input_format": "A single line containing string s.",
        "output_format": "Print the 0-based index or -1.",
        "constraints": "1 <= s.length <= 10^5, s consists of only lowercase English letters.",
        "sample_input": "leetcode",
        "sample_output": "0",
        "explanation": "The character 'l' at index 0 is the first non-repeating character.",
        "test_inputs": ["loveleetcode", "aabb"],
        "variant_inputs": ["swiss", "programming"],
        "starter_archetype": "single_string",
        "solver": solver_162
    },
    {
        "index": 163,
        "title_base": "Intersection of Two Arrays",
        "description": "Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and returned in sorted order.",
        "input_format": "First line contains N and M. Second line contains N integers. Third line contains M integers.",
        "output_format": "Print the unique intersection values in sorted order separated by spaces.",
        "constraints": "1 <= N, M <= 1000, 0 <= nums1[i], nums2[i] <= 1000",
        "sample_input": "4 2\n1 2 2 1\n2 2",
        "sample_output": "2",
        "explanation": "The only element in both arrays is 2.",
        "test_inputs": ["3 5\n4 9 5\n9 4 9 8 4", "2 2\n1 2\n2 3"],
        "variant_inputs": ["3 3\n1 2 3\n2 3 4", "4 4\n10 20 30 40\n20 40 60 80"],
        "starter_archetype": "general",
        "solver": solver_163
    },
    {
        "index": 164,
        "title_base": "Happy Number Cycle",
        "description": "Write an algorithm to determine if a number n is happy. A happy number reaches 1 when repeatedly replaced by the sum of the squares of its digits.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= n <= 2^31 - 1",
        "sample_input": "19",
        "sample_output": "true",
        "explanation": "1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> 6^2 + 8^2 = 100 -> 1^2 + 0^2 + 0^2 = 1.",
        "test_inputs": ["2", "7"],
        "variant_inputs": ["1", "4"],
        "starter_archetype": "single_number",
        "solver": solver_164
    },
    {
        "index": 165,
        "title_base": "Word Pattern Matching",
        "description": "Given a pattern and a string s, find if s follows the same pattern where each letter corresponds to a full word in a bijection.",
        "input_format": "First line contains pattern. Second line contains space-separated words of s.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= pattern.length <= 300, 1 <= s.length <= 3000",
        "sample_input": "abba\ndog cat cat dog",
        "sample_output": "true",
        "explanation": "'a' maps to 'dog' and 'b' maps to 'cat'.",
        "test_inputs": ["abba\ndog cat cat fish", "aaaa\ndog cat cat dog"],
        "variant_inputs": ["abc\napple banana orange", "ab\ncat dog"],
        "starter_archetype": "general",
        "solver": solver_165
    },
    {
        "index": 166,
        "title_base": "Subarray Sum Equals K",
        "description": "Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print the number of subarrays.",
        "constraints": "1 <= N <= 2 * 10^4, -1000 <= nums[i] <= 1000, -10^7 <= k <= 10^7",
        "sample_input": "2 3\n1 1 1",
        "sample_output": "2",
        "explanation": "[1, 1] at indices 0..1 and 1..2 both sum to 2.",
        "test_inputs": ["3 3\n1 2 3", "0 2\n1 -1"],
        "variant_inputs": ["5 4\n2 3 -1 1", "4 4\n1 3 2 2"],
        "starter_archetype": "target_and_array",
        "solver": solver_166
    },
    {
        "index": 167,
        "title_base": "Longest Consecutive Sequence",
        "description": "Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence in O(n) time.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the length of the longest consecutive sequence.",
        "constraints": "0 <= N <= 10^5, -10^9 <= nums[i] <= 10^9",
        "sample_input": "6\n100 4 200 1 3 2",
        "sample_output": "4",
        "explanation": "The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.",
        "test_inputs": ["10\n0 3 7 2 5 8 4 6 0 1", "1\n5"],
        "variant_inputs": ["5\n10 20 30 40 50", "4\n1 2 3 4"],
        "starter_archetype": "array",
        "solver": solver_167
    },
    {
        "index": 168,
        "title_base": "Top K Frequent Elements",
        "description": "Given an integer array nums and an integer k, return the k most frequent elements in descending order of frequency.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print the k most frequent elements separated by spaces.",
        "constraints": "1 <= N <= 10^5, k is in the range [1, the number of unique elements in the array].",
        "sample_input": "2 6\n1 1 1 2 2 3",
        "sample_output": "1 2",
        "explanation": "1 appears 3 times, 2 appears 2 times. The top 2 elements are 1 and 2.",
        "test_inputs": ["1 1\n1", "1 3\n4 4 2"],
        "variant_inputs": ["2 5\n10 10 20 20 30", "3 6\n5 5 5 4 4 3"],
        "starter_archetype": "target_and_array",
        "solver": solver_168
    },
    {
        "index": 169,
        "title_base": "Sort Characters by Frequency",
        "description": "Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.",
        "input_format": "A single line containing string s.",
        "output_format": "Print the sorted string.",
        "constraints": "1 <= s.length <= 5 * 10^5, s consists of uppercase and lowercase English letters and digits.",
        "sample_input": "tree",
        "sample_output": "eert",
        "explanation": "'e' appears twice, while 'r' and 't' each appear once.",
        "test_inputs": ["cccaaa", "Aabb"],
        "variant_inputs": ["banana", "mississippi"],
        "starter_archetype": "single_string",
        "solver": solver_169
    },
    {
        "index": 170,
        "title_base": "Four Sum Quadruplets",
        "description": "Given an array nums of n integers, return the count of all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that they sum to target.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print the number of unique quadruplets.",
        "constraints": "1 <= N <= 200, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9",
        "sample_input": "0 6\n1 0 -1 0 -2 2",
        "sample_output": "3",
        "explanation": "Unique quadruplets: [-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]. Total = 3.",
        "test_inputs": ["8 5\n2 2 2 2 2", "0 4\n1 2 3 4"],
        "variant_inputs": ["4 4\n1 1 1 1", "0 5\n-2 -1 0 1 2"],
        "starter_archetype": "target_and_array",
        "solver": solver_170
    },
    {
        "index": 171,
        "title_base": "Contiguous Array Zero One Balance",
        "description": "Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.",
        "input_format": "First line contains N. Second line contains N binary digits (0 or 1).",
        "output_format": "Print the maximum length.",
        "constraints": "1 <= N <= 10^5, nums[i] is either 0 or 1.",
        "sample_input": "2\n0 1",
        "sample_output": "2",
        "explanation": "[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.",
        "test_inputs": ["4\n0 1 0 1", "3\n0 0 0"],
        "variant_inputs": ["6\n0 1 1 0 1 1", "5\n0 0 1 1 0"],
        "starter_archetype": "array",
        "solver": solver_171
    },
    {
        "index": 172,
        "title_base": "Brick Wall Least Cuts",
        "description": "There is a rectangular brick wall made of several rows of bricks. Given the brick widths row by row, draw a vertical line from top to bottom that crosses the least number of bricks. Return the minimum number of crossed bricks.",
        "input_format": "First line contains numRows. Each following row starts with brick count k followed by k brick widths.",
        "output_format": "Print the minimum number of crossed bricks.",
        "constraints": "1 <= wall.length <= 10^4, 1 <= wall[i].length <= 10^4",
        "sample_input": "6\n4 1 2 2 1\n3 3 1 2\n3 1 3 2\n2 2 4\n3 3 1 2\n4 1 3 1 1",
        "sample_output": "2",
        "explanation": "Drawing the line at position 4 cuts through only 2 bricks.",
        "test_inputs": ["1\n1 1", "2\n1 3\n1 3"],
        "variant_inputs": ["2\n2 1 2\n2 2 1", "3\n2 2 2\n2 2 2\n2 2 2"],
        "starter_archetype": "general",
        "solver": solver_172
    },
    {
        "index": 173,
        "title_base": "Insert Delete GetRandom O(1)",
        "description": "Implement the RandomizedSet class supporting insert and remove in average O(1) time. For each operation, return 'true' if the set was modified, or 'false' otherwise.",
        "input_format": "First line contains num_ops. Next num_ops pairs contain operation ('insert' or 'remove') and integer value.",
        "output_format": "Print operation results separated by spaces.",
        "constraints": "1 <= num_ops <= 1000",
        "sample_input": "3\ninsert 1\nremove 2\ninsert 2",
        "sample_output": "true false true",
        "explanation": "insert 1 -> true; remove 2 (not found) -> false; insert 2 -> true.",
        "test_inputs": ["2\ninsert 5\ninsert 5", "2\nremove 1\ninsert 1"],
        "variant_inputs": ["4\ninsert 1\ninsert 2\nremove 1\ninsert 1", "2\ninsert 10\nremove 10"],
        "starter_archetype": "general",
        "solver": solver_173
    },
    {
        "index": 174,
        "title_base": "Insert Delete GetRandom Duplicates",
        "description": "Implement the RandomizedCollection class supporting duplicates. Insert returns 'true' if the item was not already present, 'false' if it was. Remove returns 'true' if the item was present, 'false' if not.",
        "input_format": "First line contains num_ops. Following lines contain operation ('insert' or 'remove') and value.",
        "output_format": "Print operation results separated by spaces.",
        "constraints": "1 <= num_ops <= 1000",
        "sample_input": "4\ninsert 1\ninsert 1\ninsert 2\nremove 1",
        "sample_output": "true false true true",
        "explanation": "1 inserted (new) -> true; 1 inserted (duplicate) -> false; 2 inserted -> true; 1 removed -> true.",
        "test_inputs": ["2\ninsert 1\nremove 2", "2\nremove 5\ninsert 5"],
        "variant_inputs": ["3\ninsert 10\ninsert 10\nremove 10", "2\ninsert 7\ninsert 7"],
        "starter_archetype": "general",
        "solver": solver_174
    },
    {
        "index": 175,
        "title_base": "All O`one Data Structure",
        "description": "Design a data structure to store strings' count with the ability to return strings with minimum and maximum counts.",
        "input_format": "First line contains num_ops. Following lines contain commands (inc key, dec key, getMaxKey, getMinKey).",
        "output_format": "Print the outputs of get operations separated by spaces.",
        "constraints": "1 <= num_ops <= 1000",
        "sample_input": "5\ninc hello\ninc hello\ngetMaxKey\ngetMinKey\ninc leet",
        "sample_output": "hello hello",
        "explanation": "Max key is 'hello', min key is 'hello'.",
        "test_inputs": ["3\ninc a\ngetMaxKey\ngetMinKey", "2\ngetMaxKey\ngetMinKey"],
        "variant_inputs": ["4\ninc a\ninc b\ninc b\ngetMaxKey", "4\ninc x\ninc y\ngetMinKey\ngetMaxKey"],
        "starter_archetype": "general",
        "solver": solver_175
    },
    {
        "index": 176,
        "title_base": "LRU Cache Architecture",
        "description": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.",
        "input_format": "First line contains capacity and num_ops. Following lines contain 'put k v' or 'get k'.",
        "output_format": "Print the results of get operations separated by spaces.",
        "constraints": "1 <= capacity <= 3000, 1 <= num_ops <= 10^4",
        "sample_input": "2 6\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2\nget 3",
        "sample_output": "1 -1 3",
        "explanation": "get(1) returns 1; put(3,3) evicts key 2; get(2) returns -1; get(3) returns 3.",
        "test_inputs": ["1 3\nput 1 10\nget 1\nget 2", "2 2\nget 1\nget 2"],
        "variant_inputs": ["2 4\nput 1 1\nput 2 2\nput 1 10\nget 1", "3 4\nput 1 1\nput 2 2\nput 3 3\nget 2"],
        "starter_archetype": "general",
        "solver": solver_176
    },
    {
        "index": 177,
        "title_base": "LFU Cache Architecture",
        "description": "Design and implement a data structure for a Least Frequently Used (LFU) cache.",
        "input_format": "First line contains capacity and num_ops. Following lines contain 'put k v' or 'get k'.",
        "output_format": "Print the results of get operations separated by spaces.",
        "constraints": "1 <= capacity <= 10^4, 0 <= num_ops <= 10^4",
        "sample_input": "2 6\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2\nget 3",
        "sample_output": "1 -1 3",
        "explanation": "Key 1 frequency is 2. Key 2 frequency is 1, so key 2 is evicted on put(3,3).",
        "test_inputs": ["1 3\nput 1 5\nget 1\nget 2", "2 2\nget 1\nget 2"],
        "variant_inputs": ["2 4\nput 1 10\nput 2 20\nget 1\nget 2", "3 4\nput 1 1\nput 2 2\nput 3 3\nget 1"],
        "starter_archetype": "general",
        "solver": solver_177
    },
    {
        "index": 178,
        "title_base": "Contains Duplicate Check",
        "description": "Given an integer array nums, return 'true' if any value appears at least twice in the array, and return 'false' if every element is distinct.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= N <= 10^5, -10^9 <= nums[i] <= 10^9",
        "sample_input": "4\n1 2 3 1",
        "sample_output": "true",
        "explanation": "1 appears twice.",
        "test_inputs": ["4\n1 2 3 4", "10\n1 1 1 3 3 4 3 2 4 2"],
        "variant_inputs": ["5\n10 20 30 40 50", "3\n5 5 5"],
        "starter_archetype": "array",
        "solver": solver_178
    },
    {
        "index": 179,
        "title_base": "Contains Duplicate II Distance",
        "description": "Given an integer array nums and an integer k, return 'true' if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= N <= 10^5, 0 <= k <= 10^5",
        "sample_input": "3 4\n1 2 3 1",
        "sample_output": "true",
        "explanation": "nums[0] == nums[3] and abs(0 - 3) = 3 <= 3.",
        "test_inputs": ["1 4\n1 0 1 1", "2 6\n1 2 3 1 2 3"],
        "variant_inputs": ["2 4\n1 2 3 1", "3 5\n1 2 3 4 5"],
        "starter_archetype": "target_and_array",
        "solver": solver_179
    },
    {
        "index": 180,
        "title_base": "Subarray Product Less Than K",
        "description": "Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print the number of subarrays.",
        "constraints": "1 <= N <= 3 * 10^4, 1 <= nums[i] <= 1000, 0 <= k <= 10^6",
        "sample_input": "100 4\n10 5 2 6",
        "sample_output": "8",
        "explanation": "The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].",
        "test_inputs": ["0 3\n1 2 3", "1 2\n1 2"],
        "variant_inputs": ["50 3\n10 5 2", "10 3\n2 3 4"],
        "starter_archetype": "target_and_array",
        "solver": solver_180
    }
]
