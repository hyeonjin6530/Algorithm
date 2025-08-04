from collections import deque

n, l = map(int, input().split())
nums = list(map(int, input().split()))

dq = deque()


for i in range(n):
  # 덱은 비어있으면 false라서 덱이 true일 때는 덱에 값이 있다는 것이다.
  # dq[-1][0]은 여기서는 덱의 맨 뒤의 요소의 값을 의미한다.
  # 즉, 맨 뒤의 값이 새로 들어오는 값보다 클 경우에는 해당 값을 꺼낸다는 것이다.
  while dq and dq[-1][0] > nums[i]:
    dq.pop()
  
  # (값, 인덱스)의 튜플 구조로 저장
  dq.append((nums[i], i))

  # 덱의 가장 첫번째 요소의 인덱스가 현재 윈도우 범위를 벗어날 경우, 첫번째 요소를 꺼낸다.
  if dq[0][1] <= i - l:
    dq.popleft()
  
  # 덱의 가장 첫번째 요소의 값은 최소값이 된다.
  print(dq[0][0], end=' ')