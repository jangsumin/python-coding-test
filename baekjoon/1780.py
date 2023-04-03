# 종이의 개수

n = int(input())

graph = []
for _ in range(n):
  row = list(map(int, input().split()))
  graph.append(row)

result = {-1: 0, 0: 0, 1: 0}

def divide(row, col, n):
  curr = graph[row][col]

  for i in range(row, row + n):
    for j in range(col, col + n):
      if graph[i][j] != curr:
        next = n // 3
        divide(row, col, next)
        divide(row, col + next, next)
        divide(row, col + next * 2, next)
        divide(row + next, col, next)
        divide(row + next, col + next, next)
        divide(row + next, col + next * 2, next)
        divide(row + next * 2, col, next)
        divide(row + next * 2, col + next, next)
        divide(row + next * 2, col + next * 2, next)
        return
  
  result[curr] += 1
  return

divide(0, 0, n)

for value in result.values():
  print(value)