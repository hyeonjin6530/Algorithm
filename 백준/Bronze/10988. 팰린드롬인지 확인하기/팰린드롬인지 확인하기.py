word = input()

if word == "".join(reversed(word)):
    print(1)
else:
    print(0)