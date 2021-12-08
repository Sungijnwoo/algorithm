N = int(input())
K = int(input())

maps = [[0 for _ in range(N)] for __ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    maps[y][x] = 1

L = int(input())
move = {}

for _ in range(L):
    t, r = input().split()
    move[int(t)] = r

directions = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

body = [[(0, 0), "R"]]
time = 0
maps[0][0] = 2


while body:
    # print(body)
    (head_y, head_x), head_dir = body[-1]
    if time in move.keys():
        if move[time] == "D":
            if head_dir == "U": head_dir = "R"
            elif head_dir == "R": head_dir = "D"
            elif head_dir == "D": head_dir = "L"
            else: head_dir = "U"
        else:
            if head_dir == "U": head_dir = "L"
            elif head_dir == "L": head_dir = "D"
            elif head_dir == "D": head_dir = "R"
            else: head_dir = "U"

    head_dy, head_dx = directions[head_dir]
    next_head_y, next_head_x = head_y + head_dy, head_x + head_dx

    if next_head_y < 0 or next_head_y >= N or next_head_x < 0 or next_head_y >= N:
        # print("hi")
        # print(next_head_y, next_head_x)
        break

    body.append([(next_head_y, next_head_x), head_dir])
    try:
        if maps[next_head_y][next_head_x] == 0:
            (tail_y, tail_x), tail_dir = body[0]
            maps[tail_y][tail_x] = 0
            body = body[1:]

        elif maps[next_head_y][next_head_x] == 2:
            # print("hi2")
            # print(next_head_y, next_head_x)
            break
        
        maps[next_head_y][next_head_x] = 2
        time += 1
    except:
        break

print(time+1)
