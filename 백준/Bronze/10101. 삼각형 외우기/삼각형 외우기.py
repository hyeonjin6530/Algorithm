angleList = [int(input()) for i in range(3)]

if angleList.count(60) == 3:
    print('Equilateral')
elif sum(angleList) == 180:
    if len(set(angleList)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')