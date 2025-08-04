n = int(input())

count = 1  # n일 경우가 포함되기 때문에 처음부터 +1을 하고 시작

start_idx = 1
end_idx = 1

sum = 1  # 1부터 시작하기 때문에

while end_idx != n:
  if sum == n:
    count += 1
    end_idx += 1
    sum += end_idx
  elif sum > n:
    sum -= start_idx
    start_idx += 1
  elif sum < n:
    end_idx += 1
    sum += end_idx

print(count)