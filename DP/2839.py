N = int(input())

dp = [10001 for i in range(N+1)]

array = [3, 5]
dp[0] = 0

for i in range(2):
    money = array[i]
    for j in range(money, N+1):
        if dp[j-money] != 1001:
            dp[j] = min(dp[j], dp[j-money]+1)

if dp[N] == 10001:
    print(-1)
else:
    print(dp[N])
