from collections import defaultdict
T = int(input())

cnt = 0
for test_case in range(T):
    word = input()
    params = {}
    group = True
    for x, s in enumerate(word):
        if params.get(s) != None and x - params.get(s) > 1:
            group = False
            break
        params[s] = x
    if group:
        cnt += 1

print(cnt)

