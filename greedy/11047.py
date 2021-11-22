N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
coins.sort(reverse=True)

result = 0
for i in coins:
    result += K // i
    K = K % i

print(result)