# 재귀로 풀어보기
import sys
sys.setrecursionlimit(10**6)

n = int(input())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(n))