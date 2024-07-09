paper = [[0]*100 for j in range(100)]
result = 0

num = int(input())

for i in range(num):
    left, bottom = map(int, input().split())
    for j in range(left, left+10):
        for k in range(bottom, bottom+10):
            paper[j][k] = 1
        

for i in range(100):
    result += paper[i].count(1)

print(result)


