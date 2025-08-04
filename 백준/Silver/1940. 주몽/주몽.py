import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()  # 정렬을 해야함

start_idx = 0
end_idx = n-1

count = 0

while start_idx < end_idx:
  if nums[start_idx] + nums[end_idx] < m:
    start_idx += 1
  elif nums[start_idx] + nums[end_idx] > m:
    end_idx -= 1
  elif nums[start_idx] + nums[end_idx] == m:
    count += 1
    start_idx += 1
    end_idx -= 1

print(count)