# 구구단2(D3)

tc = int(input())
for t in range(1, tc + 1):
  a, b = map(int, input().split())
  if a >= 10 or b >= 10:
    print(f'#{t} -1')
  else:
    print(f'#{t} {a * b}')