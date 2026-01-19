n = int(input())

plan = list(input().split())

x = 1  # 여행자의 x좌표
y = 1  # 여행자의 y좌표

for i in plan:
  if i == 'L':
    if 1 <= y - 1 <= n:
      y -= 1
    else:
      continue
  elif i == 'R':
    if 1 <= y + 1 <= n:
      y += 1
    else:
      continue
  elif i == 'U':
    if 1 <= x - 1 <= n:
      x -= 1
    else:
      continue
  elif i == 'D':
    if 1 <= x + 1 <= n:
      x += 1
    else:
      continue

print(x, y)