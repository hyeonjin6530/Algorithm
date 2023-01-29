n, k = map(int, input().split())
num = []  # n의 약수를 저장할 리스트

for i in range(1, n+1):
    if n % i == 0:
        num.append(i)

if len(num) >=k:
    print(num[k-1])
else:
    print("0")