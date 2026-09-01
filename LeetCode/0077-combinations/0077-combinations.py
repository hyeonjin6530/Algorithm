class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(idx, arr):
            if len(arr) == k:
                answer.append(arr)
                return
            
            for i in range(idx, n+1):
                dfs(i+1, arr+[i])
        
        dfs(1, [])

        return answer