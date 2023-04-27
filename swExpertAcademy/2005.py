# 파스칼의 삼각형(D2)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  i = 1

  res = [[1], [1, 1]]
  i = 2
  while i <= 10:
    res.append([1])
    for j in range(0, i - 1):
      res[i].append(res[i - 1][j] + res[i - 1][j + 1])
    res[i].append(1)
    i += 1
  
  print(f'#{t}')
  for j in range(0, n):
    print(*res[j])