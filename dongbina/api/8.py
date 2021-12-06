S = list(input())

number = []
string = []
for i in S:
    if i.isdigit():
        number.append(int(i))
    else:
        string.append(i)

string.sort()
n = sum(number)

print(''.join(string) + str(n))

