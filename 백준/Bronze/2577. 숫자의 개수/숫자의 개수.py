sum = 1

for i in range(3):
    n = int(input())
    sum *= n

for i in range(10):
    print(str(sum).count(str(i)))
