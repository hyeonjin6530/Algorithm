import sys

basket, num = map(int, sys.stdin.readline().split())

basketList = [0 for i in range(basket)]

for i in range(num):
    start, end, ballNum = map(int, sys.stdin.readline().split())
    for j in range(start-1, end):
        basketList[j] = ballNum

for i in range(basket):
    print(basketList[i], end=' ')