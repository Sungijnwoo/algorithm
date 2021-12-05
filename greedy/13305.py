import sys

N = int(input())

distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

price = [(x, i) for x, i in enumerate(price)]

price.sort(key=lambda x: x[1])

result = 0
pos = N-1
for i in price:
    if i[0] < pos:
        result += (i[1] * sum(distance[i[0]:pos]))
        pos = i[0]
        
print(result)