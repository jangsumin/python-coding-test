# 간단한 압축 풀기(D2)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  s = ''
  for _ in range(n):
    c, k = map(str, input().split())
    s += c * int(k)
  
  i = 0
  print(f'#{t}')
  for i in range(0, len(s) // 10 + 1):
    print(s[(i * 10) : (i * 10) + 10])