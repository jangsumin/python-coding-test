# !밀비 급일

while True:
  s = list(input())
  if ''.join(s) == 'END':
    exit(0)
  s.reverse()
  print(''.join(s))