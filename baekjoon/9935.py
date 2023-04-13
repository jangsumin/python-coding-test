# 문자열 폭발

# import time
# start_time = time.time()
s = input()
bomb = input()

# 시간 초과
# ds = len(s)
# while True:
#   s = ''.join(s.split(bomb))
#   if len(s) == ds:
#     break
#   ds = len(s)

# if s == '':
#   print('FRULA')
# else:
#   print(s)

stack = []
bomb_len = len(bomb)
for i in range(len(s)):
  stack.append(s[i])
  if ''.join(stack[-bomb_len:]) == bomb:
    for _ in range(bomb_len):
      stack.pop()

if stack:
  print(''.join(stack))
else:
  print('FRULA')

# end_time = time.time()
# print(f'걸린 시간: {end_time - start_time}')