'''
    처음엔 dfs를 사용하려 했으나 거리 제한이 2로 매우 작고 확인해야 할 위치가 고정되어 있어서 
    주변 좌표만 직접 검사하는 것이 더 단순하고 효율적이므로 그냥 맨해튼 거리가 2인 곳만 확인하기로 함
'''

def solution(places):
    answer = []
    
    # 거리 1
    near = [(-1,0), (1,0), (0,-1), (0,1)]

    # 거리 2 직선
    straight = [(-2,0), (2,0), (0,-2), (0,2)]

    # 대각선
    diagonal = [(-1,-1), (-1,1), (1,-1), (1,1)]
    
    def in_range(x, y):
        return 0 <= x < 5 and 0 <= y < 5
    
    # 거리두기 규칙 확인 함수
    def check(r, c, place):
        
        # 1. 거리 1에 P가 있으면 바로 실패
        for dr, dc in near:
            nr = r + dr
            nc = c + dc
            
            if in_range(nr, nc):
                if place[nr][nc] == 'P':
                    return False

        # 2. 거리 2 직선에 P가 있으면 중간 칸이 X인지 확인
        for dr, dc in straight:
            nr = r + dr
            nc = c + dc
            
            if in_range(nr, nc):
                if place[nr][nc] == 'P':
                    # 중간 칸
                    mr = r + dr // 2
                    mc = c + dc // 2
                    if place[mr][mc] != 'X':
                        return False

        # 3. 대각선에 P가 있으면 사이 두 칸이 둘 다 X인지 확인
        for dr, dc in diagonal:
            nr = r + dr
            nc = c + dc
            
            if in_range(nr, nc):
                if place[nr][nc] == 'P':
                    # 사이 두 칸
                    br1 = r + dr
                    bc1 = c
                    br2 = r
                    bc2 = c + dc
                    
                    if place[br1][bc1] != 'X' or place[br2][bc2] != 'X':
                        return False 
                    
        # 다 통과 했으면 True 반환            
        return True
        
        
    for i in range(5):
        isOkay = True
        
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    if not check(j, k, places[i]):
                        isOkay = False                        
                    
        # 거리두기를 잘 지켰을 경우 1
        if isOkay:
            answer.append(1)
        # 거리두기를 안 지켰을 경우 1
        else:
            answer.append(0)
    
        
    return answer