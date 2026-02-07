import heapq

def solution(scoville, K):
    answer = 0
    
    q = []
    
    for i in scoville:
        heapq.heappush(q, i)
    
    while q[0] < K:
        if len(q) == 1:
            answer = -1
            break
            
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        
        new = first + second*2
        
        answer += 1
        
        heapq.heappush(q, new)
    
    return answer