import sys

num = int(sys.stdin.readline())
count = 0

for i in range(0, num):
    n = int(sys.stdin.readline())
    count += n

print(count - (num-1))