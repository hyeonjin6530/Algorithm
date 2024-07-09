import sys

row, col = map(int, sys.stdin.readline().split())

matrix1 = [0 for i in range(row)]
matrix2 = [0 for i in range(row)]
result = [[0 for i in range(col)] for i in range(row)]

for i in range(row):
    matrix1[i] = list(map(int, sys.stdin.readline().split()))

for i in range(row):
    matrix2[i] = list(map(int, sys.stdin.readline().split()))

for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        print(result[i][j], end=' ')
    print()  # 줄바꿈