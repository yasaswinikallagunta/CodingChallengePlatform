# Domain 12: SQL - Relational & Aggregates (Problems 221 - 240)
from collections import Counter, defaultdict

def solver_221(s: str) -> str:
    # Second Highest Salary Query
    parts = s.strip().split()
    if not parts: return "null"
    n = int(parts[0])
    salaries = sorted(set(int(x) for x in parts[1:1+n]), reverse=True)
    return str(salaries[1]) if len(salaries) >= 2 else "null"

def solver_222(s: str) -> str:
    # Nth Highest Salary Function
    parts = s.strip().split()
    k = int(parts[0])
    n = int(parts[1])
    salaries = sorted(set(int(x) for x in parts[2:2+n]), reverse=True)
    return str(salaries[k - 1]) if 1 <= k <= len(salaries) else "null"

def solver_223(s: str) -> str:
    # Duplicate Emails Detection
    parts = s.strip().split()
    n = int(parts[0])
    emails = parts[1:1+n]
    counts = Counter(emails)
    dups = sorted([e for e, cnt in counts.items() if cnt > 1])
    return " ".join(dups) if dups else "none"

def solver_224(s: str) -> str:
    # Customers Who Never Order
    parts = s.strip().split()
    n = int(parts[0])
    customers = parts[1:1+n]
    idx = 1 + n
    m = int(parts[idx])
    idx += 1
    ordered = set(parts[idx:idx+m])
    never = [c for c in customers if c not in ordered]
    return " ".join(never) if never else "none"

def solver_225(s: str) -> str:
    # Employees Earning More Than Manager
    # Format: N then N rows of (id, name, salary, manager_id)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    emps = {}
    for _ in range(n):
        eid = int(parts[idx])
        name = parts[idx+1]
        sal = int(parts[idx+2])
        mid = int(parts[idx+3])
        emps[eid] = (name, sal, mid)
        idx += 4
    res = []
    for eid, (name, sal, mid) in emps.items():
        if mid in emps and sal > emps[mid][1]:
            res.append(name)
    return " ".join(sorted(res)) if res else "none"

def solver_226(s: str) -> str:
    # Department Highest Salary
    # Format: N then N rows of (name, salary, dept)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    by_dept = defaultdict(list)
    for _ in range(n):
        name = parts[idx]
        sal = int(parts[idx+1])
        dept = parts[idx+2]
        by_dept[dept].append((name, sal))
        idx += 3
    res = []
    for dept in sorted(by_dept.keys()):
        max_sal = max(sal for name, sal in by_dept[dept])
        for name, sal in by_dept[dept]:
            if sal == max_sal:
                res.append(f"{dept} {name} {sal}")
    return " ".join(res)

def solver_227(s: str) -> str:
    # Department Top Three Salaries
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    by_dept = defaultdict(list)
    for _ in range(n):
        name = parts[idx]
        sal = int(parts[idx+1])
        dept = parts[idx+2]
        by_dept[dept].append((name, sal))
        idx += 3
    res = []
    for dept in sorted(by_dept.keys()):
        distinct_sals = set(sorted(set(sal for name, sal in by_dept[dept]), reverse=True)[:3])
        sorted_dept_emps = sorted([e for e in by_dept[dept] if e[1] in distinct_sals], key=lambda x: (-x[1], x[0]))
        for name, sal in sorted_dept_emps:
            res.append(f"{dept} {name} {sal}")
    return " ".join(res)

def solver_228(s: str) -> str:
    # Delete Duplicate Emails In-Place (keep smallest id)
    # Format: N then pairs of (id, email)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    first_id = {}
    for _ in range(n):
        eid = int(parts[idx])
        email = parts[idx+1]
        idx += 2
        if email not in first_id or eid < first_id[email]:
            first_id[email] = eid
    return " ".join(str(x) for x in sorted(first_id.values()))

