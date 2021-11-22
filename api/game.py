N, M = map(int, input().split())

pos_y, pos_x, dir = map(int, input().split())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

noc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
r_dirs = {0: 3, 1: 0, 2: 1, 3: 2}
re_dirs = {0: 2, 1: 3, 2: 0, 3: 1}
cnt = 1

# import pdb; pdb.set_trace()
while True:
    if grid[pos_y][pos_x] == 1:
        break
    grid[pos_y][pos_x] = 2
    for _ in range(4):
        dy, dx = noc[r_dirs[dir]]
        dir = r_dirs[dir]
        if grid[pos_y+dy][pos_x+dx] == 0:
            pos_y, pos_x = pos_y + dy, pos_x + dx
            cnt += 1
            break
    
        if _ == 3:
            dy, dx = noc[re_dirs[dir]]
            pos_y, pos_x = pos_y + dy, pos_x + dx
    
print(cnt)