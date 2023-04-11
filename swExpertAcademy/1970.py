# 쉬운 거스름돈(D2)

tc = int(input())
rests = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(1, tc + 1):
  n = int(input())
  result = []
  for rest in rests:
    result.append(n // rest)
    n -= (n // rest) * rest
  print(f'#{i}')
  print(*result)