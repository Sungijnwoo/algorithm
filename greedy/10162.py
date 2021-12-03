time = int(input())
buttons = [300, 60, 10]
press = [0, 0, 0]

for x, i in enumerate(buttons):
    if time == 0:
        break
    if time < i:
        continue
    press[x] = time // i
    time = time % i

if time != 0:
    print(-1)
else:
    for i in press:
        print(i, end=" ")