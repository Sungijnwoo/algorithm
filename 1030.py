s, n, k, r1, r2, c1, c2 = map(int, input().split())

graph = [[0] * (n ** s) for _ in range(n**s)]

def black(pos, time):
    if time == s:
        return
    # print(pos)
    y1, x1, y2, x2 = pos
    dy, dx = (y2-y1), (x2-x1)
    black_y1, black_y2 = y1 + dy // n, y1 + ((dy // n) * (k+1))
    black_x1, black_x2 = x1 + dx // n, x1 + ((dx // n) * (k+1))
    for i in range(black_y1, black_y2):
        for j in range(black_x1, black_x2):
            graph[i][j] = 1
    
    for i in range(n):
        for j in range(n):
            # print(i*(dy//n), j*(dy//n), i*(dy//n)+(dy//n), j*(dy//n)+(dx//n))
            black((i*(dy//n), j*(dy//n), i*(dy//n)+(dy//n), j*(dy//n)+(dx//n)), time+1)


black((0, 0, len(graph), len(graph)), 0)
# for i in graph:
#     print(i)
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(graph[i][j], end="")
    print()