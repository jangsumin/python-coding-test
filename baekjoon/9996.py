# 한국이 그리울 땐 서버에 접속하지

# 입력
import sys
t = int(sys.stdin.readline())
pattern = list(sys.stdin.readline().rstrip().split('*'))

for _ in range(t):
  s = sys.stdin.readline().rstrip()
  success = False

  start, end = pattern[0], pattern[1]
  if s[:len(start)] == start and s[-len(end):] == end and len(''.join(pattern)) <= len(s):
    success = True
  
  print('DA' if success == True else 'NE')