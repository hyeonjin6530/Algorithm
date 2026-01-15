def solution(array, commands):
    answer = []
    
    for a in commands:
        i, j, k = a
        
        n_array = array[i-1:j]
        n_array.sort()
        answer.append(n_array[k-1])
    
    return answer