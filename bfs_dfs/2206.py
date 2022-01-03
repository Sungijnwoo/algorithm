import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[0] * (m) for _ in range(n)]
q = deque([(0, 0, 1, 0)])
noc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited[0][0] = 1
while q:
    y, x, cost, br = q.popleft()

    if y == n-1 and x == m-1:
        break
    for dy, dx in noc:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 0 and (1 << br) & visited[ny][nx] == 0:
                visited[ny][nx] = (1 << br) | visited[ny][nx]
                q.append((ny, nx, cost+1, br))
            elif graph[ny][nx] == 1 and br == 0 and (1 << 1) & visited[ny][nx] == 0:
                visited[ny][nx] = (1 << 1) | visited[ny][nx]
                q.append((ny, nx, cost+1, 1))

if y != n-1 or x != m-1:
    print(-1)
else:
    print(cost)