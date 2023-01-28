date = int(input())
carList = list(map(int, input().split()))
count = 0

for i in carList:
    if date == i:
        count += 1

print(count)