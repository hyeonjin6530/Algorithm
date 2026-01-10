answer = 0

def dfs(idx, current, numbers, target):
    global answer

    if idx == len(numbers):
        if current == target:
            answer += 1
        return answer

    dfs(idx+1, current + numbers[idx],numbers, target)
    dfs(idx+1, current - numbers[idx], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    
    return answer