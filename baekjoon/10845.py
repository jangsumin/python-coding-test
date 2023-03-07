# 큐

import sys
input = sys.stdin.readline
n = int(input())

queue = []
for _ in range(n):
  command = input()
  if command[0 : 4] == 'push':
    queue.append(int(command.split()[1]))
  if command[0 : 3] == 'pop':
    if len(queue) >= 1:
      print(queue.pop(0))
    else:
      print(-1)
  if command[0 : 4] == 'size':
    print(len(queue))
  if command[0 : 5] == 'empty':
    if len(queue) >= 1:
      print(0)
    else:
      print(1)
  if command[0 : 5] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  if command[0 : 4] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])
  # print(queue)