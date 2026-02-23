n = int(input())

arr = []

for _ in range(n):
  start, end = map(int, input().split())
  arr.append((start, end))

# 종료 시간으로 정렬한 다음 시작 시간으로 정렬 (빨리 끝나는 회의를 선택해야 더 많은 회의를 넣을 수 있기 때문)
arr.sort(key = lambda x: (x[1], x[0]))

count = 1 # 무조건 첫 번째 회의는 포함된다는 가정하에 시작
k = 0  # 마지막으로 추가된 회의의 인덱스

for i in range(1, n):
  # 이전 회의의 종료 시간 보다 이후 회의의 시작 시간이 같거나 크다면 회의 추가
  if arr[k][1] <= arr[i][0]:
    count += 1
    k = i

print(count)