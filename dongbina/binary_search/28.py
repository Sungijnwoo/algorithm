N = int(input())
li = list(map(int, input().split()))

start, end = 0, N-1

result = -1
if li[start] == start:
    result = start
elif li[end] == end:
    result = end
else:
    while start <= end:
        middle = (start + end) // 2

        if li[middle] == middle:
            result = middle
            break
        
        elif li[middle] < middle:
            start = middle + 1
        
        elif li[middle] > middle:
            end = middle - 1
        # print(start, end)
    
print(result)