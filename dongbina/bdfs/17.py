from collections import deque
N, K = map(int, input().split())

maps = []
data = []

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] != 0:
            data.append((maps[i][j], 0, i, j))

q = deque(data)
S, Y, X = map(int, input().split())
noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    print(q)
    virus, s, x, y = q.popleft()
    if s == S:
        break

    for dy, dx in noc:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if maps[nx][ny] == 0:
                maps[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(maps[Y-1][X-1])

    




