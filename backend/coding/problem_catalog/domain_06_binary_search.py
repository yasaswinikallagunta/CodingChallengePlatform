# Domain 06: Algorithms - Binary Search & Divide Conquer (Problems 101 - 120)
import math

def solver_101(s: str) -> str:
    # Standard Binary Search
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    arr = [int(x) for x in parts[2:2+n]]
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return str(mid)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "-1"

def solver_102(s: str) -> str:
    # Search Insert Position
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    arr = [int(x) for x in parts[2:2+n]]
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(ans)

def solver_103(s: str) -> str:
    # First and Last Position of Element
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    arr = [int(x) for x in parts[2:2+n]]
    first, last = -1, -1
    for i, v in enumerate(arr):
        if v == target:
            if first == -1: first = i
            last = i
    return f"{first} {last}"

def solver_104(s: str) -> str:
    # Search in Rotated Sorted Array
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    arr = [int(x) for x in parts[2:2+n]]
    try:
        return str(arr.index(target))
    except ValueError:
        return "-1"

def solver_105(s: str) -> str:
    # Search Rotated Array with Duplicates
    parts = s.strip().split()
    target = int(parts[0])
    n = int(parts[1])
    arr = [int(x) for x in parts[2:2+n]]
    return "true" if target in arr else "false"

def solver_106(s: str) -> str:
    # Find Minimum in Rotated Array
    parts = s.strip().split()
    n = int(parts[0])
    arr = [int(x) for x in parts[1:1+n]]
    return str(min(arr))

def solver_107(s: str) -> str:
    # Find Peak Element
    parts = s.strip().split()
    n = int(parts[0])
    arr = [int(x) for x in parts[1:1+n]]
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return str(low)

def solver_108(s: str) -> str:
    # Square Root Integer Computation
    x = int(s.strip().split()[0])
    return str(math.isqrt(x))

def solver_109(s: str) -> str:
    # Peak Index in Mountain Array
    parts = s.strip().split()
    n = int(parts[0])
    arr = [int(x) for x in parts[1:1+n]]
    return str(arr.index(max(arr)))

def solver_110(s: str) -> str:
    # Single Element in Sorted Array
    parts = s.strip().split()
    n = int(parts[0])
    arr = [int(x) for x in parts[1:1+n]]
    ans = 0
    for v in arr:
        ans ^= v
    return str(ans)

