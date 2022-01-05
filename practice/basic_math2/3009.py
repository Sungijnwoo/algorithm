point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))

x, y = zip(point1, point2, point3)
result = [0, 0]
for i, j in zip(x, y):
    if x.count(i) == 1:
        result[0] = i
    if y.count(j) == 1:
        result[1] = j

print(result[0], result[1])
