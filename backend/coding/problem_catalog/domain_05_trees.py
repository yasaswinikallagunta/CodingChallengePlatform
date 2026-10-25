# Domain 05: Data Structures - Binary Trees & BST (Problems 81 - 100)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def parse_tree(tokens):
    if not tokens or tokens[0] == "null":
        return None
    root = TreeNode(int(tokens[0]))
    queue = deque([root])
    idx = 1
    while queue and idx < len(tokens):
        curr = queue.popleft()
        if idx < len(tokens):
            if tokens[idx] != "null":
                curr.left = TreeNode(int(tokens[idx]))
                queue.append(curr.left)
            idx += 1
        if idx < len(tokens):
            if tokens[idx] != "null":
                curr.right = TreeNode(int(tokens[idx]))
                queue.append(curr.right)
            idx += 1
    return root

def serialize_tree(root):
    if not root:
        return "null"
    res = []
    q = deque([root])
    while q:
        curr = q.popleft()
        if curr:
            res.append(str(curr.val))
            q.append(curr.left)
            q.append(curr.right)
        else:
            res.append("null")
    while res and res[-1] == "null":
        res.pop()
    return " ".join(res)

def solver_81(s: str) -> str:
    # Maximum Depth
    tokens = s.strip().split()
    root = parse_tree(tokens)
    def depth(node):
        if not node: return 0
        return 1 + max(depth(node.left), depth(node.right))
    return str(depth(root))

def solver_82(s: str) -> str:
    # Minimum Depth
    tokens = s.strip().split()
    root = parse_tree(tokens)
    if not root: return "0"
    def min_depth(node):
        if not node: return 0
        if not node.left and not node.right: return 1
        if not node.left: return 1 + min_depth(node.right)
        if not node.right: return 1 + min_depth(node.left)
        return 1 + min(min_depth(node.left), min_depth(node.right))
    return str(min_depth(root))

def solver_83(s: str) -> str:
    # Invert Tree
    tokens = s.strip().split()
    root = parse_tree(tokens)
    def invert(node):
        if not node: return None
        node.left, node.right = invert(node.right), invert(node.left)
        return node
    return serialize_tree(invert(root))

