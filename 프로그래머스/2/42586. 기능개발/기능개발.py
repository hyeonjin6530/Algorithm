from collections import deque

def solution(progresses, speeds):
    answer = []
    
    works = deque(progresses)
    doWorks = deque(speeds)
    
    # 모든 작업이 끝날 때까지 반복
    while works:
        
        count = 0
        
        # 만약 맨 앞의 작업이 끝났을 경우에만 끝난 작업을 다 꺼냄
        if works[0] >= 100:
            while works and works[0] >= 100:
                works.popleft()
                doWorks.popleft()
                count += 1
            answer.append(count)
        
        # 작업 진도 + 작업 속도 해주기
        for i in range(len(works)):
            works[i] += doWorks[i]
        
    return answer