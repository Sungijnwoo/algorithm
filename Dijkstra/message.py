import heapq as hq

N, M, C = map(int, input().split())
C -= 1
road = [[] for _ in range(N)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    road[u-1].append((cost, v-1))

q = []
hq.heappush(q, (0, C))
distance = [int(1e9) for _ in range(N)]
distance[C] = 0

while q:
    cost, pos = hq.heappop(q)
    
    if distance[pos] < cost:
        continue

    for i in road[pos]:
        if cost + i[0] < distance[i[1]]:
            distance[i[1]] = cost = i[0]
            hq.heappush(q, (cost + i[0], i[1]))
    
cnt = 0
max_time = 0
for x, i in enumerate(distance):
    if x != C and i != 1e9:
        cnt += 1
        if max_time < i:
            max_time = i

print(cnt, max_time)
    

    

