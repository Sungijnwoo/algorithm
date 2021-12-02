import heapq as hq
N, M = map(int, input().split())
road = [[] for _ in range(N)]


for _ in range(M):
    u, v = map(int, input().split())
    road[u-1].append(v-1)
    road[v-1].append(u-1)

x, k = map(int, input().split())
x -= 1
k -= 1

start = 0
q = []
hq.heappush(q, (0, start))
distance = [int(1e4) for _ in range(N)]
distance[start] = 0

while q:
    dist, pos = hq.heappop(q)
    if distance[pos] < dist:
        continue

    for i in road[pos]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            hq.heappush(q, (cost, i))

if distance[x] == 1e4 or distance[k] == 1e4:
    print(-1)

else:
    print(distance[x] + distance[k])

