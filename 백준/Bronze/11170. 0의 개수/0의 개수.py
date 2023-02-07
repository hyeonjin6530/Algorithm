n = int(input())

for i in range(n):
    sum = 0  # 0의 개수
    a, b = map(int, input().split())
    for i in range(a, b+1):
        sum += str(i).count('0')
    print(sum)
