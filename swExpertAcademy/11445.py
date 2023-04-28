# 무한 사전(D3)

tc = int(input())
for t in range(1, tc + 1):
  p = input().rstrip()
  q = input().rstrip()
  if q == p + 'a' or q == p[0:-1]:
    print(f'#{t} N')
  else:
    print(f'#{t} Y')