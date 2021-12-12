from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for __ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [-1 for _ in range(N+1)]
start = X

distance[start] = 0

q = deque([start])
while q:
    pos = q.popleft()
    for n_pos in graph[pos]:
        if distance[n_pos] == -1:
            distance[n_pos] = distance[pos] + 1
            q.append(n_pos)

judge = False
for x, i in enumerate(distance):
    if i == K:
        print(x)
        judge = True

if not judge:
    print(-1)

