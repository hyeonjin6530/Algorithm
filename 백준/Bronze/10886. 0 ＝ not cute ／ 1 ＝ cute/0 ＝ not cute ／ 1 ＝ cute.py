n = int(input())

cuteCount = 0
notCute = 0

for i in range(n):
    s = input()
    if s == '1':
        cuteCount += 1
    else:
        notCute += 1

if cuteCount > notCute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
