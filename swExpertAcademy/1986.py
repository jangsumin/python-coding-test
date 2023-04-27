# 지그재그 숫자(D2)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())

  sum = 0
  for i in range(1, n + 1):
    if i % 2 == 1:
      sum += i
    else:
      sum -= i
  
  print(f'#{t} {sum}')