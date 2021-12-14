from itertools import combinations
import copy
from collections import deque

N = int(input())

maps = [input().split() for _ in range(N)]

candidates = []
teachers = []
visited = []

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def check(teachers, graph):
    for y, x in teachers:
        for dy, dx in directions:
            tmp_y, tmp_x = y, x
            while True:
                tmp_y, tmp_x = tmp_y + dy, tmp_x + dx
                if tmp_y < 0 or tmp_y >= N or tmp_x < 0 or tmp_x >= N:
                    break
                if graph[tmp_y][tmp_x] == "S":
                    return False
                elif graph[tmp_y][tmp_x] == "O":
                    break
                
    return True

for y, i in enumerate(maps):
    for x, j in enumerate(i):
        if j == "X":
            candidates.append((y, x))
        elif j == "T":
            teachers.append((y, x))

noc = combinations(candidates, 3)
judge = False
for case in noc:
    temp_maps = copy.deepcopy(maps)
    for y, x in case:
        temp_maps[y][x] = "O"
    if check(teachers, temp_maps):
        judge = True
        break

if judge:
    print("YES")
else:
    print("NO")

        