def solver_111(s: str) -> str:
    # Koko Eating Bananas
    parts = s.strip().split()
    h = int(parts[0])
    n = int(parts[1])
    piles = [int(x) for x in parts[2:2+n]]
    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        hours = sum((p + mid - 1) // mid for p in piles)
        if hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(ans)

def solver_112(s: str) -> str:
    # Capacity to Ship Packages
    parts = s.strip().split()
    days = int(parts[0])
    n = int(parts[1])
    weights = [int(x) for x in parts[2:2+n]]
    low, high = max(weights), sum(weights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        need = 1
        cur = 0
        for w in weights:
            if cur + w > mid:
                need += 1
                cur = 0
            cur += w
        if need <= days:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(ans)

def solver_113(s: str) -> str:
    # Split Array Largest Sum
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = [int(x) for x in parts[2:2+n]]
    low, high = max(nums), sum(nums)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        count = 1
        cur = 0
        for x in nums:
            if cur + x > mid:
                count += 1
                cur = 0
            cur += x
        if count <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(ans)

def solver_114(s: str) -> str:
    # Median of Two Sorted Arrays
    parts = s.strip().split()
    n = int(parts[0])
    m = int(parts[1])
    idx = 2
    a = [int(x) for x in parts[idx:idx+n]]
    idx += n
    b = [int(x) for x in parts[idx:idx+m]]
    c = sorted(a + b)
    L = len(c)
    if L % 2 == 1:
        return f"{float(c[L//2]):.1f}"
    else:
        med = (c[L//2 - 1] + c[L//2]) / 2.0
        return f"{med:.1f}"

def solver_115(s: str) -> str:
    # Find Kth Smallest Pair Distance
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    nums = sorted(int(x) for x in parts[2:2+n])
    low, high = 0, nums[-1] - nums[0]
    ans = high
    while low <= high:
        mid = (low + high) // 2
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        if count >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(ans)

def solver_116(s: str) -> str:
    # Magnetic Force Between Balls
    parts = s.strip().split()
    m = int(parts[0])
    n = int(parts[1])
    position = sorted(int(x) for x in parts[2:2+n])
    low, high = 1, position[-1] - position[0]
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        count = 1
        last = position[0]
        for p in position[1:]:
            if p - last >= mid:
                count += 1
                last = p
        if count >= m:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(ans)

def solver_117(s: str) -> str:
    # Find Smallest Letter Greater Target
    parts = s.strip().split()
    target = parts[0]
    n = int(parts[1])
    letters = parts[2:2+n]
    for c in letters:
        if c > target:
            return c
    return letters[0]

def solver_118(s: str) -> str:
    # Search in 2D Sorted Matrix
    parts = s.strip().split()
    target = int(parts[0])
    r = int(parts[1])
    c = int(parts[2])
    matrix = [int(x) for x in parts[3:3+r*c]]
    return "true" if target in matrix else "false"

def solver_119(s: str) -> str:
    # Search in 2D Matrix II
    parts = s.strip().split()
    target = int(parts[0])
    r = int(parts[1])
    c = int(parts[2])
    matrix = [int(x) for x in parts[3:3+r*c]]
    return "true" if target in matrix else "false"

def solver_120(s: str) -> str:
    # Count Negative Numbers in Grid
    parts = s.strip().split()
    r = int(parts[0])
    c = int(parts[1])
    matrix = [int(x) for x in parts[2:2+r*c]]
    neg = sum(1 for x in matrix if x < 0)
    return str(neg)

PROBLEMS = [
    {
        "index": 101,
        "title_base": "Standard Binary Search",
        "description": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.",
        "input_format": "The first line contains target and N. The second line contains N sorted integers.",
        "output_format": "Print the 0-based index of target or -1.",
        "constraints": "1 <= N <= 10^5, -10^4 < nums[i], target < 10^4",
        "sample_input": "9 6\n-1 0 3 5 9 12",
        "sample_output": "4",
        "explanation": "9 exists in nums and its index is 4.",
        "test_inputs": ["2 6\n-1 0 3 5 9 12", "5 1\n5"],
        "variant_inputs": ["10 5\n2 4 6 8 10", "3 4\n1 2 4 5"],
        "starter_archetype": "target_and_array",
        "solver": solver_101
    },
    {
        "index": 102,
        "title_base": "Search Insert Position",
        "description": "Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.",
        "input_format": "First line contains target and N. Second line contains N sorted integers.",
        "output_format": "Print the insertion index.",
        "constraints": "1 <= N <= 10^4, -10^4 <= nums[i] <= 10^4",
        "sample_input": "5 4\n1 3 5 6",
        "sample_output": "2",
        "explanation": "5 is found at index 2.",
        "test_inputs": ["2 4\n1 3 5 6", "7 4\n1 3 5 6"],
        "variant_inputs": ["0 3\n1 3 5", "4 4\n1 2 3 5"],
        "starter_archetype": "target_and_array",
        "solver": solver_102
    },
    {
        "index": 103,
        "title_base": "First and Last Position of Element",
        "description": "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found, return [-1, -1].",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print start and end index separated by a space.",
        "constraints": "0 <= N <= 10^5, -10^9 <= nums[i] <= 10^9",
        "sample_input": "8 6\n5 7 7 8 8 10",
        "sample_output": "3 4",
        "explanation": "8 appears starting at index 3 and ending at index 4.",
        "test_inputs": ["6 6\n5 7 7 8 8 10", "1 1\n1"],
        "variant_inputs": ["5 5\n5 5 5 5 5", "3 4\n1 2 4 5"],
        "starter_archetype": "target_and_array",
        "solver": solver_103
    },
    {
        "index": 104,
        "title_base": "Search in Rotated Sorted Array",
        "description": "Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print the index or -1.",
        "constraints": "1 <= N <= 5000, -10^4 <= nums[i] <= 10^4",
        "sample_input": "0 7\n4 5 6 7 0 1 2",
        "sample_output": "4",
        "explanation": "0 is found at index 4.",
        "test_inputs": ["3 7\n4 5 6 7 0 1 2", "1 1\n1"],
        "variant_inputs": ["2 4\n3 4 1 2", "5 5\n2 3 4 5 1"],
        "starter_archetype": "target_and_array",
        "solver": solver_104
    },
    {
        "index": 105,
        "title_base": "Search Rotated Array with Duplicates",
        "description": "There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values). Given the array nums after rotation and an integer target, return 'true' if target is in nums, or 'false' if it is not.",
        "input_format": "First line contains target and N. Second line contains N integers.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= N <= 5000, -10^4 <= nums[i] <= 10^4",
        "sample_input": "0 7\n2 5 6 0 0 1 2",
        "sample_output": "true",
        "explanation": "0 exists in nums.",
        "test_inputs": ["3 7\n2 5 6 0 0 1 2", "1 3\n1 0 1"],
        "variant_inputs": ["4 5\n1 1 3 1 1", "2 4\n2 2 2 2"],
        "starter_archetype": "target_and_array",
        "solver": solver_105
    },
    {
        "index": 106,
        "title_base": "Find Minimum in Rotated Array",
        "description": "Given the sorted rotated array nums of unique elements, return the minimum element of this array.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the minimum element.",
        "constraints": "1 <= N <= 5000, -5000 <= nums[i] <= 5000",
        "sample_input": "5\n3 4 5 1 2",
        "sample_output": "1",
        "explanation": "Original array was [1, 2, 3, 4, 5] rotated 3 times. Min is 1.",
        "test_inputs": ["7\n4 5 6 7 0 1 2", "1\n11"],
        "variant_inputs": ["4\n11 13 15 17", "6\n2 3 4 5 6 1"],
        "starter_archetype": "array",
        "solver": solver_106
    },
    {
        "index": 107,
        "title_base": "Find Peak Element",
        "description": "A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the index of any peak element.",
        "constraints": "1 <= N <= 1000, -2^31 <= nums[i] <= 2^31 - 1",
        "sample_input": "4\n1 2 3 1",
        "sample_output": "2",
        "explanation": "3 is a peak element and its index is 2.",
        "test_inputs": ["7\n1 2 1 3 5 6 4", "1\n1"],
        "variant_inputs": ["5\n1 2 3 4 5", "3\n3 2 1"],
        "starter_archetype": "array",
        "solver": solver_107
    },
    {
        "index": 108,
        "title_base": "Square Root Integer Computation",
        "description": "Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.",
        "input_format": "A single line containing integer x.",
        "output_format": "Print the integer square root.",
        "constraints": "0 <= x <= 2^31 - 1",
        "sample_input": "4",
        "sample_output": "2",
        "explanation": "Square root of 4 is 2.",
        "test_inputs": ["8", "0"],
        "variant_inputs": ["16", "25"],
        "starter_archetype": "single_number",
        "solver": solver_108
    },
    {
        "index": 109,
        "title_base": "Peak Index in Mountain Array",
        "description": "An array arr is a mountain if it increases to a peak element and then decreases. Return the index of the peak element.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the peak index.",
        "constraints": "3 <= N <= 10^5, 0 <= arr[i] <= 10^6",
        "sample_input": "3\n0 1 0",
        "sample_output": "1",
        "explanation": "Peak is 1 at index 1.",
        "test_inputs": ["4\n0 2 1 0", "4\n0 10 5 2"],
        "variant_inputs": ["5\n1 3 5 4 2", "5\n0 5 10 3 1"],
        "starter_archetype": "array",
        "solver": solver_109
    },
    {
        "index": 110,
        "title_base": "Single Element in Sorted Array",
        "description": "You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Return the single element that appears only once.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the single unique element.",
        "constraints": "1 <= N <= 10^5, 0 <= nums[i] <= 10^5",
        "sample_input": "9\n1 1 2 3 3 4 4 8 8",
        "sample_output": "2",
        "explanation": "2 appears only once.",
        "test_inputs": ["7\n3 3 7 7 10 11 11", "1\n5"],
        "variant_inputs": ["5\n1 1 2 2 3", "5\n0 1 1 2 2"],
        "starter_archetype": "array",
        "solver": solver_110
    },
    {
        "index": 111,
        "title_base": "Koko Eating Bananas",
        "description": "Koko loves to eat bananas. There are n piles of bananas. She can decide her bananas-per-hour eating speed of k. Return the minimum integer k such that she can eat all the bananas within h hours.",
        "input_format": "First line contains h and N. Second line contains N integers for pile sizes.",
        "output_format": "Print the minimum eating speed k.",
        "constraints": "1 <= N <= 10^4, N <= h <= 10^9, 1 <= piles[i] <= 10^9",
        "sample_input": "8 4\n3 6 7 11",
        "sample_output": "4",
        "explanation": "At speed 4, Koko finishes in 1 + 2 + 2 + 3 = 8 hours.",
        "test_inputs": ["5 5\n30 11 23 4 20", "6 5\n30 11 23 4 20"],
        "variant_inputs": ["4 4\n1 2 3 4", "10 3\n10 15 20"],
        "starter_archetype": "target_and_array",
        "solver": solver_111
    },
    {
        "index": 112,
        "title_base": "Capacity to Ship Packages",
        "description": "A conveyor belt has packages that must be shipped within days days. Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.",
        "input_format": "First line contains days and N. Second line contains N integers.",
        "output_format": "Print the least weight capacity.",
        "constraints": "1 <= days <= N <= 5 * 10^4, 1 <= weights[i] <= 500",
        "sample_input": "5 10\n1 2 3 4 5 6 7 8 9 10",
        "sample_output": "15",
        "explanation": "A ship capacity of 15 ships packages over 5 days.",
        "test_inputs": ["3 6\n3 2 2 4 1 4", "1 3\n1 2 3"],
        "variant_inputs": ["2 5\n10 20 30 40 50", "4 4\n1 2 3 4"],
        "starter_archetype": "target_and_array",
        "solver": solver_112
    },
    {
        "index": 113,
        "title_base": "Split Array Largest Sum",
        "description": "Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print the minimized largest sum.",
        "constraints": "1 <= N <= 1000, 1 <= k <= min(50, N), 0 <= nums[i] <= 10^6",
        "sample_input": "2 5\n7 2 5 10 8",
        "sample_output": "18",
        "explanation": "Best split: [7, 2, 5] and [10, 8]. Max sum is max(14, 18) = 18.",
        "test_inputs": ["2 5\n1 2 3 4 5", "3 4\n1 4 4 5"],
        "variant_inputs": ["1 4\n10 20 30 40", "4 4\n1 2 3 4"],
        "starter_archetype": "target_and_array",
        "solver": solver_113
    },
    {
        "index": 114,
        "title_base": "Median of Two Sorted Arrays",
        "description": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.",
        "input_format": "First line contains N and M. Second line contains N integers. Third line contains M integers.",
        "output_format": "Print the median formatted with one decimal place.",
        "constraints": "0 <= N, M <= 1000, -10^6 <= nums1[i], nums2[i] <= 10^6",
        "sample_input": "2 1\n1 3\n2",
        "sample_output": "2.0",
        "explanation": "Merged array = [1, 2, 3] and median is 2.0.",
        "test_inputs": ["2 2\n1 2\n3 4", "1 1\n0\n0"],
        "variant_inputs": ["3 2\n1 3 5\n2 4", "2 3\n10 20\n5 15 25"],
        "starter_archetype": "general",
        "solver": solver_114
    },
    {
        "index": 115,
        "title_base": "Find Kth Smallest Pair Distance",
        "description": "The distance of a pair of integers a and b is defined as the absolute difference |a - b|. Given an integer array nums and an integer k, return the kth smallest distance among all the pairs.",
        "input_format": "First line contains k and N. Second line contains N integers.",
        "output_format": "Print the kth smallest distance.",
        "constraints": "2 <= N <= 10^4, 0 <= nums[i] <= 10^6, 1 <= k <= N*(N-1)/2",
        "sample_input": "1 3\n1 3 1",
        "sample_output": "0",
        "explanation": "Pairs are (1,3):2, (1,1):0, (3,1):2. Sorted distances: 0, 2, 2. 1st is 0.",
        "test_inputs": ["1 3\n1 1 1", "3 4\n1 6 1 1"],
        "variant_inputs": ["2 3\n1 4 8", "1 4\n5 2 9 1"],
        "starter_archetype": "target_and_array",
        "solver": solver_115
    },
    {
        "index": 116,
        "title_base": "Magnetic Force Between Balls",
        "description": "In the universe Earth C-137, Rick has n empty baskets at given positions. Given integer m, distribute m balls into the baskets such that the minimum magnetic force between any two balls is maximum.",
        "input_format": "First line contains m and N. Second line contains N basket positions.",
        "output_format": "Print the maximum minimum magnetic force.",
        "constraints": "2 <= N <= 10^5, 2 <= m <= N, 1 <= position[i] <= 10^9",
        "sample_input": "3 5\n1 2 3 4 7",
        "sample_output": "3",
        "explanation": "Distributing 3 balls at baskets 1, 4, 7 gives minimum force of 3.",
        "test_inputs": ["2 3\n1 5 9", "3 6\n5 4 3 2 1 1000000000"],
        "variant_inputs": ["2 4\n2 4 8 16", "3 4\n1 3 6 9"],
        "starter_archetype": "target_and_array",
        "solver": solver_116
    },
    {
        "index": 117,
        "title_base": "Find Smallest Letter Greater Target",
        "description": "You are given an array of characters letters that is sorted in non-decreasing order, and a character target. Return the smallest character in letters that is lexicographically greater than target.",
        "input_format": "First line contains target character and N. Second line contains N characters.",
        "output_format": "Print the smallest character greater than target.",
        "constraints": "2 <= N <= 10^4, letters[i] and target are lowercase English letters.",
        "sample_input": "a 3\nc f j",
        "sample_output": "c",
        "explanation": "The smallest character strictly greater than 'a' in letters is 'c'.",
        "test_inputs": ["c 3\nc f j", "d 3\nc f j"],
        "variant_inputs": ["z 3\nx y z", "k 4\na b c d"],
        "starter_archetype": "general",
        "solver": solver_117
    },
    {
        "index": 118,
        "title_base": "Search in 2D Sorted Matrix",
        "description": "Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. Each row is sorted and the first integer of each row is greater than the last integer of the previous row.",
        "input_format": "First line contains target, rows, and cols. Following lines contain the matrix elements.",
        "output_format": "Print 'true' if target is found, otherwise 'false'.",
        "constraints": "1 <= m, n <= 100, -10^4 <= matrix[i][j], target <= 10^4",
        "sample_input": "3 3 4\n1 3 5 7\n10 11 16 20\n23 30 34 60",
        "sample_output": "true",
        "explanation": "3 exists in the matrix at row 0 col 1.",
        "test_inputs": ["13 3 4\n1 3 5 7\n10 11 16 20\n23 30 34 60", "1 1 1\n1"],
        "variant_inputs": ["5 2 2\n1 2\n3 4", "10 2 3\n1 2 3\n4 10 12"],
        "starter_archetype": "general",
        "solver": solver_118
    },
    {
        "index": 119,
        "title_base": "Search in 2D Matrix II",
        "description": "Write an efficient algorithm that searches for a value target in an m x n integer matrix. Integers in each row are sorted in ascending from left to right, and integers in each column are sorted in ascending from top to bottom.",
        "input_format": "First line contains target, rows, and cols. Following lines contain the matrix elements.",
        "output_format": "Print 'true' if target is found, otherwise 'false'.",
        "constraints": "1 <= m, n <= 300, -10^9 <= matrix[i][j], target <= 10^9",
        "sample_input": "5 5 5\n1 4 7 11 15\n2 5 8 12 19\n3 6 9 16 22\n10 13 14 17 24\n18 21 23 26 30",
        "sample_output": "true",
        "explanation": "5 is present at position (1, 1).",
        "test_inputs": ["20 5 5\n1 4 7 11 15\n2 5 8 12 19\n3 6 9 16 22\n10 13 14 17 24\n18 21 23 26 30", "1 1 1\n2"],
        "variant_inputs": ["10 2 2\n1 3\n5 10", "4 2 2\n1 2\n3 5"],
        "starter_archetype": "general",
        "solver": solver_119
    },
    {
        "index": 120,
        "title_base": "Count Negative Numbers in Grid",
        "description": "Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.",
        "input_format": "First line contains rows and cols. Following lines contain the matrix elements.",
        "output_format": "Print the count of negative numbers.",
        "constraints": "1 <= m, n <= 100, -100 <= grid[i][j] <= 100",
        "sample_input": "4 4\n4 3 2 -1\n3 2 1 -1\n1 1 -1 -2\n-1 -1 -2 -3",
        "sample_output": "8",
        "explanation": "There are 8 negative numbers in the matrix.",
        "test_inputs": ["2 2\n3 2\n1 0", "1 1\n-5"],
        "variant_inputs": ["3 3\n5 4 3\n2 1 -1\n-2 -3 -4", "2 3\n1 -1 -2\n-3 -4 -5"],
        "starter_archetype": "general",
        "solver": solver_120
    }
]
