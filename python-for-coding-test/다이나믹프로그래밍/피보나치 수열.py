# 1. 점화식을 활용하여 재귀함수로 구현한 방식
def fibo(n):
  if n == 1 or n == 2:
    return 1
  
  return fibo(n-1) + fibo(n-2)

print(fibo(4))


# 2. 메모이제이션(탑다운, 하향식)으로 구현한 방식 -> 재귀함수 사용
d = [0] * 100

def fibo(n):
  if n == 1 or n == 2:
    return 1
  
  if d[n] != 0:
    return d[n]
  
  d[n] = fibo[n-1] + fibo[n-2]
  return d[n]

print(fibo(99))


# 3. 바텀업(상향식)으로 구현한 방식 -> 반복문 사용
d = [0] * 100
d[1] = 1
d[2] = 1

n = 99

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])