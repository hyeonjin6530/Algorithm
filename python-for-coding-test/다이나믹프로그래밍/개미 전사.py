# 바텀업
# 점화식: ai = max(ai-1, ai-2 + k)
n = int(input())

storage = list(map(int, input().split()))

# 계산된 결과를 저장하기 위한 dp table
d = [0] * 100

d[0] = storage[0]
d[1] = max(storage[0], storage[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + storage[i])

print(d[n-1])