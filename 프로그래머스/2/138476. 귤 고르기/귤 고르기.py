# from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # counts = Counter(tangerine)
    # sorted_counts = sorted(counts.values(), reverse=True)

    counts = {}
    for i in tangerine:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    sorted_counts = sorted(counts.values(), reverse=True)
    
    total = 0
    
    for i in sorted_counts:
        total += i
        answer += 1
        if total >= k:
            break
            
    return answer