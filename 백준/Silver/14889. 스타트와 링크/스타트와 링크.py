'''
  문제 유형: dfs, 백트래킹

  문제 풀이 방법: 
    'N명 중 N/2명을 선택한다' -> 조합

    1. n명 중 n/2명 선택
    2. 스타트팀 점수 계산
    3. 링크팀 점수 계산
    4. 차이 최소값 갱신
    
'''
import sys
input = sys.stdin.readline

n = int(input())

# 능력치를 저장할 그래프
s = [list(map(int, input().split())) for _ in range(n)]

# 사람이 팀에 들어갔는지 표시
visited = [False] * n

# start = 다음에 볼 사람 번호
# count = 지금 팀에 몇 명 들어왔는지
def dfs(start, count):
  # 팀 완성 조건
  if count == n//2:
    start_score = 0
    link_score = 0

    for i in range(n):
      for j in range(i+1, n):
        if visited[i] and visited[j]:
          start_score += s[i][j] + s[j][i]
        elif not visited[i] and not visited[j]:
          link_score += s[i][j] + s[j][i]

    return abs(start_score - link_score)
  
  min_diff = 1e9
  
  for i in range(start, n):
    # 팀에 넣기
    visited[i] = True
    min_diff = min(min_diff, dfs(i+1, count+1))
    # 다시 팀을 짜야하니까 꺼내주기
    visited[i] = False
  
  return min_diff

print(dfs(0, 0))
