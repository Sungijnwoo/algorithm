import copy 
from collections import deque
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

s, target_x, target_y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))

virus.sort()
time = 0
noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
virus = deque(virus)
while virus:
    if time == s:
        break
    for _ in range(len(virus)):
        v, x, y = virus.popleft()
        for dx, dy in noc:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                virus.append((graph[nx][ny], nx, ny))
    time += 1

print(graph[target_x-1][target_y-1])

