# 뜨거운 붕어빵

n, m = map(int, input().split())
graph = []
for _ in range(n):
  row = list(input())
  row.reverse()
  graph.append(row)

for i in range(n):
  print(''.join(graph[i]))