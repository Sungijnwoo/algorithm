n = int(input())
target = n
cnt= 0
while True:
    cnt += 1
    str_n = str(n)
    if len(str_n) < 2:
        str_n = '0' + str_n
    
    t = str(int(str_n[0]) + int(str_n[1]))

    n = int(str_n[-1] + t[-1])

    if n == target:
        break
print(cnt)





        
    
    
