# 길이로 정렬을 하고 싶을 때 list.sort(key=len)
import sys

num = int(sys.stdin.readline())
words = set()

for i in range(num):
    words.add(sys.stdin.readline())  # 집합에서는 요소를 추가할 때 add 사용

words = list(sorted(words))
words.sort(key=len)

for i in words:
    print(i.rstrip())  # \n을 없애기 위함

