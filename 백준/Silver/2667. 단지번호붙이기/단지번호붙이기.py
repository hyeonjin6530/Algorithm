'''
  문제 유형: bfs

  문제 풀이 방법: 
    1. bfs 로직 그대로 사용하기
    2. 그래프를 돌면서 1이 나오면(= 집이 있으면) bfs 돌리고 빠져나오면 count + 1 해주기
    3. bfs안에서 새로운 집을 만날 때 마다 house + 1 해주기

    
'''
from collections import deque

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
  q = deque()
  q.append((start_x, start_y))

  house = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
        house += 1
  return house

# 단지 수
count = 0

# 단지에 속하는 집 수
house_arr = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      h = bfs(i, j)
      if h == 0:
        house_arr.append(1)
      else:
        house_arr.append(h)
      count += 1

house_arr.sort()

print(count)
for i in range(count):
  print(house_arr[i])