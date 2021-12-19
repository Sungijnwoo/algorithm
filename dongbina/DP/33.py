N = int(input())

schedule = {}

for _ in range(N):
    period, payback = map(int, input().split())
    schedule[_] = (period, payback)

dp = [0] * N

for i in range(N-1, -1, -1):
    period, payback = schedule[i]

    if i + period == N:
        dp[i] = payback
        continue
    elif i + period > N:
        continue
    
    dp[i] = payback + max(dp[i+period:])

print(max(dp))
    