def solver_229(s: str) -> str:
    # Rising Temperature Weather Days
    # Format: N then rows of (id, temp)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    records = []
    for _ in range(n):
        rid = int(parts[idx])
        temp = int(parts[idx+1])
        records.append((rid, temp))
        idx += 2
    res = []
    for i in range(1, len(records)):
        if records[i][1] > records[i-1][1]:
            res.append(str(records[i][0]))
    return " ".join(res) if res else "none"

def solver_230(s: str) -> str:
    # Consecutive Numbers Logged (at least three times consecutively)
    parts = s.strip().split()
    n = int(parts[0])
    logs = [int(x) for x in parts[1:1+n]]
    res = set()
    for i in range(len(logs) - 2):
        if logs[i] == logs[i+1] == logs[i+2]:
            res.add(logs[i])
    return " ".join(str(x) for x in sorted(res)) if res else "none"

def solver_231(s: str) -> str:
    # Rank Scores Dense Ranking
    parts = s.strip().split()
    n = int(parts[0])
    scores = [float(x) for x in parts[1:1+n]]
    unique_sorted = sorted(set(scores), reverse=True)
    rank_map = {sc: i + 1 for i, sc in enumerate(unique_sorted)}
    return " ".join(str(rank_map[sc]) for sc in scores)

def solver_232(s: str) -> str:
    # Exchange Seats Alternate
    parts = s.strip().split()
    n = int(parts[0])
    students = parts[1:1+n]
    res = list(students)
    for i in range(0, n - 1, 2):
        res[i], res[i+1] = res[i+1], res[i]
    return " ".join(res)

def solver_233(s: str) -> str:
    # Tree Node Hierarchy Type (Root, Inner, Leaf)
    # Format: N then pairs of (id, p_id) (-1 for null)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    nodes = []
    parents = set()
    for _ in range(n):
        nid = int(parts[idx])
        pid = int(parts[idx+1])
        nodes.append((nid, pid))
        if pid != -1:
            parents.add(pid)
        idx += 2
    res = []
    for nid, pid in nodes:
        if pid == -1:
            res.append(f"{nid}:Root")
        elif nid in parents:
            res.append(f"{nid}:Inner")
        else:
            res.append(f"{nid}:Leaf")
    return " ".join(res)

def solver_234(s: str) -> str:
    # Trips and Users Cancellation Rate
    # Format: N then pairs (status, banned: 0 or 1)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    total_unbanned = 0
    cancelled_unbanned = 0
    for _ in range(n):
        status = parts[idx]
        banned = int(parts[idx+1])
        idx += 2
        if banned == 0:
            total_unbanned += 1
            if status == "cancelled":
                cancelled_unbanned += 1
    if total_unbanned == 0: return "0.00"
    rate = cancelled_unbanned / total_unbanned
    return f"{rate:.2f}"

def solver_235(s: str) -> str:
    # Human Traffic of Stadium (>= 100 people for >= 3 consecutive days)
    # Format: N then pairs (id, people)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    stadium = []
    for _ in range(n):
        sid = int(parts[idx])
        cnt = int(parts[idx+1])
        stadium.append((sid, cnt))
        idx += 2
    valid_ids = set()
    for i in range(len(stadium) - 2):
        if stadium[i][1] >= 100 and stadium[i+1][1] >= 100 and stadium[i+2][1] >= 100:
            valid_ids.add(stadium[i][0])
            valid_ids.add(stadium[i+1][0])
            valid_ids.add(stadium[i+2][0])
    return " ".join(str(x) for x in sorted(valid_ids)) if valid_ids else "none"

def solver_236(s: str) -> str:
    # Game Play Analysis First Login
    # Format: N then pairs (player_id, date)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    first_login = {}
    for _ in range(n):
        pid = int(parts[idx])
        dt = parts[idx+1]
        idx += 2
        if pid not in first_login or dt < first_login[pid]:
            first_login[pid] = dt
    res = [f"{pid} {first_login[pid]}" for pid in sorted(first_login.keys())]
    return " ".join(res)

