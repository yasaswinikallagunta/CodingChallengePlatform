# Domain 10: C - Bitwise & Memory (Problems 181 - 200)

def solver_181(s: str) -> str:
    # Single Number Odd Occurrences
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    ans = 0
    for x in nums: ans ^= x
    return str(ans)

def solver_182(s: str) -> str:
    # Number of 1 Bits Hamming Weight
    n = int(s.strip().split()[0])
    return str(bin(n).count('1'))

def solver_183(s: str) -> str:
    # Counting Bits Array
    n = int(s.strip().split()[0])
    res = [str(bin(i).count('1')) for i in range(n + 1)]
    return " ".join(res)

def solver_184(s: str) -> str:
    # Reverse Bits in 32-bit Int
    n = int(s.strip().split()[0])
    b = f"{n:032b}"
    return str(int(b[::-1], 2))

def solver_185(s: str) -> str:
    # Power of Two Bitwise
    n = int(s.strip().split()[0])
    return "true" if n > 0 and (n & (n - 1)) == 0 else "false"

def solver_186(s: str) -> str:
    # Missing Number in Range
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    ans = 0
    for i in range(n + 1): ans ^= i
    for x in nums: ans ^= x
    return str(ans)

def solver_187(s: str) -> str:
    # Sum of Two Integers Bitwise
    parts = s.strip().split()
    a = int(parts[0])
    b = int(parts[1])
    mask = 0xFFFFFFFF
    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return str(a if a <= 0x7FFFFFFF else ~(a ^ mask))

def solver_188(s: str) -> str:
    # Single Number II Triplets
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    ones, twos = 0, 0
    for x in nums:
        ones = (ones ^ x) & ~twos
        twos = (twos ^ x) & ~ones
    return str(ones)

def solver_189(s: str) -> str:
    # Single Number III Two Elements
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    x_xor_y = 0
    for num in nums: x_xor_y ^= num
    lowbit = x_xor_y & -x_xor_y
    x, y = 0, 0
    for num in nums:
        if num & lowbit:
            x ^= num
        else:
            y ^= num
    res = sorted([x, y])
    return f"{res[0]} {res[1]}"

def solver_190(s: str) -> str:
    # Bitwise AND of Numbers Range
    parts = s.strip().split()
    m = int(parts[0])
    n = int(parts[1])
    shift = 0
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1
    return str(m << shift)

def solver_191(s: str) -> str:
    # Power of Four Check
    n = int(s.strip().split()[0])
    return "true" if n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0 else "false"

def solver_192(s: str) -> str:
    # Hamming Distance Between Ints
    parts = s.strip().split()
    x = int(parts[0])
    y = int(parts[1])
    return str(bin(x ^ y).count('1'))

def solver_193(s: str) -> str:
    # Complement of Base 10 Integer
    n = int(s.strip().split()[0])
    if n == 0: return "1"
    mask = (1 << n.bit_length()) - 1
    return str(n ^ mask)

def solver_194(s: str) -> str:
    # Maximum XOR of Two Numbers
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    max_xor = 0
    mask = 0
    for i in range(30, -1, -1):
        mask |= (1 << i)
        prefixes = {num & mask for num in nums}
        candidate = max_xor | (1 << i)
        if any(candidate ^ p in prefixes for p in prefixes):
            max_xor = candidate
    return str(max_xor)

def solver_195(s: str) -> str:
    # UTF-8 Validation Parsing
    parts = s.strip().split()
    n = int(parts[0])
    data = [int(x) for x in parts[1:1+n]]
    num_bytes = 0
    for num in data:
        byte = num & 0xFF
        if num_bytes == 0:
            if (byte >> 5) == 0b110: num_bytes = 1
            elif (byte >> 4) == 0b1110: num_bytes = 2
            elif (byte >> 3) == 0b11110: num_bytes = 3
            elif (byte >> 7): return "false"
        else:
            if (byte >> 6) != 0b10: return "false"
            num_bytes -= 1
    return "true" if num_bytes == 0 else "false"

def solver_196(s: str) -> str:
    # Repeated DNA Sequences
    dna = s.strip().split()[0]
    seen = set()
    repeated = set()
    for i in range(len(dna) - 9):
        sub = dna[i:i+10]
        if sub in seen:
            repeated.add(sub)
        else:
            seen.add(sub)
    if not repeated: return "none"
    return " ".join(sorted(repeated))

