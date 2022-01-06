from collections import Counter, defaultdict
n = int(input())
numbers = list(map(int, input().split()))

eigen_numbers = list(set(numbers))
eigen_numbers.sort(reverse=True)

result = {i: len(eigen_numbers)-x-1 for x, i in enumerate(eigen_numbers)}

for i in numbers:
    print(result[i], end= " ")
