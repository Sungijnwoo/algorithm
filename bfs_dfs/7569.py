from collections import deque
m, n, k = map(int, input().split())

graph = [[[0] * (m) for i in range(n)] for _ in range(k)]

for i in range(k):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))

q = deque([])
for z in range(k):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                q.append((z, y, x))

noc = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
time = 0
while True:
    for _ in range(len(q)):
        z, y, x = q.popleft()
        for dz, dy, dx in noc:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < k and 0 <= ny < n and 0 <= nx < m and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                q.append((nz, ny, nx))
    if not q:
        break
    time += 1

judge = True
for z in range(k):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                judge = False

result = time if judge else -1
print(result)

