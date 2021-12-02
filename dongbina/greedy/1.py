from collections import deque
N = int(input())
afraid = list(map(int, input().split()))

afraid.sort()
q = deque(afraid)

result = 0
while True:
    select = q.popleft()

    target = 1
    while target != select and q:
        invite = q.popleft()
        if invite > select:
            select = invite
        target += 1
    if not q:
        break
    result += 1

print(result)