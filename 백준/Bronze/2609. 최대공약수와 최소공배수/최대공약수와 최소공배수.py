# 유클리드 호제법 사용

a, b = map(int, input().split())

def gcd(a,b):  # 최대공약수
    while b > 0:
        a, b = b, a%b  # 여기서 유클리드 호제법이 사용된다.
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))