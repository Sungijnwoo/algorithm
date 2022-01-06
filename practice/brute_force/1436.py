result = []
cnt = 0
while len(result) != 10000:
    if '666' in str(cnt):
        result.append(cnt)
    cnt += 1

print(result[int(input())-1])