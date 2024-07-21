import sys
input = sys.stdin.readline

num = 123456 * 2

def is_prime(number):
    if number<2 :
        return False
    for i in range(2, int(number**(1/2)+1)):
        if number % i == 0:
            return False
    return True

prime_list = []
for i in range(1, num+1):
    if is_prime(i):
        prime_list.append(i)

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in prime_list:
        if i > n and i <= 2*n:
            count += 1
    print(count)