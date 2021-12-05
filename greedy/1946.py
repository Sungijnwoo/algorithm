import sys
T = int(input())

result = []
for _ in range(T):
    cnt = 1
    people = int(input())

    noc = []
    for i in range(people):
        left, right = map(int, sys.stdin.readline().split())
        noc.append((left, right))

    noc.sort()
    Max = noc[0][1]

    for i in range(1, people):
        if Max > noc[i][1]:
            cnt += 1
            Max = noc[i][1]
    result.append(cnt)

for i in result:
    print(i)