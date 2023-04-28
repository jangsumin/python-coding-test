# 제곱수 만들기(D3)

prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
  isPrime = True
  for p in prime:
    if i % p == 0:
      isPrime = False
      break
  if isPrime:
    prime.append(i)

tc = int(input())
answer = []
for t in range(1, tc + 1):
  a = int(input())
  res = 1
  if (a ** 0.5) != int(a ** 0.5):
    for p in prime:
      cnt = 0
      while a % p == 0:
        a //= p
        cnt += 1
      if cnt % 2:
        res *= p
      if a == 1 or p > a:
        break
    if a > 1:
      res *= a
  answer.append(res)

for t in range(1, tc + 1):
  print(f'#{t} {answer[t - 1]}')