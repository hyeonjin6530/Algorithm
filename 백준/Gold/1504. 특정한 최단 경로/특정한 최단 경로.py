import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

p1, p2 = map(int, input().split())

def dijkstra(start):
  distance = [INF] * (n+1)
  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))
  
  return distance

w1 = dijkstra(1)
w2 = dijkstra(p1)
w3 = dijkstra(p2)

path1 = w1[p1] + w2[p2] + w3[n]
path2 = w1[p2] + w3[p1] + w2[n]

result = min(path1, path2)

if result >= INF:
  print(-1)
else: print(result)


