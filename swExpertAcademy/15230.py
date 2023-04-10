# 알파벳 공부(D3)

tc = int(input())
order = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1, tc + 1):
  s = input()
  j = 0
  while j <= len(s) - 1:
    if order[j] != s[j]:
      break
    j += 1
  print(f'#{i} {j}')