n = int(input())

for i in range(1, n+1):
    num = list(map(int, input().split()))
    student = num[0]
    score = list(num[1:])

    gap = 0
    score.sort(reverse=True)  # 점수 차이를 구하기 위해 내림차순 정렬
    for j in range(len(score)-1):
        if gap < (score[j] - score[j+1]):
            gap = score[j] - score[j+1]

    print("Class", i)
    print("Max {0}, Min {1}, Largest gap {2}".format(max(score), min(score), gap))