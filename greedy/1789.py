S = int(input())

result = 0
num = 1
while True:
    result += num
    if result > S:
        print(num-1)
        break
    elif result == S:
        print(num)
        break
    num += 1
