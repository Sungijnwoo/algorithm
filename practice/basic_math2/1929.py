import math
m, n = map(int, input().split())

numbers = [True for i in range(n+1)]
numbers[0] = numbers[1] = False
for i in range(2, int(n**0.5)+1):
    if numbers[i]:
        j =2
        while i * j <= n:
            numbers[i * j] = False
            j += 1

result = []
for i in range(m, n+1):
    if numbers[i]:
        print(i)

