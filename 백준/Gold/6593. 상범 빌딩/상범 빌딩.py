'''
  문제 유형: bfs

  문제 풀이 방법: 
    
'''
from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
  l, r, c = map(int, input().split())

  # l, r, c가 0일 경우 종료
  if l == 0 and r == 0 and c == 0:
    break

  # 3차원 그래프 [층][행][열]
  graph = [[[0]* c for _ in range(r)] for _ in range(l)]

  for i in range(l):
    for j in range(r):
      graph[i][j] = list(input().strip())
    input() # 빈 줄 버리기

  # 시작점 좌표
  sx, sy, sz = 0, 0, 0

  # 출구 좌표
  ex, ey, sz = 0, 0, 0

  for i in range(l):
    for j in range(r):
      for k in range(c):
        if graph[i][j][k] == 'S':
          sx = j
          sy = k
          sz = i
        elif graph[i][j][k] == 'E':
          ex = j
          ey = k
          ez = i
        elif graph[i][j][k] == '#':
          continue

        graph[i][j][k] = 0

  q = deque()
  q.append((sx, sy, sz))

  while q:
    x, y, z = q.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if nx < 0 or nx >= r or ny < 0 or ny >= c or nz <0 or nz >= l:
        continue

      if graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y] + 1
        q.append((nx, ny, nz))
  
  if graph[ez][ex][ey] == 0:
    print("Trapped!")
  else:
    print('Escaped in', graph[ez][ex][ey], 'minute(s).')