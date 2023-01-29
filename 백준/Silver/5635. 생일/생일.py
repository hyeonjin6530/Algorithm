num = int(input())
list = []

for i in range(num):
    n, d, m, y = input().split()
    d, m, y = map(int, (d, m, y))
    list.append((y, m, d, n))  # 순서대로 리스트에 저장

list.sort()  # 정렬

print(list[-1][3])  # 맨 뒤에 있는 것
print(list[0][3])
