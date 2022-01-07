n, m = map(int, input().split())

# s = []

# def dfs():
#     if len(s) == m:
#         print(*s)
#         return
    
#     for i in range(1, n+1):
#         s.append(i)
#         dfs()
#         s.pop()

# dfs()
from itertools import product
candidates = [i for i in range(1, n+1)]

noc = product(candidates, repeat=m)

for case in noc:
    print(*case)
