num = int(input())

for i in range(num):
    a = 0  # 근우의 총 학점
    b = 0  # 근우의 총 평점
    subject = int(input())
    for j in range(subject):
        score, grade = map(float, input().split())
        a += score
        b += grade * score
    print(int(a), '%.1f' %(b/a) )  # 소수점 한 자리까지 나타내기 위해서 %.1f 사용