'''
  문제 유형: bfs

  문제 풀이 방법: 

    
'''
from collections import deque

n, m = map(int, input().split())

# 그래프 저장
graph = [list(map(int, input().strip())) for _ in range(n)]

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  q = deque()
  q.append((a, b))

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))

  return int(graph[n-1][m-1])

print(bfs(0, 0))

