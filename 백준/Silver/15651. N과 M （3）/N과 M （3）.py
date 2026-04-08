n, m = map(int, input().split())

# 중복순열
def backtracking(arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(1, n + 1):
    backtracking(arr + [i])

backtracking([])