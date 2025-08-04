import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0

for i in range(n):
  find = nums[i]
  start = 0
  end = n-1
  while start < end:  # 투 포인터 알고리즘
    if nums[start] + nums[end] == find:
      if start != i and end != i:
        count += 1
        break
      elif start == i:
        start += 1
      elif end == i:
        end -= 1
    elif nums[start] + nums[end] < find:
      start += 1
    else:
      end -= 1

print(count)