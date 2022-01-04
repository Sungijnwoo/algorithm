import math
T = int(input())

result = []
for test_case in range(T):
    h, w, n = map(int, input().split())

    col = n // h + 1
    row = n % h
    
    if row == 0:
        col = n // h
        row = h
    print(f'{row*100+col}')

    