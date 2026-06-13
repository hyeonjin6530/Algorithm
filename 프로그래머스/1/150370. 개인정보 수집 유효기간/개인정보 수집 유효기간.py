def solution(today, terms, privacies):
    answer = []
    
    dict = {}
    
    for t in terms:
        a, b = t.split()
        dict[a] = b
    
    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        
        year = int(date[0:4])
        month = int(date[5:7]) + int(dict[kind])
        
        # 날짜 계산하기
        if month > 12:
            year += (month - 1) // 12
            month = (month - 1) % 12 + 1
        
        if month < 10:
            month = '0' + str(month)
        new_date = str(year) + '.' + str(month) + date[7:]

        # 유효기간을 지났는지 계산하기
        if new_date <= today:
            answer.append(i+1)
        
    return answer