def solver_237(s: str) -> str:
    # Game Play Analysis Day Next Login (fraction of players with consecutive logins)
    # Format: N players count, M records of (player_id, day_int)
    parts = s.strip().split()
    num_players = int(parts[0])
    m = int(parts[1])
    idx = 2
    logins = defaultdict(set)
    for _ in range(m):
        pid = int(parts[idx])
        day = int(parts[idx+1])
        logins[pid].add(day)
        idx += 2
    consec = 0
    for pid, days in logins.items():
        min_day = min(days)
        if min_day + 1 in days:
            consec += 1
    rate = consec / num_players if num_players > 0 else 0.0
    return f"{rate:.2f}"

def solver_238(s: str) -> str:
    # Managers with at Least 5 Reports
    # Format: N then pairs (name, manager_id) with id 1..N
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    names = {}
    mgr_counts = defaultdict(int)
    for i in range(1, n + 1):
        name = parts[idx]
        mid = int(parts[idx+1])
        names[i] = name
        if mid != -1:
            mgr_counts[mid] += 1
        idx += 2
    res = [names[mid] for mid, cnt in mgr_counts.items() if cnt >= 5 and mid in names]
    return " ".join(sorted(res)) if res else "none"

def solver_239(s: str) -> str:
    # Sales Person Without Red Orders
    # Format: N salespersons, M red orders (salesperson names)
    parts = s.strip().split()
    n = int(parts[0])
    salespersons = parts[1:1+n]
    idx = 1 + n
    m = int(parts[idx])
    idx += 1
    red_orders = set(parts[idx:idx+m])
    res = [sp for sp in salespersons if sp not in red_orders]
    return " ".join(sorted(res)) if res else "none"

def solver_240(s: str) -> str:
    # Investments in 2016 Total Sum
    # Format: N rows of (pid, tiv_2015, tiv_2016, lat, lon)
    parts = s.strip().split()
    n = int(parts[0])
    idx = 1
    records = []
    tiv15_counts = defaultdict(int)
    loc_counts = defaultdict(int)
    for _ in range(n):
        pid = int(parts[idx])
        t15 = int(parts[idx+1])
        t16 = float(parts[idx+2])
        lat = int(parts[idx+3])
        lon = int(parts[idx+4])
        records.append((pid, t15, t16, lat, lon))
        tiv15_counts[t15] += 1
        loc_counts[(lat, lon)] += 1
        idx += 5
    total = 0.0
    for pid, t15, t16, lat, lon in records:
        if tiv15_counts[t15] > 1 and loc_counts[(lat, lon)] == 1:
            total += t16
    return f"{total:.2f}"

