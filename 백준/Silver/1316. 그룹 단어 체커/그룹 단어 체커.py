num = int(input())
count = 0

for n in range(num):
    word = input()
    error = 0  # 겹치는 문자가 나오는 횟수
    for i in range(len(word)-1):  # 인덱스 번호는 0부터 문자수-1까지
        if word[i] != word[i+1]:  # 현재 문자가 다음 문자와 다를 때
            words = word[i+1:]  # 현재 문자를 제외한 문자열을 words에 대입한다.
            if words.count(word[i]) > 0:  # 만약 현재 문자가 words라는 문자열에 1개 이상 있다면
                error += 1  # error가 증가한다 -> 그룹문자가 아닌거임
    if error == 0:  # 만약 error가 0이라면
        count += 1  # 이 문자열은 그룹 단어이다.



print(count)

