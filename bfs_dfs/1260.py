from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(1000)]

for _ in range(M):
    s, v = map(int, input().split())
    graph[s-1].append(v)
    graph[v-1].append(s)

graph = [sorted(i) for i in graph]
dfs_visited = [V]

def dfs(s):
    for i in graph[s-1]:
        if i not in dfs_visited:
            dfs_visited.append(i)
            dfs(i)
dfs(V)
print(dfs_visited)



q = deque([V])
bfs_visited = [V]

while q:
    s = q.popleft()
    for i in graph[s-1]:
        if i not in bfs_visited:
            q.append(i)
            bfs_visited.append(i)

print(bfs_visited)

