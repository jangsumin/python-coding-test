# 토마토

# 입력
from collections import deque
m, n = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  for j in range(m):
    if graph[i][j] == 1:
      queue.append([i, j])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          queue.append([nx, ny])

bfs()
result = 0
# 아래 반복문에서 1인 원소들을 찾아서 bfs 함수 실행해야 함
# 완성된 graph에 0이 있으면 -1 출력, 아니면 cnt 출력
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      print(-1)
      exit(0)
    result = max(result, graph[i][j])

print(result - 1)