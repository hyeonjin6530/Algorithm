'''
  문제 유형: 분할 정복(큰 문제를 작은 문제로 분할하여 계산하는 방법)

  문제 풀이 방법: 
    a^n을 계산할 때 지수 n을 반으로 나누어 O(log n) 시간에 계산
      - n이 짝수: a^n = (a^n//2)*(a^n//2)
      - n이 홀수: a^n = (a^n//2)*(a^n//2)*a

'''

n, b = map(int, input().split())

matrix = []

for i in range(n):
  matrix.append(list(map(int, input().split())))

def mul(A, B):
  m = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        m[i][j] += A[i][k] * B[k][j]
      m[i][j] %= 1000
  return m

def power(A, B):
  # 만약 B가 1이 되면 1000으로 나눈 나머지를 반환
  if B == 1:
    for i in range(n):
      for j in range(n):
        A[i][j] %= 1000
    return A
  
  tmp = power(A, B//2)
  
  if B % 2:
    return mul(mul(tmp, tmp), A)
  else:
    return mul(tmp, tmp)

result = power(matrix, b)
for r in result:
  print(*r) # *은 언패킹 연산자로, 리스트의 각 원소를 하나씩 꺼내서 전달한다는 뜻