# 유기농 배추
# 탐색

# 테스트 케이스 개수 입력
import sys
input = sys.stdin.readline
t = int(input())

def dfs(x, y):
    if x < 0 or y < 0 or x > y_len - 1 or y > x_len - 1:
      return False
    if graph[x][y] == 1:
      graph[x][y] = 0
      dfs(x + 1, y)
      dfs(x - 1, y)
      dfs(x, y + 1)
      dfs(x, y - 1)
      return True
    return False

# 테스트 케이스 별 정답 출력
for _ in range(t):

  # 배추 관련 정보 입력
  x_len, y_len, green_cnt = map(int, input().split())
  graph = [[0] * x_len for _ in range(y_len)]
  answer = 0
  
  for _ in range(green_cnt):
    x, y = map(int, input().split())
    graph[y][x] = 1

  for i in range(0, y_len):
    for j in range(0, x_len):
      if dfs(i, j) == True:
        answer += 1
  
  print(answer)