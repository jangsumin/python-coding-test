# 세제곱근을 찾아라(D3)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())

  i = 1
  res = 0
  while True:
    if i * i * i == n:
      res = i
      break
    if i * i * i > n:
      res = -1
      break
    i += 1
  
  print(f'#{t} {res}')