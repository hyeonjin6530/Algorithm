while True:
    word = input()
    if word == 'END':  # 만약 END를 입력 받는다면
        break  # while문을 탈출해라
    word = "".join(reversed(word))  # reversed를 하고 join을 해줘야한다.
    print(word)