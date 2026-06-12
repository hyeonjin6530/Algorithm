def solution(s):
    answer = len(s)
    
    n = len(s) // 2
    
    for i in range(1, n+1): # 압축 단위
        prev = s[0:i]  # 현재 기억 중인 조각
        count = 1  # 몇 개가 같은지
        compressed = ""  # 압축 결과
        
        for j in range(i, len(s), i): # 문자열 순회
            if prev == s[j:j+i]:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev 
                else:
                    compressed += prev 
                prev = s[j:j+i]
                count = 1
        
        # 마지막 묶음이 자동으로 결과에 들어가지 않기 때문에 한 번 더 체크를 해줘야함
        if count > 1:
                    compressed += str(count) + prev 
        else:
            compressed += prev 
        
        answer = min(answer, len(compressed))
    
    return answer