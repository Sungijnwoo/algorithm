import sys
import heapq as hq
import copy
def solution(n, start, end, roads, traps):
    INF = sys.maxsize
    reverse = 0
    graph = [[0] *(n+1) for i in range(n+1)]
    for u, v, c in roads:
        graph[u][v] = c

    distance = [INF for _ in range(n+1)]
    distance[start] = 0

    q = [(0, start, graph)]
    hq.heapify(q)
    visited = []

    while q:
        dist, now, graph = hq.heappop(q)
        for idx, i in enumerate(graph[now]):
            next_graph = copy.deepcopy(graph)
            if i != 0:
                total_cost = dist + i
                if (now, idx) not in visited:
                    visited.append((now, idx))
                    if idx in traps:
                        distance[idx] = min(distance[idx], total_cost)
                        next_graph = reverse_graph(next_graph, idx)
                        hq.heappush(q, (total_cost, idx, next_graph))
                    else:
                        distance[idx] = min(distance[idx], total_cost)
                        hq.heappush(q, (total_cost, idx, next_graph))
    return distance[end]

def reverse_graph(graph, n):
    for x, i in enumerate(graph[n]):
        graph[n][x], graph[x][n] = graph[x][n], graph[n][x]

    return graph



if __name__ == "__main__":
    assert solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]) == 5
    assert solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]) == 4