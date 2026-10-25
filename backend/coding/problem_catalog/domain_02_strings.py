"""
Domain 2: Python - String & Parsing (20 problems)
"""
import re

def solve_valid_palindrome(s):
    cleaned = [c.lower() for c in s.strip() if c.isalnum()]
    return "true" if cleaned == cleaned[::-1] else "false"

def solve_reverse_words(s):
    words = s.strip().split()
    return " ".join(reversed(words))

def solve_longest_common_prefix(s):
    toks = s.strip().split()
    if not toks: return ""
    n = int(toks[0])
    strs = toks[1:1+n]
    if not strs: return ""
    prefix = strs[0]
    for w in strs[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return "empty"
    return prefix if prefix else "empty"

def solve_string_compression(s):
    s = s.strip()
    if not s: return ""
    res = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        res.append(f"{s[i]}{j - i}")
        i = j
    return "".join(res)

def solve_valid_anagram(s):
    toks = s.strip().split()
    if len(toks) < 2: return "false"
    s1, s2 = toks[0], toks[1]
    return "true" if sorted(s1) == sorted(s2) else "false"

def solve_group_anagrams(s):
    toks = s.strip().split()
    if not toks: return "0"
    n = int(toks[0])
    words = toks[1:1+n]
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return str(len(groups))

def solve_longest_palindrome_sub(s):
    s = s.strip()
    if not s: return ""
    res = ""
    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
    return res

def solve_count_and_say(s):
    n = int(s.strip())
    cur = "1"
    for _ in range(n - 1):
        nxt = []
        i = 0
        while i < len(cur):
            j = i
            while j < len(cur) and cur[j] == cur[i]:
                j += 1
            nxt.append(f"{j - i}{cur[i]}")
            i = j
        cur = "".join(nxt)
    return cur

def solve_roman_to_int(s):
    roman = s.strip()
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and vals[roman[i]] < vals[roman[i+1]]:
            ans -= vals[roman[i]]
        else:
            ans += vals[roman[i]]
    return str(ans)

def solve_int_to_roman(s):
    num = int(s.strip())
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    res = []
    for val, sym in mapping:
        while num >= val:
            res.append(sym)
            num -= val
    return "".join(res)

def solve_zigzag(s):
    toks = s.strip().split()
    if not toks: return ""
    text = toks[0]
    numRows = int(toks[1])
    if numRows == 1 or numRows >= len(text):
        return text
    rows = [[] for _ in range(numRows)]
    r, step = 0, 1
    for c in text:
        rows[r].append(c)
        if r == 0: step = 1
        elif r == numRows - 1: step = -1
        r += step
    return "".join("".join(row) for row in rows)

def solve_decode_string(s):
    s = s.strip()
    stack = []
    cur_num = 0
    cur_str = []
    for c in s:
        if c.isdigit():
            cur_num = cur_num * 10 + int(c)
        elif c == '[':
            stack.append((cur_str, cur_num))
            cur_str = []
            cur_num = 0
        elif c == ']':
            prev_str, k = stack.pop()
            cur_str = prev_str + cur_str * k
        else:
            cur_str.append(c)
    return "".join(cur_str)

def solve_word_break(s):
    toks = s.strip().split()
    if len(toks) < 3: return "false"
    target = toks[0]
    n = int(toks[1])
    words = set(toks[2:2+n])
    dp = [False] * (len(target) + 1)
    dp[0] = True
    for i in range(1, len(target) + 1):
        for j in range(i):
            if dp[j] and target[j:i] in words:
                dp[i] = True
                break
    return "true" if dp[len(target)] else "false"

def solve_isomorphic(s):
    toks = s.strip().split()
    if len(toks) < 2: return "false"
    s1, s2 = toks[0], toks[1]
    if len(s1) != len(s2): return "false"
    m1, m2 = {}, {}
    for c1, c2 in zip(s1, s2):
        if m1.get(c1, c2) != c2 or m2.get(c2, c1) != c1:
            return "false"
        m1[c1] = c2
        m2[c2] = c1
    return "true"

def solve_repeated_substring_match(s):
    toks = s.strip().split()
    if len(toks) < 2: return "-1"
    a, b = toks[0], toks[1]
    times = (len(b) // len(a)) + 2
    for count in range(1, times + 2):
        if b in (a * count):
            return str(count)
    return "-1"

def solve_wildcard_matching(s):
    toks = s.strip().split()
    if len(toks) < 2: return "false"
    text, pat = toks[0], toks[1]
    n, m = len(text), len(pat)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(1, m + 1):
        if pat[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pat[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif pat[j-1] in (text[i-1], '?'):
                dp[i][j] = dp[i-1][j-1]
    return "true" if dp[n][m] else "false"

def solve_regex_matching(s):
    toks = s.strip().split()
    if len(toks) < 2: return "false"
    text, pat = toks[0], toks[1]
    n, m = len(text), len(pat)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(1, m + 1):
        if pat[j-1] == '*' and j >= 2:
            dp[0][j] = dp[0][j-2]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pat[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if pat[j-2] in (text[i-1], '.'):
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif pat[j-1] in (text[i-1], '.'):
                dp[i][j] = dp[i-1][j-1]
    return "true" if dp[n][m] else "false"

def solve_min_window(s):
    toks = s.strip().split()
    if len(toks) < 2: return ""
    S, T = toks[0], toks[1]
    from collections import Counter
    target_cnt = Counter(T)
    needed = len(target_cnt)
    window = {}
    have = 0
    res_len = float('inf')
    res = ""
    l = 0
    for r, c in enumerate(S):
        window[c] = window.get(c, 0) + 1
        if c in target_cnt and window[c] == target_cnt[c]:
            have += 1
        while have == needed:
            if (r - l + 1) < res_len:
                res_len = r - l + 1
                res = S[l:r+1]
            window[S[l]] -= 1
            if S[l] in target_cnt and window[S[l]] < target_cnt[S[l]]:
                have -= 1
            l += 1
    return res if res else "empty"

def solve_distinct_subsequences(s):
    toks = s.strip().split()
    if len(toks) < 2: return "0"
    S, T = toks[0], toks[1]
    n, m = len(S), len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return str(dp[n][m])

def solve_text_justification_lines(s):
    toks = s.strip().split()
    if not toks: return "0"
    width = int(toks[0])
    n = int(toks[1])
    words = toks[2:2+n]
    lines = []
    cur_line, cur_len = [], 0
    for w in words:
        if cur_len + len(w) + len(cur_line) <= width:
            cur_line.append(w)
            cur_len += len(w)
        else:
            lines.append(cur_line)
            cur_line = [w]
            cur_len = len(w)
    if cur_line:
        lines.append(cur_line)
    return str(len(lines))

PROBLEMS = [
    {
        "title_base": "Valid Palindrome Phrase",
        "description": "A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.",
        "input_format": "Line 1: A string representing the phrase",
        "output_format": "Output 'true' if it is a palindrome, or 'false' otherwise.",
        "constraints": "1 <= length <= 2 * 10^5",
        "io_type": "single_string",
        "sample_input": "A man, a plan, a canal: Panama",
        "sample_output": "true",
        "explanation": "'amanaplanacanalpanama' is a palindrome.",
        "test_inputs": [
            "A man, a plan, a canal: Panama",
            "race a car",
            " ",
            "Madam, I'm Adam."
        ],
        "variant_inputs": [
            "Was it a car or a cat I saw?",
            "No lemon, no melon",
            "Not a palindrome at all!",
            "12321"
        ],
        "solver": solve_valid_palindrome
    },
    {
        "title_base": "Reverse Words in Sentence",
        "description": "Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. Return a string of the words in reverse order concatenated by a single space.",
        "input_format": "Line 1: A string containing words separated by spaces",
        "output_format": "Output the sentence with words reversed.",
        "constraints": "1 <= s.length <= 10^4",
        "io_type": "single_string",
        "sample_input": "the sky is blue",
        "sample_output": "blue is sky the",
        "explanation": "The words are reversed in order.",
        "test_inputs": [
            "the sky is blue",
            "  hello world  ",
            "a good   example",
            "antigravity"
        ],
        "variant_inputs": [
            "data structures and algorithms",
            "one two three four",
            "coding challenge platform",
            "AI engineering pro"
        ],
        "solver": solve_reverse_words
    },
    {
        "title_base": "Longest Common Prefix",
        "description": "Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return 'empty'.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated strings",
        "output_format": "Output the longest common prefix or 'empty'.",
        "constraints": "1 <= N <= 200\n0 <= strings[i].length <= 200",
        "io_type": "general",
        "sample_input": "3\nflower flow flight",
        "sample_output": "fl",
        "explanation": "The longest common prefix is 'fl'.",
        "test_inputs": [
            "3\nflower flow flight",
            "3\ndog racecar car",
            "1\napple",
            "2\ninterspecies interstellar"
        ],
        "variant_inputs": [
            "4\nprefix preview prepare pretend",
            "3\nthrone throne throat",
            "2\ncat dog",
            "3\naaa aa a"
        ],
        "solver": solve_longest_common_prefix
    },
    {
        "title_base": "String Compression Format",
        "description": "Given a string of repeated characters, compress the string such that each consecutive run of identical characters is followed by its frequency count.",
        "input_format": "Line 1: A string to compress",
        "output_format": "Output the compressed format string.",
        "constraints": "1 <= s.length <= 10^4",
        "io_type": "single_string",
        "sample_input": "aabcccccaaa",
        "sample_output": "a2b1c5a3",
        "explanation": "'a' appears 2 times, 'b' 1 time, 'c' 5 times, 'a' 3 times.",
        "test_inputs": [
            "aabcccccaaa",
            "abcd",
            "aaaaa",
            "wwweeeqqq"
        ],
        "variant_inputs": [
            "aabbbccccddddd",
            "z",
            "kkklllmmm",
            "aaabbbccc"
        ],
        "solver": solve_string_compression
    },
    {
        "title_base": "Valid Anagram Strings",
        "description": "Given two strings s and t, return 'true' if t is an anagram of s, and 'false' otherwise.",
        "input_format": "Line 1: Two space-separated strings s and t",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "1 <= s.length, t.length <= 5 * 10^4",
        "io_type": "two_strings",
        "sample_input": "anagram nagaram",
        "sample_output": "true",
        "explanation": "Both strings contain the exact same characters with the same frequencies.",
        "test_inputs": [
            "anagram nagaram",
            "rat car",
            "listen silent",
            "a b"
        ],
        "variant_inputs": [
            "triangle integral",
            "apple pale",
            "secure rescue",
            "hello world"
        ],
        "solver": solve_valid_anagram
    },
    {
        "title_base": "Group Anagram Words",
        "description": "Given an array of strings, group the anagrams together. Output the total number of distinct anagram groups formed.",
        "input_format": "Line 1: An integer N\nLine 2: N space-separated strings",
        "output_format": "Output the count of anagram groups.",
        "constraints": "1 <= N <= 10^4",
        "io_type": "general",
        "sample_input": "6\neat tea tan ate nat bat",
        "sample_output": "3",
        "explanation": "Groups are [\"bat\"], [\"nat\",\"tan\"], and [\"ate\",\"eat\",\"tea\"]. Total = 3 groups.",
        "test_inputs": [
            "6\neat tea tan ate nat bat",
            "1\na",
            "3\na b c",
            "4\nlisten silent elbow below"
        ],
        "variant_inputs": [
            "5\ncat tac act dog god",
            "4\none two three four",
            "2\nloop pool",
            "3\naa bb cc"
        ],
        "solver": solve_group_anagrams
    },
    {
        "title_base": "Longest Palindromic Substring",
        "description": "Given a string s, return the longest palindromic substring in s.",
        "input_format": "Line 1: A string s",
        "output_format": "Output the longest palindromic substring.",
        "constraints": "1 <= s.length <= 1000",
        "io_type": "single_string",
        "sample_input": "babad",
        "sample_output": "bab",
        "explanation": "'bab' is a valid longest palindromic substring ('aba' is also valid).",
        "test_inputs": [
            "babad",
            "cbbd",
            "a",
            "racecar"
        ],
        "variant_inputs": [
            "forgeeksskeegfor",
            "bananas",
            "abacdfgdcaba",
            "noon"
        ],
        "solver": solve_longest_palindrome_sub
    },
    {
        "title_base": "Count and Say Sequence",
        "description": "The count-and-say sequence is a sequence of digit strings defined by the rule that each term describes the character run-lengths of the previous term. Given an integer n, generate the nth term.",
        "input_format": "Line 1: An integer n",
        "output_format": "Output the nth count-and-say string.",
        "constraints": "1 <= n <= 30",
        "io_type": "single_number",
        "sample_input": "4",
        "sample_output": "1211",
        "explanation": "n=1: '1', n=2: '11', n=3: '21', n=4: '1211'.",
        "test_inputs": [
            "4",
            "1",
            "5",
            "2"
        ],
        "variant_inputs": [
            "6",
            "7",
            "3",
            "8"
        ],
        "solver": solve_count_and_say
    },
    {
        "title_base": "Roman to Integer Conversion",
        "description": "Given a roman numeral string, convert it to an integer.",
        "input_format": "Line 1: A valid Roman numeral string",
        "output_format": "Output the converted integer value.",
        "constraints": "s contains only characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'). Value <= 3999.",
        "io_type": "single_string",
        "sample_input": "MCMXCIV",
        "sample_output": "1994",
        "explanation": "M = 1000, CM = 900, XC = 90 and IV = 4, total = 1994.",
        "test_inputs": [
            "MCMXCIV",
            "III",
            "LVIII",
            "IX"
        ],
        "variant_inputs": [
            "XL",
            "CD",
            "MMXXVI",
            "X"
        ],
        "solver": solve_roman_to_int
    },
    {
        "title_base": "Integer to Roman Numeral",
        "description": "Given an integer, convert it to a roman numeral string.",
        "input_format": "Line 1: An integer n",
        "output_format": "Output the Roman numeral string representation.",
        "constraints": "1 <= n <= 3999",
        "io_type": "single_number",
        "sample_input": "1994",
        "sample_output": "MCMXCIV",
        "explanation": "1000 = M, 900 = CM, 90 = XC, 4 = IV.",
        "test_inputs": [
            "1994",
            "3",
            "58",
            "9"
        ],
        "variant_inputs": [
            "40",
            "400",
            "2026",
            "10"
        ],
        "solver": solve_int_to_roman
    },
    {
        "title_base": "Zigzag Conversion",
        "description": "The string is written in a zigzag pattern on a given number of rows, then read line by line. Output the zigzag encoded string.",
        "input_format": "Line 1: String and integer numRows separated by space",
        "output_format": "Output the converted zigzag string.",
        "constraints": "1 <= s.length <= 1000\n1 <= numRows <= 1000",
        "io_type": "general",
        "sample_input": "PAYPALISHIRING 3",
        "sample_output": "PAHNAPLSIIGYIR",
        "explanation": "Writing in 3 rows and reading row by row yields 'PAHNAPLSIIGYIR'.",
        "test_inputs": [
            "PAYPALISHIRING 3",
            "PAYPALISHIRING 4",
            "A 1",
            "ABCDE 2"
        ],
        "variant_inputs": [
            "ANTIGRAVITY 3",
            "HELLOWORLD 4",
            "PYTHON 2",
            "TEST 1"
        ],
        "solver": solve_zigzag
    },
    {
        "title_base": "Decode String Pattern",
        "description": "Given an encoded string formatted as k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times, return its decoded string.",
        "input_format": "Line 1: Encoded string",
        "output_format": "Output the fully decoded string.",
        "constraints": "1 <= s.length <= 1000",
        "io_type": "single_string",
        "sample_input": "3[a]2[bc]",
        "sample_output": "aaabcbc",
        "explanation": "3 'a' followed by 2 'bc' -> 'aaabcbc'.",
        "test_inputs": [
            "3[a]2[bc]",
            "3[a2[c]]",
            "2[abc]3[cd]ef",
            "10[a]"
        ],
        "variant_inputs": [
            "2[2[y]pq]3[a]",
            "3[z]2[2[b]]",
            "1[code]",
            "2[ab3[c]]"
        ],
        "solver": solve_decode_string
    },
    {
        "title_base": "Word Break Problem",
        "description": "Given a string s and a dictionary of strings wordDict, return 'true' if s can be segmented into a space-separated sequence of one or more dictionary words.",
        "input_format": "Line 1: Target string s\nLine 2: An integer N\nLine 3: N space-separated dictionary words",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "1 <= s.length <= 300\n1 <= wordDict.length <= 1000",
        "io_type": "general",
        "sample_input": "leetcode 2\nleet code",
        "sample_output": "true",
        "explanation": "'leetcode' can be segmented as 'leet code'.",
        "test_inputs": [
            "leetcode 2\nleet code",
            "applepenapple 2\napple pen",
            "catsandog 5\ncats dog sand and cat",
            "a 1\na"
        ],
        "variant_inputs": [
            "cars 2\ncar ca",
            "goalspecial 2\ngoal special",
            "program 2\npro gram",
            "abcd 2\nab cd"
        ],
        "solver": solve_word_break
    },
    {
        "title_base": "Isomorphic String Check",
        "description": "Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t under a 1-to-1 character mapping.",
        "input_format": "Line 1: Two space-separated strings s and t",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "1 <= s.length <= 5 * 10^4\nt.length == s.length",
        "io_type": "two_strings",
        "sample_input": "egg add",
        "sample_output": "true",
        "explanation": "'e' maps to 'a', 'g' maps to 'd'.",
        "test_inputs": [
            "egg add",
            "foo bar",
            "paper title",
            "ab aa"
        ],
        "variant_inputs": [
            "badc baba",
            "turtle tslrle",
            "paper title",
            "xyz abc"
        ],
        "solver": solve_isomorphic
    },
    {
        "title_base": "Repeated Substring Match",
        "description": "Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring of a after any number of repeats, return -1.",
        "input_format": "Line 1: Two space-separated strings a and b",
        "output_format": "Output the minimum repetitions or -1.",
        "constraints": "1 <= a.length, b.length <= 10^4",
        "io_type": "two_strings",
        "sample_input": "abcd cdabcda",
        "sample_output": "3",
        "explanation": "Repeating a 3 times gives 'abcdabcdabcd', which contains b.",
        "test_inputs": [
            "abcd cdabcda",
            "a aa",
            "a a",
            "abc def"
        ],
        "variant_inputs": [
            "abc cba",
            "ab b",
            "baa aab",
            "xyz yzxyzx"
        ],
        "solver": solve_repeated_substring_match
    },
    {
        "title_base": "Wildcard Pattern Matching",
        "description": "Given an input string s and a pattern p, implement wildcard pattern matching with support for '?' (matches any single char) and '*' (matches any sequence of chars).",
        "input_format": "Line 1: Two space-separated strings: text and pattern",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "0 <= s.length, p.length <= 2000",
        "io_type": "two_strings",
        "sample_input": "aa *",
        "sample_output": "true",
        "explanation": "'*' matches any sequence, including 'aa'.",
        "test_inputs": [
            "aa *",
            "cb ?a",
            "adceb *a*b",
            "acdcb a*c?b"
        ],
        "variant_inputs": [
            "abc a?c",
            "hello h*d",
            "mississippi m*i*p*.",
            "code c*e"
        ],
        "solver": solve_wildcard_matching
    },
    {
        "title_base": "Regular Expression Engine",
        "description": "Given an input string s and a pattern p, implement regular expression matching with support for '.' (matches any single character) and '*' (matches zero or more of the preceding element).",
        "input_format": "Line 1: Two space-separated strings: text and pattern",
        "output_format": "Output 'true' or 'false'.",
        "constraints": "1 <= s.length, p.length <= 20",
        "io_type": "two_strings",
        "sample_input": "aa a*",
        "sample_output": "true",
        "explanation": "'*' repeats 'a', matching 'aa'.",
        "test_inputs": [
            "aa a*",
            "aa a",
            "ab .* ",
            "aab c*a*b"
        ],
        "variant_inputs": [
            "mississippi mis*is*p*.",
            "hello h.*o",
            "abc a.c",
            "aaa a*a"
        ],
        "solver": solve_regex_matching
    },
    {
        "title_base": "Minimum Window Substring",
        "description": "Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If no such substring exists, return 'empty'.",
        "input_format": "Line 1: Two space-separated strings s and t",
        "output_format": "Output the minimum window substring or 'empty'.",
        "constraints": "1 <= s.length, t.length <= 10^5",
        "io_type": "two_strings",
        "sample_input": "ADOBECODEBANC ABC",
        "sample_output": "BANC",
        "explanation": "The minimum window substring 'BANC' includes 'A', 'B', and 'C' from string t.",
        "test_inputs": [
            "ADOBECODEBANC ABC",
            "a a",
            "a aa",
            "XAYBZC ABC"
        ],
        "variant_inputs": [
            "ABBACBA ABC",
            "HELLO LLO",
            "KAVITA VIT",
            "CAT DOG"
        ],
        "solver": solve_min_window
    },
    {
        "title_base": "Distinct Subsequences Count",
        "description": "Given two strings s and t, return the number of distinct subsequences of s which equals t.",
        "input_format": "Line 1: Two space-separated strings s and t",
        "output_format": "Output the count of distinct subsequences.",
        "constraints": "1 <= s.length, t.length <= 1000",
        "io_type": "two_strings",
        "sample_input": "rabbbit rabbit",
        "sample_output": "3",
        "explanation": "There are 3 ways you can generate 'rabbit' from 'rabbbit'.",
        "test_inputs": [
            "rabbbit rabbit",
            "babgbag bag",
            "abc abc",
            "a b"
        ],
        "variant_inputs": [
            "banana an",
            "geeksforgeeks ge",
            "aaaa a",
            "test est"
        ],
        "solver": solve_distinct_subsequences
    },
    {
        "title_base": "Text Justification Formatter",
        "description": "Given an array of words and a maxWidth, count the number of lines required to format the text such that each line has exactly maxWidth characters and is fully justified.",
        "input_format": "Line 1: An integer maxWidth\nLine 2: An integer N\nLine 3: N space-separated words",
        "output_format": "Output the number of formatted lines.",
        "constraints": "1 <= words.length <= 300\n1 <= maxWidth <= 100",
        "io_type": "general",
        "sample_input": "16\n7\nThis is an example of text justification.",
        "sample_output": "3",
        "explanation": "Text packs into 3 justified lines.",
        "test_inputs": [
            "16\n7\nThis is an example of text justification.",
            "16\n6\nWhat must be acknowledgment shall be",
            "20\n3\nScience is what",
            "10\n2\nHello world"
        ],
        "variant_inputs": [
            "14\n4\nCode challenge platform pro",
            "25\n5\nFull stack web developer role",
            "12\n3\nFast safe code",
            "8\n2\nGo win"
        ],
        "solver": solve_text_justification_lines
    }
]
