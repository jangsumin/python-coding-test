# 수도 요금 경쟁(D2)

tc = int(input())
for t in range(1, tc + 1):
  p, q, r, s, w = map(int, input().split())
  a = p * w
  b = 0
  if w <= r:
    b = q
  else:
    b = q + (w - r) * s
  
  if a <= b:
    print(f'#{t} {a}')
  else:
    print(f'#{t} {b}')