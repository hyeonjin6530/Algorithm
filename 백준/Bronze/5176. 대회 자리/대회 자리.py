n = int(input())

for i in range(n):
    p, m = map(int, input().split())
    count = []  # 입력을 저장할 리스트
    for j in range(p):
        num = int(input())
        if num in count:
            pass
        else:
            count.append(num)
    print(p - len(count))