# DFS로 풀면 시간 초과 발생

from collections import deque

def solution(maps):
  row_len = len(maps)
  col_len = len(maps[0])
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
      row, col = queue.popleft()
      if (row, col) == (row_len - 1, col_len - 1):
        return maps[row][col]
      for (y, x) in zip(dy, dx):
        new_y = row + y
        new_x = col + x
        if new_y < 0 or new_y >= row_len or \
          new_x < 0 or new_x >= col_len or \
          maps[new_y][new_x] == 0 or \
          (maps[new_y][new_x] != 1 and
          maps[new_y][new_x] <= maps[row][col] + 1):
          continue
        maps[new_y][new_x] = maps[row][col] + 1
        queue.append((new_y, new_x))
    return -1
  return bfs()

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])