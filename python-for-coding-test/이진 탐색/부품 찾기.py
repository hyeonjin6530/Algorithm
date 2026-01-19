n = int(input())
store = list(map(int, input().split()))

m = int(input())
client = list(map(int, input().split()))

store.sort()
client.sort()

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
      return "yes"
    
    elif arr[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1
  
  return "no"

for i in client:
  print(binary_search(store, i, 0, n-1), end=" ")