import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
  arr.append((int(input()), i))

max = 0 # 왼쪽으로 가장 많이 이동한 횟수
sorted_arr = sorted(arr)

for i in range(n):
  if max < sorted_arr[i][1] - i:
    max = sorted_arr[i][1] - i

print(max+1)