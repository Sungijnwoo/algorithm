import sys
from collections import deque
import copy
input = sys.stdin.readline

graph = [[] for i in range(4)]
for i in range(4):
    fishes = list(map(int, input().split()))
    for j in range(0, 8, 2):
        fishes[j+1] -= 1
        graph[i].append(fishes[j:j+2])

dirs = {0: (-1, 0), 1: (-1, -1), 2: (0, -1), 3: (1, -1), 4: (1, 0), 5: (1, 1), 6: (0, 1), 7: (-1, 1)}

ate = graph[0][0][0]
graph[0][0][0] = 'Shark'

def move_fish(g):
    for i in range(1, 17):
        y, x = find_fish(i)
        if (y, x) == ("x", "x"):
            continue
        direction = g[y][x][1]
        for j in range(8):
            dy, dx = dirs[(direction+j) % 8]
            ny, nx = y + dy, x + dx
            if 0 <= ny < 4 and 0 <= nx < 4 and g[ny][nx][0] != "Shark":
                g[y][x][1] = (direction+j) % 8
                g[y][x], graph[ny][nx] = g[ny][nx], g[y][x]
                break
    return g

def find_fish(n):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == n:
                return i, j
    return 'x', 'x'

def print_fish(g):
    for i in range(4):
        print(g[i])
    print()

# print_fish(graph)
q = deque([(0, 0, ate, graph)])
result = 0
cnt = 0
while q:
    y, x, ate, graph = q.popleft()
    direction = graph[y][x][1]

    graph[y][x][0] = 0
    graph = move_fish(graph)
    dy, dx = dirs[direction]
    judge = False
    for i in range(1, 4):
        ny, nx = y + (dy*i), x + (dx*i)
        if 0 <= ny < 4 and 0 <= nx < 4 and graph[ny][nx][0] != 0:
            next_graph = copy.deepcopy(graph)
            judge = True
            next_ate = ate + graph[ny][nx][0]
            next_graph[ny][nx][0] = "Shark"
            print(ate, next_ate)
            print_fish(next_graph)
            q.append((ny, nx, next_ate, next_graph))
            
    if judge == False:
        result = max(result, ate)
print(result)
            





