from itertools import permutations  # 순열 라이브러리

def solution(n, weak, dist):
    # 불가능한 큰 값으로 시작
    answer = len(dist) + 1
    
    length = len(weak)

    # 원형 -> 선형으로 처리
    extended = weak + [x + n for x in weak]
    
    # 시작점 선택
    for start in range(length):
        
        # 순열을 통해 친구 순서 선택
        for friends in permutations(dist):
            count = 1
            
            # 첫 친구가 막을 수 있는 위치
            cover = extended[start] + friends[count-1]
            
            # 취약지점 검사
            for i in range(start, start + length):
                
                # 현재 친구가 못막으면
                if extended[i] > cover:
                    count += 1
                    
                    # 친구 다 썼으면 종료
                    if count > len(dist):
                        break
                        
                    # 새 친구 투입
                    cover = extended[i] + friends[count - 1]
            
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
            
    
    return answer