N = list(input())
N.sort(reverse=True)

s = 0
for i in N:
    s += int(i)

if s % 3 != 0 or '0' not in N:
    print(-1)
else:
    print(''.join(N)) 