# 최소공배수는 두 수의 곱을 두 수의 최대공약수(유클리드 호제법 사용)로 나눈 값과 같다.

a, b = map(int, input().split())
multi =a*b

while b !=0:
    a, b = b, a%b

print(multi//a)