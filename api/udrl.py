N = int(input())
commands = input().split()

y, x = 0, 0

for cmd in commands:
    if cmd == "U":
        if y != 0:
            y -= 1
    elif cmd == "D":
        if y != N-1:
            y += 1
    elif cmd == "R":
        if x != N-1:
            x += 1
    elif cmd == "L":
        if x != 0:
            x -= 1

print(y+1, x+1)