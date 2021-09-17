from collections import deque

def Bucket_Brigade():
    maps = []

    for i in range(10):
        maps.append(list(input()))
        if 'B' in maps[-1]:
            start = [i, maps[-1].index('B')]
        if 'L' in maps[-1]:
            end = [i, maps[-1].index('L')]
    
    noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    min_cnt = [[20 for i in range(10)] for j in range(10)]

    q = deque()
    q.append([start, [start], 0])   # current_pos, visited, cnt
    while q:
        pos, visited, cnt = q.popleft()
        for dx, dy in noc:
            X, Y = pos[0] + dx, pos[1] + dy
            if 0 <= X < 10 and 0 <= Y < 10 and [X, Y] not in visited and min_cnt[X][Y] > cnt + 1:
                if maps[X][Y] == 'R':
                    continue
                elif maps[X][Y] == 'L':
                    print(cnt)
                    return
                else:
                    min_cnt[X][Y] = cnt + 1
                    q.append([[X, Y], visited + [[X, Y]], cnt+1])
   
Bucket_Brigade()