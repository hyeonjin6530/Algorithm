def solution(n, wires):
    answer = n
    
    # 인접 리스트로 변환
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # wires를 순회하며 하나씩 지워보기
    for a, b in wires:
        visited = [False] * (n+1)
        
        def dfs(node):
            visited[node] = True
            count = 1
            
            for i in graph[node]:
                if (node == a and i == b) or (node == b and i == a):
                    continue
                
                if not visited[i]:
                    count += dfs(i)
            
            return count
        
        cnt = dfs(1)
        
        diff = abs(cnt - (n-cnt))
        
        answer = min(answer, diff)      
    
    return answer