def solution(sizes):
    answer = 0
    
    w = []
    h = []

    for i in sizes:
        # 가장 긴 값들 저장
        w.append(max(i))
        # 가장 작은 값들 저장
        h.append(min(i))
    
    # 그중 가장 긴 것들로 크기 구하기
    answer = max(w) * max(h)
    
    return answer