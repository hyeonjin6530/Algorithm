import sys

n = int(sys.stdin.readline())
A_list = set(map(int, sys.stdin.readline().split()) ) 
# 시간초과 문제로 인해 list가 아닌 set을 이용한다.
# 중복값이 없을 뿐더라 탐색을 하는 용도로만 쓰이기 때문에

m = int(sys.stdin.readline())
B_list = list(map(int, sys.stdin.readline().split()))

for i in B_list:
    if i in A_list:
        print(1)
    else:
        print(0)
