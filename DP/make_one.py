from collections import deque
n = int(input())

# visited = []
# q = deque([(n, 0)])

# while q:
#     n, cnt = q.popleft()
#     visited.append(n)
#     if n == 1:
#         print(cnt)
#         break
#     if n % 5 == 0 and n // 5 not in visited:
#         q.append((n//5, cnt+1))
#     if n % 3 == 0 and n // 3 not in visited:
#         q.append((n//3, cnt+1))
#     if n % 2 == 0 and n // 2 not in visited:
#         q.append((n//2, cnt+1))
#     if n-1 not in visited:
#         q.append((n-1, cnt+1))

d = [0] * 27

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d)


