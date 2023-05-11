# 달팽이 숫자(D2)

def isValid(row, col):
  if row >= 0 and row < n and col >= 0 and col < n:
    return True
  return False

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  graph = [[0] * n for _ in range(n)]
  
  # 오른, 아래, 왼, 위
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  row_num, col_num = 0, -1
  # 오른: 0, 아래: 1, 왼: 2, 위: 3
  direction = 0

  i = 1
  while i <= n * n:
    row_num += dx[direction]
    col_num += dy[direction]

    while(isValid(row_num, col_num) and graph[row_num][col_num] == 0):
      graph[row_num][col_num] = i
      row_num += dx[direction]
      col_num += dy[direction]
      i += 1
    
    row_num -= dx[direction]
    col_num -= dy[direction]

    direction = (direction + 1) % 4
  
  print(f'#{t}')
  for row in graph:
    print(*row)