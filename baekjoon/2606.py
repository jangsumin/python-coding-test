# 바이러스

# 입력
computers = int(input())
connections = int(input())
graph = []
for _ in range(connections):
  graph.append(list(map(int, input().split())))

visited = [0] * (computers + 1)
result = 0

def dfs(visited, v, graph):
  visited[v] = 1
  for connection in graph:
    if connection[0] == v:
      if not visited[connection[1]]:
        dfs(visited, connection[1], graph)
    elif connection[1] == v:
      if not visited[connection[0]]:
        dfs(visited, connection[0], graph)

dfs(visited, 1, graph)
for i in range(len(visited)):
  if i != 1 and visited[i]:
    result += 1
print(result)