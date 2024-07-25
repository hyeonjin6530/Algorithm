n = int(input())
numList = list(map(int, input().split()))

s = []
target = 1

while numList:
    if numList[0] == target:
        numList.pop(0)
        target += 1
    else:
        s.append(numList.pop(0))

    while s:
        if s[-1] == target:
            s.pop()
            target += 1
        else:
            break

if not s:
    print('Nice')
else:
    print('Sad')