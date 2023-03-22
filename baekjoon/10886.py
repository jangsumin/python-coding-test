# 0 = not cute / 1 = cute

n = int(input())
zero_cnt = 0
one_cnt = 0
for _ in range(n):
  input_value = int(input())
  if input_value == 1:
    one_cnt += 1
  if input_value == 0:
    zero_cnt += 1

if zero_cnt > one_cnt:
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')