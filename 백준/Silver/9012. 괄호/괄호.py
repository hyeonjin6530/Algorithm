t = int(input())
for i in range(t):
    ps = []
    n = input()
    for j in n:
        if j == ')':
            if len(ps) != 0:
                ps.pop()
            else:
                print('NO')
                break
        elif j == '(':
            ps.append(j)
    else:
        if len(ps) == 0:
            print('YES')
        else:
            print('NO')