num, prize = map(int, input().split())

grade = list(map(int, input().split()))

grade.sort(reverse=True)

print(grade[prize-1])