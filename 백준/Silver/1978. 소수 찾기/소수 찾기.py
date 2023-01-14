num = int(input())
numbers = map(int, input().split())
count = 0

for n in numbers:
    error = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                error += 1
        if error == 0:
            count += 1

print(count)
