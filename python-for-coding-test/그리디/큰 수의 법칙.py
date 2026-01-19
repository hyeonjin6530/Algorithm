n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

result = nums[-1]*(m - (m%k)) + nums[-2]*(m%k)

print(result)