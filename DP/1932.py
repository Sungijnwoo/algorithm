n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for i in range(0, j+1)] for j in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))