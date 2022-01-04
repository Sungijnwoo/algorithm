from typing import final


T = int(input())

final_result = []
for _ in range(T):
    scores = list(input())
    result = 0
    score = 0
    for i in scores:
        if i == 'X':
            score = 0
        elif i == 'O':
            score += 1
        result += score
    final_result.append(result)

for i in final_result:
    print(i)