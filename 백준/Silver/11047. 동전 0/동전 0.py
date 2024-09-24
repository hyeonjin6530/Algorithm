import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
coins = [ int(input()) for _ in range(n) ]

while k > 0:
    for i in range(n-1, -1, -1):
        if k >= coins[i]:
            count += k//coins[i]
            k %= coins[i]

print(count)