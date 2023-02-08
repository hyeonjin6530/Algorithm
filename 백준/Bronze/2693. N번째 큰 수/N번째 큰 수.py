n = int(input())

for i in range(n):
    numlist = list(map(int, input().split()))
    numlist.sort(reverse=True)
    print(numlist[2])