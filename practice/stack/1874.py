import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

result = []
stack = []
number = 1
for i in range(2*n):
    if not stack or numbers[0] != stack[-1]:
        result.append('+')
        stack.append(number)
        number += 1
    elif numbers[0] == stack[-1]:
        stack.pop()
        del numbers[0]
        result.append('-')

if stack:
    print("NO")
else:
    for i in result:
        print(i)
        