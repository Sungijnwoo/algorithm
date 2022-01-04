from collections import defaultdict
result = 1
for _ in range(3):
    result *= int(input())

result = str(result)
params = defaultdict(int)

for i in result:
    params[i] += 1

for i in range(10):
    print(params[str(i)])
