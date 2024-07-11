edgeList = list(map(int, input().split()))
edgeList.sort()

while True:
    if(edgeList[0] + edgeList[1] > edgeList[2]):
        print(sum(edgeList))
        break
    else:
        edgeList[2] -= 1
        edgeList.sort()