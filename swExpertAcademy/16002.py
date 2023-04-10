# 합성수 방정식(D3)

import math
tc = int(input())
for tc_num in range(1, tc + 1):
  n = int(input())

  y = 2
  x = y + n
  while True:
    i, j = 2, 2
    isSuccess_x, isSuccess_y = False, False
    while i <= math.sqrt(x):
      if x % i == 0:
        isSuccess_x = True
        break
      i += 1
    
    while j <= math.sqrt(y):
      if y % j == 0:
        isSuccess_y = True
        break
      j += 1
    
    if isSuccess_x and isSuccess_y:
      print('#' + str(tc_num) + ' ' + str(x) + ' ' + str(y))
      break

    x += 1
    y += 1