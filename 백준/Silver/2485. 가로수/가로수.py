# 간격들의 최대공약수
def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

num = int(input())
trees = [int(input()) for _ in range(num)]

interval = []

for i in range(1, num):
    interval.append(trees[i]- trees[i-1])

for i in range(1, len(interval)):
    interval[i] = GCD(interval[i], interval[i-1])

print((trees[num-1] - trees[0]) // interval[-1] + 1 - num )