def solver_84(s: str) -> str:
    # Symmetric Tree
    tokens = s.strip().split()
    root = parse_tree(tokens)
    def is_sym(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and is_sym(t1.left, t2.right) and is_sym(t1.right, t2.left)
    return "true" if is_sym(root, root) else "false"

def solver_85(s: str) -> str:
    # Same Tree Check
    lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
    if len(lines) < 2: return "false"
    t1 = parse_tree(lines[0].split())
    t2 = parse_tree(lines[1].split())
    def same(n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        return n1.val == n2.val and same(n1.left, n2.left) and same(n1.right, n2.right)
    return "true" if same(t1, t2) else "false"

def solver_86(s: str) -> str:
    # Balanced Binary Tree Check
    tokens = s.strip().split()
    root = parse_tree(tokens)
    def check(node):
        if not node: return 0
        lh = check(node.left)
        if lh == -1: return -1
        rh = check(node.right)
        if rh == -1: return -1
        if abs(lh - rh) > 1: return -1
        return 1 + max(lh, rh)
    return "true" if check(root) != -1 else "false"

def solver_87(s: str) -> str:
    # Diameter of Binary Tree
    tokens = s.strip().split()
    root = parse_tree(tokens)
    max_d = 0
    def height(node):
        nonlocal max_d
        if not node: return 0
        lh = height(node.left)
        rh = height(node.right)
        max_d = max(max_d, lh + rh)
        return 1 + max(lh, rh)
    height(root)
    return str(max_d)

def solver_88(s: str) -> str:
    # Path Sum
    parts = s.strip().split('\n', 1)
    target = int(parts[0].strip())
    tokens = parts[1].strip().split() if len(parts) > 1 else []
    root = parse_tree(tokens)
    def has_sum(node, rem):
        if not node: return False
        rem -= node.val
        if not node.left and not node.right:
            return rem == 0
        return has_sum(node.left, rem) or has_sum(node.right, rem)
    return "true" if has_sum(root, target) else "false"

def solver_89(s: str) -> str:
    # All Root to Leaf Paths
    tokens = s.strip().split()
    root = parse_tree(tokens)
    if not root: return ""
    paths = []
    def dfs(node, path):
        if not node: return
        path.append(str(node.val))
        if not node.left and not node.right:
            paths.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    dfs(root, [])
    return " ".join(paths)

def solver_90(s: str) -> str:
    # Subtree of Another Tree
    lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
    if len(lines) < 2: return "false"
    root = parse_tree(lines[0].split())
    sub = parse_tree(lines[1].split())
    def same(n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        return n1.val == n2.val and same(n1.left, n2.left) and same(n1.right, n2.right)
    def check_sub(r):
        if not r: return False
        if same(r, sub): return True
        return check_sub(r.left) or check_sub(r.right)
    return "true" if check_sub(root) else "false"

def solver_91(s: str) -> str:
    # Lowest Common Ancestor in BST
    lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
    p_val, q_val = [int(x) for x in lines[0].split()]
    tokens = lines[1].split() if len(lines) > 1 else []
    root = parse_tree(tokens)
    curr = root
    while curr:
        if p_val < curr.val and q_val < curr.val:
            curr = curr.left
        elif p_val > curr.val and q_val > curr.val:
            curr = curr.right
        else:
            return str(curr.val)
    return "-1"

def solver_92(s: str) -> str:
    # Validate Binary Search Tree
    tokens = s.strip().split()
    root = parse_tree(tokens)
    def valid(node, low, high):
        if not node: return True
        if not (low < node.val < high): return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return "true" if valid(root, float('-inf'), float('inf')) else "false"

def solver_93(s: str) -> str:
    # Kth Smallest Element in BST
    parts = s.strip().split('\n', 1)
    k = int(parts[0].strip())
    tokens = parts[1].strip().split() if len(parts) > 1 else []
    root = parse_tree(tokens)
    res = []
    def inorder(node):
        if not node or len(res) >= k: return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return str(res[k-1]) if len(res) >= k else "-1"

def solver_94(s: str) -> str:
    # Level Order Tree Traversal
    tokens = s.strip().split()
    root = parse_tree(tokens)
    if not root: return ""
    res = []
    q = deque([root])
    while q:
        curr = q.popleft()
        res.append(str(curr.val))
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return " ".join(res)

def solver_95(s: str) -> str:
    # Zigzag Level Order Traversal
    tokens = s.strip().split()
    root = parse_tree(tokens)
    if not root: return ""
    res = []
    q = deque([root])
    left_to_right = True
    while q:
        level_size = len(q)
        level_vals = []
        for _ in range(level_size):
            curr = q.popleft()
            level_vals.append(str(curr.val))
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        if not left_to_right:
            level_vals.reverse()
        res.extend(level_vals)
        left_to_right = not left_to_right
    return " ".join(res)

def solver_96(s: str) -> str:
    # Binary Tree Right Side View
    tokens = s.strip().split()
    root = parse_tree(tokens)
    if not root: return ""
    res = []
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            curr = q.popleft()
            if i == level_size - 1:
                res.append(str(curr.val))
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
    return " ".join(res)

def solver_97(s: str) -> str:
    # Construct Tree from Preorder & Inorder (return level-order)
    lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
    if len(lines) < 2: return ""
    preorder = [int(x) for x in lines[0].split()]
    inorder = [int(x) for x in lines[1].split()]
    idx_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0
    def build(in_left, in_right):
        nonlocal pre_idx
        if in_left > in_right: return None
        val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(val)
        split = idx_map[val]
        root.left = build(in_left, split - 1)
        root.right = build(split + 1, in_right)
        return root
    root = build(0, len(inorder) - 1)
    return serialize_tree(root)

def solver_98(s: str) -> str:
    # Lowest Common Ancestor in Tree
    lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
    p_val, q_val = [int(x) for x in lines[0].split()]
    tokens = lines[1].split() if len(lines) > 1 else []
    root = parse_tree(tokens)
    def lca(node):
        if not node: return None
        if node.val == p_val or node.val == q_val:
            return node
        left = lca(node.left)
        right = lca(node.right)
        if left and right: return node
        return left if left else right
    ans = lca(root)
    return str(ans.val) if ans else "-1"

def solver_99(s: str) -> str:
    # Serialize and Deserialize Tree
    tokens = s.strip().split()
    root = parse_tree(tokens)
    return serialize_tree(root)

def solver_100(s: str) -> str:
    # Binary Tree Maximum Path Sum
    tokens = s.strip().split()
    root = parse_tree(tokens)
    max_sum = float('-inf')
    def gain(node):
        nonlocal max_sum
        if not node: return 0
        left_gain = max(gain(node.left), 0)
        right_gain = max(gain(node.right), 0)
        price_newpath = node.val + left_gain + right_gain
        max_sum = max(max_sum, price_newpath)
        return node.val + max(left_gain, right_gain)
    gain(root)
    return str(max_sum)

PROBLEMS = [
    {
        "index": 81,
        "title_base": "Maximum Depth of Binary Tree",
        "description": "Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        "input_format": "A single line containing space-separated level-order traversal values ('null' for missing nodes).",
        "output_format": "Print the maximum depth as an integer.",
        "constraints": "The number of nodes in the tree is in the range [0, 10^4]. -100 <= Node.val <= 100",
        "sample_input": "3 9 20 null null 15 7",
        "sample_output": "3",
        "explanation": "Longest root-to-leaf path is 3 -> 20 -> 15 with 3 nodes.",
        "test_inputs": ["1 null 2", "1"],
        "variant_inputs": ["1 2 3 4 null null 5", "10 20 30 40 50 null null"],
        "starter_archetype": "general",
        "solver": solver_81
    },
    {
        "index": 82,
        "title_base": "Minimum Depth of Binary Tree",
        "description": "Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.",
        "input_format": "A single line containing space-separated level-order traversal values ('null' for missing nodes).",
        "output_format": "Print the minimum depth as an integer.",
        "constraints": "The number of nodes in the tree is in the range [0, 10^5]. -1000 <= Node.val <= 1000",
        "sample_input": "3 9 20 null null 15 7",
        "sample_output": "2",
        "explanation": "Shortest root-to-leaf path is 3 -> 9 with 2 nodes.",
        "test_inputs": ["2 null 3 null 4 null 5 null 6", "1 2"],
        "variant_inputs": ["1 2 3 4 5", "10 null 20 null 30"],
        "starter_archetype": "general",
        "solver": solver_82
    },
    {
        "index": 83,
        "title_base": "Invert Binary Tree",
        "description": "Given the root of a binary tree, invert the tree, and return its level-order representation.",
        "input_format": "A single line of level-order values of the tree.",
        "output_format": "Print the level-order traversal of the inverted tree.",
        "constraints": "The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100",
        "sample_input": "4 2 7 1 3 6 9",
        "sample_output": "4 7 2 9 6 3 1",
        "explanation": "Inverting swaps children at each level: left and right subtrees are exchanged.",
        "test_inputs": ["2 1 3", "1"],
        "variant_inputs": ["5 3 8 2 4 7 9", "1 2 3"],
        "starter_archetype": "general",
        "solver": solver_83
    },
    {
        "index": 84,
        "title_base": "Symmetric Binary Tree",
        "description": "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).",
        "input_format": "A single line of level-order values.",
        "output_format": "Print 'true' if the tree is symmetric, otherwise 'false'.",
        "constraints": "The number of nodes in the tree is in the range [1, 1000]. -100 <= Node.val <= 100",
        "sample_input": "1 2 2 3 4 4 3",
        "sample_output": "true",
        "explanation": "Left and right subtrees mirror each other.",
        "test_inputs": ["1 2 2 null 3 null 3", "1"],
        "variant_inputs": ["1 2 2 2 null 2", "5 3 3 1 2 2 1"],
        "starter_archetype": "general",
        "solver": solver_84
    },
    {
        "index": 85,
        "title_base": "Same Binary Tree Check",
        "description": "Given the roots of two binary trees p and q, write a function to check if they are the same or not.",
        "input_format": "First line contains tree p level-order. Second line contains tree q level-order.",
        "output_format": "Print 'true' if identical, otherwise 'false'.",
        "constraints": "The number of nodes in both trees is in the range [0, 100].",
        "sample_input": "1 2 3\n1 2 3",
        "sample_output": "true",
        "explanation": "Both trees have the same structure and node values.",
        "test_inputs": ["1 2\n1 null 2", "1 2 1\n1 1 2"],
        "variant_inputs": ["4 2 7\n4 2 7", "10 20\n10 30"],
        "starter_archetype": "general",
        "solver": solver_85
    },
    {
        "index": 86,
        "title_base": "Balanced Binary Tree Check",
        "description": "Given a binary tree, determine if it is height-balanced (a binary tree in which the left and right subtrees of every node differ in height by no more than 1).",
        "input_format": "A single line of level-order values.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "The number of nodes in the tree is in the range [0, 5000].",
        "sample_input": "3 9 20 null null 15 7",
        "sample_output": "true",
        "explanation": "Height of left subtree is 1, right subtree is 2. Difference is 1 <= 1.",
        "test_inputs": ["1 2 2 3 3 null null 4 4", "1"],
        "variant_inputs": ["1 2 3 4 5 6 null", "1 null 2 null 3"],
        "starter_archetype": "general",
        "solver": solver_86
    },
    {
        "index": 87,
        "title_base": "Diameter of Binary Tree",
        "description": "Given the root of a binary tree, return the length of the diameter of the tree. The diameter is the length of the longest path between any two nodes in a tree, measured in number of edges.",
        "input_format": "A single line containing level-order traversal values.",
        "output_format": "Print the diameter as an integer.",
        "constraints": "The number of nodes in the tree is in the range [1, 10^4].",
        "sample_input": "1 2 3 4 5",
        "sample_output": "3",
        "explanation": "The path [4, 2, 1, 3] or [5, 2, 1, 3] has 3 edges.",
        "test_inputs": ["1 2", "1"],
        "variant_inputs": ["1 2 3 4 null null 5 6", "1 2 3"],
        "starter_archetype": "general",
        "solver": solver_87
    },
    {
        "index": 88,
        "title_base": "Binary Tree Path Sum",
        "description": "Given the root of a binary tree and an integer targetSum, return 'true' if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.",
        "input_format": "First line contains targetSum. Second line contains level-order tree values.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "The number of nodes in the tree is in the range [0, 5000]. -1000 <= Node.val <= 1000",
        "sample_input": "22\n5 4 8 11 null 13 4 7 2 null null null 1",
        "sample_output": "true",
        "explanation": "Path 5 -> 4 -> 11 -> 2 sums to 22.",
        "test_inputs": ["5\n1 2 3", "0\n1 2"],
        "variant_inputs": ["10\n5 5", "15\n10 5 null 2"],
        "starter_archetype": "general",
        "solver": solver_88
    },
    {
        "index": 89,
        "title_base": "All Root to Leaf Paths",
        "description": "Given the root of a binary tree, return all root-to-leaf paths in any order.",
        "input_format": "A single line containing level-order tree values.",
        "output_format": "Print all paths separated by spaces, where each path is formatted as node1->node2->node3.",
        "constraints": "The number of nodes in the tree is in the range [1, 100].",
        "sample_input": "1 2 3 null 5",
        "sample_output": "1->2->5 1->3",
        "explanation": "The two root-to-leaf paths are 1->2->5 and 1->3.",
        "test_inputs": ["1", "1 2 3"],
        "variant_inputs": ["4 2 6 1 3", "1 2 null 3"],
        "starter_archetype": "general",
        "solver": solver_89
    },
    {
        "index": 90,
        "title_base": "Subtree of Another Tree",
        "description": "Given the roots of two binary trees root and subRoot, return 'true' if there is a subtree of root with the same structure and node values of subRoot and 'false' otherwise.",
        "input_format": "First line contains root level-order values. Second line contains subRoot level-order values.",
        "output_format": "Print 'true' or 'false'.",
        "constraints": "The number of nodes in root is in the range [1, 2000]. The number of nodes in subRoot is in the range [1, 1000].",
        "sample_input": "3 4 5 1 2\n4 1 2",
        "sample_output": "true",
        "explanation": "The subtree at node 4 matches subRoot.",
        "test_inputs": ["3 4 5 1 2 null null null null 0\n4 1 2", "1 1\n1"],
        "variant_inputs": ["1 2 3\n2", "5 3 7 2 4\n3 2 4"],
        "starter_archetype": "general",
        "solver": solver_90
    },
    {
        "index": 91,
        "title_base": "Lowest Common Ancestor in BST",
        "description": "Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes p and q in the BST.",
        "input_format": "First line contains two integers p and q. Second line contains level-order values of the BST.",
        "output_format": "Print the value of the LCA node.",
        "constraints": "The number of nodes in the tree is in the range [2, 10^5]. All Node.val are unique.",
        "sample_input": "2 8\n6 2 8 0 4 7 9 null null 3 5",
        "sample_output": "6",
        "explanation": "The LCA of nodes 2 and 8 is 6.",
        "test_inputs": ["2 4\n6 2 8 0 4 7 9 null null 3 5", "2 1\n2 1"],
        "variant_inputs": ["3 5\n6 2 8 0 4 7 9 null null 3 5", "7 9\n6 2 8 0 4 7 9"],
        "starter_archetype": "general",
        "solver": solver_91
    },
    {
        "index": 92,
        "title_base": "Validate Binary Search Tree",
        "description": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).",
        "input_format": "A single line containing level-order tree values.",
        "output_format": "Print 'true' if the tree is a valid BST, otherwise 'false'.",
        "constraints": "The number of nodes in the tree is in the range [1, 10^4]. -2^31 <= Node.val <= 2^31 - 1",
        "sample_input": "2 1 3",
        "sample_output": "true",
        "explanation": "Left child 1 < root 2 < right child 3.",
        "test_inputs": ["5 1 4 null null 3 6", "1"],
        "variant_inputs": ["10 5 15 null null 6 20", "2 2 2"],
        "starter_archetype": "general",
        "solver": solver_92
    },
    {
        "index": 93,
        "title_base": "Kth Smallest Element in BST",
        "description": "Given the root of a binary search tree and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.",
        "input_format": "First line contains k. Second line contains level-order values of the BST.",
        "output_format": "Print the kth smallest integer.",
        "constraints": "The number of nodes in the tree is n, 1 <= k <= n <= 10^4.",
        "sample_input": "1\n3 1 4 null 2",
        "sample_output": "1",
        "explanation": "Sorted order of BST is 1, 2, 3, 4. The 1st smallest is 1.",
        "test_inputs": ["3\n5 3 6 2 4 null null 1", "1\n1"],
        "variant_inputs": ["2\n4 2 5 1 3", "4\n5 3 7 2 4 6 8"],
        "starter_archetype": "general",
        "solver": solver_93
    },
    {
        "index": 94,
        "title_base": "Level Order Tree Traversal",
        "description": "Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).",
        "input_format": "A single line of level-order values.",
        "output_format": "Print all visited node values separated by spaces.",
        "constraints": "The number of nodes in the tree is in the range [0, 2000].",
        "sample_input": "3 9 20 null null 15 7",
        "sample_output": "3 9 20 15 7",
        "explanation": "Level 0: 3; Level 1: 9, 20; Level 2: 15, 7.",
        "test_inputs": ["1", "1 2 3 4 5"],
        "variant_inputs": ["10 20 30 null 40", "1 2 null 3"],
        "starter_archetype": "general",
        "solver": solver_94
    },
    {
        "index": 95,
        "title_base": "Zigzag Level Order Traversal",
        "description": "Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).",
        "input_format": "A single line of level-order values.",
        "output_format": "Print the zigzag traversal values separated by spaces.",
        "constraints": "The number of nodes in the tree is in the range [0, 2000].",
        "sample_input": "3 9 20 null null 15 7",
        "sample_output": "3 20 9 15 7",
        "explanation": "Level 0: 3; Level 1 (right to left): 20, 9; Level 2 (left to right): 15, 7.",
        "test_inputs": ["1", "1 2 3 4 null null 5"],
        "variant_inputs": ["5 3 8 1 4 7 9", "1 2 3"],
        "starter_archetype": "general",
        "solver": solver_95
    },
    {
        "index": 96,
        "title_base": "Binary Tree Right Side View",
        "description": "Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.",
        "input_format": "A single line of level-order values.",
        "output_format": "Print the right-side visible values separated by spaces.",
        "constraints": "The number of nodes in the tree is in the range [0, 100].",
        "sample_input": "1 2 3 null 5 null 4",
        "sample_output": "1 3 4",
        "explanation": "Visible nodes from top to bottom are 1, 3, 4.",
        "test_inputs": ["1 null 3", "1"],
        "variant_inputs": ["1 2 3 4", "5 3 8 2 null 7 9"],
        "starter_archetype": "general",
        "solver": solver_96
    },
    {
        "index": 97,
        "title_base": "Construct Tree from Preorder & Inorder",
        "description": "Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree level-order.",
        "input_format": "First line contains space-separated preorder values. Second line contains space-separated inorder values.",
        "output_format": "Print the constructed binary tree in level-order.",
        "constraints": "1 <= preorder.length <= 3000, inorder.length == preorder.length",
        "sample_input": "3 9 20 15 7\n9 3 15 20 7",
        "sample_output": "3 9 20 null null 15 7",
        "explanation": "Tree root is 3, left child 9, right child 20 with children 15 and 7.",
        "test_inputs": ["-1\n-1", "1 2\n2 1"],
        "variant_inputs": ["1 2 3\n2 1 3", "2 1 3\n1 2 3"],
        "starter_archetype": "general",
        "solver": solver_97
    },
    {
        "index": 98,
        "title_base": "Lowest Common Ancestor in Tree",
        "description": "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.",
        "input_format": "First line contains two integers p and q. Second line contains level-order values of the tree.",
        "output_format": "Print the value of the LCA node.",
        "constraints": "The number of nodes in the tree is in the range [2, 10^5]. All Node.val are unique.",
        "sample_input": "5 1\n3 5 1 6 2 0 8 null null 7 4",
        "sample_output": "3",
        "explanation": "The LCA of 5 and 1 is 3.",
        "test_inputs": ["5 4\n3 5 1 6 2 0 8 null null 7 4", "1 2\n1 2"],
        "variant_inputs": ["6 4\n3 5 1 6 2 0 8 null null 7 4", "7 4\n3 5 1 6 2 0 8 null null 7 4"],
        "starter_archetype": "general",
        "solver": solver_98
    },
    {
        "index": 99,
        "title_base": "Serialize and Deserialize Tree",
        "description": "Design an algorithm to serialize a binary tree into a string and deserialize that string back into the original tree structure. Output the verified reconstructed tree.",
        "input_format": "A single line containing space-separated level-order tree values.",
        "output_format": "Print the serialized representation of the tree.",
        "constraints": "The number of nodes in the tree is in the range [0, 10^4].",
        "sample_input": "1 2 3 null null 4 5",
        "sample_output": "1 2 3 null null 4 5",
        "explanation": "Serialization encodes structure and deserialization restores it identically.",
        "test_inputs": ["1", "1 2"],
        "variant_inputs": ["2 1 3", "5 3 8 2 4"],
        "starter_archetype": "general",
        "solver": solver_99
    },
    {
        "index": 100,
        "title_base": "Binary Tree Maximum Path Sum",
        "description": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. Return the maximum path sum of any non-empty path.",
        "input_format": "A single line containing level-order tree values.",
        "output_format": "Print the maximum path sum as an integer.",
        "constraints": "The number of nodes in the tree is in the range [1, 3 * 10^4]. -1000 <= Node.val <= 1000",
        "sample_input": "-10 9 20 null null 15 7",
        "sample_output": "42",
        "explanation": "The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.",
        "test_inputs": ["1 2 3", "-3"],
        "variant_inputs": ["2 -1", "1 -2 3"],
        "starter_archetype": "general",
        "solver": solver_100
    }
]
