n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

# 조합
def backtracking(idx, arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(idx, n):
    backtracking(i, arr + [nums[i]])


backtracking(0, [])