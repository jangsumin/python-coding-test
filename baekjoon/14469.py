# 소가 길을 건너간 이유 3

n = int(input())
info = []
for _ in range(n):
  arrival, time = map(int, input().split())
  info.append((arrival, time))

info.sort(key=lambda x: x[0])
opt = -1
for i in range(n):
  if info[i][0] >= opt:
    opt = info[i][0] + info[i][1]
  else:
    opt += info[i][1]
print(opt)