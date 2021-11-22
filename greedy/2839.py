n = int(input())

max_five = n // 5

for i in range(max_five, -1, -1):
    tmp = n - (5 * i)
    if tmp % 3 == 0:
        print(i + (tmp // 3))
        break

    if i == 0:
        print(-1)