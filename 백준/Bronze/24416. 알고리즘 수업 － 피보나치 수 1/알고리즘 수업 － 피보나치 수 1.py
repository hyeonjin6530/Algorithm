import sys
input = sys.stdin.readline

n = int(input())
count1 = 0
count2 = 0
f = [0] * (n+1)

def fib(n):
    global count1
    if n == 1 or n ==2:
        count1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibonacci(n):
    global count2
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count2 += 1
    return f[n]

fib(n)
fibonacci(n)

print(count1, count2)