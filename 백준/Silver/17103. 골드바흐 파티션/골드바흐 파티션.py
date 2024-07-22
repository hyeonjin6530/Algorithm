import sys
input = sys.stdin.readline

num = 1000000

prime_list = [False, False] + [True] * (num-1)
for i in range(2, 1001):
    if prime_list[i]:
        for j in range(i*2, num+1, i):
            prime_list[j] = False

n = int(input())

for i in range(n):
    number = int(input())
    count = 0
    for j in range(2, number//2+1):
        if prime_list[j] and prime_list[number-j]:
            count += 1
        
    print(count)