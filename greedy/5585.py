n = int(input())
n = 1000 - n

noc = [500, 100, 50, 10, 5, 1]
result = 0

for i in noc:
    if n == 0:
        break
    if n < i:
        continue
    result += n // i
    n = n % i
    
    
print(result)