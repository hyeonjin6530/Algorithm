h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

currentTime = (h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1)

if currentTime < 0:
    currentTime += 60 * 60 * 24  # 값이 음수라면 24시간을 더해준다.

h = currentTime//3600
m = (currentTime%3600)//60
s = currentTime%60

print("%02d:%02d:%02d" %(h, m, s))

