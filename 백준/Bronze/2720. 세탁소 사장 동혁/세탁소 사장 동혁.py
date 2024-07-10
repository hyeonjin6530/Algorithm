import sys

t = int(sys.stdin.readline())

for i in range(t):
    change_list = [0] * 4
    change = int(sys.stdin.readline())

    while change > 0:
        if change >= 25:
            change_list[0] += 1
            change -= 25
        elif change >= 10:
            change_list[1] += 1
            change -= 10
        elif change >= 5:
            change_list[2] += 1
            change -= 5
        else:
            change_list[3] += 1
            change -= 1
    
    print(change_list[0], change_list[1], change_list[2], change_list[3], end=' ')
    print()