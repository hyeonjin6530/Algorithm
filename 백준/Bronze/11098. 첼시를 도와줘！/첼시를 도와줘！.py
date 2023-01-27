test = int(input())

for i in range(test):
    player = int(input())
    list = []  # 선수들을 저장할 리스트
    buy = []  # 가장 비싼 선수를 저장할 리스트

    for j in range(player):
        a, b = input().split()
        list.append((int(a), b))

    buy = max(list)
    print(buy[1])  # 리스트의 두 번째 요소인 선수이름 출력

