import copy
n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
reverse_graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    reverse_graph[v][u] = 1

def dfs(n):
    for x, i in enumerate(tmp_graph[n]):
        if i == 1:
            tmp_graph[i][x] = 0
            visited.append(x)
            dfs(x)

def reverse_dfs(n):   
    for x, i in enumerate(tmp_reverse_graph[n]):
        if i == 1:
            tmp_reverse_graph[i][x] = 0
            visited.append(x)
            reverse_dfs(x)


result = 0
for i in range(1,n+1):
    visited = [i]
    tmp_graph = copy.deepcopy(graph)
    tmp_reverse_graph = copy.deepcopy(reverse_graph)
    dfs(i)
    reverse_dfs(i)
    if len(set(visited)) == n:
        result += 1

print(result)


        