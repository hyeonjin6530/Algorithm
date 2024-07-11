x, y, width, height = map(int, input().split())

print(min(x, y, width-x, height-y))