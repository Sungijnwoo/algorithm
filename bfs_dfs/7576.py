from collections import deque

M, N = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(N)]

q = deque([])
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            q.append((i, j, 0))

noc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    y, x, cnt = q.popleft()
    for dy, dx in noc:
        n_y, n_x = y + dy, x + dx
        if 0 <= n_y < N and 0 <= n_x < M and grid[n_y][n_x] == 0:
            grid[n_y][n_x] = 1
            q.append((n_y, n_x, cnt+1))

can = True
for i in grid:
    if 0 in i:
        print(-1)
        can = False
        break

if can == True:
    print(cnt)


