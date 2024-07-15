import sys

num = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

num_sorted = sorted(list(set(num_list)))

dic = {num_sorted[i]: i for i in range(len(num_sorted))}

for i in num_list:
    print(dic[i], end=' ')
