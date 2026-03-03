'''
  문제 유형: 재귀, 분할 정복

  문제 풀이 방법: 
    n이 3보다 클 경우, 공백으로 채워진 (n/3)*(n/3) 정사각형을 n/3의 패턴으로 둘러싼다.
'''

num = int(input())

def star(n):
  # 1. 가장 작은 단위
  if n == 1:
    return ['*']
  
  # 2. n/3 패턴 먼저 구하기
  small = star(n // 3)

  result = []

  # 3-1. 위쪽 블록
  for line in small:
    result.append(line + line + line)
  
  # 3-2. 가운데 블록
  for line in small:
    result.append(line + ' ' * (n // 3) + line)

  # 3-3. 아래쪽 블록
  for line in small:
      result.append(line + line + line)
  
  return result

pattern = star(num)

for line in pattern:
  print(line)