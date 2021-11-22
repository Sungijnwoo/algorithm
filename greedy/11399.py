n = int(input())
deltatime = list(map(int, input().split()))

deltatime.sort()


result = [i * (len(deltatime) - x) for x, i in enumerate(deltatime)]

print(sum(result))