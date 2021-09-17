from collections import deque
def kick_number():
    n = int(input())
    
    for i in range(n):
        S, T = list(map(int, input().split()))
        q = deque()
        pos, cnt, visited = [S, T], 0, [[S, T]]
        q.append([pos, cnt, visited])
        while q:
            pos, cnt, visited = q.popleft()
            s, t = pos

            if s > t:
                continue

            if s == t:
                print(cnt)
                break

            if [s*2, t+3] not in visited:
                q.append([[s*2, t+3], cnt+1, visited + [[s*2, t+3]]])

            if [s+1, t] not in visited:
                q.append([[s+1, t], cnt+1, visited + [[s+1, t]]])


kick_number()