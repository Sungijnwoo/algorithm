import heapq as hq
N = int(input())

cards = [int(input()) for _ in range(N)]

cards.sort()

result = 0
hq.heapify(cards)

if len(cards) == 1:
    print(0)
else:
    while True:
        tmp = hq.heappop(cards) + hq.heappop(cards)
        result += tmp
        if not cards:
            break
        hq.heappush(cards, tmp)
    print(result)

