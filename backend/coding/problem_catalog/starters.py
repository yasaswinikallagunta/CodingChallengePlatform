"""
Starter code generation for supported languages:
Python, JavaScript, C++, C, Java
"""

def generate_starters(io_type, description=""):
    """
    Generates language-specific starter code for a problem based on its I/O type.
    Supported io_types:
    - 'target_and_array' (target, N, array)
    - 'array' (N, array)
    - 'two_arrays' (N, array1, M, array2)
    - 'single_string' (s)
    - 'two_strings' (s1, s2)
    - 'single_number' (n)
    - 'two_numbers' (a, b)
    - 'matrix' (R, C, matrix)
    - 'graph' (V, E, edges)
    - 'general' (fallback)
    """
    
    if io_type == 'target_and_array':
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    tokens = sys.stdin.read().split()\n"
            "    if not tokens:\n"
            "        return\n"
            "    target = int(tokens[0])\n"
            "    n = int(tokens[1])\n"
            "    nums = [int(x) for x in tokens[2:2+n]]\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n\n"
            "int main() {\n"
            "    int target, n;\n"
            "    if (scanf(\"%d %d\", &target, &n) != 2) return 0;\n"
            "    int* nums = (int*)malloc(n * sizeof(int));\n"
            "    for (int i = 0; i < n; i++) {\n"
            "        scanf(\"%d\", &nums[i]);\n"
            "    }\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    free(nums);\n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n"
            "#include <vector>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    int target, n;\n"
            "    if (!(cin >> target >> n)) return 0;\n"
            "    vector<int> nums(n);\n"
            "    for (int i = 0; i < n; i++) {\n"
            "        cin >> nums[i];\n"
            "    }\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNextInt()) return;\n"
            "        int target = sc.nextInt();\n"
            "        int n = sc.nextInt();\n"
            "        int[] nums = new int[n];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            nums[i] = sc.nextInt();\n"
            "        }\n"
            "        \n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n"
            "    if (!tokens || tokens[0] === '') return;\n"
            "    const target = parseInt(tokens[0], 10);\n"
            "    const n = parseInt(tokens[1], 10);\n"
            "    const nums = tokens.slice(2, 2 + n).map(Number);\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    elif io_type == 'array':
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    tokens = sys.stdin.read().split()\n"
            "    if not tokens:\n"
            "        return\n"
            "    n = int(tokens[0])\n"
            "    nums = [int(x) for x in tokens[1:1+n]]\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n\n"
            "int main() {\n"
            "    int n;\n"
            "    if (scanf(\"%d\", &n) != 1) return 0;\n"
            "    int* nums = (int*)malloc(n * sizeof(int));\n"
            "    for (int i = 0; i < n; i++) {\n"
            "        scanf(\"%d\", &nums[i]);\n"
            "    }\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    free(nums);\n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n"
            "#include <vector>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    int n;\n"
            "    if (!(cin >> n)) return 0;\n"
            "    vector<int> nums(n);\n"
            "    for (int i = 0; i < n; i++) {\n"
            "        cin >> nums[i];\n"
            "    }\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNextInt()) return;\n"
            "        int n = sc.nextInt();\n"
            "        int[] nums = new int[n];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            nums[i] = sc.nextInt();\n"
            "        }\n"
            "        \n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n"
            "    if (!tokens || tokens[0] === '') return;\n"
            "    const n = parseInt(tokens[0], 10);\n"
            "    const nums = tokens.slice(1, 1 + n).map(Number);\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    elif io_type == 'single_string':
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    s = sys.stdin.read().strip()\n"
            "    if not s:\n"
            "        return\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n"
            "#include <string.h>\n\n"
            "int main() {\n"
            "    char s[100005];\n"
            "    if (scanf(\"%s\", s) != 1) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n"
            "#include <string>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    string s;\n"
            "    if (!(cin >> s)) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNext()) return;\n"
            "        String s = sc.next();\n"
            "        \n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const s = fs.readFileSync(0, 'utf-8').trim();\n"
            "    if (!s) return;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    elif io_type == 'two_strings':
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    tokens = sys.stdin.read().split()\n"
            "    if len(tokens) < 2:\n"
            "        return\n"
            "    s1, s2 = tokens[0], tokens[1]\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n"
            "#include <string.h>\n\n"
            "int main() {\n"
            "    char s1[100005], s2[100005];\n"
            "    if (scanf(\"%s %s\", s1, s2) != 2) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n"
            "#include <string>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    string s1, s2;\n"
            "    if (!(cin >> s1 >> s2)) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNext()) return;\n"
            "        String s1 = sc.next();\n"
            "        String s2 = sc.next();\n"
            "        \n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n"
            "    if (tokens.length < 2) return;\n"
            "    const s1 = tokens[0];\n"
            "    const s2 = tokens[1];\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    elif io_type == 'single_number':
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    token = sys.stdin.read().strip()\n"
            "    if not token:\n"
            "        return\n"
            "    n = int(token)\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n\n"
            "int main() {\n"
            "    long long n;\n"
            "    if (scanf(\"%lld\", &n) != 1) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    long long n;\n"
            "    if (!(cin >> n)) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNextLong()) return;\n"
            "        long n = sc.nextLong();\n"
            "        \n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const token = fs.readFileSync(0, 'utf-8').trim();\n"
            "    if (!token) return;\n"
            "    const n = parseInt(token, 10);\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    elif io_type == 'two_numbers':
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    tokens = sys.stdin.read().split()\n"
            "    if len(tokens) < 2:\n"
            "        return\n"
            "    a = int(tokens[0])\n"
            "    b = int(tokens[1])\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n\n"
            "int main() {\n"
            "    long long a, b;\n"
            "    if (scanf(\"%lld %lld\", &a, &b) != 2) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    long long a, b;\n"
            "    if (!(cin >> a >> b)) return 0;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "    \n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNextLong()) return;\n"
            "        long a = sc.nextLong();\n"
            "        long b = sc.nextLong();\n"
            "        \n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n"
            "    if (tokens.length < 2) return;\n"
            "    const a = parseInt(tokens[0], 10);\n"
            "    const b = parseInt(tokens[1], 10);\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    else:
        # General / Multi-line fallback
        py = (
            "import sys\n\n"
            "def solve():\n"
            "    lines = sys.stdin.read().splitlines()\n"
            "    if not lines:\n"
            "        return\n"
            "    \n"
            "    # TODO: Implement your solution here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        c = (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n\n"
            "int main() {\n"
            "    // TODO: Implement your solution here reading from stdin\n"
            "    return 0;\n"
            "}\n"
        )
        cpp = (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "    \n"
            "    // TODO: Implement your solution here reading from cin\n"
            "    return 0;\n"
            "}\n"
        )
        java = (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        // TODO: Implement your solution here\n"
            "    }\n"
            "}\n"
        )
        js = (
            "const fs = require('fs');\n\n"
            "function solve() {\n"
            "    const lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\n"
            "    if (!lines || lines.length === 0) return;\n"
            "    \n"
            "    // TODO: Implement your solution here\n"
            "}\n\n"
            "solve();\n"
        )

    return {
        'python': py,
        'c': c,
        'cpp': cpp,
        'java': java,
        'javascript': js,
    }
