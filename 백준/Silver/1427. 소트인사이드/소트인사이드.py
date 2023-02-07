n = input()
n_list = []

for i in n:
    n_list.append(int(i))

n_list.sort(reverse = True)

print(''.join(map(str, n_list)))