PROBLEMS = [
    {
        "index": 221,
        "title_base": "Second Highest Salary Query",
        "description": "Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null.",
        "input_format": "First line contains N. Second line contains N salaries.",
        "output_format": "Print the second highest salary or 'null'.",
        "constraints": "1 <= N <= 100, 1 <= salary <= 10^6",
        "sample_input": "3\n100 200 300",
        "sample_output": "200",
        "explanation": "200 is the second highest distinct salary.",
        "test_inputs": ["1\n100", "2\n100 100"],
        "variant_inputs": ["4\n500 200 500 300", "3\n100 200 200"],
        "starter_archetype": "array",
        "solver": solver_221
    },
    {
        "index": 222,
        "title_base": "Nth Highest Salary Function",
        "description": "Write a function to get the nth highest distinct salary from the Employee table. If there is no nth highest salary, return null.",
        "input_format": "First line contains n and N. Second line contains N salaries.",
        "output_format": "Print the nth highest salary or 'null'.",
        "constraints": "1 <= N <= 100, 1 <= salary <= 10^6",
        "sample_input": "2 3\n100 200 300",
        "sample_output": "200",
        "explanation": "The 2nd highest distinct salary is 200.",
        "test_inputs": ["1 3\n100 200 300", "4 3\n100 200 300"],
        "variant_inputs": ["2 2\n100 100", "3 4\n400 300 200 100"],
        "starter_archetype": "target_and_array",
        "solver": solver_222
    },
    {
        "index": 223,
        "title_base": "Duplicate Emails Detection",
        "description": "Write a solution to report all the duplicate emails in the Person table.",
        "input_format": "First line contains N. Second line contains N emails.",
        "output_format": "Print duplicate emails in sorted order separated by spaces, or 'none'.",
        "constraints": "1 <= N <= 100",
        "sample_input": "3\na@b.com c@d.com a@b.com",
        "sample_output": "a@b.com",
        "explanation": "'a@b.com' is repeated twice.",
        "test_inputs": ["2\na@b.com c@d.com", "4\nx@y.com x@y.com z@w.com z@w.com"],
        "variant_inputs": ["3\n1@a.com 2@b.com 3@c.com", "3\nm@n.com m@n.com m@n.com"],
        "starter_archetype": "general",
        "solver": solver_223
    },
    {
        "index": 224,
        "title_base": "Customers Who Never Order",
        "description": "Find all customers who never order anything.",
        "input_format": "First line contains N. Second line contains N customer names. Third line contains M. Fourth line contains M names of customers who placed orders.",
        "output_format": "Print customer names who never ordered, or 'none'.",
        "constraints": "1 <= N <= 100, 0 <= M <= N",
        "sample_input": "4\nJoe Henry Sam Max\n2\nHenry Sam",
        "sample_output": "Joe Max",
        "explanation": "Joe and Max never placed any orders.",
        "test_inputs": ["2\nAlice Bob\n1\nAlice", "1\nJohn\n1\nJohn"],
        "variant_inputs": ["3\nTom Jerry Spike\n2\nJerry Spike", "2\nA B\n0"],
        "starter_archetype": "general",
        "solver": solver_224
    },
    {
        "index": 225,
        "title_base": "Employees Earning More Than Manager",
        "description": "Write a solution to find the employees who earn more than their managers.",
        "input_format": "First line contains N. Following lines contain N rows: id, name, salary, manager_id.",
        "output_format": "Print employee names sorted alphabetically, or 'none'.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\n1 Joe 70000 3\n2 Henry 80000 4\n3 Sam 60000 -1\n4 Max 90000 -1",
        "sample_output": "Joe",
        "explanation": "Joe earns 70000 which is more than manager Sam (60000).",
        "test_inputs": ["2\n1 A 50000 2\n2 B 60000 -1", "2\n1 A 60000 2\n2 B 50000 -1"],
        "variant_inputs": ["3\n1 X 100 2\n2 Y 90 3\n3 Z 80 -1", "1\n1 Boss 100000 -1"],
        "starter_archetype": "general",
        "solver": solver_225
    },
    {
        "index": 226,
        "title_base": "Department Highest Salary",
        "description": "Write a solution to find employees who have the highest salary in each of the departments.",
        "input_format": "First line contains N. Next lines contain name salary department.",
        "output_format": "Print formatted results: Department Name Salary separated by spaces.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\nJoe 70000 IT\nJim 90000 IT\nHenry 80000 Sales\nSam 60000 Sales",
        "sample_output": "IT Jim 90000 Sales Henry 80000",
        "explanation": "Jim has highest in IT (90000), Henry highest in Sales (80000).",
        "test_inputs": ["2\nAlice 50000 HR\nBob 60000 HR", "1\nCarol 40000 Legal"],
        "variant_inputs": ["3\nA 100 D1\nB 100 D1\nC 50 D2", "2\nX 50 D1\nY 60 D2"],
        "starter_archetype": "general",
        "solver": solver_226
    },
    {
        "index": 227,
        "title_base": "Department Top Three Salaries",
        "description": "A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.",
        "input_format": "First line contains N. Next lines contain name salary department.",
        "output_format": "Print top 3 earners formatted as Dept Name Salary.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\nJoe 70000 IT\nJim 90000 IT\nHenry 80000 IT\nSam 60000 IT",
        "sample_output": "IT Jim 90000 IT Henry 80000 IT Joe 70000",
        "explanation": "Top 3 distinct salaries in IT are 90000, 80000, 70000.",
        "test_inputs": ["2\nA 10 D1\nB 20 D1", "1\nX 50 D2"],
        "variant_inputs": ["3\nM 30 D1\nN 20 D1\nO 10 D1", "3\nP 50 D1\nQ 40 D2\nR 30 D2"],
        "starter_archetype": "general",
        "solver": solver_227
    },
    {
        "index": 228,
        "title_base": "Delete Duplicate Emails In-Place",
        "description": "Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.",
        "input_format": "First line contains N. Following lines contain N pairs of id and email.",
        "output_format": "Print remaining IDs in ascending order separated by spaces.",
        "constraints": "1 <= N <= 100",
        "sample_input": "3\n1 john@example.com\n2 bob@example.com\n3 john@example.com",
        "sample_output": "1 2",
        "explanation": "id 3 has a duplicate email and is deleted. IDs 1 and 2 remain.",
        "test_inputs": ["2\n1 a@b.com\n2 a@b.com", "1\n1 x@y.com"],
        "variant_inputs": ["3\n1 a@b.com\n2 b@c.com\n3 c@d.com", "4\n1 m@n.com\n2 p@q.com\n3 m@n.com\n4 p@q.com"],
        "starter_archetype": "general",
        "solver": solver_228
    },
    {
        "index": 229,
        "title_base": "Rising Temperature Weather Days",
        "description": "Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).",
        "input_format": "First line contains N. Following lines contain id and temperature.",
        "output_format": "Print IDs with rising temperature separated by spaces, or 'none'.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\n1 10\n2 25\n3 20\n4 30",
        "sample_output": "2 4",
        "explanation": "Day 2 temp 25 > day 1 temp 10. Day 4 temp 30 > day 3 temp 20.",
        "test_inputs": ["2\n1 15\n2 10", "1\n1 20"],
        "variant_inputs": ["3\n1 5\n2 10\n3 15", "3\n1 20\n2 20\n3 20"],
        "starter_archetype": "general",
        "solver": solver_229
    },
    {
        "index": 230,
        "title_base": "Consecutive Numbers Logged",
        "description": "Find all numbers that appear at least three times consecutively.",
        "input_format": "First line contains N. Second line contains N logged numbers.",
        "output_format": "Print unique consecutive numbers separated by spaces, or 'none'.",
        "constraints": "1 <= N <= 1000",
        "sample_input": "7\n1 1 1 2 1 2 2",
        "sample_output": "1",
        "explanation": "1 appears consecutively at positions 0, 1, 2.",
        "test_inputs": ["3\n2 2 2", "4\n1 2 3 4"],
        "variant_inputs": ["6\n1 1 1 2 2 2", "5\n3 3 1 3 3"],
        "starter_archetype": "array",
        "solver": solver_230
    },
    {
        "index": 231,
        "title_base": "Rank Scores Dense Ranking",
        "description": "Write a solution to find the rank of the scores. The ranking should be calculated according to DENSE_RANK without holes.",
        "input_format": "First line contains N. Second line contains N scores.",
        "output_format": "Print the dense ranks separated by spaces.",
        "constraints": "1 <= N <= 1000",
        "sample_input": "6\n3.50 3.65 4.00 3.85 4.00 3.65",
        "sample_output": "4 3 1 2 1 3",
        "explanation": "Highest score 4.00 has rank 1, 3.85 rank 2, 3.65 rank 3, 3.50 rank 4.",
        "test_inputs": ["2\n10 10", "3\n1 2 3"],
        "variant_inputs": ["4\n90 80 80 70", "1\n5"],
        "starter_archetype": "array",
        "solver": solver_231
    },
    {
        "index": 232,
        "title_base": "Exchange Seats Alternate",
        "description": "Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.",
        "input_format": "First line contains N. Second line contains N student names.",
        "output_format": "Print swapped student names separated by spaces.",
        "constraints": "1 <= N <= 100",
        "sample_input": "5\nAbbot Doris Emerson Green Jeames",
        "sample_output": "Doris Abbot Green Emerson Jeames",
        "explanation": "Seats 1 and 2 swap, seats 3 and 4 swap, seat 5 remains.",
        "test_inputs": ["2\nA B", "1\nSolo"],
        "variant_inputs": ["4\n1 2 3 4", "3\nX Y Z"],
        "starter_archetype": "general",
        "solver": solver_232
    },
    {
        "index": 233,
        "title_base": "Tree Node Hierarchy Type",
        "description": "Each node in the tree can be one of three types: 'Leaf': if the node is a leaf node; 'Root': if the node is the root of the tree; 'Inner': If the node is neither a leaf node nor a root node.",
        "input_format": "First line contains N. Following lines contain N pairs of id and p_id (-1 for null).",
        "output_format": "Print id:Type separated by spaces.",
        "constraints": "1 <= N <= 100",
        "sample_input": "3\n1 -1\n2 1\n3 1",
        "sample_output": "1:Root 2:Leaf 3:Leaf",
        "explanation": "1 is Root, 2 and 3 are Leaves.",
        "test_inputs": ["1\n1 -1", "4\n1 -1\n2 1\n3 2\n4 2"],
        "variant_inputs": ["2\n1 -1\n2 1", "3\n1 -1\n2 1\n3 2"],
        "starter_archetype": "general",
        "solver": solver_233
    },
    {
        "index": 234,
        "title_base": "Trips and Users Cancellation Rate",
        "description": "The cancellation rate is computed by dividing the number of canceled requests made by unbanned users by the total number of requests made by unbanned users.",
        "input_format": "First line contains N. Following lines contain status ('completed' or 'cancelled') and banned (0 or 1).",
        "output_format": "Print the cancellation rate with 2 decimal places.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\ncompleted 0\ncancelled 0\ncompleted 0\ncancelled 1",
        "sample_output": "0.33",
        "explanation": "Unbanned trips: 3 (1 cancelled, 2 completed). Rate: 1 / 3 = 0.33.",
        "test_inputs": ["2\ncompleted 0\ncompleted 0", "1\ncancelled 0"],
        "variant_inputs": ["3\ncancelled 0\ncancelled 0\ncompleted 0", "2\ncancelled 1\ncompleted 1"],
        "starter_archetype": "general",
        "solver": solver_234
    },
    {
        "index": 235,
        "title_base": "Human Traffic of Stadium",
        "description": "Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.",
        "input_format": "First line contains N. Following lines contain id and people count.",
        "output_format": "Print valid IDs separated by spaces, or 'none'.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\n1 10\n2 109\n3 150\n4 120",
        "sample_output": "2 3 4",
        "explanation": "IDs 2, 3, 4 have >= 100 people for 3 consecutive days.",
        "test_inputs": ["2\n1 100\n2 100", "3\n1 50\n2 50\n3 50"],
        "variant_inputs": ["5\n1 110\n2 120\n3 130\n4 90\n5 100", "3\n1 100\n2 100\n3 100"],
        "starter_archetype": "general",
        "solver": solver_235
    },
    {
        "index": 236,
        "title_base": "Game Play Analysis First Login",
        "description": "Write a solution to find the first login date for each player.",
        "input_format": "First line contains N. Following lines contain player_id and event_date.",
        "output_format": "Print player_id first_date separated by spaces.",
        "constraints": "1 <= N <= 100",
        "sample_input": "3\n1 2016-03-01\n1 2016-05-02\n2 2017-06-25",
        "sample_output": "1 2016-03-01 2 2017-06-25",
        "explanation": "Player 1 first login was 2016-03-01, player 2 was 2017-06-25.",
        "test_inputs": ["1\n1 2020-01-01", "2\n3 2019-02-01\n3 2018-01-01"],
        "variant_inputs": ["2\n1 2022-01-01\n2 2022-01-02", "3\n5 2021-05-01\n5 2020-05-01\n5 2019-05-01"],
        "starter_archetype": "general",
        "solver": solver_236
    },
    {
        "index": 237,
        "title_base": "Game Play Analysis Day Next Login",
        "description": "Write a solution to report the fraction of players that logged in again on the day immediately following their first login date.",
        "input_format": "First line contains total_players and M. Following lines contain M pairs of player_id and login_day_number.",
        "output_format": "Print the fraction rounded to 2 decimal places.",
        "constraints": "1 <= total_players <= 100",
        "sample_input": "3 4\n1 1\n1 2\n2 5\n3 10",
        "sample_output": "0.33",
        "explanation": "Only player 1 logged in on the day immediately following day 1. Fraction = 1 / 3 = 0.33.",
        "test_inputs": ["2 2\n1 1\n2 3", "1 2\n1 1\n1 2"],
        "variant_inputs": ["2 4\n1 1\n1 2\n2 3\n2 4", "3 3\n1 1\n2 2\n3 3"],
        "starter_archetype": "general",
        "solver": solver_237
    },
    {
        "index": 238,
        "title_base": "Managers with at Least 5 Reports",
        "description": "Write a solution to find managers with at least five direct reports.",
        "input_format": "First line contains N. Following lines contain N pairs of employee_name and manager_id (-1 for null).",
        "output_format": "Print manager names sorted alphabetically, or 'none'.",
        "constraints": "1 <= N <= 100",
        "sample_input": "6\nJohn -1\nDan 1\nJames 1\nAmy 1\nAnne 1\nRon 1",
        "sample_output": "John",
        "explanation": "John (id 1) has 5 direct reports.",
        "test_inputs": ["3\nA -1\nB 1\nC 1", "1\nBoss -1"],
        "variant_inputs": ["6\nBoss -1\nE1 1\nE2 1\nE3 1\nE4 1\nE5 1", "2\nA 1\nB 1"],
        "starter_archetype": "general",
        "solver": solver_238
    },
    {
        "index": 239,
        "title_base": "Sales Person Without Red Orders",
        "description": "Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name 'RED'.",
        "input_format": "First line contains N. Second line contains N salesperson names. Third line contains M. Fourth line contains M salesperson names with RED orders.",
        "output_format": "Print salesperson names sorted alphabetically, or 'none'.",
        "constraints": "1 <= N <= 100",
        "sample_input": "5\nAmy Mark Alex John Pam\n2\nAmy Mark",
        "sample_output": "Alex John Pam",
        "explanation": "Alex, John, and Pam have no orders related to RED.",
        "test_inputs": ["2\nAlice Bob\n1\nAlice", "1\nSole\n1\nSole"],
        "variant_inputs": ["3\nX Y Z\n1\nX", "2\nA B\n0"],
        "starter_archetype": "general",
        "solver": solver_239
    },
    {
        "index": 240,
        "title_base": "Investments in 2016 Total Sum",
        "description": "Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who have the same tiv_2015 value as one or more other policyholders, and are not located in the same city as any other policyholder.",
        "input_format": "First line contains N. Following lines contain N rows: pid tiv_2015 tiv_2016 lat lon.",
        "output_format": "Print the total sum with 2 decimal places.",
        "constraints": "1 <= N <= 100",
        "sample_input": "4\n1 10 5 10 10\n2 20 20 20 20\n3 10 30 20 20\n4 10 40 40 40",
        "sample_output": "45.00",
        "explanation": "pid 1 and 4 have shared tiv_2015 of 10 and unique coordinates. Total = 5 + 40 = 45.00.",
        "test_inputs": ["1\n1 10 10 10 10", "2\n1 10 20 1 1\n2 10 30 2 2"],
        "variant_inputs": ["3\n1 10 10 1 1\n2 10 20 2 2\n3 20 30 3 3", "2\n1 10 5 1 1\n2 20 5 1 1"],
        "starter_archetype": "general",
        "solver": solver_240
    }
]
