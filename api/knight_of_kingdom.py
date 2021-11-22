pos = input()
alphabet = 'abcdefgh'

x, y = alphabet.find(pos[0]), int(pos[1]) - 1

noc = [(1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)]

result = 0

for dy, dx in noc:
    if 0 <= x + dx < 8 and 0 <= y + dy < 8:
        result += 1

print(result)