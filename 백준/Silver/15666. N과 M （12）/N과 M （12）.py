n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

# 조합
def backtracking(idx, arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  # 같은 depth에서 같은 값을 선택할 수 없도록
  prev = None
  for i in range(idx, n):
    if nums[i] != prev:
      prev = nums[i]
      backtracking(i, arr + [nums[i]])

backtracking(0, [])