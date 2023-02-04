import sys

n = int(sys.stdin.readline())

for i in range(n):
    num, word = sys.stdin.readline().split()
    word = list(word)
    word[int(num)-1] = ''
    print(''.join(word))