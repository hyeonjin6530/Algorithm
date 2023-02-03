n = int(input())

for i in range(n):
    word = list(input())
    word[0] = word[0].upper()
    print(''.join(word))