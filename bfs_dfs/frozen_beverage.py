from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input())) for i in range(N)]

def dfs(y, x):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False

    if grid[y][x] == 0:
        grid[y][x] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
