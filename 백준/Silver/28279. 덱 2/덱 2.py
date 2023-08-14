import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "1":
        d.appendleft(command[1])  # 리스트 맨 앞에 추가
    elif command[0] == "2":
        d.append(command[1])  # 리스트 맨 뒤에 추가
    elif command[0] == "3":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())  # 리스트 맨 앞 삭제
    elif command[0] == "4":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())  # 리스트 맨 뒤 삭제
    elif command[0] == "5":
        print(len(d))
    elif command[0] == "6":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "7":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif command[0] == "8":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
