import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

most_common = Counter(numbers).most_common()

print(int(round(sum(numbers) / n, 0)))
print(numbers[n//2])
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print(most_common[1][0])
else: print(most_common[0][0])
print(max(numbers) - min(numbers))