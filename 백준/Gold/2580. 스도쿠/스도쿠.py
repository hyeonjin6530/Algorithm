import sys
input = sys.stdin.readline

# 스도쿠 전체 배열과 빈칸의 좌표를 저장할 배열을 만든다.
arr = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank = []

# 빈칸의 좌표를 저장한다.
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

# 스도쿠를 풀기 위한 함수들
def checkRow(x, num):
    for i in range(9):
        if num == arr[x][i]:
            return False
    return True

def checkCol(y, num):
    for i in range(9):
        if num == arr[i][y]:
            return False
    return True

def checkBox(x, y, num):
    for i in range(3):
        for j in range(3):
            if num == arr[x//3*3+i][y//3*3+j]:
                return False
    return True

def dfs(idx):
    # 빈칸이 없다면 출력하고 종료
    if idx == len(blank):
        for i in range(9):
            print(*arr[i])  # *를 사용하여 리스트의 요소를 공백으로 구분하여 출력
        sys.exit(0)
    
    x, y = blank[idx]
    
    # 1부터 9까지의 숫자를 넣어보며 가능한지 확인
    for i in range(1, 10):
        if checkRow(x, i) and checkCol(y, i) and checkBox(x, y, i):
            arr[x][y] = i
            dfs(idx+1)
            # 백트레킹
            arr[x][y] = 0

dfs(0)