from collections import deque

import sys

input = sys.stdin.readline

t = int(input())


for i in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    count = 0
    while q:
        priority = max(q)
        front = q.popleft()
        m -= 1

        if priority == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            q.append(front)
            if m < 0:
                m = len(q) - 1
