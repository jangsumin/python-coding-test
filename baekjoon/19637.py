# IF문 좀 대신 써줘

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
info = []

for i in range(n):
  name, high_value = map(str, input().split())
  info.append([name, int(high_value)])

for _ in range(m):
  ad = int(input())
  
  start = 0
  end = n - 1
  mid = (start + end) // 2
  while start <= end:
    if ad > info[mid][1]:
      start = mid + 1
    else:
      end = mid - 1
    mid = (start + end) // 2
  mid = start

  print(info[mid][0])