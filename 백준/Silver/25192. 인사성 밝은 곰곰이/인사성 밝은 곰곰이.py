import sys

input = sys.stdin.readline

n = int(input())
nickname = []
count = 0

for i in range(n):
    s = input().strip()
    if s == 'ENTER':
        count += len(set(nickname))
        nickname = []
    else:
        nickname.append(s)

print(count + len(set(nickname)))