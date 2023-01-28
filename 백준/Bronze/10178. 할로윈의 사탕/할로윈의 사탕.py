num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    print("You get", (a//b), "piece(s) and your dad gets", (a%b), "piece(s).")