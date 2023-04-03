# 최소 힙

# 입력 수가 많아지는 것에 대비햐여 sys 라이브러리 사용 권장
import sys
import heapq

n = int(sys.stdin.readline())
h = []

def heapsort(command):
  if command == 0:
    if len(h) == 0:
      print(0)
    else:
      min_value = heapq.heappop(h)
      print(min_value)
  else:
    heapq.heappush(h, command)

for _ in range(n):
  command = int(sys.stdin.readline())
  heapsort(command)