def solution(n):
    answer = 1 # 자기 자신은 무조건 포함

    for i in range(1, n):
        result = 0
        for j in range(i, n):
            result += j
            
            # 누적합이 n이 되면 결과 +1
            if result == n:
                answer += 1

            # 누적합이 n을 넘어가면 종료
            if result > n:
                break
    
    return answer