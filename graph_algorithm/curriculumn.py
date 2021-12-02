from collections import deque
import copy
N = int(input())

graph = [[] for i in range(N+1)]
costs = [0] * (N+1)
indegree = [0] * (N+1)
for _ in range(1, N+1):
    li = list(map(int, input().split()))
    cost = li[0]
    costs[_] = cost
    for j in li[1:-1]:
        graph[j].append(_)
        indegree[_] += 1


q = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

result = copy.deepcopy(costs)
while q:
    now = q.popleft()
    print(graph[now])
    for i in graph[now]:
        result[i] = max(result[i], result[now] + costs[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in result[1:]:
    print(i)

