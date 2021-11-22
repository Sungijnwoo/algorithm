def factorial_iterative(n):
    return n * factorial_iterative(n-1) if n > 1 else 1

print(factorial_iterative(5))