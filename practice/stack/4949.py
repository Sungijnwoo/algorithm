busket = {']': '[', ')': '('}
result = []
while True:
    s = input()
    if s == '.':
        break
    stack = []
    judge = True
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if not stack:
                judge = False
                break
            if stack[-1] == busket[i]:
                stack.pop()
            else:
                judge = False
    if stack:
        judge = False
    result.append("yes" if judge else "no")

for i in result:
    print(i)

            