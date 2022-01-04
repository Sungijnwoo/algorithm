T = int(input())

result = []
for test_case in range(T):
    r, s = input().split()
    r = int(r)
    qr = ''
    for i in s:
        qr += i * r
    result.append(qr)

for i in result:
    print(i)