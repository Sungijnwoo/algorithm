from collections import deque
layer = int(input())

triangles = [list(map(int, input().split())) for i in range(layer)]

noc = [(1, 0), (1, 1)]

dp = [[0] * (i+1) for i in range(layer)]

dp[0][0] = triangles[0][0]

q = deque([(0, 0)])

while q:
    y, x = q.popleft()
    for dy, dx in noc:
        n_y, n_x = y + dy, x + dx
        try:
            dp[n_y][n_x] = max(triangles[n_y][n_x] + dp[y][x], dp[n_y][n_x])
            if (n_y, n_x) not in q and n_y != layer-1:
                q.append((n_y, n_x))
        except:
            pass

print(max(dp[-1]))

