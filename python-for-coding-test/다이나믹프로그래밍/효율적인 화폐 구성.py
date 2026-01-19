# 큰 단위가 작은 단위의 배수가 아니기 때문에 그리디 사용 x

n, m = map(int, input().split())

money = [int(input()) for _ in range(n)]

d = [10001] * (m+1)
d[0] = 0

for i in money:
  for j in range(i, m+1):
      d[j] = min(d[j], d[j-i] + 1)


if d[m] == 10001:
  print(-1)
else:
  print(d[m])