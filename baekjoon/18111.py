# 마인크래프트

# 입력
n, m, b = map(int, input().split())
blocks = []
for _ in range(n):
  row = list(map(int, input().split()))
  blocks += row

min_time = 500 * 500 * 2 * 257
height = blocks[0]
blocks_out = sum(blocks)
for h in range(max(blocks), min(blocks) - 1, -1):
  if blocks_out + b >= h * n * m:
    time = 0
    for i in blocks:
      diff = i - h
      if diff > 0:
        time += diff * 2
      elif diff < 0:
        time -= diff * 1
    
    if time < min_time:
      min_time = time
      height = h

print(min_time, height)

# 이 코드의 문제점은 키 값 범위 내의 모든 height에 대해서 계산하지 않는 것
# blocks = {}
# for _ in range(n):
#   row = list(map(int, input().split()))
#   for i in row:
#     if i in blocks:
#       blocks[i] += 1
#     else:
#       blocks[i] = 1

# blocks = dict(sorted(blocks.items()))
# res = []
# for key in blocks:
#   inventory = b
#   base = int(key)
#   time = 0
#   for key2 in blocks:
#     if int(key2) - base > 0:
#       time += 2 * blocks[key2]
#       inventory += blocks[key2]
#     if int(key2) - base < 0:
#       time += blocks[key2]
#       inventory -= blocks[key2]
#   if inventory < 0:
#     continue
#   else:
#     res.append([time, base])
  
# res.sort(key = lambda x: (x[0], -x[1]))
# print(res[0][0], res[0][1])