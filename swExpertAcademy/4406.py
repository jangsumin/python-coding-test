# 모음이 보이지 않는 사람

tc = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(1, tc + 1):
  s = input()
  new_s = ''
  for alphabet in s:
    if alphabet not in vowel:
      new_s += alphabet
  print(f'#{i} {new_s}')