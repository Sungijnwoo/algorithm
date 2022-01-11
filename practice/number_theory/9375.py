from collections import defaultdict
from functools import reduce
T = int(input())

for test_case in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        wear, kind = input().split()
        clothes[kind] += 1
    clothes = list(clothes.values())
    clothes = [i+1 for i in clothes]

    print(reduce(lambda x, y: (x*y), clothes)-1)