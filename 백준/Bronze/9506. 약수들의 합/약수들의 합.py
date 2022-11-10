while(True):
    list = []
    num = int(input())

    if num == -1:
        break

    for i in range(1, num):
        if num % i == 0:
            list.append(i) 

    if num == sum(list):
        print(num, "=", " + ".join(map(str,list)))
        #  list의 요소가 int형이라서 join하면 오류가 나므로 map을 통해 list를 str로 바꿔준다.
    else:
        print(num, "is NOT perfect.")