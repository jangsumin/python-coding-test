# 단지번호붙이기

# 입력
n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y, graph):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False
  if graph[x][y] == 1:
    global cnt
    cnt += 1
    graph[x][y] = 0
    dfs(x + 1, y, graph)
    dfs(x - 1, y, graph)
    dfs(x, y + 1, graph)
    dfs(x, y - 1, graph)
    return True
  return False

cnt = 0
arr = []
result = 0
for i in range(n):
  for j in range(n):
    if dfs(i, j, graph) == True:
      result += 1
      arr.append(cnt)
      cnt = 0

arr.sort()
print(result)
for num in arr:
  print(num)