def solver_197(s: str) -> str:
    # Concatenation of Consecutive Binary
    n = int(s.strip().split()[0])
    MOD = 10**9 + 7
    ans = 0
    length = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:
            length += 1
        ans = ((ans << length) | i) % MOD
    return str(ans)

def solver_198(s: str) -> str:
    # Minimum Flips for A OR B == C
    parts = s.strip().split()
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    flips = 0
    for i in range(32):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1
        if (bit_a | bit_b) != bit_c:
            if bit_c == 1:
                flips += 1
            else:
                flips += bit_a + bit_b
    return str(flips)

def solver_199(s: str) -> str:
    # Sort Integers by Number of 1 Bits
    parts = s.strip().split()
    n = int(parts[0])
    arr = [int(x) for x in parts[1:1+n]]
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return " ".join(str(x) for x in arr)

def solver_200(s: str) -> str:
    # Total Hamming Distance Across Array
    parts = s.strip().split()
    n = int(parts[0])
    nums = [int(x) for x in parts[1:1+n]]
    total = 0
    for i in range(32):
        ones = sum((num >> i) & 1 for num in nums)
        total += ones * (len(nums) - ones)
    return str(total)

PROBLEMS = [
    {
        "index": 181,
        "title_base": "Single Number Odd Occurrences",
        "description": "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the single unique integer.",
        "constraints": "1 <= N <= 3 * 10^4, -3 * 10^4 <= nums[i] <= 3 * 10^4",
        "sample_input": "3\n2 2 1",
        "sample_output": "1",
        "explanation": "2 appears twice, 1 appears once.",
        "test_inputs": ["5\n4 1 2 1 2", "1\n1"],
        "variant_inputs": ["5\n10 20 10 30 20", "3\n5 9 5"],
        "starter_archetype": "array",
        "solver": solver_181
    },
    {
        "index": 182,
        "title_base": "Number of 1 Bits Hamming Weight",
        "description": "Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the number of set bits.",
        "constraints": "1 <= n <= 2^31 - 1",
        "sample_input": "11",
        "sample_output": "3",
        "explanation": "11 in binary is 1011, which has 3 set bits.",
        "test_inputs": ["128", "2147483645"],
        "variant_inputs": ["7", "15"],
        "starter_archetype": "single_number",
        "solver": solver_182
    },
    {
        "index": 183,
        "title_base": "Counting Bits Array",
        "description": "Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print space-separated bit counts from 0 to n.",
        "constraints": "0 <= n <= 10^5",
        "sample_input": "2",
        "sample_output": "0 1 1",
        "explanation": "0 -> 0, 1 -> 1, 2 -> 1.",
        "test_inputs": ["5", "0"],
        "variant_inputs": ["4", "7"],
        "starter_archetype": "single_number",
        "solver": solver_183
    },
    {
        "index": 184,
        "title_base": "Reverse Bits in 32-bit Int",
        "description": "Reverse bits of a given 32 bits unsigned integer and return its decimal value.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the reversed integer.",
        "constraints": "0 <= n <= 2^32 - 1",
        "sample_input": "43261596",
        "sample_output": "964176192",
        "explanation": "Reversing the 32-bit representation of 43261596 produces 964176192.",
        "test_inputs": ["1", "0"],
        "variant_inputs": ["2", "2147483648"],
        "starter_archetype": "single_number",
        "solver": solver_184
    },
    {
        "index": 185,
        "title_base": "Power of Two Bitwise",
        "description": "Given an integer n, return 'true' if it is a power of two. Otherwise, return 'false'.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "-2^31 <= n <= 2^31 - 1",
        "sample_input": "1",
        "sample_output": "true",
        "explanation": "2^0 = 1.",
        "test_inputs": ["16", "3"],
        "variant_inputs": ["8", "14"],
        "starter_archetype": "single_number",
        "solver": solver_185
    },
    {
        "index": 186,
        "title_base": "Missing Number in Range",
        "description": "Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.",
        "input_format": "First line contains N. Second line contains N distinct integers.",
        "output_format": "Print the missing number.",
        "constraints": "n == nums.length, 1 <= n <= 10^4, 0 <= nums[i] <= n",
        "sample_input": "3\n3 0 1",
        "sample_output": "2",
        "explanation": "n = 3, numbers are in [0, 3]. 2 is missing.",
        "test_inputs": ["2\n0 1", "9\n9 6 4 2 3 5 7 0 1"],
        "variant_inputs": ["4\n0 1 2 4", "1\n0"],
        "starter_archetype": "array",
        "solver": solver_186
    },
    {
        "index": 187,
        "title_base": "Sum of Two Integers Bitwise",
        "description": "Given two integers a and b, return the sum of the two integers without using the operators + and -.",
        "input_format": "A single line containing two integers a and b.",
        "output_format": "Print the sum.",
        "constraints": "-1000 <= a, b <= 1000",
        "sample_input": "1 2",
        "sample_output": "3",
        "explanation": "1 + 2 = 3.",
        "test_inputs": ["2 3", "-1 1"],
        "variant_inputs": ["10 20", "-5 -5"],
        "starter_archetype": "two_numbers",
        "solver": solver_187
    },
    {
        "index": 188,
        "title_base": "Single Number II Triplets",
        "description": "Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the single unique integer.",
        "constraints": "1 <= N <= 3 * 10^4, -2^31 <= nums[i] <= 2^31 - 1",
        "sample_input": "4\n2 2 3 2",
        "sample_output": "3",
        "explanation": "2 appears three times, 3 appears once.",
        "test_inputs": ["7\n0 1 0 1 0 1 99", "1\n5"],
        "variant_inputs": ["4\n10 10 10 20", "4\n5 5 5 1"],
        "starter_archetype": "array",
        "solver": solver_188
    },
    {
        "index": 189,
        "title_base": "Single Number III Two Elements",
        "description": "Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once in ascending order.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the two unique integers in ascending order separated by a space.",
        "constraints": "2 <= N <= 3 * 10^4, -2^31 <= nums[i] <= 2^31 - 1",
        "sample_input": "6\n1 2 1 3 2 5",
        "sample_output": "3 5",
        "explanation": "3 and 5 appear only once.",
        "test_inputs": ["2\n-1 0", "2\n0 1"],
        "variant_inputs": ["4\n1 2 3 2", "6\n10 20 30 10 40 20"],
        "starter_archetype": "array",
        "solver": solver_189
    },
    {
        "index": 190,
        "title_base": "Bitwise AND of Numbers Range",
        "description": "Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.",
        "input_format": "A single line containing left and right.",
        "output_format": "Print the range bitwise AND.",
        "constraints": "0 <= left <= right <= 2^31 - 1",
        "sample_input": "5 7",
        "sample_output": "4",
        "explanation": "5 & 6 & 7 = 4.",
        "test_inputs": ["0 0", "1 2147483647"],
        "variant_inputs": ["10 15", "8 11"],
        "starter_archetype": "two_numbers",
        "solver": solver_190
    },
    {
        "index": 191,
        "title_base": "Power of Four Check",
        "description": "Given an integer n, return 'true' if it is a power of four. Otherwise, return 'false'.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "-2^31 <= n <= 2^31 - 1",
        "sample_input": "16",
        "sample_output": "true",
        "explanation": "4^2 = 16.",
        "test_inputs": ["5", "1"],
        "variant_inputs": ["64", "8"],
        "starter_archetype": "single_number",
        "solver": solver_191
    },
    {
        "index": 192,
        "title_base": "Hamming Distance Between Ints",
        "description": "The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers x and y, return the Hamming distance between them.",
        "input_format": "A single line containing x and y.",
        "output_format": "Print the Hamming distance.",
        "constraints": "0 <= x, y <= 2^31 - 1",
        "sample_input": "1 4",
        "sample_output": "2",
        "explanation": "1: 0001, 4: 0100. They differ at 2 bit positions.",
        "test_inputs": ["3 1", "0 0"],
        "variant_inputs": ["7 0", "15 1"],
        "starter_archetype": "two_numbers",
        "solver": solver_192
    },
    {
        "index": 193,
        "title_base": "Complement of Base 10 Integer",
        "description": "The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation. Given an integer n, return its complement.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the complement integer.",
        "constraints": "0 <= n < 10^9",
        "sample_input": "5",
        "sample_output": "2",
        "explanation": "5 is '101' in binary, its complement is '010' which is 2 in base 10.",
        "test_inputs": ["7", "10"],
        "variant_inputs": ["0", "1"],
        "starter_archetype": "single_number",
        "solver": solver_193
    },
    {
        "index": 194,
        "title_base": "Maximum XOR of Two Numbers",
        "description": "Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the maximum XOR value.",
        "constraints": "1 <= N <= 2 * 10^5, 0 <= nums[i] <= 2^31 - 1",
        "sample_input": "6\n3 10 5 25 2 8",
        "sample_output": "28",
        "explanation": "The maximum result is 5 XOR 25 = 28.",
        "test_inputs": ["2\n14 70", "1\n5"],
        "variant_inputs": ["4\n1 2 3 4", "3\n8 10 2"],
        "starter_archetype": "array",
        "solver": solver_194
    },
    {
        "index": 195,
        "title_base": "UTF-8 Validation Parsing",
        "description": "Given an integer array data representing the data, return 'true' if it is a valid UTF-8 encoding, or 'false' otherwise.",
        "input_format": "First line contains N. Second line contains N integers representing byte values.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= N <= 2 * 10^4, 0 <= data[i] <= 255",
        "sample_input": "3\n197 130 1",
        "sample_output": "true",
        "explanation": "197 130 is a valid 2-byte sequence, followed by 1 (valid 1-byte).",
        "test_inputs": ["4\n235 140 4 0", "1\n0"],
        "variant_inputs": ["2\n195 130", "1\n255"],
        "starter_archetype": "array",
        "solver": solver_195
    },
    {
        "index": 196,
        "title_base": "Repeated DNA Sequences",
        "description": "Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule in sorted order, or 'none'.",
        "input_format": "A single line containing DNA string s.",
        "output_format": "Print the repeated 10-letter sequences separated by spaces, or 'none'.",
        "constraints": "1 <= s.length <= 10^5, s[i] is either 'A', 'C', 'G', or 'T'.",
        "sample_input": "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "sample_output": "AAAAACCCCC CCCCCAAAAA",
        "explanation": "AAAAACCCCC and CCCCCAAAAA each appear twice.",
        "test_inputs": ["AAAAAAAAAAAAA", "ACGT"],
        "variant_inputs": ["AAAAAAAAAAA", "GATTACAGATTACA"],
        "starter_archetype": "single_string",
        "solver": solver_196
    },
    {
        "index": 197,
        "title_base": "Concatenation of Consecutive Binary",
        "description": "Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.",
        "input_format": "A single line containing integer n.",
        "output_format": "Print the decimal value modulo 10^9 + 7.",
        "constraints": "1 <= n <= 10^5",
        "sample_input": "1",
        "sample_output": "1",
        "explanation": "'1' in binary is 1.",
        "test_inputs": ["3", "12"],
        "variant_inputs": ["4", "5"],
        "starter_archetype": "single_number",
        "solver": solver_197
    },
    {
        "index": 198,
        "title_base": "Minimum Flips for A OR B == C",
        "description": "Given 3 positives numbers a, b and c. Return the minimum flips needed in some bits of a and to make (a OR b == c).",
        "input_format": "A single line containing a, b, and c.",
        "output_format": "Print the minimum number of flips.",
        "constraints": "1 <= a, b, c <= 10^9",
        "sample_input": "2 6 5",
        "sample_output": "3",
        "explanation": "After 3 flips: a=1, b=4, c=5: (1 OR 4 == 5).",
        "test_inputs": ["4 2 7", "1 2 3"],
        "variant_inputs": ["8 3 5", "5 5 5"],
        "starter_archetype": "general",
        "solver": solver_198
    },
    {
        "index": 199,
        "title_base": "Sort Integers by Number of 1 Bits",
        "description": "You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the sorted array separated by spaces.",
        "constraints": "1 <= N <= 500, 0 <= arr[i] <= 10^4",
        "sample_input": "9\n0 1 2 3 4 5 6 7 8",
        "sample_output": "0 1 2 4 8 3 5 6 7",
        "explanation": "[0] has 0 ones. [1,2,4,8] have 1 one. [3,5,6] have 2 ones. [7] has 3 ones.",
        "test_inputs": ["5\n1024 512 256 128 64", "1\n5"],
        "variant_inputs": ["4\n10 100 1000 10000", "3\n7 3 1"],
        "starter_archetype": "array",
        "solver": solver_199
    },
    {
        "index": 200,
        "title_base": "Total Hamming Distance Across Array",
        "description": "The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the total Hamming distance.",
        "constraints": "1 <= N <= 10^4, 0 <= nums[i] <= 10^9",
        "sample_input": "3\n4 14 2",
        "sample_output": "6",
        "explanation": "d(4, 14) = 2, d(4, 2) = 2, d(14, 2) = 2. Total = 6.",
        "test_inputs": ["3\n4 14 4", "1\n10"],
        "variant_inputs": ["4\n1 2 3 4", "2\n1 2"],
        "starter_archetype": "array",
        "solver": solver_200
    }
]
