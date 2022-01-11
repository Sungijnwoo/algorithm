import sys
input = sys.stdin.readline
T = int(input())

stack = []
result = []
for _ in range(T):
    order = input().rstrip().split()
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif order[0] == 'size':
        result.append(len(stack))
    elif order[0] == 'empty':
        if stack:
            result.append(0)
        else:
            result.append(1)
    elif order[0] == 'top':
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

for i in result:
    print(i)

