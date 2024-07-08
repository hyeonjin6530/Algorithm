import sys

credit_sum = 0.0
total = 0.0  # 전공과목별(학점*과목평점)의 합

for i in range(20):
    subject, credit, grade = sys.stdin.readline().split()
    if grade != 'P':
        credit_sum += float(credit)

        if grade == 'A+': grade = 4.5
        elif grade == 'A0': grade = 4.0
        elif grade == 'B+': grade = 3.5
        elif grade == 'B0': grade = 3.0
        elif grade == 'C+': grade = 2.5
        elif grade == 'C0': grade = 2.0
        elif grade == 'D+': grade = 1.5
        elif grade == 'D0': grade = 1.0
        elif grade == 'F': grade = 0.0

        total += float(credit) * float(grade)

print(round(total / credit_sum, 6))
