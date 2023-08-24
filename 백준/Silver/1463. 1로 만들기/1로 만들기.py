# 다이나믹 프로그래밍을 이용(모든 가능성을 두고 그 안의 최솟값 찾기)
# +) 그리디 알고리즘은 내가 생각한 최적의 방법이 끝까지 반례 없이 적용되는 경우에 이용한다.
import sys

num = int(sys.stdin.readline())
dynamic = [0] * (num + 1)

for i in range(2, num + 1):  # 2부터 num까지 반복
    dynamic[i] = dynamic[i - 1] + 1  # 1을 빼는 연산을 1회 진행
    if i % 3 == 0:
        dynamic[i] = min(dynamic[i], dynamic[i // 3] + 1)
    if i % 2 == 0:
        dynamic[i] = min(dynamic[i], dynamic[i // 2] + 1)

print(dynamic[num])
