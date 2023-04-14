# 베르트랑 공준

import math

# 에라토스테네스의 체 활용
limit = 123456
isPrime = [True] * (2 * limit + 1)
isPrime[0] = 0
isPrime[1] = 0

for i in range(2, int(math.sqrt(len(isPrime)))):
  if isPrime[i]:
    for j in range(i + i, len(isPrime), i):
      isPrime[j] = False

while True:
  n = int(input())
  if n == 0:
    exit(0)
  else:
    print(sum(isPrime[n + 1: 2 * n + 1]))

  # 시간 초과
  # start = n + 1
  # end = 2 * n
  # cnt = 0
  # while start <= end:
  #   i = 2
  #   isPrime = True
  #   while i <= math.pow(start, 1 / 2):
  #     if start % i == 0:
  #       isPrime = False
  #       break
  #     i += 1
  #   if isPrime:
  #     cnt += 1
  #   start += 1
  
  # print(cnt)