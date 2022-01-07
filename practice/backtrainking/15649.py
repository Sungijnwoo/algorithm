n, m = map(int, input().split())

s = []

def dfs():
    print(s)
    if len(s) == m:
        print(*s)
        return
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
