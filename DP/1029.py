n = int(input())
dp =  [[[0] * 10 for j in range(1<<n)] for i in range(n)]

graph = [list(map(int, list(input()))) for _ in range(n)]


def dfs(artist, path, price):
    if dp[artist][path][price] != 0:
        return dp[artist][path][price]
    
    count = 0
    for nextA in range(1, n):
        if graph[artist][nextA] < price or path & (1 << nextA) > 0:
            continue
        count = max(count, 1 + dfs(nextA, path|(1 << nextA), graph[artist][nextA]))
    dp[artist][path][price] = count

    return count

print(1 + dfs(0, 1, 0))
for i in dp:
    print(i)