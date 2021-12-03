import re

s = input()

s = s.split('-')

for i in range(len(s)):
    s[i] = s[i].split("+")
    s[i] = str(sum(list(map(int, s[i]))))


result = eval('-'.join(s))
print(result)



