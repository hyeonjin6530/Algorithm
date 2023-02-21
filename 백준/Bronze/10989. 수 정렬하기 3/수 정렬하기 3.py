import sys

n = int(sys.stdin.readline())
number = [0]*10001 # 최대입력값+1 만큼의 리스트를 만들어둔다.

# for i in range(n):
#     number.append(int(sys.stdin.readline()))
# 이 코드는 메모리 재할당으로 인해 메모리를 효율적으로 사용하지 못한다.

for i in range(n):
    number[int(sys.stdin.readline())] += 1
    # 입력 받은 숫자에 해당되는 인덱스에 +1을 한다. (즉, 리스트를 정렬할 필요가 없어짐)

for i in range(len(number)):
    if number[i] != 0:
        for j in range(number[i]):
            print(i)
