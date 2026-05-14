from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "2"  # 방문처리

            while q:
                pr, pc = q.popleft()

                for i in range(4):
                    nr = pr + dx[i]
                    nc = pc + dy[i]

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if grid[nr][nc] == "1":
                         grid[nr][nc] = "2"
                         q.append((nr, nc))

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count


