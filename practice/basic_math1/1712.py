import math
a, b, c = map(int, input().split())


benefit = (c - b)
if benefit <= 0:
    print(-1)
else:
    result = int(a / benefit)
    print(result+1)