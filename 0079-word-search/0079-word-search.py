class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        def dfs(y, x, idx):
            # 현재 위치가 범위를 벗어나면 실패
            if y < 0 or y >= n or x < 0 or x >= m:
                return False

            # 현재 칸이 찾는 문자와 다르면 실패
            if board[y][x] != word[idx]:
                return False
            
            # 마지막 문자까지 찾았으면 성공
            if idx == len(word) - 1:
                return True
            
            # 방문 처리
            temp = board[y][x]
            board[y][x] = "#"

            # 상하좌우 탐색
            found = (
                dfs(y + 1, x, idx + 1) or
                dfs(y - 1, x, idx + 1) or
                dfs(y, x - 1, idx + 1) or
                dfs(y, x + 1, idx + 1)
            )

            # 원상복구
            board[y][x] = temp

            return found
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False

        