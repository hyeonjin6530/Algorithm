def solution(prices): 
    
    n = len(prices)
    
    answer = [0] * n

    # 효율성 문제로 스택 사용해서 풀기
    stack = []
    
    for i in range(n):
        # 가격이 떨어졌을 경우
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top  
        
        # 가격이 떨어지지 않았을 경우
        stack.append(i)
    
    # 끝까지 가격이 떨어지지 않았을 경우
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top
    
    return answer