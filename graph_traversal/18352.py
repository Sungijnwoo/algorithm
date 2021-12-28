import sys
input = sys.stdin.readline
import heapq as hq
n, m, k, x = map(int, input().split())

INF = sys.maxsize
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

distance = [INF for _ in range(len(graph))]
distance[x] = 0
q = [(0, x)]
hq.heapify(q)

while q:
    dist, now = hq.heappop(q)

    if distance[now] < dist:
        continue

    for idx in graph[now]:
        total_cost = dist + 1
        if total_cost < distance[idx]:
            distance[idx] = total_cost
            hq.heappush(q, (total_cost, idx))

if k not in distance:
    print(-1)
else:
    for x, i in enumerate(distance):
        if i == k:
            print(x)



