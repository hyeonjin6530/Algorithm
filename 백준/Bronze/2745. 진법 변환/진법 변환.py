result = 0

num, formation = input().split()

for i in range(len(num)):
    if 'A' <= num[i] <= 'Z':
        result += (ord(num[i]) - 55) * int(formation) ** (len(num) - i - 1)
    else:
        result += int(num[i]) * int(formation) ** (len(num) - i - 1)

print(result)