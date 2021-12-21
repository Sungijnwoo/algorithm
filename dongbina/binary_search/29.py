from itertools import combinations

N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

start = 0
end = houses[-1] - houses[0]
result = 0

while start <= end:
    middle = (start + end) // 2

    count = 1
    selected = houses[0]
    for house in houses[1:]:
        if house - selected >= middle:
            selected = house
            count += 1
    
    if count >= C:
        start = middle + 1
        result = middle
    
    else:
        end = middle - 1

print(result)