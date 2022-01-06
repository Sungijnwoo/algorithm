import heapq as hq

n = int(input())
q = []
for _ in range(n):
    hq.heappush(q, int(input()))

for _ in range(n):
    print(hq.heappop(q))