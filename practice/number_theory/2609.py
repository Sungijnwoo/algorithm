a, b = map(int, input().split())

min_n = min(a, b)
max_n = max(a, b)

common_divisor = 1
for i in range(min_n, 0, -1):
    if b % i == 0 and a % i == 0:
        common_divisor = i
        break

multiply = 1
while True:
    if multiply * min_n % max_n == 0:
        common_factor = multiply * min_n
        break
    multiply += 1

print(common_divisor)
print(common_factor)