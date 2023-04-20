# Digit sum(D3)

tc = int(input())
res = []
for t in range(1, tc + 1):
  n = int(input())

  while True:
    sum = 0
    if len(str(n)) == 1:
      break
    for i in range(len(str(n))):
      sum += int(str(n)[i])
    n = sum

  res.append(n)

for t in range(1, tc + 1):
  print('#{} {}'.format(t, res[t - 1]))