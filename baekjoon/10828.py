# 스택

import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
  command = input()
  if command[0 : 4] == 'push':
    stack.append(int(command.split()[1]))
  if command[0 : 3] == 'pop':
    if len(stack) >= 1:
      print(stack.pop())
    else:
      print(-1)
  if command[0 : 4] == 'size':
    print(len(stack))
  if command[0 : 5] == 'empty':
    if len(stack) >= 1:
      print(0)
    else:
      print(1)
  if command[0 : 3] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])     
  # print(stack)