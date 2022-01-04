T = int(input())

result = []
for test_case in range(T):
    n, *scores = map(int, input().split())
    avg = sum(scores) / n
    above_avg = [i for i in scores if i > avg]
    result.append(len(above_avg) / n)

for i in result:
    print(f'{i*100:.3f}%')
