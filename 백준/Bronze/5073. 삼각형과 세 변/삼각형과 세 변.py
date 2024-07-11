edgeList = [0] * 3

while True:
    edgeList = list(map(int, input().split()))
    if edgeList == [0, 0, 0]:
        break

    edgeList.sort()
    if edgeList[2] < edgeList[1] + edgeList[0]:
        if len(set(edgeList)) == 1:
            print('Equilateral')
        elif len(set(edgeList)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')