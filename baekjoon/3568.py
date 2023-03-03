# iSharp
# 시뮬레이션

info = list(map(str, input().split()))

for i in range(1, len(info)):
  info[i] = info[i][0 : -1]

for i in range(1, len(info)):
  s = info[0]
  var = ''
  reverse_list = list(reversed(list(info[i][0 : ])))
  for el in reverse_list:
    if el == '&':
      s += '&'
    elif el == ']':
      s += '[]'
    elif el == '*':
      s += '*'
    elif el == '[':
      continue
    else:
      var += el
  s += ' ' + ''.join(list(reversed(list(var)))) + ';'
  print(s)