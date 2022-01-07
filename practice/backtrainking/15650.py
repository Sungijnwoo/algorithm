n, m = map(int, input().split())
# candidates = [i for i in range(1, n+1)]

# s = []
# def dfs(start):
#     if len(s) == m:
#         print(*s)
#         return
    
#     for i in range(start, n+1):
#         if i not in s:
#             s.append(i)
#             dfs(i+1)
#             s.pop()

# dfs(1)

from itertools import combinations
candidiates = [i for i in range(1, n+1)]

noc = combinations(candidiates, m)

for case in noc:
    print(*case)