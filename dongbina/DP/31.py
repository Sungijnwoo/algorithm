from collections import deque
import copy
T = int(input())

result = []
noc = [(0, 1), (-1, 1), (1, 1)]

for _ in range(T):
    n, m = map(int, input().split())

    gold_map = [[] for _ in range(n)]
    value = map(int, input().split())
    for idx, v in enumerate(value):
        gold_map[idx//m].append(v)

    dp = copy.deepcopy(gold_map)
    for start in range(n):
        q = deque([(start, 0)])
        while q:
            y, x = q.popleft()
            for dy, dx in noc:
                n_y, n_x = y + dy, x + dx
                if 0 <= n_y < n and 0 <= n_x < m:
                    dp[n_y][n_x] = max(dp[y][x] + gold_map[n_y][n_x], dp[n_y][n_x])
                    q.append((n_y, n_x))
    
    for i in dp:
        print(i)
    last_value = [dp[i][-1] for i in range(n)]
    result.append(max(last_value))

print(result)


        
    

