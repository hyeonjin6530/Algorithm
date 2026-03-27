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

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
  num, s1, s2 = map(int, input().split())

  if num:
    if find_parent(parent, s1) == find_parent(parent, s2):
      print("YES")
    else:
      print("NO")
  else:
    union_parent(parent, s1, s2)