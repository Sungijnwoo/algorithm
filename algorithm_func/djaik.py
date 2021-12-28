import heapq as hq

def djaik(graph, pos):
    distance = [1e9 for _ in range(len(graph))]
    distance[pos] = 0
    q = [(0, pos)]
    hq.heapify(q)
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue

        for val, pos in graph[now]:
            cost = dist + val
            if cost < distance[pos]:
                distance[pos] = cost
                hq.heappush(q, (cost, pos))

    return distance[1:]