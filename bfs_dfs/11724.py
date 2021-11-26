from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 5)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (N+1)

def dfs(u):
    visited[u] = True
    for _ in graph[u]:
        if not visited[_]:
            dfs(_)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)


