# 브루트 포스: 문제를 해결하기 위해 가능한 모든 경우의 수를 전부 시도해 보는 방법
import sys

m = int(input())

for i in range(1, m+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    if sum + i == m:
        print(i)
        sys.exit()

print(0)
