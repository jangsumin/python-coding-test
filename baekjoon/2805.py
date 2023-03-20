# 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 시간 초과 코드
# max_tall = max(trees)
# while True:
#   sum = 0
#   for tree in trees:
#     if tree - max_tall <= 0:
#       continue
#     else:
#       sum += tree - max_tall
#   if sum == m:
#     break
#   max_tall -= 1

# print(max_tall)

max_tall = max(trees)
start, end = 1, max_tall

while start <= end:
  mid = (start + end) // 2
  sum = 0
  for tree in trees:
    if tree - mid <= 0:
      continue
    else:
      sum += tree - mid
  
  if sum >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)