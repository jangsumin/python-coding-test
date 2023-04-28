# 새로운 불면증 치료법(D2)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  num_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
  i = 1
  while True:
    if len(num_set) == 0:
      break
    for el in str(n * i):
      num_set.discard(el)
    i += 1
  
  print(f'#{t} {(i - 1) * n}')