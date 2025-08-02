n = int(input())

scores = list(map(int, input().split()))

high_score = max(scores)

sum_score = sum(scores)

print(sum_score/high_score*100/len(scores))