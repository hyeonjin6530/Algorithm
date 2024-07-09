import sys

words = []
max_len = 0

for i in range(5):
    word = sys.stdin.readline().strip()  # 개행 문자 제거
    if max_len <= len(word):
        max_len = len(word)
    words.append(word)

for i in range(max_len):
    for j in range(5):
        if len(words[j]) > i:
            print(words[j][i], end="")
        else:
            pass