n = int(input())

i = 2  # 소인수분해는 2부터 나눠야함
if n == 1:
    pass
else:
    while n != 1:  # n이 1이 되면 멈춘다.
        if n % i == 0:
            n = n // i  # n에 나눈 값을 넣어줘야지
            print(i) 
        else:
            i += 1  # 더이상 나누어지지 않을 때 숫자를 +1