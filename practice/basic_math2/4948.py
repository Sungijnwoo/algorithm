numbers = [True for i in range(123456*2+1)]
numbers[0] = numbers[1] = False
for i in range(2, int((123456*2)**0.5)+1):
    if numbers[i]:
        j = 2
        while i * j <= 123456*2:
            numbers[i * j] = False
            j += 1
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if numbers[i]:
            cnt += 1
    print(cnt)