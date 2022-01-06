from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]

#평균값
print(round(sum(numbers) / len(numbers)))

#중앙값
numbers.sort()
print(numbers[len(numbers)//2])

#최빈값
most_frequency = Counter(numbers).most_common(2)
if len(numbers) > 1:
    if most_frequency[0][1] == most_frequency[1][1]:
        print(most_frequency[1][0])
    else:
        print(most_frequency[0][0])
    
else:
    print(most_frequency[0][0])

#범위값
print(numbers[-1] - numbers[0])