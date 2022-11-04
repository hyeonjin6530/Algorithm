n = int(input())
money = []  
# 빈 리스트로 하면 IndexError: list assignment index out of range 이런 오류가 난다.
# 왜냐하면 아래 for문 안에서 리스트의 인덱스를 사용해야하기 때문이다.
# 그래서 아래서 리스트에 값을 넣어줄 것이다.

for i in range(n):
    money.append(0)
    a, b, c = map(int, input().split())
    if a == b and b == c:
        money[i] = 10000 + a*1000
    else:
        if a == b or a == c:
            money[i] = 1000 + a*100
        elif b == c:
            money[i] = 1000 + b*100
        else:
            money[i] = max(a, b, c)*100

print(max(money))