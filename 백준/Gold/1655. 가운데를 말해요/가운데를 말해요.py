'''
  문제 유형: 우선순위 큐

  문제 풀이 방법: 정렬을 계속 반복하면 시간초과가 나기 때문에 우선순위 큐 사용
    1. leftHeap(최대힙)과 rightHeap(최소힙) 사용
    2. leftHeap과 rightHeap에 숫자를 번갈아가며 넣기
    3. 만약 rightHeap에 leftHeap보다 작은 숫자가 들어간다면 하나씩 pop해서 바꿔주기
    4. leftHeap을 pop하고 -를 붙여주면 정답!

'''

import heapq
import sys

input = sys.stdin.readline

n = int(input())

leftHeap = []
rightHeap = []

for _ in range(n):
  num = int(input())

  if len(leftHeap) == len(rightHeap):
    heapq.heappush(leftHeap, -num)
  else:
    heapq.heappush(rightHeap, num)
  
  if rightHeap and rightHeap[0] < -leftHeap[0]:
    left = heapq.heappop(leftHeap)
    right = heapq.heappop(rightHeap)

    heapq.heappush(leftHeap, -right)
    heapq.heappush(rightHeap, -left)
  
  print(-leftHeap[0])