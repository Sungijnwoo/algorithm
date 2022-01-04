dp = [[0] * (16) for _ in range(16)]

for i in range(1, 16):
    dp[0][i] = i

for i in range(1, 16):
    for j in range(1, 16):
        dp[i][j] = sum(dp[i-1][:j+1])

result = []
T = int(input())
for test_case in range(T):
    k = int(input())
    n = int(input())
    result.append(dp[k][n])

for i in result:
    print(i)

