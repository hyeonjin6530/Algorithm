score = 0
winner = 0

for i in range(1, 6):
    a = sum(map(int, input().split()))
    if score < a:
        score = a
        winner = i

print(winner, score)
