num = int(input())

for i in range(num):
    n = list(format(int(input()), 'b'))
    n.reverse()
    for j in range(len(n)):
        if n[j] == '1':
            print(j, end=' ')