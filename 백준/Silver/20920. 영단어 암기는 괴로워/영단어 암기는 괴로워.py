import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())

words = []
for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

most_common = Counter(words).most_common()

for i in range(len(most_common)):
    most_common[i] = list(most_common[i])
    most_common[i].append(len(most_common[i][0]))

most_common = sorted(most_common, key=lambda x: (-x[1], -x[2], x[0]))

for i in range(len(most_common)):
    print(most_common[i][0])