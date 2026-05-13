from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)

        visited = [False] * n

        def bfs(x):
            q = deque()
            q.append(x)
            visited[x] = True

            while q:
                now = q.popleft()

                for i in rooms[now]:
                    if not visited[i]:
                        visited[i] = True
                        q.append(i)
        
        bfs(0)

        for i in visited:
            if not i:
                return False
            
        return True
        