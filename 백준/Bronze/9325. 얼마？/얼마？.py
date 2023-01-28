t = int(input())

for i in range(t):
    price = int(input())
    num = int(input())
    for j in range(num):
        q, p = map(int, input().split())
        price += (q*p)
    print(price)