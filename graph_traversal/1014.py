import copy

T = int(input())
noc = [(0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
def find_seats(graph):
    global n, m
    possibles = []
    global n, m
    for i in range(n):
        for j in range(m):
            if graph[i][j] == ".":
                tmp_graph = copy.deepcopy(graph)
                tmp_graph[i][j] = 's'
                for dy, dx in noc:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        tmp_graph[ny][nx] = 'x'
                possibles.append(tmp_graph)
    return possibles

def dfs(graph, students):
    global result
    possibles = find_seats(graph)
    if not possibles:
        result = max(result, students)
    
    for next_graph in possibles:
        for i in next_graph:
            print(i)
        print()
        dfs(next_graph, students+1)


final_result = []
for test_case in range(T):
    n, m = map(int, input().split())
    graph = [list(input()) for _ in range(n)]

    result = 0
    dfs(graph, 0)
    final_result.append(result)
print(final_result)



    
