n, m = map(int, input().split())

# s = []

# def dfs(start):
#     if len(s) == m:
#         print(*s)
#         return
    
#     for i in range(start, n+1):
#         s.append(i)
#         dfs(i)
#         s.pop()

# dfs(1)

from itertools import combinations_with_replacement
candidates = [i for i in range(1, n+1)]

noc = combinations_with_replacement(candidates, r=m)
for case in noc:
    print(*case)