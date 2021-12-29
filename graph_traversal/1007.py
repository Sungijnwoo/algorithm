from itertools import combinations
import math

test_case = int(input())
final_result = []
for _ in range(test_case):
    n = int(input())

    points = []
    total_x, total_y = 0, 0
    for i in range(n):
        x, y = list(map(int, input().split()))
        points.append([x, y])
        total_x += x
        total_y += y

    result = 1e9
    noc = combinations(points, n // 2)

    for case in noc:
        x1_total, y1_total = 0, 0
        for x1, y1 in case:
            x1_total += x1
            y1_total += y1
        
        x2_total = total_x - x1_total
        y2_total = total_y - y1_total

        result = min(result, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))
    final_result.append(result)

for i in final_result:
    print(i)