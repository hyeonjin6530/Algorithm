def solution(numbers, target):
    answer = 0
    
    def dfs(idx, current):
        nonlocal answer

        if idx == len(numbers):
            if current == target:
                answer += 1
            return answer

        dfs(idx+1, current + numbers[idx])
        dfs(idx+1, current - numbers[idx])
    
    dfs(0, 0)
    
    return answer