# 소수

import math
m = int(input())
n = int(input())

prime_list = list()
for num in range(m, n + 1):
  i = 2
  isPrime = True
  
  if num == 1:
    isPrime = False

  while i <= math.floor(num ** 0.5):
    if num % i == 0:
      isPrime = False
      break
    i += 1

  if isPrime == True:
    prime_list.append(num)

if len(prime_list) == 0:
  print(-1)
else:
  print(sum(prime_list))
  print(min(prime_list))