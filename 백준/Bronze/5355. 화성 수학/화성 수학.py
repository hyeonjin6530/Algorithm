num = int(input())

for i in range(num):
    s = input().split()

    result = 0
    result += float(s[0])

    for i in s[1:]:
        if i == '@': 
            result *= 3
        elif i == '%':
            result += 5
        elif i == '#':
            result -= 7

    print("{:.2f}" .format(result)) # 소수점 두 자리까지 나타내려면



