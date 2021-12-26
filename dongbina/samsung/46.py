from collections import deque
INF = 1e9

n= int(input())

array = [list(map(int, input().split())) for _ in range(n)]

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

noc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs():
    dist = [[-1] * n for _ in range(n)]

    q = deque([(now_x, now_y)])

    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in noc:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]

        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0

