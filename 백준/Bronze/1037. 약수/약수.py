num = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

print(numbers[0]*numbers[num-1])  # 가장 작은 수 * 가장 큰 수 = N이 된다.
