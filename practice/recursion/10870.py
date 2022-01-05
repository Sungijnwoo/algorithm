n = int(input())
dp = [0 for i in range(n+2)]
dp[1] = 1
def fibonacci(n):
    if n <= 1:
        return
    if dp[n-1] == 0:
        fibonacci(n-1)
    if dp[n-2] == 0:
        fibonacci(n-2)
    dp[n] = dp[n-1] + dp[n-2]

fibonacci(n)
print(dp[n])
    