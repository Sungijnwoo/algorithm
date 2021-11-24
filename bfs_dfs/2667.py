from collections import deque

N = int(input())


grid = [list(map(int, input())) for i in range(N)]

y, x = 0, 0
cnt = 0

def dfs(y, x):
    global cnt
    if 0 <= y < N and 0 <= x < N and grid[y][x] == 1:
        cnt += 1
        grid[y][x] = 0
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False

result = []
for y in range(N):
    for x in range(N):
        if dfs(y, x) == True:
            result.append(cnt)
        else:
            cnt = 0
            
result.sort()
print(len(result))
for _ in result:
    print(_)