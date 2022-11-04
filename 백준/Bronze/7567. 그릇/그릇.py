plate = list(input())
sum = 10

for i in range(1,len(plate)):
    if plate[i-1] == plate[i]:
        sum += 5
    else:
        sum += 10

print(sum)

