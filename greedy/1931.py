N = int(input())

meetings = [list(map(int, input().split())) for i in range(N)]
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))


end_time = 0
result = 0

for start, end in meetings:
    if start >= end_time:
        result += 1
        end_time = end

print(result)
    



