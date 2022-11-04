price, num, money = map(int, input().split())

if price*num > money:
    print(price*num - money)
else:
    print(0)