n, m = map(int, input().split())

visited = [False] * (n+1)

def backtracking(arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(1, n+1):
    if visited[i] == False:
      visited[i] = True  # 방문!
      backtracking(arr + [i])
      # 제거해줘야지 나중에 또 방문할 수 있기 때문에 [1, 2] 방문하고 2를 제거해줘야지 [1, 3] 이렇게 방문이 가능하다.
      visited[i] = False

backtracking([])