import math

n = int(input())
factorial = str(math.factorial(n))
result = 0
for x, i in enumerate(factorial[::-1]):
    if i != '0':
        result = x
        break

print(result)
