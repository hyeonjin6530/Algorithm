n = int(input())

drink = {}

for i in range(n):
    num = int(input())
    for j in range(num):
        a, b= input().split() 
        drink[a] = int(b)
    print(max(drink, key = drink.get))
        
# 딕셔너리에서 value 값이 최대인 key 차기: max_key = max(dict, key=dict.get)