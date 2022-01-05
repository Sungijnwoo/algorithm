from itertools import combinations, permutations

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    tmp = [a, b]
    tmp.sort()
    parent[tmp[1]] = tmp[0]

def solution(status):
    graph = {}
    parent = {}
    for i in range(len(status)+1):
        for j in range(len(status)+1):
            graph[(i, j)] = []
            parent[(i, j)] = (i, j)
    for i in range(len(status)):
        for j in range(len(status)):
            if status[i][j] == 0:
                if (j+1, i) not in graph[(i+1, j)]: graph[(i+1, j)].append((i, j+1))
                if (i+1, j) not in graph[(j+1, i)]: graph[(i, j+1)].append((i+1, j))
            elif status[i][j] == 1:
                if (i+1, j+1) not in graph[(i, j)]: graph[(i, j)].append((i+1, j+1))
                if (i, j) not in graph[(i+1, j+1)]: graph[(i+1, j+1)].append((i, j))

    for u, value in graph.items():
        for v in value:
            if find_parent(parent, u) != find_parent(parent, v):
                union_parent(parent, u, v)
    
    noc = permutations([i for i in range(len(status)+1)], len(status)+1)
    cnt = 0

    for case in noc:
        case = [(i, x) for x, i in enumerate(case)]
        noc2 = combinations(case, 2)
        judge = True
        for case2 in noc2:
            if find_parent(parent, case2[0]) == find_parent(parent, case2[1]):
                judge = False
                break
        if judge:
            cnt += 1
    return cnt


if __name__ == "__main__":
    assert solution([[0, 1], [1, 0]]) == 2