num = int(input())
current = 0  # n번째 값
next = 1  # n+1번째 값

for i in range(num):
    current, next = next, (current + next)

print(current)