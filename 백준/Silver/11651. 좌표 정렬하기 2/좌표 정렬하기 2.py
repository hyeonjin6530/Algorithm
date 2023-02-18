n = int(input())
dots = []

for i in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

sorted_dots = sorted(dots, key = lambda a : (a[1], a[0]))

for i in range(len(dots)):
    print(sorted_dots[i][0], sorted_dots[i][1])
