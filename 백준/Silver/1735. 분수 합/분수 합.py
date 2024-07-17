a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

result1 = a1*b2 + b1*a2
result2= a2*b2

def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

gcd = GCD(result1, result2)

print(result1//gcd, result2//gcd)