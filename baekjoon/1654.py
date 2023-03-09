# 랜선 자르기

k, n = map(int, input().split())

group = []
for _ in range(k):
  group.append(int(input()))

start, end = 1, max(group)
while start <= end:
  mid = (start + end) // 2
  cnt = 0
  for num in group:
    cnt += num // mid
  
  if cnt >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)