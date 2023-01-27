num = int(input())

for i in range(1, num+1):
    print("*"*i + " "*(2*(num-i)) + "*"*i)

for i in reversed(range(1, num)):
    print("*"*i + " "*(2*(num-i)) + "*"*i)