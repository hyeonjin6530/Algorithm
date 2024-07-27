import sys
from collections import deque
input = sys.stdin.readline

num_data = int(input())
data_Structure = list(map(int, input().split()))
numbers = list(map(int, input().split()))
new_data = int(input())
new_numbers = list(map(int, input().split()))

q_list = deque(numbers[index] for index, value in enumerate(data_Structure) if value == 0)

for i in range(new_data):
    q_list.appendleft(new_numbers[i])
    print(q_list.pop(), end=' ')