import sys

num = int(sys.stdin.readline())
list = []

for i in range(num):
    list.append(int(sys.stdin.readline()))

result = sorted(list)

for i in result:
    print(i)