# 설탕 배달

n = int(input())

five_cnt = n // 5

cnt = list()
for i in range(0, five_cnt + 1):
  three_cnt = 0
  if (n - (i * 5)) % 3 == 0:
    three_cnt = (n - (i * 5)) // 3
    cnt.append(i + three_cnt)
  else:
    continue

if len(cnt) == 0:
  print(-1)
else:
  print(min(cnt))