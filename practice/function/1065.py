n = int(input())

def is_p(n: int) -> bool:
    t = list(map(int, list(str(n))))
    differintial = [t[x+1]-t[x] for x, i in enumerate(t[:-1])]
    return True if len(set(differintial)) == 1 else False

count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
    elif i >= 100 and is_p(i):
        count += 1
print(count)

