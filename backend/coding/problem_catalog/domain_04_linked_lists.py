# Domain 04: C++ - Pointers & Linked Lists (Problems 61 - 80)

def solver_61(s: str) -> str:
    # Reverse Singly Linked List
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    arr = parts[1:1+n]
    return " ".join(reversed(arr))

def solver_62(s: str) -> str:
    # Merge Two Sorted Linked Lists
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    m = int(parts[1])
    idx = 2
    l1 = [int(x) for x in parts[idx:idx+n]]
    idx += n
    l2 = [int(x) for x in parts[idx:idx+m]]
    res = sorted(l1 + l2)
    return " ".join(str(x) for x in res)

def solver_63(s: str) -> str:
    # Detect Cycle in Linked List
    parts = s.strip().split()
    if not parts: return "false"
    n = int(parts[0])
    pos = int(parts[1])
    return "true" if pos >= 0 else "false"

def solver_64(s: str) -> str:
    # Find Cycle Beginning Node
    parts = s.strip().split()
    if not parts: return "-1"
    n = int(parts[0])
    pos = int(parts[1])
    idx = 2
    vals = parts[idx:idx+n]
    if 0 <= pos < len(vals):
        return vals[pos]
    return "-1"

def solver_65(s: str) -> str:
    # Middle Node of Linked List
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    mid = len(vals) // 2
    return vals[mid]

def solver_66(s: str) -> str:
    # Remove Nth Node From End
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    k = int(parts[1])
    vals = parts[2:2+n]
    remove_idx = n - k
    if 0 <= remove_idx < len(vals):
        del vals[remove_idx]
    return " ".join(vals)

def solver_67(s: str) -> str:
    # Add Two Numbers in Lists (digits in reverse order)
    parts = s.strip().split()
    if not parts: return "0"
    n = int(parts[0])
    m = int(parts[1])
    idx = 2
    l1 = [int(x) for x in parts[idx:idx+n]]
    idx += n
    l2 = [int(x) for x in parts[idx:idx+m]]
    res = []
    carry = 0
    p1, p2 = 0, 0
    while p1 < len(l1) or p2 < len(l2) or carry:
        v1 = l1[p1] if p1 < len(l1) else 0
        v2 = l2[p2] if p2 < len(l2) else 0
        total = v1 + v2 + carry
        carry = total // 10
        res.append(total % 10)
        p1 += 1
        p2 += 1
    return " ".join(str(x) for x in res)

def solver_68(s: str) -> str:
    # Palindrome Linked List Check
    parts = s.strip().split()
    if not parts: return "true"
    n = int(parts[0])
    vals = parts[1:1+n]
    return "true" if vals == vals[::-1] else "false"

def solver_69(s: str) -> str:
    # Intersection Node of Two Lists
    # Input format: intersectVal n m skipA skipB followed by arrA then arrB
    parts = s.strip().split()
    if not parts: return "null"
    inter_val = parts[0]
    return inter_val

def solver_70(s: str) -> str:
    # Remove Duplicates from Sorted List
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    res = []
    for v in vals:
        if not res or res[-1] != v:
            res.append(v)
    return " ".join(res)

def solver_71(s: str) -> str:
    # Remove All Duplicate Valued Nodes (leave only distinct)
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    from collections import Counter
    c = Counter(vals)
    res = [x for x in vals if c[x] == 1]
    return " ".join(res)

def solver_72(s: str) -> str:
    # Rotate List by K Steps right
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    k = int(parts[1])
    vals = parts[2:2+n]
    if not vals: return ""
    k = k % len(vals)
    if k == 0: return " ".join(vals)
    res = vals[-k:] + vals[:-k]
    return " ".join(res)

def solver_73(s: str) -> str:
    # Partition List around Value X
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    x = int(parts[1])
    vals = [int(v) for v in parts[2:2+n]]
    less = [v for v in vals if v < x]
    ge = [v for v in vals if v >= x]
    return " ".join(str(v) for v in (less + ge))

def solver_74(s: str) -> str:
    # Reorder List Pattern (L0 -> Ln -> L1 -> Ln-1 ...)
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    res = []
    i, j = 0, len(vals) - 1
    while i <= j:
        if i == j:
            res.append(vals[i])
            break
        res.append(vals[i])
        res.append(vals[j])
        i += 1
        j -= 1
    return " ".join(res)

def solver_75(s: str) -> str:
    # Odd Even Linked List (group odd-indexed nodes then even-indexed nodes, 1-based)
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    odds = [vals[i] for i in range(len(vals)) if i % 2 == 0]
    evens = [vals[i] for i in range(len(vals)) if i % 2 == 1]
    return " ".join(odds + evens)

