import sys

num = int(sys.stdin.readline())
data = []
rank = []

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

for i in range(num):
    count = 0
    for j in range(num):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:  # 자신보다 덩치가 큰 사람을 찾기 위해서
            count += 1
    rank.append(count + 1)  # 등수는 큰 사람의 수 + 1

for i in rank:
    print(i, end=" ")

