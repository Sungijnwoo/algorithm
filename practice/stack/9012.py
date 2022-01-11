T = int(input())

result = []
for _ in range(T):
    s = input()
    stack = []
    judge = True
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                judge = False
    
    if stack:
        judge = False
    result.append("YES" if judge else "NO")

for i in result:
    print(i)
