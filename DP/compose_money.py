N, M = map(int, input().split())

array = [int(input()) for _ in range(N)]

dp = [10001] * (M+1)
dp[0] = 0

for i in range(N):
    for j in range(array[i], M+1):
        if dp[j-array[i]] != 10001:
            dp[j] = min(dp[j], dp[j-array[i]]+1)
    print(dp)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])