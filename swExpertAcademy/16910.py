# 원 안의 점(D3)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  cnt = 0
  for i in range(-1 * n, n + 1):
    for j in range(-1 * n, n + 1):
      if i ** 2 + j ** 2 <= n ** 2:
        cnt += 1
  
  print(f'#{t} {cnt}')