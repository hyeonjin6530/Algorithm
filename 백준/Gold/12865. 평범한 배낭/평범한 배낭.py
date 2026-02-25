'''
  문제 유형: 다이나믹프로그래밍

  문제 풀이 방법: 
    각 물건을 한 번만 사용할 수 있으며,
    무게 제한 k 이하에서 최대 가치를 구하는 전형적인 0/1 배낭 문제
'''

# 물품의 수, 버틸 수 있는 무게
n, k = map(int, input().split())

# 물건의 무게, 가치를 저장할 리스트
item = []

for _ in range(n):
  weight, cost = map(int, input().split())
  item.append((weight, cost))

# 현재 가방 무게가 w일 때 얻을 수 있는 최대 가치
dp = [0] * (k+1)

for weight, cost in item:
  # 뒤에서 부터 순회(같은 물건 중복 사용 방지)
  for w in range(k, weight-1, -1):
    # 각 물건에 대해 넣지 않는 경우, 넣는 경우 중 큰 값을 선택한다.
    dp[w] = max(dp[w], dp[w-weight] + cost)

print(dp[k])