num = int(input())
result = list(map(int, input().split()))
count = 0  # 연속적으로 문제의 답이 맞는 경우
score = 0  # 최종 점수

for i in result:
    if i == 1:
        count += 1  # 정답을 연속으로 맞추면 count가 올라간다.
        score += count
    else:
        count = 0  # 정답을 맞추지 못할 경우 count는 0이 된다.

print(score)