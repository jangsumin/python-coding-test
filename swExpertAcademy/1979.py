# 어디에 단어가 들어갈 수 있을까(D2)

tc = int(input())
for t in range(1, tc + 1):
  m, k = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(m)]
  
  cnt = 0
  for i in range(m):
    row_cnt = 0
    column_cnt = 0
    for j in range(m):
      if graph[i][j] == 1:
        row_cnt += 1
      if graph[j][i] == 1:
        column_cnt += 1
      if graph[i][j] == 0:
        if row_cnt == k:
          cnt += 1
        row_cnt = 0
      if graph[j][i] == 0:
        if column_cnt == k:
          cnt += 1
        column_cnt = 0
    
    if row_cnt == k:
      cnt += 1
    if column_cnt == k:
      cnt += 1
  
  print(f'#{t} {cnt}')