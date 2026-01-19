n = int(input())

score = []

for i in range(n):
  score.append(input().split())

score.sort(key=lambda x : x[1])

for i in score:
  print(i[0], end=" ")