import sys
input = sys.stdin.readline

def cantor(n):
    if n == 0:
        return '-'
    else:
        return cantor(n-1) + ' '*(3**(n-1)) + cantor(n-1)
    
while True:
    try:
        n = int(input())
        print(cantor(n))
    except:
        break