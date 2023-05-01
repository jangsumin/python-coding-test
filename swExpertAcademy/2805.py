# 농작물 수확하기

tc = int(input())

for t in range(1, tc + 1):
  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input())))
  
  total = 0
  pattern = [1 + (2 * i) for i in range(n // 2 + 1)]
  pattern = pattern + list(reversed(pattern))[1:]

  for i in range(n):
    total += sum(graph[i][n // 2 - (pattern[i] // 2) : n // 2 + (pattern[i] // 2) + 1])
  
  print(f'#{t} {total}')