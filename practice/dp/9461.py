dp = [0 for _ in range(101)]
dp[0] = 0
dp[1] = dp[2] = 1

T = int(input())
for test_case in range(T):
    n = int(input())
    if n <= 2:
        print(dp[n])
        continue
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[n])