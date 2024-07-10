import sys

num = int(sys.stdin.readline())
number = 1
count = 1

# 1 7 19 37 61와 같이 (기존 벌집 숫자) + 6의 배수로 증가함을 이용
while num > number:
    number = number + 6 * count
    count += 1

print(count)