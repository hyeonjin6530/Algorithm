# 이진탐색, 파라메트릭 서치
n, m = map(int, input().split())

rice_cake = list(map(int, input().split()))

result = 0

def binary_search(arr, target, start, end):
  global result
  
  while start <= end:
    total = 0

    mid = (start + end) // 2

    for i in rice_cake:
      if i > mid:
        total += i - mid

    if total == target:
      return mid
    
    elif total >= target:
      result = mid
      start = mid + 1

    else:
      end = mid - 1

print(binary_search(rice_cake, m, 0, max(rice_cake)))