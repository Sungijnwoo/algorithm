n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


parent = [i for i in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i, j)

for i in parent:
    find_parent(parent, i)

print(parent)