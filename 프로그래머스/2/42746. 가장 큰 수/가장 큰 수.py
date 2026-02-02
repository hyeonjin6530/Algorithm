def solution(numbers):
    answer = ''
    
    # 전부 문자열로 바꾸기
    numbers = list(map(str, numbers))
    
    # 최대 자리수로 맞추어 정렬하기
    numbers.sort(key = lambda x : x*4, reverse=True)
    
    answer = ''.join(numbers)
    
    # 모든 수가 0일 경우
    if answer[0] == '0':
        answer = '0'
    
    return answer