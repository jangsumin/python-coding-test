# 일요일(D3)

tc = int(input())
for t in range(1, tc + 1):
  s = str(input())

  res = 0
  if s == 'SUN':
    res = 7
  if s == 'SAT':
    res = 1
  if s == 'FRI':
    res = 2
  if s == 'THU':
    res = 3
  if s == 'WED':
    res = 4
  if s == 'TUE':
    res = 5
  if s == 'MON':
    res = 6

  print(f'#{t} {res}')