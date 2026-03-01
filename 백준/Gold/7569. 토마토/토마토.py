'''
  문제 유형: bfs

  문제 풀이 방법: 
    처음에 익은 토마토를 전부 큐에 넣고 시작한다.
    왜냐하면 여러 곳에서 동시에 퍼져야하기 때문!
'''
import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

# 3차원 그래프 사용
box = [[[0] * m for _ in range(n)] for _ in range(h)]

# 그래프에 토마토 담기
for i in range(h):
  for j in range(n):
    box[i][j] = list(map(int, input().split()))

# 이동할 방향(6방향)
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 1. 처음에 익은 토마토를 전부 큐에 넣고 시작
q = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if box[i][j][k] == 1:
        q.append((i, j, k))

# 2. bfs 시작
while q:
  z, x, y = q.popleft()

  # 현재 위치에서 여섯 방향으로의 위치 확인
  for i in range(6):
    nz = z + dz[i]
    nx = x + dx[i]
    ny = y + dy[i]

    # 유효한 범위일 경우
    if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
      # 아직 안익은 토마토라면
      if box[nz][nx][ny] == 0:
        box[nz][nx][ny] = box[z][x][y] + 1
        q.append((nz, nx, ny))

# 3. 위에서 계산이 다 끝났기 때문에 정답 출력하기
result = 0

# box 순회하기
for i in range(h):
  for j in range(n):
    for k in range(m):
      # 만약 익지 않은 토마토가 있다면 -1 출력 후 종료
      if box[i][j][k] == 0:
        print(-1)
        exit(0)
      # 아니라면 box에 있는 값 중 최대값을 갱신
      result = max(result, box[i][j][k])

# 처음 익은 토마토가 1로 시작했기 때문에 -1해주기
print(result - 1)