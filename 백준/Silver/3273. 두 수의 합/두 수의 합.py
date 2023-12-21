# 두 수의 합이 x가 되는 순서쌍의 개수 구하기

# 시간초과 해결 방법
# 1. input 대신 sys.stdin.readline 사용
# 2. 투 포인터 사용

import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
x = int(input())

l.sort()  # 숫자 리스트 정렬하기

count = 0  # 순서쌍의 개수를 저장하는 변수
left = 0
right = n - 1


while left < right:
    if l[left] + l[right] == x:
        count += 1
        left += 1
    elif l[left] + l[right] < x:
        left += 1
    elif l[left] + l[right] > x:
        right -= 1

print(count)
