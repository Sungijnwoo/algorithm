N = int(input())
array = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

n = max(array)

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in array:
    for j in dp[i]:
        print(j, end=" ")
    print()



