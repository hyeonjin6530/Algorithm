'''
  문제 유형: bfs

  문제 풀이 방법: 
    가장 빠른 시간 => bfs

    이동하는 방법
      1. x-1 -> 비용 1
      2. x+1 -> 비용 1
      3. 2*x -> 비용 0
    
    비용이 다르기 때문에 deque의 함수를 다르게 처리
      비용 0 -> appendleft()
      비용 1 -> append()
'''
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

dist = [-1] * 100001

q = deque()
q.append(n)
dist[n] = 0

while q:
  x = q.popleft()

  # 정답이라면 출력 후 종료
  if x == k:
    print(dist[x])
    break

  # 1. 순간이동(비용 0)
  nx = x * 2
  if 0 <= nx < 100001 and dist[nx] == -1:
    dist[nx] = dist[x]
    q.appendleft(nx) # 비용이 0이니까 앞에 넣기
  
  # 2. -1 이동(비용 1)
  nx = x - 1
  if 0 <= nx < 100001 and dist[nx] == -1:
    dist[nx] = dist[x] + 1
    q.append(nx)

  # 3. 1 이동(비용 1)
  nx = x + 1
  if 0 <= nx < 100001 and dist[nx] == -1:
    dist[nx] = dist[x] + 1
    q.append(nx)