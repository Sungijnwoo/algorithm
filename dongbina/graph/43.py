n, m = map(int, input().split())

graph = []

for _ in range(m):
    x, y, cost = map(int, input().split())
    graph.append([cost, x, y])

graph.sort()

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

parent = [i for i in range(n)]
total_cost = 0
for cost, x, y in graph:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        total_cost += cost

print(total_cost)