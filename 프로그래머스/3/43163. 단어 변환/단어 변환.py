from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = []
    
    q = deque()
    q.append((begin, 0))
    visited.append(begin)
    
    while q:
        w, dist = q.popleft()
        
        # 한 개의 알파벳만 다른 것을 그래프에 추가
        graph = []
        for word in words:
            diff = sum(x != y for x, y in zip(w, word))
            if diff == 1:
                graph.append(word)
                
        for i in graph:
            if i not in visited:
                q.append((i, dist+1))
                visited.append(i)
            
                if i == target:
                    answer = dist + 1
    
    return answer