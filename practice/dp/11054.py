n = int(input())
a = list(map(int, input().split()))

left_dp = [0 for _ in range(n)]
right_dp = [0 for _ in range(n)]
for i in range(1, n):
    for j in range(i, -1, -1):
        if a[i] > a[j]:
            left_dp[i] = max(left_dp[i], left_dp[j]+1)

for i in range(n-2, -1, -1):
    for j in range(i, n):
        if a[i] > a[j]:
            right_dp[i] = max(right_dp[i], right_dp[j]+1)


result = []
for l, r in zip(left_dp, right_dp):
    result.append(l+r)

print(max(result) + 1)

