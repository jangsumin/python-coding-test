# 단어 뒤집기

t = int(input())
s_arr = []
for _ in range(t):
  s_arr.append(input())

for s in s_arr:
  new_s = ''
  for word in s.split(' '):
    new_s += word[::-1]
    new_s += ' '
  print(new_s[0:-1])