'''
  문제 유형: 위상정렬
'''

from collections import deque
import copy  # 리스트 복제

n = int(input())

# 진입차수를 처음엔 다 0으로 초기화
indegree = [0] * (n+1)

# 연결 리스트
graph = [[] for _ in range(n+1)]

# 강의 시간
time = [0] * (n+1)

for i in range(1, n+1):
  arr = list(map(int, input().split()))
  time[i] = arr[0]  # 강의 시간 저장

  for j in arr[1:]:
    if j == -1:
      continue  
    graph[j].append(i)  # j -> i로 이동
    indegree[i] += 1  # i의 진입차수 +1 해주기

def topology_sort():
  q = deque()
  # 최종 강의 시간을 저장할 리스트
  result = copy.deepcopy(time)

  # 진입차수가 0인 것들 먼저 큐에 넣기
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()

    for i in graph[now]:
      # 해당 노드와 연결된 노드의 진입차수 -1해주기
      indegree[i] -= 1

      # 연결된 노드의 최종 강의 시간 수정해주기
      result[i] = max(result[i], time[i] + result[now])

      # 진입차수가 0이 되면 큐에 넣어주기
      if indegree[i] == 0:
        q.append(i)
  
  for t in result[1:]:
    print(t)

topology_sort()