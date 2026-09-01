class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        n = len(nums)

        visited = [False] * n

        def dfs(arr):
            if len(arr) == n:
                answer.append(arr)
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dfs(arr + [nums[i]])
                    visited[i] = False
        
        dfs([])

        return answer