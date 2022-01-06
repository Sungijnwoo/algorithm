n = int(input())

for i in range(n):
    generator = i
    for j in str(i):
        generator += int(j)
    
    if generator == n:
        break

if i == n-1:
    print(0)
else:
    print(i)