def solution(people, limit):
    answer = 0
    
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        weight = people[start] + people[end]
        
        if weight > limit:
            answer += 1  # 무거운 애 혼자 태우기
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1
    
    return answer