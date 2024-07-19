m, n = map(int, input().split())

def is_prime(number):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    for i in range(2, int(number**(1/2)+1)):
        if number % i == 0:
            return False
    return True
        
for i in range(m, n+1):
        if is_prime(i):
            print(i)