n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

for x, i in enumerate(scores):
    scores[x] = (i / max_score) * 100

print(sum(scores) / n)