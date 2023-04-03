# 최대 힙

import sys, heapq

n = int(sys.stdin.readline())
h = []
for _ in range(n):
  command = int(sys.stdin.readline())
  if command == 0:
    if len(h) == 0:
      print(0)
    else:
      min_value = heapq.heappop(h)
      max_value = min_value * -1
      print(max_value)
  else:
    heapq.heappush(h, -command)