from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    cnt = 0
    while q:
        y, x = q.popleft()
        for dy, dx in noc:
            Y, X = y+dy, x+dx
            if (0 <= Y < N) and (0 <= X < N) and graph[Y][X] == '-': # check index range
                q.append((Y, X))
                graph[Y][X] = 'w'      # check visited point by change 'w'
                cnt += 1
    return cnt

for _ in range(int(input())):
    N = int(input())
    graph = [list(input()) for _ in range(N)]   # define map status
    noc = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)] #number of case that can go 
    res = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'w':
                res += bfs(i, j)
    print(res)
