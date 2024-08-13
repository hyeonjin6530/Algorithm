import sys
input = sys.stdin.readline

l, c = map(int, input().split())

alpha = list(input().rstrip().split())

alpha.sort()

count_consonant = 0
count_vowel = 0
result = []

def backtracking(index, count_consonant, count_vowel):
    if len(result) == l and count_consonant >= 2 and count_vowel >= 1:
        print(''.join(result))
        return
    for i in range(index, c):
        result.append(alpha[i])
        if alpha[i] in 'aeiou':
            backtracking(i+1, count_consonant, count_vowel+1)
        else:
            backtracking(i+1, count_consonant+1, count_vowel)
        result.pop()

backtracking(0, 0, 0)