def solution(id_list, report, k):
    answer = []
    
    users = {}
    
    dict = {}
    
    for i in id_list:
        dict[i] = set()
        users[i] = 0
    
    for i in report:
        server, receiver = i.split()
        dict[receiver].add(server)
    
    for key, value in dict.items():
        if len(value) >= k:
            for v in value:
                users[v] += 1 
                
    for key, value in users.items():
        answer.append(value)
        
    return answer