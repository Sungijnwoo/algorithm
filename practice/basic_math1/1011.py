from collections import deque
T = int(input())

for test_case in range(T):
    start, end = map(int, input().split())

    q = deque([(start, 0, 0)])
    noc = [-1, 0, 1]
    while q:
        position, distance, cnt = q.popleft()

        if position == end and distance == 1:
            break

        for diff in noc:
            next_distance = distance + diff
            next_pos = position + next_distance
            if next_pos <= end and next_distance > 0:
                q.append((next_pos, next_distance, cnt+1))
    print(cnt)
