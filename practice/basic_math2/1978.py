import math
n = int(input())
numbers = map(int, input().split())

cnt = 0
for number in numbers:
    if number == 1:
        continue
    else:
        judge = True
        for j in range(2, int(math.sqrt(number))+1):
            if number % j == 0:
                judge = False
                break
        if judge:
            cnt += 1

print(cnt)
