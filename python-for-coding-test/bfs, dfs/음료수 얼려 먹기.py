# dfs 사용

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  # 범위를 벗어나는 경우 바로 종료
  if x <= -1  or n <= x or y <= -1 or m <= y:
    return False
  
  # 아직 방문하지 않은 노드라면
  if graph[x][y] == 0:
    # 1. 해당 노드 방문 처리
    graph[x][y] = 1
    
    # 2. 상하좌우 노드도 재귀적으로 호출
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

    return True
  
  return False

# 결과
result = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)