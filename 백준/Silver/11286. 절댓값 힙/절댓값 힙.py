from queue import PriorityQueue
import sys

input = sys.stdin.readline

n = int(input())
q = PriorityQueue()

for i in range(n):
  request = int(input())

  if request == 0:
    if q.empty():
      print(0)
    else:
      print(q.get()[1])
  else:
    # (절댓값, 원래값)의 튜플 형태로 삽입 (절댓값을 기준으로 정렬하고, 같으면 두번째 원래 값으로 정렬)
    q.put((abs(request), request))