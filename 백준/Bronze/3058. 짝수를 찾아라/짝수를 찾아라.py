num = int(input())

for i in range(num):
    even = []  # 짝수를 저장할 리스트
    n = list(map(int, input().split()))
    for j in n:
        if j%2 == 0:
            even.append(j)
    print(sum(even), end=" ")
    print(min(even))

