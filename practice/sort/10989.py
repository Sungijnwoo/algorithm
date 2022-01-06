import sys
input = sys.stdin.readline

dp = [0] * 100001
n = int(input())

for _ in range(n):
    dp[int(input())] += 1

for x, i in enumerate(dp):
    for _ in range(i):
        print(x)