def solver_76(s: str) -> str:
    # Sort Linked List in O(N log N)
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = [int(x) for x in parts[1:1+n]]
    vals.sort()
    return " ".join(str(x) for x in vals)

def solver_77(s: str) -> str:
    # Reverse Nodes in k-Group
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    k = int(parts[1])
    vals = parts[2:2+n]
    res = []
    for i in range(0, len(vals), k):
        grp = vals[i:i+k]
        if len(grp) == k:
            res.extend(reversed(grp))
        else:
            res.extend(grp)
    return " ".join(res)

def solver_78(s: str) -> str:
    # Merge K Sorted Linked Lists
    parts = s.strip().split()
    if not parts: return ""
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

def solver_79(s: str) -> str:
    # Copy List with Random Pointer
    # Input: N followed by values
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    return " ".join(vals)

def solver_80(s: str) -> str:
    # Flatten Multilevel Doubly List
    parts = s.strip().split()
    if not parts: return ""
    n = int(parts[0])
    vals = parts[1:1+n]
    return " ".join(vals)

PROBLEMS = [
    {
        "index": 61,
        "title_base": "Reverse Singly Linked List",
        "description": "Given the head of a singly linked list with N nodes, reverse the list and return the reversed list values.",
        "input_format": "The first line contains integer N. The second line contains N integers representing the node values.",
        "output_format": "Print the values of the reversed linked list separated by spaces.",
        "constraints": "1 <= N <= 10^5, -10^6 <= Node.val <= 10^6",
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "5 4 3 2 1",
        "explanation": "Reversing 1 -> 2 -> 3 -> 4 -> 5 results in 5 -> 4 -> 3 -> 2 -> 1.",
        "test_inputs": ["1\n100", "4\n10 20 30 40"],
        "variant_inputs": ["6\n1 2 3 4 5 6", "5\n9 8 7 6 5"],
        "starter_archetype": "array",
        "solver": solver_61
    },
    {
        "index": 62,
        "title_base": "Merge Two Sorted Linked Lists",
        "description": "Given the heads of two sorted linked lists list1 and list2 of size N and M respectively, merge the two lists into one sorted list.",
        "input_format": "First line contains N and M. Second line contains N integers for list1. Third line contains M integers for list2.",
        "output_format": "Print the merged sorted list values separated by spaces.",
        "constraints": "0 <= N, M <= 10^4, -10^5 <= Node.val <= 10^5",
        "sample_input": "3 3\n1 2 4\n1 3 4",
        "sample_output": "1 1 2 3 4 4",
        "explanation": "Merging [1, 2, 4] and [1, 3, 4] yields [1, 1, 2, 3, 4, 4].",
        "test_inputs": ["1 1\n2\n1", "2 3\n1 5\n2 3 6"],
        "variant_inputs": ["3 4\n10 20 30\n5 15 25 35", "2 2\n1 10\n2 20"],
        "starter_archetype": "general",
        "solver": solver_62
    },
    {
        "index": 63,
        "title_base": "Detect Cycle in Linked List",
        "description": "Given head, the head of a linked list, determine if the linked list has a cycle in it using Floyd's Tortoise and Hare algorithm.",
        "input_format": "First line contains N and pos (0-indexed position where the tail connects, or -1 if no cycle). Second line contains N integers.",
        "output_format": "Print 'true' if there is a cycle, otherwise 'false'.",
        "constraints": "0 <= N <= 10^4, -1 <= pos < N",
        "sample_input": "4 1\n3 2 0 -4",
        "sample_output": "true",
        "explanation": "There is a cycle where tail connects to the 1st node (0-indexed).",
        "test_inputs": ["2 0\n1 2", "1 -1\n1"],
        "variant_inputs": ["5 -1\n1 2 3 4 5", "5 2\n1 2 3 4 5"],
        "starter_archetype": "general",
        "solver": solver_63
    },
    {
        "index": 64,
        "title_base": "Find Cycle Beginning Node",
        "description": "Given the head of a linked list, return the value of the node where the cycle begins. If there is no cycle, return -1.",
        "input_format": "First line contains N and pos (-1 if no cycle). Second line contains N integers.",
        "output_format": "Print the value of the node where cycle begins or -1.",
        "constraints": "0 <= N <= 10^4, -1 <= pos < N",
        "sample_input": "4 1\n3 2 0 -4",
        "sample_output": "2",
        "explanation": "The tail connects to index 1 which has value 2.",
        "test_inputs": ["2 0\n1 2", "1 -1\n1"],
        "variant_inputs": ["5 3\n10 20 30 40 50", "4 -1\n1 2 3 4"],
        "starter_archetype": "general",
        "solver": solver_64
    },
    {
        "index": 65,
        "title_base": "Middle Node of Linked List",
        "description": "Given the head of a singly linked list, return the value of the middle node of the linked list. If there are two middle nodes, return the second middle node.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the value of the middle node.",
        "constraints": "1 <= N <= 10^5, 1 <= Node.val <= 10^5",
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "3",
        "explanation": "The middle node of [1, 2, 3, 4, 5] is 3.",
        "test_inputs": ["6\n1 2 3 4 5 6", "1\n42"],
        "variant_inputs": ["7\n10 20 30 40 50 60 70", "4\n2 4 6 8"],
        "starter_archetype": "array",
        "solver": solver_65
    },
    {
        "index": 66,
        "title_base": "Remove Nth Node From End",
        "description": "Given the head of a linked list, remove the nth node from the end of the list and return its values in one pass.",
        "input_format": "First line contains N and k (the 1-based index from end). Second line contains N integers.",
        "output_format": "Print the remaining linked list values separated by spaces.",
        "constraints": "1 <= k <= N <= 10^4",
        "sample_input": "5 2\n1 2 3 4 5",
        "sample_output": "1 2 3 5",
        "explanation": "Removing the 2nd node from end (4) results in 1 2 3 5.",
        "test_inputs": ["3 1\n1 2 3", "2 1\n1 2"],
        "variant_inputs": ["6 3\n10 20 30 40 50 60", "3 3\n1 2 3"],
        "starter_archetype": "target_and_array",
        "solver": solver_66
    },
    {
        "index": 67,
        "title_base": "Add Two Numbers in Lists",
        "description": "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.",
        "input_format": "First line contains N and M. Second line contains N space-separated digits of list1. Third line contains M digits of list2.",
        "output_format": "Print the digits of the sum in reverse order separated by spaces.",
        "constraints": "1 <= N, M <= 100, 0 <= Node.val <= 9",
        "sample_input": "3 3\n2 4 3\n5 6 4",
        "sample_output": "7 0 8",
        "explanation": "342 + 465 = 807, represented in reverse as 7 -> 0 -> 8.",
        "test_inputs": ["1 1\n0\n0", "7 4\n9 9 9 9 9 9 9\n9 9 9 9"],
        "variant_inputs": ["3 3\n5 5 5\n5 5 5", "2 2\n9 9\n1 0"],
        "starter_archetype": "general",
        "solver": solver_67
    },
    {
        "index": 68,
        "title_base": "Palindrome Linked List Check",
        "description": "Given the head of a singly linked list, return 'true' if it is a palindrome, or 'false' otherwise in O(1) space.",
        "input_format": "First line contains integer N. Second line contains N integers.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "1 <= N <= 10^5, -10^6 <= Node.val <= 10^6",
        "sample_input": "4\n1 2 2 1",
        "sample_output": "true",
        "explanation": "1 -> 2 -> 2 -> 1 is a palindrome.",
        "test_inputs": ["2\n1 2", "1\n5"],
        "variant_inputs": ["5\n1 2 3 2 1", "4\n1 2 3 4"],
        "starter_archetype": "array",
        "solver": solver_68
    },
    {
        "index": 69,
        "title_base": "Intersection Node of Two Lists",
        "description": "Given the heads of two singly linked-lists headA and headB, return the value of the node at which the two lists intersect. If they do not intersect, return null.",
        "input_format": "First line contains intersectVal (the value or 'null'), N, M, skipA, skipB. Next lines contain list elements.",
        "output_format": "Print the intersection node value or 'null'.",
        "constraints": "1 <= N, M <= 3 * 10^4",
        "sample_input": "8 5 6 2 3\n4 1 8 4 5\n5 6 1 8 4 5",
        "sample_output": "8",
        "explanation": "The intersected node has value 8.",
        "test_inputs": ["2 3 3 1 1\n1 2 3\n4 2 3", "null 2 3 2 3\n1 2\n3 4 5"],
        "variant_inputs": ["15 4 4 2 2\n1 2 15 20\n3 4 15 20", "null 3 3 3 3\n1 2 3\n4 5 6"],
        "starter_archetype": "general",
        "solver": solver_69
    },
    {
        "index": 70,
        "title_base": "Remove Duplicates from Sorted List",
        "description": "Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.",
        "input_format": "First line contains N. Second line contains N sorted integers.",
        "output_format": "Print the deduplicated list values separated by spaces.",
        "constraints": "0 <= N <= 300, -100 <= Node.val <= 100",
        "sample_input": "5\n1 1 2 3 3",
        "sample_output": "1 2 3",
        "explanation": "Duplicates of 1 and 3 are removed leaving 1 2 3.",
        "test_inputs": ["3\n1 1 2", "5\n1 1 1 1 1"],
        "variant_inputs": ["6\n2 2 3 3 4 5", "4\n10 10 20 20"],
        "starter_archetype": "array",
        "solver": solver_70
    },
    {
        "index": 71,
        "title_base": "Remove All Duplicate Valued Nodes",
        "description": "Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.",
        "input_format": "First line contains N. Second line contains N sorted integers.",
        "output_format": "Print the distinct node values separated by spaces.",
        "constraints": "0 <= N <= 300, -100 <= Node.val <= 100",
        "sample_input": "7\n1 2 3 3 4 4 5",
        "sample_output": "1 2 5",
        "explanation": "Values 3 and 4 appear multiple times and are removed, leaving 1 2 5.",
        "test_inputs": ["5\n1 1 1 2 3", "4\n1 1 2 3"],
        "variant_inputs": ["6\n1 2 2 3 4 4", "5\n10 20 30 40 50"],
        "starter_archetype": "array",
        "solver": solver_71
    },
    {
        "index": 72,
        "title_base": "Rotate List by K Steps",
        "description": "Given the head of a linked list, rotate the list to the right by k places.",
        "input_format": "First line contains N and k. Second line contains N integers.",
        "output_format": "Print the rotated list values separated by spaces.",
        "constraints": "0 <= N <= 500, 0 <= k <= 2 * 10^9",
        "sample_input": "5 2\n1 2 3 4 5",
        "sample_output": "4 5 1 2 3",
        "explanation": "Rotate 1: 5 1 2 3 4; Rotate 2: 4 5 1 2 3.",
        "test_inputs": ["3 4\n0 1 2", "1 99\n1"],
        "variant_inputs": ["5 5\n1 2 3 4 5", "4 1\n10 20 30 40"],
        "starter_archetype": "target_and_array",
        "solver": solver_72
    },
    {
        "index": 73,
        "title_base": "Partition List around Value X",
        "description": "Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x while preserving relative order.",
        "input_format": "First line contains N and x. Second line contains N integers.",
        "output_format": "Print the partitioned list values separated by spaces.",
        "constraints": "0 <= N <= 200, -100 <= Node.val <= 100, -200 <= x <= 200",
        "sample_input": "6 3\n1 4 3 2 5 2",
        "sample_output": "1 2 2 4 3 5",
        "explanation": "Nodes less than 3 are [1, 2, 2], nodes >= 3 are [4, 3, 5]. Combined: 1 2 2 4 3 5.",
        "test_inputs": ["2 2\n2 1", "3 5\n1 2 3"],
        "variant_inputs": ["5 3\n5 4 3 2 1", "4 10\n12 5 8 15"],
        "starter_archetype": "target_and_array",
        "solver": solver_73
    },
    {
        "index": 74,
        "title_base": "Reorder List Pattern",
        "description": "You are given the head of a singly linked-list: L0 -> L1 -> ... -> Ln - 1 -> Ln. Reorder the list to be on the form: L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the reordered list values separated by spaces.",
        "constraints": "1 <= N <= 5 * 10^4, 1 <= Node.val <= 1000",
        "sample_input": "4\n1 2 3 4",
        "sample_output": "1 4 2 3",
        "explanation": "1 2 3 4 becomes 1 4 2 3.",
        "test_inputs": ["5\n1 2 3 4 5", "1\n10"],
        "variant_inputs": ["6\n10 20 30 40 50 60", "3\n1 2 3"],
        "starter_archetype": "array",
        "solver": solver_74
    },
    {
        "index": 75,
        "title_base": "Odd Even Linked List",
        "description": "Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices (1-based indices), and return the reordered list.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the reordered list values separated by spaces.",
        "constraints": "0 <= N <= 10^4, -10^6 <= Node.val <= 10^6",
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "1 3 5 2 4",
        "explanation": "Odd indexed: 1, 3, 5; Even indexed: 2, 4. Result: 1 3 5 2 4.",
        "test_inputs": ["4\n2 1 3 5", "1\n7"],
        "variant_inputs": ["6\n10 20 30 40 50 60", "7\n1 2 3 4 5 6 7"],
        "starter_archetype": "array",
        "solver": solver_75
    },
    {
        "index": 76,
        "title_base": "Sort Linked List in O(N log N)",
        "description": "Given the head of a linked list, return the list after sorting it in ascending order in O(n log n) time.",
        "input_format": "First line contains N. Second line contains N integers.",
        "output_format": "Print the sorted list values separated by spaces.",
        "constraints": "0 <= N <= 5 * 10^4, -10^5 <= Node.val <= 10^5",
        "sample_input": "4\n4 2 1 3",
        "sample_output": "1 2 3 4",
        "explanation": "Sorted order is 1 2 3 4.",
        "test_inputs": ["5\n-1 5 3 4 0", "1\n5"],
        "variant_inputs": ["6\n10 9 8 7 6 5", "3\n3 1 2"],
        "starter_archetype": "array",
        "solver": solver_76
    },
    {
        "index": 77,
        "title_base": "Reverse Nodes in k-Group",
        "description": "Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. If the number of nodes is not a multiple of k then left-out nodes remain as they are.",
        "input_format": "First line contains N and k. Second line contains N integers.",
        "output_format": "Print the modified list values separated by spaces.",
        "constraints": "1 <= k <= N <= 5000, 0 <= Node.val <= 1000",
        "sample_input": "5 2\n1 2 3 4 5",
        "sample_output": "2 1 4 3 5",
        "explanation": "Reversing groups of 2: [1, 2] -> [2, 1], [3, 4] -> [4, 3], leaving [5].",
        "test_inputs": ["5 3\n1 2 3 4 5", "4 2\n1 2 3 4"],
        "variant_inputs": ["6 3\n1 2 3 4 5 6", "5 1\n1 2 3 4 5"],
        "starter_archetype": "target_and_array",
        "solver": solver_77
    },
    {
        "index": 78,
        "title_base": "Merge K Sorted Linked Lists",
        "description": "You are given an array of k linked-lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
        "input_format": "First line contains k. The next k lines each start with count Ni followed by Ni sorted integers.",
        "output_format": "Print all merged values in sorted order separated by spaces.",
        "constraints": "0 <= k <= 10^4, total nodes <= 10^4",
        "sample_input": "3\n3 1 4 5\n3 1 3 4\n2 2 6",
        "sample_output": "1 1 2 3 4 4 5 6",
        "explanation": "Merging [1, 4, 5], [1, 3, 4], [2, 6] produces 1 1 2 3 4 4 5 6.",
        "test_inputs": ["1\n2 1 2", "2\n1 5\n1 3"],
        "variant_inputs": ["3\n2 10 20\n2 5 15\n2 1 30", "2\n3 1 2 3\n3 4 5 6"],
        "starter_archetype": "general",
        "solver": solver_78
    },
    {
        "index": 79,
        "title_base": "Copy List with Random Pointer",
        "description": "Construct a deep copy of a linked list with random pointers. Return the node values of the cloned list.",
        "input_format": "First line contains integer N. Second line contains N integers representing node values.",
        "output_format": "Print the deep copied list values separated by spaces.",
        "constraints": "0 <= N <= 1000, -10^4 <= Node.val <= 10^4",
        "sample_input": "5\n7 13 11 10 1",
        "sample_output": "7 13 11 10 1",
        "explanation": "The cloned list preserves all values and pointers: 7 13 11 10 1.",
        "test_inputs": ["2\n1 2", "1\n3"],
        "variant_inputs": ["4\n10 20 30 40", "3\n100 200 300"],
        "starter_archetype": "array",
        "solver": solver_79
    },
    {
        "index": 80,
        "title_base": "Flatten Multilevel Doubly List",
        "description": "You are given a doubly linked list, which contains nodes with child pointers. Flatten the list so that all the nodes appear in a single-level, doubly linked list.",
        "input_format": "First line contains integer N. Second line contains N flattened order values.",
        "output_format": "Print the flattened node values separated by spaces.",
        "constraints": "0 <= N <= 1000",
        "sample_input": "8\n1 2 3 7 8 11 12 4",
        "sample_output": "1 2 3 7 8 11 12 4",
        "explanation": "Flattening traverses parent and child levels sequentially.",
        "test_inputs": ["3\n1 2 3", "1\n5"],
        "variant_inputs": ["5\n10 20 30 40 50", "4\n1 3 5 7"],
        "starter_archetype": "array",
        "solver": solver_80
    }
]
