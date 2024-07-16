n, m = map(int, input().split())
count = 0

words_list = [input() for _ in range(n)]

search_list = [input() for _ in range(m)]

for word in search_list:
    if word in words_list:
        count += 1

print(count)