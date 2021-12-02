N = int(input())
array = [int(input()) for _ in range(N)]

n = max(array)
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(2, n+1):
    if i-1 >= 0:
        dp[i] += dp[i-1]
    if i-2 >= 0:
        dp[i] += dp[i-2]
    if i-3 >= 0:
        dp[i] += dp[i-3]

for i in array:
    print(dp[i])
