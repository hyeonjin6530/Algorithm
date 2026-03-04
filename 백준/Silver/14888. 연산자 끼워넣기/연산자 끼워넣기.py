'''
  문제 유형: dfs, 백트래킹

  문제 풀이 방법: 
    
'''
import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

plus, minus, multiply, divide = map(int, input().split())

max_value = -1e9
min_value = 1e9

# 지금 몇 번째 숫자까지 계산했는지, 현재 계산 값, 남은 연산자 개수들
def dfs(idx, current, plus, minus, multiply, divide):
  global max_value, min_value

  # 종료 조건: 모든 숫자를 다 사용했으면
  if idx == n:
    max_value = max(max_value, current)
    min_value = min(min_value, current)
    return
  
  if plus > 0:
    dfs(idx+1, current + nums[idx], plus-1, minus, multiply, divide)

  if minus > 0:
    dfs(idx+1, current - nums[idx], plus, minus-1, multiply, divide)
  
  if multiply > 0:
    dfs(idx+1, current * nums[idx], plus, minus, multiply-1, divide)
  
  if divide > 0:
    if current < 0:
      next = -(-current // nums[idx])
    else:
      next = current // nums[idx]
    dfs(idx+1, next, plus, minus, multiply, divide-1)

dfs(1, nums[0], plus, minus, multiply, divide)

print(int(max_value))
print(int(min_value))