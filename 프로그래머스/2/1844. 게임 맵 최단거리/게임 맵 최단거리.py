from collections import deque

# 상하좌우 이동 방향 정하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m, maps):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 넘어갈 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 벽일 경우 무시
            if maps[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문할 경우에만 최단 거리 기록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
        
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    return bfs(0, 0, n, m , maps)