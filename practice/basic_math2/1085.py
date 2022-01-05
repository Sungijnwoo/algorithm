x, y, w, h = map(int, input().split())

result = [x, y, abs(x-w), abs(y-h)]
print(min(result))