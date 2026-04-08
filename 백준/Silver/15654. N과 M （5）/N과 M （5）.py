n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

visited = [False] * n

# 순열
def backtracking(arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(n):
    if visited[i] == False:
      visited[i] = True
      backtracking(arr + [nums[i]])
      visited[i] = False

backtracking([])