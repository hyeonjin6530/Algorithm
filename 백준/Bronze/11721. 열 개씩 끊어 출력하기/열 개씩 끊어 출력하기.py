n = input()

for i in range((len(n)//10)+1):
    if i == (len(n)//10):  # 마지막 줄
        print(n[i*10 : ])  # 개수에 상관 없이 끝까지 출력하기 위함
    else:
        print(n[i*10 : (i+1)*10])  # 일반적인 경우