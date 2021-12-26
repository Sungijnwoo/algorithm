n = int(input())

x, y, z = [], [], []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
    

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

edges.sort()

parent = [i for i in range(n+1)]
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

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        total_cost += cost
        union_parent(a, b)

print(total_cost)
        