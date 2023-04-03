# 연결 요소의 개수

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
  start, end = map(int, input().split())
  graph[start - 1].append(end)
  graph[end - 1].append(start)

visited = [False] * n
cnt = 0

def dfs(v):
  if visited[v - 1] == True:
    return False
  visited[v - 1] = True
  for node in graph[v - 1]:
    if visited[node - 1] == False:
      dfs(node)
  return True

for i in range(1, n + 1):
  if dfs(i) == True:
    cnt += 1

print(cnt)