n = int(input())
lines = [int(input()) for i in range(n)]
lines.sort()

weights = [i*(len(lines)-x) for x, i in enumerate(lines)]

print(max(weights))