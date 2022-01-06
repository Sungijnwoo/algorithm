n = list(input())

n.sort(key=lambda x: int(x), reverse=True)

print(''.join(n))
