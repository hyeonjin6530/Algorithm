import sys

n = int(sys.stdin.readline())
card = set(sys.stdin.readline().split())

m = int(sys.stdin.readline())
number = sys.stdin.readline().split()

for i in number:
    if i in card:
        print(1, end=" ")
    else:
        print(0, end=' ')