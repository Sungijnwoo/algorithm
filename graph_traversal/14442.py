from collections import deque
import sys
n, m, k = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


q = deque([(0, 0, k, 1)])
visited = [[[1e9]*(k+1) for i in range(m)] for j in range(n)]
visited[0][0][k] = 1
noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
possible = False
while q:
    y, x, can_break, cnt = q.popleft()

    if y == n-1 and x == m-1:
        possible = True
        print(cnt)
        break

    for dy, dx in noc:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == '0' and visited[ny][nx][can_break] > cnt + 1:
                q.append((ny, nx, can_break, cnt+1))
                visited[ny][nx][can_break] = cnt + 1
            elif graph[ny][nx] == '1' and can_break > 0 and visited[ny][nx][can_break-1] > cnt + 1:
                q.append((ny, nx, can_break-1, cnt+1))
                visited[ny][nx][can_break-1] = cnt + 1

if not possible:
    print(-1)


