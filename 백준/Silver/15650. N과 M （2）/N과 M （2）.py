import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    for i in range(1, n+1):
        if i not in arr and (len(arr) == 0 or i > arr[-1]):
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()