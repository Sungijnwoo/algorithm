import heapq as hq
n, m = map(int, input().split())

costs = [1e9 for _ in range(n+1)]
costs[1] = 0
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = [(0, 1)]
hq.heapify(q)

while q:
    print(q)
    cost, pos = hq.heappop(q)
    if costs[pos] < cost:
        continue
    for idx in graph[pos]:
        if costs[idx] > costs[pos]+1:
            costs[idx] = costs[pos]+1
            hq.heappush(q, (costs[idx], idx))
        
for x, i in enumerate(costs):
    if i == 1e9:
        costs[x] = 0

result = []
max_distance = max(costs)
cnt = 0
for x, i in enumerate(costs):
    if i == max_distance:
        if not result:
            result.append(x)
        cnt += 1
result.append(max_distance)
result.append(cnt)
print(result)
    


