def dfs(idx, n, computers, visited):
    visited[idx] = True

    for i in range(n):
        if computers[idx][i] == 1 and not visited[i]:
            dfs(i, n, computers, visited)
    

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, n, computers, visited)
    
    return answer