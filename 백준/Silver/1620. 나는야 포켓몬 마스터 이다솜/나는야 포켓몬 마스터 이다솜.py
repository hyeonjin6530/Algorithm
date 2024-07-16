import sys

n, m = map(int, sys.stdin.readline().split())

poketmonList = [sys.stdin.readline().rstrip() for i in range(1, n+1)]
poketmonDict = {poketmonList[i]: i+1 for i in range(n)}

for i in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(poketmonList[int(question)-1])
    else:
        print(poketmonDict[question])