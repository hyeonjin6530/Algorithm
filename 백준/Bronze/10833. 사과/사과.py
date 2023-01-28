num = int(input())
apple = 0

for i in range(num):
    a, b = map(int, input().split())
    apple += (b%a)

print(apple)