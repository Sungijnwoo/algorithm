from itertools import combinations
from queue import deque
from copy import deepcopy
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

zero = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero.append(M*i+j)

def dfs(y, x):
    q = deque([(y, x)])
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        y, x = q.popleft()
        for dy, dx in delta:
            n_y, n_x = y + dy, x + dx
            if 0 <= n_y < N and 0 <= n_x < M and tmp_graph[n_y][n_x] == 0:
                q.append((n_y, n_x))
                tmp_graph[n_y][n_x] = 1

nocs = combinations(zero, 3)
max_cnt = 0
for noc in nocs:
    tmp_graph = deepcopy(graph)
    for p in noc:
        tmp_graph[p//M][p%M] = 1

    for y in range(N):
        for x in range(M):
            if tmp_graph[y][x] == 2:
                dfs(y, x)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 0:
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)




