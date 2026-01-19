c = input()

# 아스키코드 변환 사용 a -> 97
x, y = int(ord(c[0])) - 96 , int(c[1])

count = 0

# 나이트가 움직일 수 있는 방법
steps = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]

for step in steps:
  if 1 <= step[0] + x <= 8 and 1 <= step[1] + y <= 8:
    count += 1
  else:
    continue

print(count)