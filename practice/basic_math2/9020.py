n = 10000
numbers = [True for i in range(n+1)]
numbers[0] = numbers[1] = False
for i in range(2, int((n)**0.5)+1):
    if numbers[i]:
        j = 2
        while i * j <= n:
            numbers[i * j] = False
            j += 1


T = int(input())
for test_case in range(T):
    n = int(input())

    start = 2
    result = [0, 1e9]
    for i in range(start, n // 2 + 1):
        if numbers[i]:
            left, right = i, n - left
            if numbers[right] and right - left < result[1] - result[0]:
                result = [left, right]
    print(result[0], result[1])

        
