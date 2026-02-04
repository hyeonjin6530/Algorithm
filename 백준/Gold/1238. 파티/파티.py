'''
출발점이 여러 개일 때 한 개로 줄일 수 있을까?
-> 리버스 그래프
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
rgraph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  rgraph[b].append((a, c))

def dijkstra(start, g):
  distance = [INF] * (n+1)

  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in g[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  
  return distance

# x -> i
from_x = dijkstra(x, graph)

# i -> x
to_x = dijkstra(x, rgraph)

result = 0

for i in range(1, n+1):
  result = max(result, from_x[i] + to_x[i])

print(result)