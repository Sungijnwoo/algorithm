n = int(input())

positions = [list(map(int, input().split())) for _ in range(n)]
graph = []
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        cost = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
        graph.append([cost, i, j])

graph.sort()
parent = [i for i in range(n)]
total_cost = 0

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for cost, a, b in graph:
    if find_parent(a) != find_parent(b):
        total_cost += cost
        union_parent(a, b)

print(total_cost)
        