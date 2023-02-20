# 시간초과로 인해 list 보다 deque를 사용하는 것이 빠르다.
from collections import deque
import sys

n = int(sys.stdin.readline())

card = deque(i for i in range(1, n+1))

while len(card) > 1:
    card.popleft()  # 첫 번째 원소를 제거
    card.rotate(-1)  # 원소를 맨 뒷자리로 이동시킴

print(card[0])