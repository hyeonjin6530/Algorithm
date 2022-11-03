# 이건 시간 초과가 납니다~~
# import sys  # 그냥 하면 시간초과가 나서

# n = int(sys.stdin.readline())

# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())

#     for j in range(max(a,b),(a*b)+1):  # a와 b 중 큰 숫자부터 a와 b의 곱까지
#         if j % a == 0 and j % b == 0:  # j가 a와 b로 나누어 떨어진다면 그건 a, b의 배수이기 때문
#             print(j)
#             break  # 한 번만 하고 나갈거라서

import math
import sys

def lcm(a, b):  # 그냥 math.lcm() 써도 된다.
    return a * b / math.gcd(a,b)

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(int(lcm(a,b)))