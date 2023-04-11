# Sum

for _ in range(10):
  tc = int(input())
  graph = []
  for _ in range(100):
    graph.append(list(map(int, input().split())))
  group_sum = []
  
  sum_cross1 = 0
  sum_cross2 = 0
  for j in range(100):
    sum_row = 0
    sum_column = 0
    for k in range(100):
      sum_row += graph[j][k]
      sum_column += graph[k][j]
      if j == k:
        sum_cross1 += graph[j][k]
      if j + k == 4:
        sum_cross2 += graph[j][k]
    group_sum.append(sum_row)
    group_sum.append(sum_column)
  group_sum.append(sum_cross1)
  group_sum.append(sum_cross2)
  print(f'#{tc} {max(group_sum)}')