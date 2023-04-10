# 구구단 걷기(D3)

import math
tc = int(input())
for i in range(1, tc + 1):
  num = int(input())

  j = 2
  tmp = 1
  while j <= math.sqrt(num):
    if num % j == 0:
      tmp = j
    j += 1
  
  result = num // tmp + tmp - 2
  print(f'#{i} {result}')