def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort()
    
    for i in range(n):
        answer = max(answer, min(n-i, citations[i]))
        
    return answer