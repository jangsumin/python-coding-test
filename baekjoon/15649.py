# N과 M(1)
# 백트래킹

n, m = map(int, input().split())
stack = []
visited = [False] * (n + 1)

def dfs():
  if len(stack) == m:
    print(' '.join(map(str, stack)))
    return
  for i in range (1, n + 1):
    if visited[i] == True:
      continue
    visited[i] = True
    stack.append(i)
    dfs()
    stack.pop()
    visited[i] = False

dfs()