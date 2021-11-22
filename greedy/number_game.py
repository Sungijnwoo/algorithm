m, n = map(int, input().split())

grids = []
for i in range(m):
    grid = input()
    grids.append(list(map(int, grid.split())))

result = [min(i) for i in grids]

print(max(result))