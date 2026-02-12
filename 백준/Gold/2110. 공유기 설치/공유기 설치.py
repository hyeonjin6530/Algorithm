n, c = map(int, input().split())

house = [int(input()) for _ in range(n)]
house.sort() # 사용하기 쉽도록 정렬

# 공유기의 최소 거리
start = 1

# 공유기의 최대 거리 (마지막 집 - 첫번째 집)
end = house[-1] - house[0]

# 정답
answer = 0

# 공유기의 거리로 이분탐색 진행
while (start <= end):
  # 공유기 사이 최소 거리 후보
  mid = (start + end) // 2

  # 마지막으로 공유기가 설치된 집
  last = house[0]

  # 공유기의 개수
  count = 1

  # 공유기를 몇 대 설치할 수 있는지 체크하면서 공유기 설치
  for i in range(1, n):
    if house[i] - last >= mid:
      count += 1
      last = house[i]
  
  if count >= c:
    answer = mid
    start = mid + 1
  else:
    end = mid -1

print(answer)