from itertools import combinations

def solution(relation):
    answer = 0
    
    c = len(relation)  # 튜플의 개수
    
    d = len(relation[0])  # 속성의 개수
    
    nums = list(range(d))
        
    # 최소성 확인을 위한 후보키 리스트
    c_list = []
    
    # 조합을 활용하여 모든 경우의 수 확인
    for r in range(1, d + 1):
        for comb in combinations(nums, r):
            
            # 최소성 검사
            is_minimal = True
            
            for i in c_list:
                if all(x in comb for x in i):
                    is_minimal = False
                    break
            
            if not is_minimal:
                continue
                    
            test_set = set()  # 유일성 확인을 위한 테스트 집합
            
            for row in relation:
                key = tuple(row[i] for i in comb)
                test_set.add(key)
            
            if len(test_set) == c:
                answer += 1
                c_list.append(comb)
    
    return answer