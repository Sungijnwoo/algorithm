from collections import deque

s, d = map(int, input().split())
visited = [False for _ in range(1000001)]

q = deque([(s, 0)])

while q:
    pos, cnt = q.popleft()
    visited[pos] = True
    if pos == d:
        print(cnt)
        break
    
    if pos+1 <= 100000 and visited[pos+1] == False:
        q.append((pos+1, cnt+1))
    if pos-1 >= 0 and visited[pos-1] == False:
        q.append((pos-1, cnt+1))
    if pos*2 <= 100000 and visited[pos*2] == False:
        q.append((pos*2, cnt+1))

