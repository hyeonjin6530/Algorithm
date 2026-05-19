def solution(numbers, target):
    answer = 0
    
    def dfs(idx, result):
        nonlocal answer
        
        # 끝까지 다 계산했을 때
        if idx == len(numbers):
            if result == target:
                answer += 1
            return
        
        # 다음 숫자를 더할 때
        dfs(idx + 1, result + numbers[idx])
        
        # 다음 숫자를 뺄 때
        dfs(idx + 1, result - numbers[idx])
        
    dfs(0, 0)
    
    return answer