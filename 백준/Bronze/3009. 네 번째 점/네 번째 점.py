xList = []  # x좌표들을 저장할 리스트 생성
yList = []  # y좌표들을 저장할 리스트 생성

for i in range(3):
    x, y = map(int, input().split())
    xList.append(x)  # .append를 이용하여 리스트에 값 저장
    yList.append(y)

for i in range(3):
    if xList.count(xList[i]) == 1:  # 리스트 안에 그 숫자가 하나만 있으면
        x4 = xList[i]
    if yList.count(yList[i]) == 1:
        y4 = yList[i]

print(x4, y4)
