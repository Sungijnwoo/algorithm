n = int(input())
numbers = [int(input()) for _ in range(n)]

lcm = numbers[0]
for i in numbers[1:]:
    j = lcm
    while i > 0:
        j, i = i, j % i
    lcm = j

result = []
min_n = min(numbers)
multiply = 1
while (n := multiply * lcm) < min_n:
    result.append(n)
    multiply += 1

print(result)