n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

# 중복순열
def backtracking(arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(n):
    backtracking(arr + [nums[i]])


backtracking([])