def rev(a):
    a = "".join(reversed(a))
    return int(a)

x, y = input().split()
print(rev(str(rev(x)+rev(y))))
