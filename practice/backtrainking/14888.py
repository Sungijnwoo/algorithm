N = int(input())

numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

min_value, max_value = 1e9, -1e9

def dfs(i, n):
    global plus, minus, multiply, divide, min_value, max_value
    if i == N:
        min_value = min(min_value, n)
        max_value = max(max_value, n)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, n+numbers[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, n-numbers[i])
            minus += 1
        if multiply > 0:
            multiply -= 1
            dfs(i+1, n*numbers[i])
            multiply += 1
        if divide > 0:
            divide -= 1
            dfs(i+1, int(n/numbers[i]))
            divide += 1

dfs(1, numbers[0])
print(max_value)
print(min_value)



