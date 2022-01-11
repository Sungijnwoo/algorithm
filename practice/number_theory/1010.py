from math import factorial

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    b = factorial(m) // (factorial(n) * factorial(m - n))
    print(b)