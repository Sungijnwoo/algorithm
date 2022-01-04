import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().rstrip().split())
    print(a+b)