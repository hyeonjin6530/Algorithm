numbers = []  # 숫자를 저장할 리스트
result = []  # 홀수를 저장할 리스트

for i in range(7):
    numbers.append(int(input()))

for i in numbers:
    if i % 2 != 0:
        result.append(i)

if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print("-1")