def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 1. N, NN, NNN... 값 저장
        dp[i].add(int(str(N)*i))
        
        # 2. i = j + (i-j)로 쪼개서 조합
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b)
    
        # 3. number이 포함되어 있을 경우 반환
        if number in dp[i]:
            return i
    
    return -1