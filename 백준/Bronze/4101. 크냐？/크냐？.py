# 딕셔너리는 중괄호 안에 값:값
# 리스트는 대괄호

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    elif a > b:
        print("Yes")
    else:
        print("No")
