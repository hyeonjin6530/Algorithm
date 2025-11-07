import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

# 소수를 판별하는 함수
def isPrime(a):
  for i in range(2, int(a ** 0.5)):
    if a % i == 0:
      return False
  return True

# dfs 함수
def DFS(v):
  if len(str(v)) == n:
    print(v)
  else:
    for i in (1, 3, 7, 9):
      if i % 2 == 0:
        continue
      if isPrime(v * 10 + i):
        DFS(v*10+i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)