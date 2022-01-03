from collections import deque
T = int(input())

result = []
noc = [(1, 2), (-1, 2), (2, 1), (-2, 1), (-1, -2), (1, -2), (-2, -1), (2, -1)]
for test_case in range(T):
    size = int(input())
    graph = [[0] * size for _ in range(size)]

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    start_y, start_x = start
    end_y, end_x = end

    q = deque([(start_y, start_x, 0)])
    while q:
        y, x, cnt = q.popleft()
        if y == end_y and x == end_x:
            result.append(cnt)
            break
        for dy, dx in noc:
            ny, nx = y + dy, x + dx
            if 0 <= ny < size and 0 <= nx < size and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx, cnt+1))

for i in result:
    print(i)


