from itertools import combinations

N, M = map(int, input().split())

houses, chickens = [], []
for i in range(N):
    grid = list(map(int, input().split()))
    for j in range(N):
        if grid[j] == 1:
            houses.append((i, j))
        elif grid[j] == 2:
            chickens.append((i, j))

noc = combinations(chickens, M)

min_chicken_street = 1e9

for case in noc:
    total_distance = 0
    for house in houses:
        m = 1e9
        for chicken in case:
            m = min(m, abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        total_distance += m
    min_chicken_street = min(min_chicken_street, total_distance)

print(min_chicken_street)

