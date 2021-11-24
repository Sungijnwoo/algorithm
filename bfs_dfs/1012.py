from collections import deque
import sys

sys.setrecursionlimit(10000)

epoch = int(input())

def dfs(y, x):
    if 0 <= y < N and 0 <= x < M and graph[y][x] == 1:
        print(y, x)
        graph[y][x] = 0
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False

for e in range(epoch):
    N, M, K = map(int, input().split())
    graph = [[0 for i in range(M)] for j in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())

        graph[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)


