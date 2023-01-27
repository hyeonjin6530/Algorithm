m = int(input())
n = int(input())
numlist = []

for i in range(m, n+1):
    if int(i**0.5) ** 2 == i:  # 제곱근의 정수형의 제곱이 원래 수와 같을 때, 이 수는 완전 제곱근이다.
        numlist.append(i)

if len(numlist) == 0:
    print("-1")
else:
    print(sum(numlist))
    print(min(numlist))
