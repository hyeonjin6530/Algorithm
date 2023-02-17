n = int(input())
dots = []

for i in range(n):
    a, b = map(int, input().split())
    dots.append((a, b))

dots.sort()

for i in range(len(dots)):
    print(dots[i][0], dots[i][1])
