crotia = {'c=': 'č', 'c-': 'ć', 'dz=': 'dž', 'd-': 'đ', 'lj': 'lj', 'nj': 'nj', 's=': 'š', 'z=': 'ž'}
s = input()

result = 0
skip = []
for x, i in enumerate(s):
    if x in skip:
        continue
    if i in crotia.keys():
        result += 1
    elif x != len(s)-1 and s[x:x+2] in crotia.keys():
        skip = [x+1]
        result += 1
    elif x != len(s)-2 and s[x:x+3] in crotia.keys():
        skip = [x+1, x+2]
        result += 1
    else:
        result += 1

print(result)

