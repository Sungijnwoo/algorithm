from collections import deque

size_x, size_y = list(map(int, input().split()))        # map size
maps = []                                               
for i in range(size_x):
    maps.append(list(input()))
    if 'I' in maps[-1]:
        start = i, maps[-1].index('I')                  # find start position

number = 0
q = deque()
q.append(start)
noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    pos = q.popleft()
    x, y = pos
    maps[x][y] = 'X'
    for dx, dy in noc:
        X, Y = x + dx, y + dy
        if 0 <= X < size_x and 0 <= Y < size_y and maps[X][Y] != 'X':
            if maps[X][Y] == 'P':
                number += 1
            maps[X][Y] = 'X'
            q.append((X, Y))

print(number) if number else print('TT')



