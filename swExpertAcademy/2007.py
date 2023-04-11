# 패턴 마디의 길이(D2)

tc = int(input())
for i in range(1, tc + 1):
  s = input()

  j = 1
  while True:
    if s[0:j] == s[j:2 * j]:
      break
    j += 1
  print(f'#{i} {j}') 