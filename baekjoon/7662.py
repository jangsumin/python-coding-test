# 이중 우선순위 큐

import heapq
t = int(input())

for _ in range(t):
  k = int(input())
  minq, maxq = [], []
  visited = [False for _ in range(1000001)]

  for i in range(k):
    command, num = input().split()

    if command == 'I':
      heapq.heappush(minq, (int(num), i))
      heapq.heappush(maxq, (-int(num), i))
      visited[i] = True
    elif command == 'D' and num == '-1':
      while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
      if minq:
        visited[minq[0][1]] = False
        heapq.heappop(minq)
    elif command == 'D' and num == '1':
      while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)
      if maxq:
        visited[maxq[0][1]] = False
        heapq.heappop(maxq)

  while minq and not visited[minq[0][1]]: heapq.heappop(minq)
  while maxq and not visited[maxq[0][1]]: heapq.heappop(maxq)  
  print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else 'EMPTY')