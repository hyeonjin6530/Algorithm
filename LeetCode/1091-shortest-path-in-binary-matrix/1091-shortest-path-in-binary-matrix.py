from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # 애초에 갈 수 없는 길이라면 바로 종료 시켜버리기
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # 갈 수 없는 길을 1 -> -1로 변경
                    grid[i][j] = -1

        # 8방향으로 이동
        dx = [-1, 1, -1, 1, -1, 1, 0, 0]
        dy = [0, 0, -1, 1, 1, -1, -1, 1]
        
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            grid[x][y] = 1
            
            while q:
                r, c = q.popleft()

                for i in range(8):
                    nr = r + dx[i]
                    nc = c + dy[i]

                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue
                    
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))
            
        
        bfs(0, 0)

        if grid[n-1][n-1] == 0:
            return -1
        else:
            return grid[n-1][n-1]
