score = []  # 점수를 저장할 리스트
number = []  # 번호를 저장할 리스트
sum = 0

for i in range(1, 9):
    score.append((i, int(input())))

score = sorted(score, key = lambda score: score[1])

for i in range(3, 8):
    sum += score[i][1]
    number.append(score[int(i)][0])

number.sort()
print(sum)
print(' '.join(map(str, number)))  # int로만 이루어진 리스트는 join되지 않기 때문에 map을 이용하여 str로 바꿔주어야한다.