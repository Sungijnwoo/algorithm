N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(M)]

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

parent = [0] * (N+1)
for i in range(N+1):
  parent[i] = i


for mode, a, b in array:
  if mode == 0:
    union_parent(parent, a, b)
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")