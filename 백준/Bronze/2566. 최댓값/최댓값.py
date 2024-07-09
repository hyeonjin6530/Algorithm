import sys

max_num, max_row, max_col = 0, 0, 0

for i in range(9):
    numbers = list(map(int, sys.stdin.readline().split()))
    if max_num <= max(numbers):
        max_num = max(numbers)
        max_col = numbers.index(max_num) +1
        max_row = i+1

print(max_num)
print(max_row, max_col, sep=' ')