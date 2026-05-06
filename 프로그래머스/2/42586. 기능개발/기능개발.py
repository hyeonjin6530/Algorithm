def solution(progresses, speeds):
    answer = []
    
    # 작업이 끝나는 날
    day = []
    
    # 작업일수를 계산해서 저장
    for i in range(len(progresses)):
        result = (100 - progresses[i]) // speeds[i]
        
        if (100 - progresses[i]) % speeds[i] == 0:
            day.append(result)
        else:
            day.append(result + 1)
    
    # 다음 요소가 지금 요소보다 클 때까지 계속 pop(0)
    while len(day) > 0:
        now = day.pop(0)
        count = 1
        
        while len(day) > 0 and now >= day[0]:
            day.pop(0)
            count += 1
            
        answer.append(count)
    
    return answer