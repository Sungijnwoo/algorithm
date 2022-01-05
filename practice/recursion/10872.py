n = int(input())

result = 1
def factorial(n):
    global result
    if n == 1 or n == 0:
        return
    result *= n
    factorial(n-1)

factorial(n)
print(result)