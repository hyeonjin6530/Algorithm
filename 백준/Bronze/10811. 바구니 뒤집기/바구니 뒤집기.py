import sys

basket, num = map(int, sys.stdin.readline().split())

basketList = [i for i in range(1, basket+1)]

for i in range(num):
    start, end = map(int, sys.stdin.readline().split())
    basketList[start-1:end] = basketList[start-1:end][::-1]

for i in range(basket):
    print(basketList[i], end=' ')