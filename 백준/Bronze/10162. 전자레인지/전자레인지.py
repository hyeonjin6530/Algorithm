t = int(input())

countA = 0
countB = 0
countC = 0

if t >= 300:
    countA = (t // 300)
    t = t % 300
if t >= 60:
    countB = (t // 60)
    t = t % 60
if t >= 10:
    countC = (t // 10)
    t = t % 10

if t == 0:
    print(countA, countB, countC)
else:
    print(-1)