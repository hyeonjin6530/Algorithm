word = input().upper()
max_word = ''
sum = 0

for i in set(word):  # 중복을 없애기 위해 set()
    n = word.count(i)
    if n > sum:
        sum = n
        max_word = i
    elif n == sum:
        max_word = "?"

print(max_word)



