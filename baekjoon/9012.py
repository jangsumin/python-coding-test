# 괄호

t = int(input())

for _ in range(t):
  stack = []
  ps = input()
  res = 'YES'

  for i in range(len(ps)):
    if ps[i] == '(':
      stack.append('(')
    
    if ps[i] == ')':
      if len(stack) == 0:
        res = 'NO'
      elif stack[-1] == '(':
        stack.pop()
      else:
        stack.append(ps[i])
  
  if len(stack) >= 1:
    res = 'NO'

  print(res)