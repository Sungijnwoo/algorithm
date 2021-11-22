N = int(input())

result = 0
for h in range(0, N+1):
    for m in range(0, 61):
        for s in range(0, 61):
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)