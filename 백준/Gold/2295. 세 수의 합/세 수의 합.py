'''
  문제 유형: 이진탐색

  문제 풀이 방법: 
    a + b + c = d를 a + b = d - c로 바꾸어서 풀기
    a + b를 다 저장하고 가장 큰 d - c부터 비교해서 정답 찾기
'''
import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort()

# a + b 저장
add = []
for i in range(n):
  for j in range(i, n):
    add.append(nums[i] + nums[j])
add.sort()

# 이분탐색 함수
def binary_search(target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if add[mid] == target:
      return True
    elif add[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False

# d - c 계산
for i in range(n-1, -1, -1):
  for j in range(0, n):
    if binary_search(nums[i] - nums[j], 0, len(add)-1):
      print(nums[i])
      exit(0)