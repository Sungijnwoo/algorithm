test_case = int(input())

for _ in range(test_case):
    n = int(input())
    data = list(map(int, input().split()))
    
    indegree = [0] * (n+1)
    graph = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = 1
            indegree[data[j]] += 1

    print(indegree)

