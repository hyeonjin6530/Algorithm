number = []

a = 0  # 숫자의 개수를 저장하기 위한 변수
max_num = 0  # 최빈값 저장을 위한 변수

for i in range(10):
    number.append(int(input()))

for i in set(number):  # 중복 제거
    n = number.count(i)
    if n > a:
        a = n
        max_num = i

print(sum(number)//10)
print(max_num)