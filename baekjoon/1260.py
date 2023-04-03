# DFS와 BFS

# 출력
n, m, v = map(int, input().split())

# BFS를 위한 라이브러리 import
from collections import deque

graph = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a - 1].append(b)
  graph[b - 1].append(a)

for conn in graph:
  conn.sort()

visited_dfs = [False] * n
res_dfs = []
def dfs(start):
  visited_dfs[start - 1] = True
  res_dfs.append(start)
  for node in graph[start - 1]:
    if visited_dfs[node - 1] == False:
      dfs(node)

visited_bfs = [False] * n
res_bfs = []
def bfs(start):
  queue = deque()
  queue.append(start)
  while queue:
    num = queue.popleft()
    visited_bfs[num - 1] = True
    res_bfs.append(num)
    for node in graph[num - 1]:
      if visited_bfs[node - 1] == False and node not in queue:
        queue.append(node)

dfs(v)
bfs(v)
for el in res_dfs:
  print(el, end = ' ')
print()
for el in res_bfs:
  print(el, end = ' ')