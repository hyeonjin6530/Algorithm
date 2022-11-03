n = int(input())

for i in range(n):
    num, s = input().split()
    p = ""
    for j in s:
        p += j*int(num)
    print(p)
