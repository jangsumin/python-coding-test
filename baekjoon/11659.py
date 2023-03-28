# 구간 합 구하기 4

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 시간초과
# res = [0] * m
# ranges = []
# for _ in range(m):
#   i, j = map(int, input().split())
#   ranges.append([i, j])

# for i in range(1, n + 1):
#   for j in range(len(ranges)):
#     if i >= ranges[j][0] and i <= ranges[j][1]:
#       res[j] += arr[i - 1]

# for el in res:
#   print(el)

sum_list = [0]
total = 0
for i in range(len(arr)):
  total += arr[i]
  sum_list.append(total)

for _ in range(m):
  i, j = map(int, input().split())
  print(sum_list[j] - sum_list[i - 1])