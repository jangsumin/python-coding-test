# 구구단 1(D3)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())

  res = 'No'
  for i in range(1, 10):
    if n % i == 0:
      if 1 <= (n // i) <= 9:
        res = 'Yes'
        break
  
  print(f'#{t} {res}')