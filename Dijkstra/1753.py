import heapq as hq
import sys 

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

start = int(input()) - 1

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((w, v-1))

costs = [INF for _ in range(V)]
costs[start] = 0
q = []
hq.heappush(q, (0, start))

while q:
    cost, pos = hq.heappop(q)
    if costs[pos] < cost:
        continue

    for w, next_node in graph[pos]:
        next_w = w + cost
        if next_w < costs[next_node]:
            costs[next_node] = next_w
            hq.heappush(q, (next_w, next_node))
    
for i in costs:
    if i == INF:
        print("INF")
    else:
        print(i)

