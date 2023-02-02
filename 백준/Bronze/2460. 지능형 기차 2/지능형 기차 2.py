sum = 0  # 버스 안에 누가 있는 지 저장할 변수
result = 0  # 가장 최대의 승객 수를 저장할 변수

for i in range(10):
    a, b = map(int, input().split())
    sum  += (b - a)
    if result < sum:
        result = sum

print(result)