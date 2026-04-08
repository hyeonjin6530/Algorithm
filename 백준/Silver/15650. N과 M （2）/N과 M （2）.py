n, m = map(int, input().split())

# 조합
def backtracking(idx, arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(idx, n + 1):
    backtracking(i+1, arr + [i])

backtracking(1, [])