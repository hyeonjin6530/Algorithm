import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

# 도시의 개수, 통로의 개수, 메시지를 보내고자하는 도시
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
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
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)

number = 0
time = 0

for i in distance:
  if i != 0 and i != INF:
    number += 1

    if i > time:
      time = i

print(number, time)