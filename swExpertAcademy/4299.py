# 태혁이의 사랑은 타이밍(D3)

tc = int(input())
for i in range(1, tc + 1):
  d, h, m = map(int, input().split())

  res = 0
  absol_time = d * 24 * 60 + h * 60 + m
  base_time = 11 * 24 * 60 + 11 * 60 + 11

  if absol_time - base_time < 0:
    print(f'#{i} -1')
  else:
    print(f'#{i} {absol_time - base_time}')