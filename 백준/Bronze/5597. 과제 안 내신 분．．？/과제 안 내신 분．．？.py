import sys

studentList = [i for i in range(1, 31)]

for i in range(28):
    studentList.remove(int(sys.stdin.readline()))

for i in studentList:
    print(i)