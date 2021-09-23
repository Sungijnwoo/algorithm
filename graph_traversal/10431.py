times = int(input())
cases = []
for i in range(times):
    cases.append(list(map(int, input().split()[1:])))

result = []
# print(cases)
for case in cases:
    line = [case[0]]
    backstep_cnt = 0
    for i in case[1:]:
        if max(line) < i:
            line.append(i)
            continue
        else:
            for cnt, j in enumerate(line):
                if j > i:
                    line.insert(cnt, i)
                    backstep_cnt += (len(line) - cnt - 1)
                    break
    result.append(backstep_cnt)

for x, i in enumerate(result):
    print(x+1, i)