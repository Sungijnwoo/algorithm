import sys
import heapq as hq
from collections import deque

def diijkstra():
    input = sys.stdin.readline
    INF = sys.maxsize

    M, N = map(int, input().split())
    maze = [list(input()) for _ in range(N)]

    graph = [[] for _ in range(N*M)]
    noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(N):
        for j in range(M):
            for dy, dx in noc:
                if 0 <= i+dy < N and 0 <= j+dx < M:
                    graph[i*M+j].append((maze[i+dy][j+dx], (i+dy)*M+j+dx))


    q = []
    dp = [INF for _ in range(N*M)]
    dp[0] = 0
    hq.heappush(q, (0, 0))

    while q:
        cost, pos = hq.heappop(q)
        if dp[pos] < cost:
            continue

        for w, n_pos in graph[pos]:
            n_w = cost + int(w)
            if n_w < dp[n_pos]:
                dp[n_pos] = n_w
                hq.heappush(q, (n_w, n_pos))
        
    print(dp[-1])

def bfs():
    input = sys.stdin.readline
    INF = sys.maxsize

    M, N = map(int, input().split())
    maze = [list(input()) for _ in range(N)]

    q = []
    hq.heappush(q, (0, 0, 0))
    noc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = []
    while q:
        w, y, x= hq.heappop(q)
        visited.append((y, x))
        if y == N-1 and x == M-1:
            print(w)
            break
        for dy, dx in noc:
            if 0 <= y+dy < N and 0 <= x+dx < M and (y+dy, x+dx) not in visited:
                hq.heappush(q, (w+int(maze[y+dy][x+dx]), y+dy, x+dx))


if __name__ == "__main__":
    bfs()
        
    