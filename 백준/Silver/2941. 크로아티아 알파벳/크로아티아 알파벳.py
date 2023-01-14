word = input()
count = 0

words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in words:
    word = word.replace(i, '*')  # 그 단어가 있으면 그 단어를 *로 대체한다.
print(len(word))  # 최종적으로 남은 문자열의 문자 수를 세면 된다.
