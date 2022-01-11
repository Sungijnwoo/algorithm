import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
n = int(input())

for _ in range(n):
    t = int(input())
    if t != 0:
        stack.append(t)
    else:
        stack.pop()

print(sum(stack))