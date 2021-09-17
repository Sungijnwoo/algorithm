from collections import deque

def frog():
    n = int(input())
    bridge = list(map(int, input().split()))
    start, end = list(map(int, input().split()))
    check = [-1] * n
    q = deque()
    q.append(start-1)

    while q:
        pos = q.popleft()
        for i in range(pos, n, bridge[pos]):
            if check[i] == -1:
                q.append(i)
                check[i] = check[pos] + 1
                if i == end - 1:
                    return check[i]
        
        for i in range(pos, -1, -bridge[pos]):
            if check[i] == -1:
                q.append(i)
                check[i] = check[pos] + 1
                if i == end - 1:
                    return check[i]
    return -1

print(frog())