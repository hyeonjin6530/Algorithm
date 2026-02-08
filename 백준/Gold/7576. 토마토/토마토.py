from collections import deque

m, n = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

# 이동할 방향
dr = [-1, 1, 0, 0] # 상, 하
dc = [0, 0, -1, 1] # 좌, 우

def bfs():
  queue = deque()

  for row in range(n):
    for col in range(m):
      if graph[row][col] == 1:
        queue.append((row, col))

  while queue:
    r, c = queue.popleft()

    # 기준 토마토로부터 4방향 확인
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]

      # 만약 상자를 넘어가는 경우 무시
      if nr < 0 or nr >= n or nc < 0 or nc >= m:
        continue

      # 만약 토마토가 없다면 무시
      if graph[nr][nc] == -1:
        continue

      # 만약 아직 멀쩡한 토마토라면 익힌 토마토로 바꾸기
      if graph[nr][nc] == 0:
        # 날짜를 graph에 기록
        graph[nr][nc] =  graph[r][c] + 1
        queue.append((nr, nc))

# bfs 함수 호출
bfs()

# 결과
result = 0

for row in range(n):
  for col in range(m):
    # 토마토가 모두 익지 못했다면 -1 출력
    if graph[row][col] == 0:
      print(-1)
      exit()
    result = max(result, graph[row][col])

# 처음 익은 토마토가 1이었으므로 -1 해주기
print(result - 1)