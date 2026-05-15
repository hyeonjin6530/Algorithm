from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start = []
    
    lever = []
    
    end = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start.append(i)
                start.append(j)
            elif maps[i][j] == 'L':
                lever.append(i)
                lever.append(j)
            elif maps[i][j] == 'E':
                end.append(i)
                end.append(j)
                
    # 시작 ~ 레버
    path1 = [[0] * m for _ in range(n)]
    
    # 레버 ~ 출구
    path2 = [[0] * m for _ in range(n)]
    
    def bfs(x, y, graph):
        q = deque()
        q.append((x, y))
        graph[x][y] += 1
        
        while q:
            r, c = q.popleft()
            
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                if maps[nr][nc] != 'X' and graph[nr][nc] == 0:
                    graph[nr][nc] = graph[r][c] + 1
                    q.append((nr, nc))
    
    bfs(start[0], start[1], path1)
    first = path1[lever[0]][lever[1]]
    
    bfs(lever[0], lever[1], path2)
    second = path2[end[0]][end[1]]
    
    if first == 0 or second == 0:
        return -1
    else:
        return first + second - 2