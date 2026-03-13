'''
  문제 유형: bfs

  문제 풀이 방법: 
    bfs를 사용해서 배추 모임의 개수를 세주면 된다!
    bfs를 돌릴 때 마다 count += 1을 해주면 됨
    최소거리가 필요 없기 때문에 중복 방문을 막기 위해 방문한 곳은 0으로 값을 바꿔준다!
    
'''
from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
  m, n, k = map(int, input().split())

  # 배추밭을 0으로 초기화
  graph = [[0] * m for _ in range(n)]

  # 배추의 위치 입력 받기
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  # bfs 함수
  def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))

    graph[start_x][start_y] = 0  # 중복을 방지하기 위해 방문처리

    while q:
      x, y = q.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          continue

        if graph[nx][ny] == 1:
          graph[nx][ny] = 0 # 중복을 방지하기 위해 방문처리
          q.append((nx, ny))
  
  count = 0

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        bfs(i, j)
        count += 1
  
  print(count)
  

