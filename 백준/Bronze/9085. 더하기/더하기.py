t = int(input())

for i in range(t):
    num = int(input())
    number = list(map(int, input().split()))
    print(sum(number))