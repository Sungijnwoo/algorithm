N, M = map(int, input().split())

def find_parent(parent, x):
  if x != parent[x]:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

parent = [i for i in range(N+1)]
costs = []
for _ in range(M):
  a, b, cost = map(int, input().split())
  costs.append((cost, a, b))

costs.sort()

result = 0
last = 0
for idx, (cost, a, b) in enumerate(costs):
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    last = cost
print(result-last)
