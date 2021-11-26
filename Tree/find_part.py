import sys

N = int(sys.stdin.readline().rstrip())
stock = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
request = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(stock, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if stock[mid] == target:
            return True
        
        if stock[mid] > target:
            end -= 1
        
        else:
            start += 1
        
    return False

for req in request:
    if binary_search(stock, req, 0, N-1):
        print('yes', end=" ")
    else:
        print('no', end=" ")