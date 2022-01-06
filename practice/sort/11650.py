n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]
coords.sort(key=lambda x: (x[0], x[1]))

for x, y in coords:
    print(x, y)