import sys
input = sys.stdin.readline
import heapq as hq

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = sys.maxsize

for _ in range(e):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

v1, v2 = map(int, input().split())


def daikj(start):
    distance = [INF for _ in range(len(graph))]
    distance[start] = 0
    q = []
    hq.heappush(q, (0, start))
    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist:
            continue
            
        for idx, cost in graph[now]:
            total_cost = cost + dist
            if total_cost < distance[idx]:
                distance[idx] = total_cost
                hq.heappush(q, (total_cost, idx))
    return distance

one_start = daikj(1)
v1_start = daikj(v1)
v2_start = daikj(v2)

case1 = one_start[v1] + v1_start[v2] + v2_start[n]
case2 = one_start[v2] + v2_start[v1] + v1_start[n]

result = min(case1, case2)

if result < INF:
    print(result)
else:
    print(-1)