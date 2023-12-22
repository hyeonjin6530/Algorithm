n = list(map(int, input()))  # list에 넣으면 알아서 한 글자씩 분리해줌

num = [0] * 10

for i in n:
    if i == 9 or i == 6:
        if num[6] > num[9]:
            num[9] += 1
        else:
            num[6] += 1
    else:
        num[i] += 1

print(max(num))
