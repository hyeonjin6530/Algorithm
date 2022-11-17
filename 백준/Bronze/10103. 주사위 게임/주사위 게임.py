num = int(input())

young = 100  # 창영이의 점수
duck = 100  # 상덕이의 점수

for i in range(num):
    a, b = map(int, input().split())
    if a > b:
        duck -= a
    elif a < b:
        young -= b
    else:
        pass

print(young)
print(duck)