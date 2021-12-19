N = int(input())

soliders = list(map(int, input().split()))
dp = [0] * N
dp[-1] = 1

for i in range(N-2, -1, -1):
    tmp = []
    for j in range(i+1, N):
        if soliders[j] < soliders[i]:
            tmp.append(dp[j])
    if tmp:
        dp[i] = max(tmp) + 1
    else:
        dp[i] = 1

print(N - max(dp))
