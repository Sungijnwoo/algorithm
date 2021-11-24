from collections import deque

computer_cnt = int(input())
N = int(input())

graph = [[0 for i in range(computer_cnt)] for j in range(computer_cnt)]


for _ in range(N):
    y, x = map(int, input().split())
    graph[y-1][x-1] = graph[x-1][y-1] = 1

cnt = 0
visited = []
def dfs(n):
    visited.append(n)
    global cnt
    for x, i in enumerate(graph[n]):
        if x != n and i == 1:
            graph[n][x] = 0
            graph[x][n] = 0
            if x not in visited:
                cnt += 1
                dfs(x)

dfs(0)
print(cnt)