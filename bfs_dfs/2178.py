from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

q = deque([(0, 0)])
noc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = []

while q:
    y, x = q.popleft()
    if y == N-1 and x == M-1:
        break

    for dy, dx in noc:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1:
            maze[ny][nx] = maze[y][x] + 1
            q.append((ny, nx))


print(maze[N-1][M-1])