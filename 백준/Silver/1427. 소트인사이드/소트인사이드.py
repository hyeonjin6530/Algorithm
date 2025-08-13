num = list(input())

for i in range(len(num)):
  max = i
  # 최댓값을 찾기
  for j in range(i+1, len(num)):
    if num[max] < num[j]:
      max = j
  # swap
  if num[max] > num[i]:
    num[max], num[i] = num[i], num[max]

print(''.join(num))