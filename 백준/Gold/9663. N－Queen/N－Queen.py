import sys
input = sys.stdin.readline

n = int(input())

# 퀸을 놓을 수 있는지 확인
def is_impossible(x):
    for i in range(x):
        # 같은 행에 퀸이 있거나, 대각선에 퀸이 있는지 확인
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return True
    return False

def dfs(x):
    global count

    if x == n:  # 마지막까지 탐색했을 경우
        count += 1
    else:
        for i in range(n):
            row[x] = i
            if not is_impossible(x):
                dfs(x + 1)

row = [0] * n  # row[i]는 i번째 행에 퀸이 놓여있다는 의미 (각 행, 열에 퀸이 하나씩만 놓일 수 있으므로 1차원으로 표현 가능)
count = 0
dfs(0)

print(count)