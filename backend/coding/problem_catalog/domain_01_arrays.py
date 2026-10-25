"""
Domain 1: Algorithms - Array & Math (20 problems)
"""

def solve_two_sum(s):
    toks = s.strip().split()
    if not toks: return ""
    target, n = int(toks[0]), int(toks[1])
    nums = [int(x) for x in toks[2:2+n]]
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return f"{seen[target - x]} {i}"
        seen[x] = i
    return "-1 -1"

def solve_prefix_sum(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    L = int(toks[1+n])
    R = int(toks[2+n])
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + nums[i]
    return str(pref[R+1] - pref[L])

def solve_max_subarray(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    max_so_far = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        max_so_far = max(max_so_far, cur)
    return str(max_so_far)

def solve_rotate_array(s):
    toks = s.strip().split()
    if not toks: return ""
    k = int(toks[0])
    n = int(toks[1])
    nums = [int(x) for x in toks[2:2+n]]
    k = k % n if n else 0
    rotated = nums[-k:] + nums[:-k] if k else nums
    return " ".join(map(str, rotated))

def solve_product_except_self(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return " ".join(map(str, res))

def solve_majority_element(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    cand, count = None, 0
    for x in nums:
        if count == 0:
            cand = x
            count = 1
        elif x == cand:
            count += 1
        else:
            count -= 1
    return str(cand)

def solve_missing_positive(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    st = set(nums)
    i = 1
    while i in st:
        i += 1
    return str(i)

def solve_trapping_rain(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    h = [int(x) for x in toks[1:1+n]]
    if n < 3: return "0"
    l, r = 0, n - 1
    l_max, r_max = h[l], h[r]
    ans = 0
    while l < r:
        if l_max < r_max:
            l += 1
            l_max = max(l_max, h[l])
            ans += max(0, l_max - h[l])
        else:
            r -= 1
            r_max = max(r_max, h[r])
            ans += max(0, r_max - h[r])
    return str(ans)

def solve_merge_sorted(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    a = [int(x) for x in toks[1:1+n]]
    m = int(toks[1+n])
    b = [int(x) for x in toks[2+n:2+n+m]]
    res = sorted(a + b)
    return " ".join(map(str, res))

def solve_sort_parity(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return " ".join(map(str, evens + odds))

def solve_partition_three(s):
    toks = s.strip().split()
    if not toks: return "false"
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    total = sum(nums)
    if total % 3 != 0: return "false"
    target = total // 3
    count, cur = 0, 0
    for x in nums[:-1]:
        cur += x
        if cur == target:
            count += 1
            cur = 0
            if count == 2:
                return "true"
    return "true" if count >= 2 else "false"

def solve_continuous_subarray_sum(s):
    toks = s.strip().split()
    if not toks: return "false"
    k = int(toks[0])
    n = int(toks[1])
    nums = [int(x) for x in toks[2:2+n]]
    rem_map = {0: -1}
    cur = 0
    for i, x in enumerate(nums):
        cur += x
        rem = cur % k if k != 0 else cur
        if rem in rem_map:
            if i - rem_map[rem] >= 2:
                return "true"
        else:
            rem_map[rem] = i
    return "false"

def solve_max_chunks_sorted(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    chunks, mx = 0, 0
    for i, x in enumerate(nums):
        mx = max(mx, x)
        if mx == i:
            chunks += 1
    return str(chunks)

def solve_first_missing_ap(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    nums = [int(x) for x in toks[1:1+n]]
    diff = (nums[-1] - nums[0]) // n
    for i in range(n - 1):
        if nums[i+1] - nums[i] != diff:
            return str(nums[i] + diff)
    return str(nums[-1] + diff)

def solve_stock_single(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    p = [int(x) for x in toks[1:1+n]]
    min_p, max_prof = float('inf'), 0
    for x in p:
        min_p = min(min_p, x)
        max_prof = max(max_prof, x - min_p)
    return str(max_prof)

def solve_stock_unlimited(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    p = [int(x) for x in toks[1:1+n]]
    ans = 0
    for i in range(1, n):
        if p[i] > p[i-1]:
            ans += p[i] - p[i-1]
    return str(ans)

def solve_stock_cooldown(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    p = [int(x) for x in toks[1:1+n]]
    if n <= 1: return "0"
    sold, held, reset = 0, -p[0], 0
    for x in p[1:]:
        prev_sold = sold
        sold = held + x
        held = max(held, reset - x)
        reset = max(reset, prev_sold)
    return str(max(sold, reset))

def solve_stock_fee(s):
    toks = s.strip().split()
    if not toks: return "0"
    fee = int(toks[0])
    n = int(toks[1])
    p = [int(x) for x in toks[2:2+n]]
    cash, hold = 0, -p[0]
    for x in p[1:]:
        cash = max(cash, hold + x - fee)
        hold = max(hold, cash - x)
    return str(cash)

def solve_max_gap(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    nums = sorted([int(x) for x in toks[1:1+n]])
    if n < 2: return "0"
    mx = max(nums[i] - nums[i-1] for i in range(1, n))
    return str(mx)

def solve_largest_rectangle(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    h = [int(x) for x in toks[1:1+n]]
    stack = []
    max_area = 0
    for i, x in enumerate(h + [0]):
        while stack and (i == n or h[stack[-1]] >= x):
            height = h[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return str(max_area)

PROBLEMS = [
    {
        "title_base": "Two Sum Variant",
        "description": "Given an array of integers and a target sum, return the 0-based indices of the two numbers such that they add up to the target.",
        "input_format": "Line 1: Target sum\nLine 2: An integer N representing the array size\nLine 3: N space-separated integers",
        "output_format": "Output two space-separated indices (e.g. '0 1').",
        "constraints": "2 <= N <= 10^5\n-10^9 <= target, nums[i] <= 10^9",
        "io_type": "target_and_array",
        "starter_archetype": "target_and_array",
        "sample_input": "9\n4\n2 7 11 15",
        "sample_output": "0 1",
        "explanation": "nums[0] + nums[1] = 2 + 7 = 9, so the indices are 0 1.",
        "test_inputs": [
            "9\n4\n2 7 11 15",
            "6\n3\n3 2 4",
            "10\n4\n1 2 5 8",
            "0\n3\n-3 4 3"
        ],
        "variant_inputs": [
            "100\n4\n15 20 35 80",
            "-5\n4\n-10 5 1 2",
            "50\n4\n25 15 25 35",
            "0\n2\n0 0"
        ],
        "solver": solve_two_sum
    },
    {
        "title_base": "Prefix Sum Queries",
        "description": "Given an array of N integers and range indices L and R (0-indexed), compute the sum of elements from index L to R inclusive in O(1) query time.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers\nLine 3: Two integers L and R",
        "output_format": "Output the range sum as a single integer.",
        "constraints": "1 <= N <= 10^5\n0 <= L <= R < N\n-10^9 <= nums[i] <= 10^9",
        "io_type": "general",
        "sample_input": "5\n1 2 3 4 5\n1 3",
        "sample_output": "9",
        "explanation": "Sum from index 1 to 3 is 2 + 3 + 4 = 9.",
        "test_inputs": [
            "5\n1 2 3 4 5\n1 3",
            "4\n10 20 30 40\n0 3",
            "3\n-5 10 -2\n0 1",
            "1\n42\n0 0"
        ],
        "variant_inputs": [
            "6\n10 -20 30 -40 50 -60\n2 4",
            "5\n0 0 0 0 0\n1 4",
            "4\n1000 2000 3000 4000\n1 2",
            "3\n-1 -1 -1\n0 2"
        ],
        "solver": solve_prefix_sum
    },
    {
        "title_base": "Running Maximum Subarray",
        "description": "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output the maximum subarray sum as a single integer.",
        "constraints": "1 <= N <= 10^5\n-10^4 <= nums[i] <= 10^4",
        "io_type": "array",
        "sample_input": "9\n-2 1 -3 4 -1 2 1 -5 4",
        "sample_output": "6",
        "explanation": "The contiguous subarray [4, -1, 2, 1] has the largest sum = 6.",
        "test_inputs": [
            "9\n-2 1 -3 4 -1 2 1 -5 4",
            "1\n1",
            "5\n5 4 -1 7 8",
            "4\n-3 -2 -1 -4"
        ],
        "variant_inputs": [
            "6\n-2 -3 4 -1 -2 1",
            "5\n-10 20 -5 15 -30",
            "4\n100 -50 200 -300",
            "3\n-5 -2 -8"
        ],
        "solver": solve_max_subarray
    },
    {
        "title_base": "Rotate Array Elements",
        "description": "Given an array of N integers, rotate the array to the right by k steps, where k is non-negative.",
        "input_format": "Line 1: An integer k (rotation steps)\nLine 2: An integer N (array size)\nLine 3: N space-separated integers",
        "output_format": "Output the rotated array elements separated by spaces.",
        "constraints": "1 <= N <= 10^5\n0 <= k <= 10^9",
        "io_type": "target_and_array",
        "sample_input": "3\n7\n1 2 3 4 5 6 7",
        "sample_output": "5 6 7 1 2 3 4",
        "explanation": "Rotate 3 steps right: [1,2,3,4,5,6,7] -> [5,6,7,1,2,3,4].",
        "test_inputs": [
            "3\n7\n1 2 3 4 5 6 7",
            "2\n4\n-1 -100 3 99",
            "0\n3\n1 2 3",
            "5\n2\n10 20"
        ],
        "variant_inputs": [
            "10\n5\n1 2 3 4 5",
            "4\n6\n10 20 30 40 50 60",
            "1\n3\n9 8 7",
            "7\n4\n2 4 6 8"
        ],
        "solver": solve_rotate_array
    },
    {
        "title_base": "Product Except Self",
        "description": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. Solve without using division.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output N space-separated integers representing the products.",
        "constraints": "2 <= N <= 10^5\n-30 <= nums[i] <= 30",
        "io_type": "array",
        "sample_input": "4\n1 2 3 4",
        "sample_output": "24 12 8 6",
        "explanation": "answer[0] = 2*3*4 = 24, answer[1] = 1*3*4 = 12, etc.",
        "test_inputs": [
            "4\n1 2 3 4",
            "5\n-1 1 0 -3 3",
            "2\n5 10",
            "3\n0 0 2"
        ],
        "variant_inputs": [
            "5\n2 3 4 5 6",
            "4\n-2 2 -3 3",
            "3\n10 20 30",
            "4\n1 0 2 0"
        ],
        "solver": solve_product_except_self
    },
    {
        "title_base": "Find Majority Element",
        "description": "Given an array nums of size n, return the majority element that appears more than ⌊n / 2⌋ times using the Boyer-Moore voting algorithm.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output the majority element.",
        "constraints": "1 <= N <= 10^5\n-10^9 <= nums[i] <= 10^9\nA majority element always exists.",
        "io_type": "array",
        "sample_input": "7\n2 2 1 1 1 2 2",
        "sample_output": "2",
        "explanation": "2 appears 4 times out of 7, which is > 7/2.",
        "test_inputs": [
            "7\n2 2 1 1 1 2 2",
            "3\n3 2 3",
            "1\n42",
            "5\n6 6 6 7 7"
        ],
        "variant_inputs": [
            "9\n1 1 1 1 2 3 1 4 1",
            "5\n-5 -5 -5 2 3",
            "3\n100 100 200",
            "7\n0 1 0 1 0 0 0"
        ],
        "solver": solve_majority_element
    },
    {
        "title_base": "Missing Positive Number",
        "description": "Given an unsorted integer array nums, return the smallest missing positive integer in O(n) time and O(1) auxiliary space.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output the smallest missing positive integer.",
        "constraints": "1 <= N <= 10^5\n-2^31 <= nums[i] <= 2^31 - 1",
        "io_type": "array",
        "sample_input": "3\n1 2 0",
        "sample_output": "3",
        "explanation": "Numbers 1 and 2 are present; smallest missing positive is 3.",
        "test_inputs": [
            "3\n1 2 0",
            "4\n3 4 -1 1",
            "5\n7 8 9 11 12",
            "1\n1"
        ],
        "variant_inputs": [
            "4\n2 3 7 6",
            "5\n-1 -2 1 2 3",
            "3\n4 5 6",
            "2\n2 1"
        ],
        "solver": solve_missing_positive
    },
    {
        "title_base": "Trapping Water Blocks",
        "description": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers representing bar heights",
        "output_format": "Output the total units of trapped water.",
        "constraints": "1 <= N <= 10^5\n0 <= height[i] <= 10^5",
        "io_type": "array",
        "sample_input": "12\n0 1 0 2 1 0 1 3 2 1 2 1",
        "sample_output": "6",
        "explanation": "6 units of rain water are trapped between elevation bars.",
        "test_inputs": [
            "12\n0 1 0 2 1 0 1 3 2 1 2 1",
            "6\n4 2 0 3 2 5",
            "3\n3 0 2",
            "3\n1 2 3"
        ],
        "variant_inputs": [
            "5\n5 1 2 1 5",
            "6\n3 1 2 4 0 1",
            "4\n2 0 0 2",
            "2\n1 2"
        ],
        "solver": solve_trapping_rain
    },
    {
        "title_base": "Merge Sorted Sequences",
        "description": "Given two sorted integer sequences A and B of sizes N and M, merge them into a single sorted sequence.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers of sequence A\nLine 3: An integer M\nLine 4: M space-separated integers of sequence B",
        "output_format": "Output the merged sorted elements separated by spaces.",
        "constraints": "1 <= N, M <= 10^5\n-10^9 <= A[i], B[i] <= 10^9",
        "io_type": "two_arrays",
        "sample_input": "3\n1 2 3\n3\n2 5 6",
        "sample_output": "1 2 2 3 5 6",
        "explanation": "Merged list in sorted order.",
        "test_inputs": [
            "3\n1 2 3\n3\n2 5 6",
            "1\n1\n0\n",
            "2\n4 5\n2\n1 2",
            "3\n-5 0 5\n2\n-2 2"
        ],
        "variant_inputs": [
            "4\n10 20 30 40\n3\n15 25 35",
            "2\n1 3\n3\n2 4 6",
            "1\n100\n1\n50",
            "3\n0 0 0\n2\n0 1"
        ],
        "solver": solve_merge_sorted
    },
    {
        "title_base": "Sort Array by Parity",
        "description": "Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output the elements sorted by parity.",
        "constraints": "1 <= N <= 10^5\n0 <= nums[i] <= 10^4",
        "io_type": "array",
        "sample_input": "4\n3 1 2 4",
        "sample_output": "2 4 3 1",
        "explanation": "Even numbers [2, 4] come first, followed by odd numbers [3, 1].",
        "test_inputs": [
            "4\n3 1 2 4",
            "1\n0",
            "4\n2 4 6 8",
            "4\n1 3 5 7"
        ],
        "variant_inputs": [
            "6\n9 8 7 6 5 4",
            "5\n10 15 20 25 30",
            "3\n1 2 3",
            "2\n4 2"
        ],
        "solver": solve_sort_parity
    },
    {
        "title_base": "Partition Array to Three",
        "description": "Given an array of integers arr, return true if we can partition the array into three non-empty contiguous parts with equal sums, otherwise return false.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "3 <= N <= 10^5\n-10^4 <= arr[i] <= 10^4",
        "io_type": "array",
        "sample_input": "11\n0 2 1 -6 6 -7 9 1 2 0 1",
        "sample_output": "true",
        "explanation": "0+2+1 = 3, -6+6-7+9+1 = 3, 2+0+1 = 3. Each part sums to 3.",
        "test_inputs": [
            "11\n0 2 1 -6 6 -7 9 1 2 0 1",
            "9\n0 2 1 -6 6 7 9 -1 2",
            "6\n3 3 6 5 -2 2",
            "3\n1 1 1"
        ],
        "variant_inputs": [
            "6\n1 2 1 2 1 2",
            "4\n1 2 3 4",
            "6\n10 -10 10 -10 10 -10",
            "3\n0 0 0"
        ],
        "solver": solve_partition_three
    },
    {
        "title_base": "Continuous Subarray Sum",
        "description": "Given an integer array nums and an integer k, return true if nums has a good subarray of length at least 2 whose elements sum up to a multiple of k.",
        "input_format": "Line 1: Integer k\nLine 2: An integer N\nLine 3: N space-separated integers",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "1 <= N <= 10^5\n1 <= k <= 2^31 - 1\n0 <= nums[i] <= 10^9",
        "io_type": "target_and_array",
        "sample_input": "6\n5\n23 2 4 6 7",
        "sample_output": "true",
        "explanation": "[2, 4] is a continuous subarray of size 2 whose sum is 6, a multiple of 6.",
        "test_inputs": [
            "6\n5\n23 2 4 6 7",
            "6\n5\n23 2 6 4 7",
            "13\n5\n23 2 6 4 7",
            "5\n2\n5 0"
        ],
        "variant_inputs": [
            "7\n4\n14 7 21 28",
            "10\n3\n1 2 3",
            "5\n3\n0 0 0",
            "8\n4\n2 4 6 8"
        ],
        "solver": solve_continuous_subarray_sum
    },
    {
        "title_base": "Max Chunks to Make Sorted",
        "description": "Given an array arr of size n that is a permutation of 0 to n - 1, find the maximum number of chunks we can partition arr into such that sorting each chunk individually sorts the entire array.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers (permutation of 0 to N-1)",
        "output_format": "Output the maximum number of chunks.",
        "constraints": "1 <= N <= 10\narr is a permutation of [0, 1, ..., N - 1]",
        "io_type": "array",
        "sample_input": "5\n4 3 2 1 0",
        "sample_output": "1",
        "explanation": "Splitting into two or more chunks cannot yield sorted order. We must keep as 1 chunk.",
        "test_inputs": [
            "5\n4 3 2 1 0",
            "5\n1 0 2 3 4",
            "1\n0",
            "4\n0 1 2 3"
        ],
        "variant_inputs": [
            "6\n0 2 1 4 3 5",
            "4\n2 0 1 3",
            "5\n0 4 2 3 1",
            "3\n2 1 0"
        ],
        "solver": solve_max_chunks_sorted
    },
    {
        "title_base": "First Missing Number",
        "description": "Given an array of integers representing an arithmetic progression with one element missing, find the missing integer.",
        "input_format": "Line 1: An integer N (number of given elements)\nLine 2: N space-separated integers",
        "output_format": "Output the missing integer in the arithmetic progression.",
        "constraints": "2 <= N <= 10^5\n-10^9 <= nums[i] <= 10^9",
        "io_type": "array",
        "sample_input": "4\n5 7 11 13",
        "sample_output": "9",
        "explanation": "The common difference is 2. The missing number is 9.",
        "test_inputs": [
            "4\n5 7 11 13",
            "4\n1 4 7 13",
            "3\n10 30 40",
            "2\n2 6"
        ],
        "variant_inputs": [
            "5\n2 4 6 10 12",
            "4\n100 200 400 500",
            "3\n-10 -4 -1",
            "3\n15 25 35"
        ],
        "solver": solve_first_missing_ap
    },
    {
        "title_base": "Best Time to Buy Stock",
        "description": "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated prices",
        "output_format": "Output the maximum profit.",
        "constraints": "1 <= N <= 10^5\n0 <= prices[i] <= 10^4",
        "io_type": "array",
        "sample_input": "6\n7 1 5 3 6 4",
        "sample_output": "5",
        "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.",
        "test_inputs": [
            "6\n7 1 5 3 6 4",
            "5\n7 6 4 3 1",
            "2\n1 5",
            "1\n10"
        ],
        "variant_inputs": [
            "5\n2 4 1 7 5",
            "6\n10 2 5 1 9 4",
            "4\n3 2 6 50",
            "3\n5 5 5"
        ],
        "solver": solve_stock_single
    },
    {
        "title_base": "Multiple Stock Transactions",
        "description": "You are given an integer array prices. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. Find and return the maximum profit you can achieve.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated prices",
        "output_format": "Output the maximum profit.",
        "constraints": "1 <= N <= 10^5\n0 <= prices[i] <= 10^4",
        "io_type": "array",
        "sample_input": "5\n7 1 5 3 6 4",
        "sample_output": "7",
        "explanation": "Buy day 2 (1), sell day 3 (5), profit=4. Buy day 4 (3), sell day 5 (6), profit=3. Total = 7.",
        "test_inputs": [
            "6\n7 1 5 3 6 4",
            "5\n1 2 3 4 5",
            "5\n7 6 4 3 1",
            "2\n2 10"
        ],
        "variant_inputs": [
            "6\n2 1 4 5 2 9",
            "4\n1 5 2 8",
            "5\n10 20 15 30 40",
            "3\n1 1 1"
        ],
        "solver": solve_stock_unlimited
    },
    {
        "title_base": "Stock with Cooldown Period",
        "description": "Maximize profit from stock prices with unlimited transactions, but after you sell your stock, you cannot buy stock on the next day (i.e., 1 day cooldown).",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated prices",
        "output_format": "Output the maximum profit achievable.",
        "constraints": "1 <= N <= 5000\n0 <= prices[i] <= 1000",
        "io_type": "array",
        "sample_input": "5\n1 2 3 0 2",
        "sample_output": "3",
        "explanation": "Transactions = [buy, sell, cooldown, buy, sell], profit = (2-1) + (2-0) = 3.",
        "test_inputs": [
            "5\n1 2 3 0 2",
            "1\n1",
            "4\n1 4 2 7",
            "3\n3 2 1"
        ],
        "variant_inputs": [
            "6\n1 2 4 2 5 7",
            "5\n6 1 3 2 4",
            "4\n2 1 4 5",
            "2\n1 2"
        ],
        "solver": solve_stock_cooldown
    },
    {
        "title_base": "Stock with Transaction Fee",
        "description": "Given prices and an integer fee, find the maximum profit you can achieve with unlimited transactions where each transaction incurs a fixed fee.",
        "input_format": "Line 1: Transaction fee\nLine 2: An integer N\nLine 3: N space-separated prices",
        "output_format": "Output the maximum profit.",
        "constraints": "1 <= N <= 50000\n1 <= prices[i] < 50000\n0 <= fee < 50000",
        "io_type": "target_and_array",
        "sample_input": "2\n6\n1 3 2 8 4 9",
        "sample_output": "8",
        "explanation": "Buy at 1, sell at 8 (profit = 8-1-2=5). Buy at 4, sell at 9 (profit = 9-4-2=3). Total = 8.",
        "test_inputs": [
            "2\n6\n1 3 2 8 4 9",
            "3\n6\n1 3 7 5 10 3",
            "1\n3\n1 4 6",
            "5\n2\n1 2"
        ],
        "variant_inputs": [
            "2\n5\n1 4 2 8 10",
            "1\n4\n1 5 3 9",
            "3\n4\n2 6 1 8",
            "4\n3\n10 20 30"
        ],
        "solver": solve_stock_fee
    },
    {
        "title_base": "Maximum Gap in Array",
        "description": "Given an integer array nums, return the maximum difference between two successive elements in its sorted form. Return 0 if the array contains less than 2 elements.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated integers",
        "output_format": "Output the maximum gap as a single integer.",
        "constraints": "1 <= N <= 10^5\n0 <= nums[i] <= 10^9",
        "io_type": "array",
        "sample_input": "4\n3 6 9 1",
        "sample_output": "3",
        "explanation": "Sorted form is [1, 3, 6, 9]. Max differences are between 3-1=2, 6-3=3, 9-6=3. Max gap is 3.",
        "test_inputs": [
            "4\n3 6 9 1",
            "1\n10",
            "5\n1 10 5 2 20",
            "2\n100 1"
        ],
        "variant_inputs": [
            "5\n1 3 100 4 7",
            "4\n10 20 40 80",
            "3\n5 5 5",
            "2\n0 1000"
        ],
        "solver": solve_max_gap
    },
    {
        "title_base": "Largest Rectangle in Histogram",
        "description": "Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated heights",
        "output_format": "Output the largest rectangle area.",
        "constraints": "1 <= N <= 10^5\n0 <= heights[i] <= 10^4",
        "io_type": "array",
        "sample_input": "6\n2 1 5 6 2 3",
        "sample_output": "10",
        "explanation": "The largest rectangle is formed by bars [5, 6] with width 2 and height 5, area = 10.",
        "test_inputs": [
            "6\n2 1 5 6 2 3",
            "2\n2 4",
            "1\n5",
            "5\n1 1 1 1 1"
        ],
        "variant_inputs": [
            "5\n6 2 5 4 5",
            "4\n2 1 2 1",
            "4\n4 3 2 1",
            "3\n5 4 6"
        ],
        "solver": solve_largest_rectangle
    }
]
