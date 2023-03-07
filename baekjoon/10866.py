# 덱

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

de = deque()
for _ in range(n):
  command = input()
  if command[0 : 10] == 'push_front':
    de.appendleft(int(command.split()[1]))
  
  if command[0 : 9] == 'push_back':
    de.append(int(command.split()[1]))

  if command[0 : 9] == 'pop_front':
    if len(de) >= 1:
      print(de.popleft())
    else:
      print(-1)
  
  if command[0 : 8] == 'pop_back':
    if len(de) >= 1:
      print(de.pop())
    else:
      print(-1)

  if command[0 : 4] == 'size':
    print(len(de))

  if command[0 : 5] == 'empty':
    if len(de) >= 1:
      print(0)
    else:
      print(1)

  if command[0 : 5] == 'front':
    if len(de) == 0:
      print(-1)
    else:
      print(de[0])
      
  if command[0 : 4] == 'back':
    if len(de) == 0:
      print(-1)
    else:
      print(de[-1])
  # print(de)