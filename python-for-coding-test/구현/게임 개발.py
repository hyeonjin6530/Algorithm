# 맵 사이즈
n, m = map(int, input().split())

# 캐릭터 위치, 방향
x, y, d = map(int, input().split())

# 방문한 곳 표시를 위한 맵
visit_land = [[0] * m for _ in range(n)]
visit_land[x][y] = 1

# 맵 (육지 = 0, 바다 = 1)
land = []

for i in range(n):
  land.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 이동 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

# 시뮬레이션 시작
turn_time = 0
count = 1

while True:
  # 1. 왼쪽으로 회전
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]
  # 2-1. 가보지 않은 칸이 존재한다면 한 칸 전진
  if visit_land[nx][ny] == 0 and land[nx][ny] == 0:
    visit_land[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 2-2. 없다면 1단계로 돌아감
  else: 
    turn_time += 1
  # 3-1. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 한 칸 뒤로 가고 1단계로 돌아간다.
  if turn_time == 4:
      nx = x - dx[d]
      ny = y - dy[d]
      # 만약 뒤쪽 방향이 바다인 칸이라면 움직임을 멈춘다.
      if land[nx][ny] == 0:
        x = nx
        y = ny
      else:
        break
      turn_time = 0

print(count)