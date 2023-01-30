num = int(input())

numbers = list(map(int, input().split()))

print(numbers.count(int(input())))  # 리스트.count(요소)는 리스트 속에서 해당되는 요소의 개수를 세준다.