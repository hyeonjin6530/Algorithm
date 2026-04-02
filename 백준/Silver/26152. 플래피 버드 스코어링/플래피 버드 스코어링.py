'''
  문제 유형: 이분탐색

  문제 풀이 방법: 플래피 버드가 틈새보다 큰 지, 작은 지만 계산하면 되는 문제이다!
               => 이렇게 하면 시간 초과 문제 발생

               1. i번째까지 가려면 크기가 어떻게 되어야할지를 미리 계산 해둔 prefix minimum 만들기
               2. prefix minimum은 점점 크기가 같거나 작아지기만 함. 그렇기 때문에 이분 탐색을 통해 경계값을 찾을 수 있음!
'''
import sys

input = sys.stdin.readline

# 장애물의 개수
n = int(input())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

# 틈새 계산
dist = []
for i in range(n):
  dist.append(top[i] - bottom[i])

# 틈새의 최솟값을 저장한 배열 생성
min_prefix = [0] * n
min_prefix[0] = dist[0]
for i in range(1, n):
  min_prefix[i] = min(min_prefix[i-1], dist[i])

# 플래피 버드의 개수
q = int(input())

size = list(map(int, input().split()))

for s in size:
  start = 0
  end = n - 1
  result = -1
  
  while start <= end:
    mid = (start + end) // 2

    if min_prefix[mid] >= s:
      result = mid  # mid까지는 통과 가능하다
      start = mid + 1
    else:
      end = mid - 1
  
  print(result + 1)