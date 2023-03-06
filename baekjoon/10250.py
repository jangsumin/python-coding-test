# ACM 호텔

import math

t = int(input())
for _ in range(t):
  h, w, nth = map(int, input().split())
  if nth % h == 0:
    ans = h * 100 + math.ceil((nth / h))
  else:
    ans = (nth % h) * 100 + math.ceil((nth / h))
  print(ans)