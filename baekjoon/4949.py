# 균형잡힌 세상

while True:
  s = input()
  if s == '.':
    break

  arr = list()
  for i in range(len(s)):
    if s[i] == '[':
      arr.append('[')
    if s[i] == '(':
      arr.append('(')
    if s[i] == ')':
      if len(arr) == 0:
        arr.append(')')
      
      if arr[-1] == '(':
        arr.pop()
      else:
        arr.append(')')
    if s[i] == ']':
      if len(arr) == 0:
        arr.append(']')
        
      if arr[-1] == '[':
        arr.pop()
      else:
        arr.append(']')
    
  if len(arr) == 0:
    print('yes')
  else:
    print('no')