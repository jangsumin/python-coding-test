# 모음의 개수

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
  cnt = 0
  s = input()
  if s == '#':
    exit(0)
  
  for alphabet in s:
    if alphabet in vowel:
      cnt += 1

  print(cnt)