import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

node, edge, v = map(int, input().split())

graph = [[] for _ in range(node+1)]

for i in range(edge):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

def DFS(n):
  visited[n] = True
  print(n, end=" ")
  for i in sorted(graph[n]):
    if not visited[i]:
      DFS(i)

visited = [False] * (node+1)
DFS(v)

def BFS(n):
  q = deque()
  q.append(n)
  visited[n] = True
  while q:
    new = q.popleft()
    print(new, end=" ")
    for i in sorted(graph[new]):
      if not visited[i]:
        visited[i] = True
        q.append(i)
        

print()
visited = [False] * (node+1)
BFS(v)