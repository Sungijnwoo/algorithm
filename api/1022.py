r1, c1, r2, c2 = map(int, input().split())
m = max(map(abs, [r1, r2, c1, c2]))
N = m * 2 + 1

grid = [[0 for i in range(c2-c1+1)] for j in range(r2-r1+1)]
number_of_grid = (c2-c1+1) * (r2-r1+1)
y, x = 0, 0
n = 1
dcnt = 1
cnt = 0
repeat = 1
d = 0
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while number_of_grid > 0:
    if r1 <= y <= r2 and c1 <= x <= c2:
        number_of_grid -= 1
        grid[y - r1][x- c1] = n 
    n += 1
    cnt += 1

    dy, dx = dirs[d]
    x += dx
    y += dy

    if cnt == dcnt:
        cnt = 0
        d = (d+1) % 4
        if d == 0 or d == 2:
            dcnt += 1

n = str(n)
for i in grid:
    for j in i:
        print(str(j).rjust(len(n)), end= " ")
    print()


    
    


