# 아스키코드에서 대문자는 65~90

n = int(input())

for i in range(n):
    a, b = map(list, input().split())
    print("Distances: " , end='')
    for j in range(len(a)):
        if ord(a[j]) <= ord(b[j]):
            print( ord(b[j]) - ord(a[j]) , end=' ')
        else:
            print( (ord(b[j])+26) - ord(a[j]) , end=' ')
        if j == len(a)-1:
            print('\n', end='')