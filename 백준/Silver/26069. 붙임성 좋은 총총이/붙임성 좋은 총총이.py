import sys
input = sys.stdin.readline

n = int(input())
dance = False
dance_list = []

for i in range(n):
    a, b = input().strip().split()
    if a == 'ChongChong' or b =='ChongChong':
        dance = True
        dance_list.append(a)
        dance_list.append(b)
    if dance:
        if a in dance_list or b in dance_list:
            dance_list.append(a)
            dance_list.append(b)

print(len(set(dance_list)))