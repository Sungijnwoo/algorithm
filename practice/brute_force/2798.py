from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

noc = combinations(cards, 3)
result = 0

for case in noc:
    if sum(case) <= m:
        result = max(result, sum(case))
    else:
        continue

print(result)