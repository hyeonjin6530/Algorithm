s, p = map(int, input().split())

data = input()

a, c, g, t = map(int, input().split())

answer = 0

start = 0
end = p-1

# 딕셔너리 사용하기 (key와 value를 사용하기 위함)
dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# 검사할 윈도우 구간
target = data[start : end]

for item in target:
  dict[item] += 1 # 여기서 p-2까지 계산함

# 슬라이딩 윈도우
while end < s:
  dict[data[end]] += 1  # 여기서 p-1을 계산해줌

  # 유효성 검사
  if dict['A'] >= a and dict['C'] >= c and dict['G'] >= g and dict['T'] >= t:
    answer += 1
  
  dict[data[start]] -= 1 # 맨 왼쪽 문자열 제거
  start += 1
  end += 1

print(answer)