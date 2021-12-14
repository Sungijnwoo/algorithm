from collections import deque

N, L, R = map(int, input().split())

graphs = [list(map(int, input().split())) for _ in range(N)]

visited = []

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(y, x):
    neighbor = []
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        neighbor.append((y, x))
        for dy, dx in directions:
            n_y, n_x = y + dy, x + dx
            if 0 <= n_y < N and 0 <= n_x < N and (n_y, n_x) not in visited:
                if L <= abs(graphs[y][x] - graphs[n_y][n_x]) <= R:
                    visited.append((n_y, n_x))
                    q.append((n_y, n_x))
    return neighbor

cnt = 0
while True:
    neighbors = []
    visited = [(0, 0)]
    for y, i in enumerate(graphs):
        for x, j in enumerate(i):
            if (y, x) == (0, 0) or (y, x) not in visited:
                neighbor = dfs(y, x)
                neighbors.append(neighbor)
    
    print(neighbors)
    for case in neighbors:
        people = sum([graphs[y][x] for y, x in case]) // len(case)
        for y, x in case:
            graphs[y][x] = people
    # if cnt == 4:
    #     break
    if len(neighbors) == N ** 2:
        break
    cnt += 1

print(cnt)
            




