from collections import deque

test_case = int(input())

def topology_sort():
    result = time.copy()
    q = deque()

    for x, i in enumerate(indegree):
        if i == 0:
            q.append(x)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result

final_result = []
for _ in range(test_case):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    time.insert(0, 0)

    indegree = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    target = int(input())
    result = topology_sort()
    final_result.append(result[target])


for i in final_result:
    print(i)


    
