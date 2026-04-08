n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

visited = [False] * n

# 순열
def backtracking(arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return

  # 같은 depth에서 같은 값을 선택할 수 없도록
  prev = None
  for i in range(n):
    if visited[i] == False and nums[i] != prev:
      visited[i] = True
      prev = nums[i]
      backtracking(arr + [nums[i]])
      visited[i] = False

backtracking([])