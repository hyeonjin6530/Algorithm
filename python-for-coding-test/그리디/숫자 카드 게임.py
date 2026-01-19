n, m = map(int, input().split())

nums = []

for i in range(n):
  nums.append(min(list(map(int, input().split()))))

print(max(nums))
