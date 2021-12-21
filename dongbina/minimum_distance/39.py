import heapq as hq
test_case = int(input())

result = []
noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(test_case):
    size = int(input())
    graph = [list(map(int, input().split())) for i in range(size)]

    costs = [[1e9 for i in range(size)] for j in range(size)]
    costs[0][0] = graph[0][0]

    q = [(5, 0, 0)]
    hq.heapify(q)
    visited = []

    while q:
        cost, y, x= hq.heappop(q)
        visited.append((y, x))
        for dy, dx in noc:
            n_y, n_x = y + dy, x + dx
            if 0 <= n_y < size and 0 <= n_x < size and (n_y, n_x) not in visited:
                costs[n_y][n_x] = min(costs[n_y][n_x], costs[y][x] + graph[n_y][n_x])
                hq.heappush(q, (costs[n_y][n_x], n_y, n_x))
    for i in costs:
        print(i)
    break

