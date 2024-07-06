import sys

basket, num = map(int, sys.stdin.readline().split())

basketList = [i for i in range(1, basket+1)]

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    basketList[a-1], basketList[b-1] = basketList[b-1], basketList[a-1]

for i in range(basket):
    print(basketList[i], end=' ')