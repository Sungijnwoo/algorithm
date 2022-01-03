n, m = map(int, input().split())

roads = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    roads.append((cost, a, b))

parent = [i for i in range(n+1)]
roads.sort()

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

total_cost = 0
max_cost = 0
for cost, a, b in roads:
    if find_parent(a) != find_parent(b):
        total_cost += cost
        max_cost = max(cost, max_cost)
        union_parent(a, b)

print(total_cost - max_cost)
