word = input()

words = 'abcdefghijklmnopqrstuvwxyz'

for i in words:
    if i in word:
        print(word.index(i), end=' ')  # 위치를 반환하는 .index()
    else:
        print('-1', end=' ')