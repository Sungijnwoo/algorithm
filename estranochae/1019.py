n = int(input())

result = [0 for _ in range(10)]
nod = 1                             # number of digit
while n >= 10:   
    end_number = str(n)[-1]
    while str(n)[-1] != '9':
        for i in str(n):
            result[int(i)] += nod
        n -= 1
    if n < 10:
        break

    repeat = int(str(n)[:-1]) + 1
    for i in range(10):
        result[i] += (nod * repeat)
    result[0] -= nod

    n = n // 10
    nod = nod * 10

for i in range(n+1):
    result[i] += nod
result[0] -= nod

for i in result:
    print(i, end= " ")

