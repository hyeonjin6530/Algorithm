n = int(input())
result = 1
zero = 0

for i in range(1, n+1):
    result *= i

result = str(result)

for i in reversed(range(len(result))):
    if result[i] == '0':
        zero += 1
    else:
        break

print(zero)