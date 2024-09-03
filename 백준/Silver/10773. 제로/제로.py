import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    
    if num == 0 and len(numbers) != 0:
            numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))