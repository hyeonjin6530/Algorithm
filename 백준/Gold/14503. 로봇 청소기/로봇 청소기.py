'''
  문제 유형: 구현

  문제 풀이 방법: 
    빠르게 문제에 적힌 규칙을 코드로 풀어내야한다.
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 로봇청소기의 처음 위치와 바라보는 방향
r, c, d = map(int, input().split())

# 방의 상태 저장
room = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부를 저장하기 위한 그래프
visited = [[0] * m for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소하는 칸의 개수
count = 0

while True:
  # 1. 현재 칸이 청소되지 않은 경우, 현재 칸 청소
  if visited[r][c] == 0:
    visited[r][c] = 1
    count += 1
  
  cleaned = False
  
  # 2. 4방향 탐색
  for _ in range(4):
    # 반시계 회전
    d = (d - 1) % 4

    nx = r + dx[d]
    ny = c + dy[d]

    # 앞쪽이 청소 안 된 빈 칸이면 청소
    if room[nx][ny] == 0 and visited[nx][ny] == 0:
      r, c = nx, ny
      cleaned = True
      break
   
  # 3. 4방향 모두 청소 불가
  if not cleaned:
    # 뒤쪽 방향
    back = (d + 2) % 4
    nr = r + dx[back]
    nc = c + dy[back]

    # 뒤가 벽이면 종료
    if room[nr][nc] == 1:
      break
    else:
      r, c = nr, nc

print(count)