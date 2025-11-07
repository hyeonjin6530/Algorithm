import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

node, edge = map(int, input().split())

# 인접리스트
graph = [[] for i in range(node+1)]

# 방문 여부를 체크할 리스트
visited = [False] * (node+1)

count = 0

# dfs 함수 선언
def DFS(v):
  visited[v] = True  # 방문했다고 표시
  for i in graph[v]:
    if not visited[i]:
      DFS(i)

# 입력 받은 노드들 리스트에 저장(방향x -> 양쪽에 다 넣어야함)
for i in range(edge):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

# 실행
for i in range(1, node+1):
  if not visited[i]:
    count += 1
    DFS(i)

print(count)