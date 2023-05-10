# 숫자 배열 회전(D2)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  graph = [list(input().split()) for _ in range(n)]

  quarter_turn_graph = []
  for i in range(n):
    row = []
    for j in range(n):
      row.append(graph[j][i])
    row.reverse()
    quarter_turn_graph.append(row)
  
  half_turn_graph = []
  half_quarter_turn_graph = []
  for i in range(n):
    row1 = []
    row2 = []
    for j in range(n):
      row1.append(graph[i][j])
      row2.append(quarter_turn_graph[i][j])
    row1.reverse()
    row2.reverse()
    half_turn_graph.append(row1)
    half_quarter_turn_graph.append(row2)
  half_turn_graph.reverse()
  half_quarter_turn_graph.reverse()

  print(f'#{t}')
  for i in range(n):
    print(''.join(quarter_turn_graph[i]), end=' ')
    print(''.join(half_turn_graph[i]), end=' ')
    print(''.join(half_quarter_turn_graph[i]))