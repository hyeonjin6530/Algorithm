n = int(input())

for i in range(n):
    num = int(input())
    car = list(map(int, input().split()))
    print((max(car) - min(car))*2)  # 거리는 (최대-최소)*2 이다.