# 좋은 단어

n = int(input())
cnt = 0
for _ in range(n):
  s = input()
  stack = []
  isGood = True

  if len(s) % 2 == 1:
    isGood = False
  else:
    for i in range(0, len(s)):
      if len(stack) == 0:
        stack.append(s[i])
      elif s[i] == stack[-1]:
        stack.pop()
      else:
        stack.append(s[i])
    if stack:
      isGood = False
  
  if isGood:
    cnt += 1
print(cnt)