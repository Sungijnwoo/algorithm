map_size = int(input())
grid = [[[] for i in range(map_size)] for j in range(map_size)]

commands = input()

#start pos
pos = (0, 0)
# command to (dx, dy)
command_dir = {'D' : (1, 0), 'U' : (-1, 0), 'R' : (0, 1), 'L' : (0, -1)}    
for command in commands:
    x, y = pos
    dx, dy = command_dir[command]
    # prevent mixing 'U' 'D' or 'R' 'L'
    if command == 'U': command = 'D'                                        
    elif command == 'L': command = 'R'

    X, Y = x + dx, y + dy
    if 0 <= X < map_size and 0 <= Y < map_size:
        if command not in grid[x][y]:
            grid[x][y].append(command)

        if command not in grid[X][Y]:
            grid[X][Y].append(command)
        pos = (X, Y)

# change dir to scar '+', '-', '.'
for x, i in enumerate(grid):
    for y, j in enumerate(i):
        if len(grid[x][y]) >= 2:
            grid[x][y] = '+'
        elif len(grid[x][y]) == 1:
            if grid[x][y][0] == 'D' or grid[x][y][0] == 'U':
                grid[x][y] = '|'
            else:
                grid[x][y] = '-'
        else:
            grid[x][y] = '.'

for i in grid:
    print(''.join(i))