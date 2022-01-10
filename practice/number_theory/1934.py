T = int(input())

for test_case in range(T):
    a, b = map(int, input().split())
    lcf = a * b
    while b > 0:
        a, b = b, a % b
    print(lcf // a)
