class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        n = len(nums)

        visited = [False] * n

        def dfs(idx, arr):
            if len(arr) == n:
                answer.append(arr)
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dfs(idx, arr + [nums[i]])
                    visited[i] = False
        
        dfs(0, [])

        return answer