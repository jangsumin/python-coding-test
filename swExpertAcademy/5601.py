# 쥬스 나누기(D3)

tc = int(input())
for i in range(1, tc + 1):
  n = int(input())
  print(f'#{i} ', end='')
  for _ in range(n):
    print(f'{1}/{n}', end=' ')
  print()