import re

s = 'start'
result = []
while s:
    s = input().lower()
    if 'problem' in s:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
