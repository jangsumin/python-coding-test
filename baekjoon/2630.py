# 색종이 만들기

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

# 분할 정복
res = [0, 0]
def devided(x, y, n):
  curr = graph[x][y]

  for i in range(x, x + n):
    for j in range(y, y + n):
      if graph[i][j] != curr:
        next = n // 2
        devided(x, y, next)
        devided(x, y + next, next)
        devided(x + next, y, next)
        devided(x + next, y + next, next)
        return
  res[curr] += 1

devided(0, 0, n)
for el in res:
  print(el)