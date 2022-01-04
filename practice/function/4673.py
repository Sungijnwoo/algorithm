result = [i for i in range(1, 10001)]

def d(n: int) -> None:
    if n > 10000:
        return
    k = list(map(int, list(str(n))))
    k = sum(k)
    n += k
    if n in result:
        result.remove(n)
        d(n)

for i in result:
    d(i)

for i in result:
    print(i)
