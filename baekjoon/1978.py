# 소수 찾기

import math

n = int(input())
arr = list(map(int, input().split()))

cnt = n
for num in arr:
  if num == 1:
    cnt -= 1
  i = 2
  while i <= math.floor(num / 2):
    if num % i == 0:
      cnt -= 1
      break
    i += 1

print(cnt)