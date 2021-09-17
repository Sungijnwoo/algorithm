from collections import deque

size = int(input())
game_map = []
for i in range(size):
    game_map.append(input())

game_map = [i.split() for i in game_map]    # define game_map status

noc = [(1, 0), (0, 1)]
def bfs(x, y, n):
    possible = deque()
    possible.append((x, y, n))
    while possible:
        x, y, n = possible.popleft()
        if game_map[x][y] == '-1':
            return "HaruHaru"
        game_map[x][y] = 'x'
        for dx, dy in noc:
            X = x + (dx * int(n))                       
            Y = y + (dy * int(n))
            if 0 <= X < size and 0 <= Y < size:
                if game_map[X][Y] != 'x':
                    possible.append((X, Y, game_map[X][Y]))

if bfs(0, 0, game_map[0][0]) == None:
    print("Hing")
else:
    print("HaruHaru")
