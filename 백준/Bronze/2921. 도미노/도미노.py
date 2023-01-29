num = int(input())
sum = 0  # 총합

for i in range(num+1):
    for j in range(i+1):
        sum += (i+j)

print(sum)