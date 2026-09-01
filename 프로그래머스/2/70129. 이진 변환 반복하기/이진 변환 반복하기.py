def solution(s):
    times = 0  # 이진 변환의 횟수
    zeros = 0  # 제거된 0의 개수
    
    while True:
        if s == '1':
            break
            
        zeros += s.count("0")
        s = s.replace("0", "")

        times += 1
        s = bin(len(s))[2:]
    
    return [times, zeros]