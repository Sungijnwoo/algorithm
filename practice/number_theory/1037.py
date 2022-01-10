n = int(input())
divisors = list(map(int, input().split()))

print(max(divisors) * min(divisors))