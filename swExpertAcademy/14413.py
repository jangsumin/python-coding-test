# 격자판 칠하기(D3)

t = int(input())
for i in range(1, t + 1):
  n, m = map(int, input().split())
  graph = []
  for j in range(n):
    row = list(input())
    graph.append(row)
  
  board = [0, 0, 0, 0]
  for x in range(n):
    for y in range(m):
      if graph[x][y] == '#':
        if (x + y) % 2 == 0:
          board[0] += 1
        else:
          board[1] += 1
      
      elif graph[x][y] == '.':
        if (x + y) % 2 == 0:
          board[2] += 1
        else:
          board[3] += 1
  
  isPossible = True
  if (board[0] != 0 and board[1] != 0) or (board[0] != 0 and board[2] != 0) or (board[2] != 0 and board[3] != 0) or (board[1] != 0 and board[3] != 0):
    isPossible = False
      
  if isPossible:
    print(f'#{i} possible')
  else:
    print(f'#{i} impossible')