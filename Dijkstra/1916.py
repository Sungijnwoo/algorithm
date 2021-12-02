import sys
import heapq as hq

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


A, B = map(int, input().split())

dp = [INF for _ in range(N+1)]
dp[A] = 0

q = []
hq.heappush(q, (0, A))

while q:
    cost, node = hq.heappop(q)
    if dp[node] < cost:
        continue

    for w, next_node in graph[node]:
        next_w = w + cost
        if next_w < dp[next_node]:
            dp[next_node] = next_w
            hq.heappush(q, (next_w, next_node))
    
print(dp[B])

