w_list = []
k_list = []

for i in range(20):
    if i < 10:
        w_list.append(int(input()))
    else:
        k_list.append(int(input()))

w_list.sort()
k_list.sort()

print(sum(w_list[7:]), sum(k_list[7:]))
    
