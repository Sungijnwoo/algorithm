n = int(input())
m = int(input())

costs = [[1e9 for i in range(n)] for j in range(n)]

for i in range(n):
    costs[i][i] = 0

for _ in range(m):
    u, v, cost = map(int, input().split())
    costs[u-1][v-1] = min(costs[u-1][v-1], cost)


for i in range(n):
    for j in range(n):
        for k in range(n):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])


for idx, cost in enumerate(costs):
    for i in cost:
        if i == 1e9:
            print(0, end= " ")
        else:
            print(i, end= " ")
    
    if idx < len(costs) - 1:
        print()