n, k = map(int, input().split())
num = [i for i in range(1, n+1)]  # 이렇게 한 줄로 정리할 수 있다.

result = []  # 요세푸스 순열을 저장할 리스트
index = 0  # num의 인덱스

for i in range(n):
    index += k-1  # 리스트의 인덱스는 0부터 시작하기 때문
    if index >= len(num):  # 만약 인덱스가 리스트의 범위를 벗어난다면
        index = index % len(num)  # 리스트의 길이에서 인덱스를 나눈 몫의 나머지를 인덱스로 선택한다.
    result.append(str(num.pop(index)))  # 그 과정에서 나온 값을 문자로 바꿔 결과 리스트에 저장한다.

print("<", ", ".join(result), ">", sep = '')
# sep = ''는 <, 숫자, > 사이의 공백을 없애주는 것이다.
 