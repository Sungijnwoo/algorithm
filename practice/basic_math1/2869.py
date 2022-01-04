import math
a, b , v = map(int, input().split())

benefit = a - b
v -= b

print(math.ceil(v/benefit))