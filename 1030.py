s, n, k, r1, r2, c1, c2 = map(int, input().split())

graph = [[0] * (n ** s) for _ in range(n**s)]

def change_black(ny1, nx1, ny2, nx2):
    for i in range(ny1, ny2):
        for j in range(nx1, nx2):
            graph[i][j] = 1

def dfs(pos, time):
    if time == s:
        return
    y1, x1, y2, x2 = pos
    dy, dx = (y2-y1) // n, (x2-x1) // n
    black_range = [t for t in range((n - k) // 2, (n-k) // 2 + k)]
    for i in range(n):
        for j in range(n): 
            ny1 = y1 + dy * i
            nx1 = x1 + dx * j
            ny2 = ny1 + dy
            nx2 = nx1 + dx
            if i in black_range and j in black_range:
                change_black(ny1, nx1, ny2, nx2)   
            dfs((ny1, nx1, ny2, nx2), time+1)


dfs((0, 0, len(graph), len(graph)), 0)
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(graph[i][j], end="")
    print()