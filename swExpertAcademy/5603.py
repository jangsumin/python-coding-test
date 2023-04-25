# 건초더미(D3)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  hays = []
  for _ in range(n):
    hays.append(int(input()))
  
  base = sum(hays) // len(hays)
  ans = 0
  for hay in hays:
    if hay > base:
      ans += hay - base
  
  print('#{} {}'.format(t, ans))