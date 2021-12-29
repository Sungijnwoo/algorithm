import heapq as hq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def daikstra():
    distance = [INF for _ in range(n)]
    history = [_ for _ in range(n)]
    distance[start] = 0
    
    q = [(0, start)]
    hq.heapify(q)
    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist:
            continue

        for idx, val in graph[now]:
            total_cost = val + dist
            if distance[idx] > total_cost:
                history[idx] = now
                distance[idx] = total_cost
                hq.heappush(q, (total_cost, idx))
    return distance, history

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    start, real_end = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
    
    distance, history = daikstra()
    
    min_distance = distance[real_end]
    if min_distance < INF:
        while True:
            end = real_end
            while True:
                for i in graph[history[end]]:
                    if i[0] == end:
                        graph[history[end]].remove(i)
                end = history[end]
                
                if end == start:
                    break
            distance, history = daikstra()
            if min_distance != distance[real_end]:
                break
        distance, history = daikstra()
    if distance[real_end] < INF:
        print(distance[real_end])
    else:
        print(-1)

        

