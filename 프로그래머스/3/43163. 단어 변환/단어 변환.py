from collections import deque

def solution(begin, target, words):

    visited = {begin : 0}
    
    for i in words:
        visited[i] = 0
    
    q = deque()
    q.append(begin)
    
    while q:
        now = q.popleft()
        
        closeWord = []
        
        for word in words:
            count = 0
            
            for i in range(len(word)):
                if now[i] != word[i]:
                    count += 1
            
            if count == 1:
                closeWord.append(word)
        
        for i in closeWord:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)
    
    print(visited)
    if target not in visited:
        return 0
    else:
        return visited[target]