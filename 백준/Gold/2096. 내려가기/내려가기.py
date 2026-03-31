'''
  문제 유형: dp

  문제 풀이 방법: 매번 계산하기엔 경우의 수가 많기 때문에 이전 계산 결과를 재사용하는 dp를 써야한다.
               -> 현재 칸의 입장에서 이 값은 어디서부터 왔는가를 생각하는 것이 더 편하다. 
    
'''

n = int(input())

# 첫 줄은 이전 줄이 없기 때문에 그냥 첫줄이 시작값이 된다.
a, b, c = map(int, input().split())
dpMax = [a, b, c]
dpMin = [a, b, c]

for _ in range(n-1):
  # 다음 줄을 입력값으로 받기
  x, y, z = list(map(int, input().split()))

  # 왼쪽 칸
  newMax0 = x + max(dpMax[0], dpMax[1]) # 이전 값이 어떤 것일지 선택하는 작업
  newMin0 = x + min(dpMin[0], dpMin[1])

  # 가운데 칸
  newMax1 = y + max(dpMax[0], dpMax[1], dpMax[2])
  newMin1 = y + min(dpMin[0], dpMin[1], dpMin[2])

  # 오른쪽 칸
  newMax2 = z + max(dpMax[1], dpMax[2])
  newMin2 = z + min(dpMin[1], dpMin[2])

  dpMax = [newMax0, newMax1, newMax2]
  dpMin = [newMin0, newMin1, newMin2]

print(max(dpMax), min(dpMin))
