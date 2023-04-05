# 숨바꼭질

from collections import deque
n, m = map(int, input().split())

distance = [0] * 100001
def bfs(v):
  queue = deque()
  queue.append(v)
  while queue:
    num = queue.popleft()
    if num == m:
      print(distance[num])
      break
    for node in (num - 1, num + 1, num * 2):
      if node >= 0 and node <= 100000 and not distance[node]:
        distance[node] = distance[num] + 1
        queue.append(node)

bfs(n)