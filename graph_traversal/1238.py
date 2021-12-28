import sys
input = sys.stdin.readline
import heapq as hq

n, m, x = map(int, input().split())

come_graph = [[] for _ in range(n+1)]
go_graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    come_graph[u].append((cost, v))
    go_graph[v].append((cost, u))

def djaik(graph, pos):
    distance = [1e9 for _ in range(len(graph))]
    distance[pos] = 0
    q = [(0, pos)]
    hq.heapify(q)
    while q:
        print(q)
        print(distance)
        dist, now = hq.heappop(q)
        
        if distance[now] < dist:
            print('hi')
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                hq.heappush(q, (cost, i[1]))

    return distance[1:]

come_distance = djaik(come_graph, x)
go_distance = djaik(go_graph, x)
final_distance = [come+go for come, go in zip(come_distance, go_distance)]
print(max(final_distance))
