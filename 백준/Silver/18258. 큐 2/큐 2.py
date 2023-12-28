# list를 그냥 사용하면 시간초과 오류 발생
# -> 발생 이유) pop을 할 때 pop(0)을 할 때, 요소들의 인덱스를 한칸씩 당기는 과정에서 O(n)의 계산량이 발생
# 해결방법 1. deque 사용
# 해결방법 2. queue의 출구를 가르키는 index 변수 사용 ✅

import sys

input = sys.stdin.readline

q = list()
idx = 0  # queue의 출구를 가르키는 변수

n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == "push":
        q.append(command[1])

    elif command[0] == "pop":
        if len(q) > idx:
            print(q[idx])
            idx += 1
        else:
            print(-1)

    elif command[0] == "size":
        print(len(q) - idx)

    elif command[0] == "empty":
        if len(q) == idx:
            print(1)
            idx = 0
            q = []  # queue를 비워준다
        else:
            print(0)

    elif command[0] == "front":
        if len(q) > idx:
            print(q[idx])
        else:
            print(-1)

    elif command[0] == "back":
        if len(q) > idx:
            print(q[-1])
        else:
            print(-1)
