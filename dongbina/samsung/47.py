import copy 
max_result = 0

graph = [[] for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(0, 8, 2):
        graph[i].append(data[j:j+2])
        graph[i][-1][1] -= 1

dirs = {0: (-1, 0), 1: (-1, -1), 2: (0, -1), 3: (1, -1), 4: (1, 0), 5: (1, 1), 6: (0, 1), 7: (-1, 1)}
result = graph[0][0][0]

def dfs(graph, pos, cnt):
    global max_result
    y, x = pos
    dir = graph[y][x][1]
    cp_graph = copy.deepcopy(graph)
    cp_graph[y][x][0] = 0
    print(graph)
    move_fish(cp_graph)
    print(cp_graph, pos, cnt)
    for i in range(1, 4):
        dy, dx = dirs[dir]
        ny, nx = y + (dy * i), x + (dx * i)
        if 0 <= ny < 4 and 0 <= nx < 4 and graph[ny][nx][0] > 0:
            dfs(cp_graph, (ny, nx), cnt+cp_graph[ny][nx][0])
    
    max_result = max(cnt, max_result)


def move_fish(graph):
    for i in range(1, 17):
        change = False
        for j in range(4):
            for k in range(4):
                number, dir = graph[j][k]
                if number == i:
                    for rotate in range(8):
                        dir = (rotate + dir) % 8
                        dy, dx = dirs[dir]
                        ny, nx = j + dy, k + dx
                        if 0 <= ny < 4 and 0 <= nx < 4 and graph[ny][nx][0] > 0:
                            graph[j][k][1] = dir
                            graph[ny][nx], graph[j][k] = graph[j][k], graph[ny][nx]
                            change = True
                            break
                if change:
                    print(graph)
                    break
            if change:
                break

dfs(graph, (0, 0), graph[0][0][0])     
print(max_result)             

