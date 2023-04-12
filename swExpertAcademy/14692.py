# 통나무 자르기(D3)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  if n % 2 == 1:
    print(f'#{t} Bob')
  else:
    print(f'#{t} Alice')