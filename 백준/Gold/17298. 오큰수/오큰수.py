n = int(input())

arr = list(map(int, input().split()))

answer = [-1] * n
stack = []

for i in range(n):
  while stack and arr[i] > arr[stack[-1]]:
    answer[stack.pop()] = arr[i]
  stack.append(i)

for i in answer:
  print(i, end=" ")