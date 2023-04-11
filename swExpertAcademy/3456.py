# 직사각형 길이 찾기(D3)

tc = int(input())
for t in range(1, tc + 1):
  a, b, c = map(int, input().split())

  if a == b:
    print(f'#{t} {c}')
  elif a == c:
    print(f'#{t} {b}')
  elif b == c:
    print(f'#{t} {a}')