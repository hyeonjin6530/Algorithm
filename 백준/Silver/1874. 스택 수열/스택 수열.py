import sys

input = sys.stdin.readline

n = int(input())

seq = []  # 문제에서 제시한 수열 저장
stack = []  # 리스트로 stack 구현
result = []  # +, - 출력 저장
count = 1  # stack에 몇 번째 숫자까지 넣었는지 확인하기 위해서
temp = True  # 해당 수열을 만들 수 있는지 없는지 여부

for i in range(n):
    seq.append(int(input()))

for i in seq:
    while count <= i:  # count부터 i까지 stack에 push
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == i:  # stack의 맨 위가 i와 같으면 pop 
        stack.pop()
        result.append("-")
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in result:
        print(i)
