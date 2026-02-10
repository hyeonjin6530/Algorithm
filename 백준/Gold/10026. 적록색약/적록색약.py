from collections import deque

n = int(input())

# 그림 저장
painting = []
for _ in range(n):
  painting.append(input())

# 방문 여부 체크 (적록색약이 아닌 사람, 적록색약인 사람)
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

# 구역 개수 (적록색약이 아닌 사람, 적록색약인 사람)
count1 = 0
count2 = 0

# 이동할 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 적록색약이 아닌 사람 bfs
def bfs1(sr, sc):
  q = deque()
  q.append((sr, sc))
  visited1[sr][sc] = True

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]

      # 범위를 넘어가는 경우 continue
      if nr < 0 or nr >= n or nc < 0 or nc >= n:
        continue
      # 이미 방문한 경우 continue
      if visited1[nr][nc]:
        continue
      # 색깔이 다를 경우 continue
      if painting[r][c] != painting[nr][nc]:
        continue

      visited1[nr][nc] = True
      q.append((nr, nc))

# 적록색약인 사람 bfs
def bfs2(sr, sc):
  q = deque()
  q.append((sr, sc))
  visited2[sr][sc] = True

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]

      # 범위를 넘어가는 경우 continue
      if nr < 0 or nr >= n or nc < 0 or nc >= n:
        continue
      # 이미 방문한 경우 continue
      if visited2[nr][nc]:
        continue
      
      # 현재 색상이 R 또는 G일 때
      if painting[r][c] in ('R', 'G'):
        # 다음 색상이 B라면 continue
        if painting[nr][nc] == 'B':
          continue
      # 현재 색상이 B일 때
      else:
        # 다음 색상이 R 또는 G라면 continue
        if painting[nr][nc] in ('R', 'G'):
          continue

      visited2[nr][nc] = True
      q.append((nr, nc))

'''
bfs는 한 번 연결된 하나의 구역만 탐색하기 때문에, 
시작점부터 한 번만 돌리는 게 아니라 모든 칸을 돌면서 방문하지 않은 칸에서 bfs를 돌려야한다.
'''
for i in range(n):
  for j in range(n):
    if not visited1[i][j]:
      bfs1(i, j)
      count1 += 1
    
    if not visited2[i][j]:
      bfs2(i, j)
      count2 += 1

print(count1, count2)