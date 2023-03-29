# 누울 자리를 찾아라

n = int(input())
space = []
for _ in range(n):
  space.append(list(map(str, input())))

res_hori = []
res_vert = []
for i in range(n):
  cnt_hori = 0
  cnt_vert = 0
  for j in range(n):
    if space[i][j] == '.':
      cnt_hori += 1
    if space[i][j] == 'X':
      res_hori.append(cnt_hori)
      cnt_hori = 0
    if space[j][i] == '.':
      cnt_vert += 1
    if space[j][i] == 'X':
      res_vert.append(cnt_vert)
      cnt_vert = 0
  res_hori.append(cnt_hori)
  res_vert.append(cnt_vert)
  cnt_hori = 0
  cnt_vert = 0
  
result = 0
for el in res_hori:
  if el >= 2:
    result += 1
print(result, end=' ')
result = 0
for el in res_vert:
  if el >= 2:
    result += 1
print(result)