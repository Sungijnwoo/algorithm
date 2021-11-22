from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
q = deque([(0, 0, 1)])
noc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    y, x, cnt = q.popleft()
    if y == N-1 and x == M-1:
        break

    for dy, dx in noc:
        try:
            target_y, target_x = y + dy, x + dx
            if grid[target_y][target_x] == 1:
                q.append((target_y, target_x, cnt+1))
        except:
            pass


print(cnt)