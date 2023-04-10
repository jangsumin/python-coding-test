# 1차원 정원(D3)

tc = int(input())
for i in range(1, tc + 1):
  n, d = map(int, input().split())
  dist = d * 2 + 1
  if n % dist == 0:
    print(f'#{i} {n // dist}')
  else:
    print(f'#{i} {n // dist + 1}')