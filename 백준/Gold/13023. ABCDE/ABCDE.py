import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n)]

visited = [False] * n

arrive = False

def DFS(now, depth):
  global arrive
  if depth == 5:
    arrive = True
    return
  visited[now] = True
  for i in arr[now]:
    if not visited[i]:
      DFS(i, depth + 1)
  visited[now] = False

for i in range(m):
  f1, f2 = map(int, input().split())
  arr[f1].append(f2)
  arr[f2].append(f1)

for i in range(n):
  DFS(i, 1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)

