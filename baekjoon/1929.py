# 소수 구하기

m, n = map(int, input().split())

for num in range(m, n + 1):
  res = True
  if num == 1:
    res = False
  i = 2
  while i <= int(num ** 0.5):
    if num % i == 0:
      res = False
      break
    i += 1
  
  if res == True:
    print(num)