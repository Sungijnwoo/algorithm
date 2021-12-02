n = int(input())
array = list(map(int, input().split()))

cnt = 0
cost = [1]

for i in range(1, n):
    m = []
    for j in range(i-1, -1, -1):
        if array[i] > array[j]:
            m.append(cost[j])
    if m:
        cost.append(max(m)+1)
    else:
        cost.append(1)

print(max(cost))

    

