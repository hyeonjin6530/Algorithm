n = int(input())
people = []

for i in range(n):
    age, name = input().split()
    people.append((int(age), name))

people = sorted(people, key = lambda x : x[0])
# lambda 함수를 이용하여 해당 조건으로만 정렬할 수 있다.

for i in people:
    print(i[0], i[1])