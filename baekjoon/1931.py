# 회의실 배정

import sys

n = int(sys.stdin.readline())

schedules = []
for _ in range(n):
  start, end = map(int, sys.stdin.readline().rstrip().split())
  schedules.append([start, end])

schedules.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = schedules[0][1]
for i in range(1, n):
  if schedules[i][0] >= end_time:
    cnt += 1
    end_time = schedules[i][1]

print(cnt)