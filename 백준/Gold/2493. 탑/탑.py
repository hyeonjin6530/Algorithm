import sys

input = sys.stdin.readline

n = int(input())  # 탑의 개수

top_list = list(map(int, input().split()))  # 입력에서 받아올 탑 리스트
stack = []  # 최댓값을 저장할 스택
answer = []  # 수신탑 인덱스 저장 (출력할 것을 저장하는 리스트임)

for i in range(n):
    while stack:  # 스택이 비어있지 않을 때
        if stack[-1][1] > top_list[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0])
            break
        else:  # 다음에 오는 탑이 stack의 마지막 탑 보다 높을 때
            stack.pop()
    if not stack:  # 스택이 비어있을 때
        answer.append(0)  # 레이저를 수신할 탑이 없음

    stack.append([i + 1, top_list[i]])


print(" ".join(map(str, answer)))
