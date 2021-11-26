import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
rice_cake = list(map(int, input().split()))

rice_cake.sort(reverse=True)

def cal(n):
    s = 0
    for i in rice_cake:
        if n >= i:
            break
        s += (i-n)
    return s

for x, i in enumerate(rice_cake):
    if cal(i) >= M:
        while True:
            if cal(i) == M or i == rice_cake[x-1]-1:
                break
            i += 1
        
        print(i)
        break

