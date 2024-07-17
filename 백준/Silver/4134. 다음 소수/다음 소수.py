import sys
num = int(sys.stdin.readline())

def is_prime(number):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    for i in range(2, int(number**(1/2)+1)):
        if number % i == 0:
            return False
    else:
        return True

for i in range(num):
    number = int(sys.stdin.readline())
    
    while(True):
        if is_prime(number):
            print(number)
            break
        number += 1
